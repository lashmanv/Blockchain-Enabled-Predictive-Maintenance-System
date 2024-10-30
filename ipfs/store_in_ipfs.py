import ipfshttpclient

def store_in_ipfs(file_path):
    client = ipfshttpclient.connect()  # Connect to local IPFS daemon
    res = client.add(file_path)
    return res['Hash']

if __name__ == '__main__':
    file_hash = store_in_ipfs('data/sensor_data.csv')
    print(f"File stored in IPFS with hash: {file_hash}")
