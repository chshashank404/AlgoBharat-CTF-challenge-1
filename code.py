from algosdk.v2client import algod
from algosdk import account, transaction
from algosdk.encoding import is_valid_address

# Connect to Nodely's TestNet endpoint
algod_address = "https://testnet-api.4160.nodely.dev"
algod_token = ""  # No token required for Nodely

# Initialize the Algod client
client = algod.AlgodClient(algod_token, algod_address)

# Your wallet's private key
sender_private_key = "" 
sender_address = account.address_from_private_key(sender_private_key)

# The wallet address that we uncovered after decrypting the smart contract's global storage
receiver_address = "2JAZQO6Z5BCXFMPVW2CACK2733VGKWLZKS6DGG565J7H5NH77JNHLIIXLY"

# Step 1: Validate the receiver address – because we don't want to mess things up!
if is_valid_address(receiver_address):
    print("Receiver address is valid!")
else:
    raise ValueError("Receiver address is invalid. Double-check your findings!")

# Step 2: Get the current transaction parameters from the Algorand TestNet
params = client.suggested_params()

# Step 3: Create a Payment Transaction – sending 1 Algo (1,000,000 microAlgos)
amount = 1000000  # 1 Algo
unsigned_txn = transaction.PaymentTxn(sender_address, params, receiver_address, amount)

# Step 4: Sign the transaction with your private key (keep it safe!)
signed_txn = unsigned_txn.sign(sender_private_key)

# Step 5: Send the transaction to the TestNet – unleash the Algo!
try:
    txid = client.send_transaction(signed_txn)
    print(f"Transaction sent! TXID: {txid}")
except Exception as e:
    print(f"Error sending transaction: {e}")

# Step 6: Wait for confirmation (don’t panic, it's in the chain’s hands now...)
try:
    confirmed_txn = transaction.wait_for_confirmation(client, txid, 4)
    print("Transaction confirmed in round:", confirmed_txn['confirmed-round'])
except Exception as e:
    print(f"Error confirming transaction: {e}")
