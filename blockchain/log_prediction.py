from web3 import Web3
import json

# Connect to local Ethereum node
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Load contract ABI and address
with open('path/to/compiled_contract_abi.json') as f:
    contract_abi = json.load(f)

contract_address = '0xYourContractAddress'  # Replace with your contract address
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def log_prediction(ipfs_hash, data_hash, maintenance_needed):
    tx_hash = contract.functions.logMaintenance(ipfs_hash, data_hash, maintenance_needed).transact()
    w3.eth.waitForTransactionReceipt(tx_hash)
    print("Maintenance logged successfully!")

if __name__ == '__main__':
    log_prediction('QmHash...', 'data_hash...', True)  # Replace with actual IPFS and data hash
