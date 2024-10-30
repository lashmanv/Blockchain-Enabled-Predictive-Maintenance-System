# Blockchain-Enabled Predictive Maintenance System

This project integrates machine learning, blockchain, and IPFS for a robust predictive maintenance system. It uses an LSTM model to predict equipment failures based on sensor data and logs predictions securely on the blockchain for transparency and traceability.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Setup and Installation](#setup-and-installation)
4. [Usage](#usage)
5. [Blockchain Integration](#blockchain-integration)
6. [Frontend Interface](#frontend-interface)
7. [Future Improvements](#future-improvements)

## Project Overview

This project demonstrates a predictive maintenance system leveraging blockchain technology for secure and transparent maintenance logs. Core components:

- **Predictive Maintenance Model**: Trained using an LSTM model on equipment sensor data to predict failures.
- **Blockchain Logging**: A Solidity smart contract logs maintenance records on the blockchain.
- **Decentralized Storage**: IPFS stores data to ensure decentralized, tamper-proof data storage.

## Project Structure

- `contracts/`: Contains smart contracts (`PredictiveMaintenance.sol`) to log predictions.
- `data/`: Contains sample sensor data and preprocessed data for model training.
- `models/`: ML model files, specifically `lstm_model.py` for predicting failures.
- `ipfs/`: Scripts for storing data in IPFS, specifically `store_in_ipfs.py`.
- `blockchain/`: Web3.py script (`log_prediction.py`) to interact with the smart contract.
- `frontend/`: Interface files for interacting with blockchain and viewing maintenance logs.

## Setup and Installation

### Requirements

- **Python 3.8+**
- **Node.js** (for frontend interaction with blockchain)
- **Ganache** (for local Ethereum blockchain simulation)
- **IPFS** (for decentralized storage)
- **Solidity Compiler** (for compiling smart contracts)

### Install Python Dependencies

```
pip install -r requirements.txt
```

### Install Node Dependencies (Frontend)

Navigate to the `frontend` directory and run:

```
npm install
```

### Install IPFS

Refer to the IPFS installation guide.

### Compile and Deploy Smart Contract

1. Compile `PredictiveMaintenance.sol` using the Solidity compiler.
2. Deploy it to your Ethereum network (Ganache setup recommended).

## Usage

1. **Data Preprocessing and Model Training**
   Run `main.py` to load, preprocess sensor data, and train the LSTM model.

2. **IPFS Integration**
   Run `store_in_ipfs.py` to store the processed data in IPFS, which returns an IPFS hash.

3. **Log Predictions to Blockchain**
   Use `log_prediction.py` to log predictions to the blockchain by providing the IPFS hash, data hash, and maintenance alert status.

4. **Start Frontend**
   Navigate to the `frontend` directory and start the web server:
   ```
   npm start
   ```
   Access `index.html` in your browser to view and interact with the logged maintenance records.

## Blockchain Integration

The smart contract is deployed to an Ethereum-compatible blockchain network. Key functions:

- `logMaintenance`: Logs prediction with IPFS hash, data hash, and maintenance alert status.
- `getMaintenanceLog`: Retrieves a specific log by ID.
  Modify the blockchain connection details in `log_prediction.py` as needed.

## Frontend Interface

The frontend allows users to view maintenance logs stored on the blockchain using Web3.js:

- **app.js** interacts with the smart contract.
- **index.html** provides a basic interface for log retrieval.
  Ensure you're connected to an Ethereum network (e.g., Ganache) while accessing the interface.

## Future Improvements

- **Anomaly Detection**: Include anomaly detection for data outliers.
- **Scalability**: Deploy on a scalable Ethereum-compatible network (Polygon, Binance Smart Chain).
- **Enhanced Frontend**: Add visualization and alert features for maintenance staff.
