# 🔐 Solving the Algorand CTF: Hidden Flag in a Smart Contract 🔐

Welcome to the wild world of Algorand smart contracts! This repo walks you through how I tackled a CTF challenge by hunting down a hidden clue inside a smart contract, decoding it, and then sending some sweet Algos programmatically.

## 🧠 The Challenge

1. **Find the Flag**: I had to analyze a deployed smart contract's transactions on the Algorand Testnet to locate a hidden clue in its global storage. The flag, once decrypted, revealed a wallet address.

2. **Send 1 Algo**: After decrypting the clue, the challenge required me to send exactly 1 Algo to the revealed address—just like a hacker would do... programmatically!

3. **Tooling**: All this went down on the [Algorand Testnet](https://testnet.explorer.perawallet.app/). Nodely services made interacting with the Algorand chain simple and free. You gotta love that!

---

## 🕵️‍♂️ Step-by-Step Breakdown

1. **Analyzing Transactions**: 
   I headed over to [Algorand Testnet Explorer](https://testnet.explorer.perawallet.app/application/718383248/) and started inspecting the smart contract's transactions.

2. **Decoding the Global Storage**: 
   I decoded the global storage from this transaction:  
   [Transaction Link](https://testnet.explorer.perawallet.app/tx/T5RNGCQXGCPAPLDPYJ5DGFVBKOFBB2VPUB2QE2Z7J3QIAXLVSMRQ/)  
   After decrypting, I found the wallet address:  
   `2JAZQO6Z5BCXFMPVW2CACK2733VGKWLZKS6DGG565J7H5NH77JNHLIIXLY`.

3. **Sending 1 Algo**: 
   With the wallet address in hand, I had to send exactly 1 Algo (1,000,000 microAlgos) to the address, using the Algorand Python SDK and Nodely TestNet service.

---

## 💻 The Code

The Python script (`code.py`) is where the magic happens. It connects to the Algorand Testnet via Nodely, creates a payment transaction, signs it, and sends 1 Algo to the decoded address. If all goes well, it waits for the transaction to be confirmed in the blockchain.
