import requests

PINATA_API_KEY = "61ec854b4a6f0d3dccdd"
PINATA_SECRET = "42bcfd310e14af4784577951a4e0e1d95690b53ef7957d47a3cac2aeb657ed08"

def upload_to_ipfs(file_path):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"

    headers = {
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_SECRET
    }

    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(url, files=files, headers=headers)

    return response.json()["IpfsHash"]