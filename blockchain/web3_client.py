from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

print("Connected:", w3.is_connected())

contract_address = Web3.to_checksum_address("0xE1E754f8d5c833C45b62e1C98476801EC2D05F62")

abi = [
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "uint256",
				"name": "index",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "hash",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "address",
				"name": "sender",
				"type": "address"
			}
		],
		"name": "HashStored",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_hash",
				"type": "string"
			}
		],
		"name": "storeHash",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "index",
				"type": "uint256"
			}
		],
		"name": "getHash",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "index",
				"type": "uint256"
			}
		],
		"name": "getRecord",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

contract = w3.eth.contract(address=contract_address, abi=abi)

account = w3.eth.accounts[0]



contract = w3.eth.contract(address=contract_address, abi=abi)
account = w3.eth.accounts[0]

def store_hash(hash_value):
    tx = contract.functions.storeHash(hash_value).transact({
        "from": account
    })
    w3.eth.wait_for_transaction_receipt(tx)

def get_hash(index):
    return contract.functions.getHash(index).call()

def get_count():
    return contract.functions.getCount().call()