# Python code to communicate with monerod through rpc
# based on the samples provided


import requests
import json

#parameters
#url from the monerod node
url = "http://localhost:38081/json_rpc"
# standard json header
headers = {'content-type': 'application/json'}

def json_getblockcount():
    # bitmonerod' procedure/method to call
    rpc_input = {
           "method": "getblockcount"
    }
    
    # add standard rpc values
    rpc_input.update({"jsonrpc": "2.0", "id": "0"})

    # execute the rpc request
    response = requests.post(
        url,
        data=json.dumps(rpc_input),
        headers=headers)

    # pretty print json output
    return (json.dumps(response.json(), indent=4))

def json_getblockheaderbyheight(height):
    # bitmonerod' procedure/method to call
    rpc_input = {
           "method": "getblockheaderbyheight",
           "params": {"height": height}
    }
    
    # add standard rpc values
    rpc_input.update({"jsonrpc": "2.0", "id": "0"})

    # execute the rpc request
    response = requests.post(
        url,
        data=json.dumps(rpc_input),
        headers=headers)

    # pretty print json output
    return (json.dumps(response.json(), indent=4))

def getblockcount():
    jsonResponse = json.loads(json_getblockcount())
    jsonData = jsonResponse["result"]["count"]
    return jsonData

class blockheaderdata(object):
    def __init__(self, nonce, reward, hash, timestamp, major_version, height, difficulty, depth, prev_hash, orphan_status, block_size, minor_version, num_txes):
        self.nonce = nonce
        self.reward = reward
        self.hash = hash
        self.timestamp = timestamp
        self.major_version = major_version

def getblockheaderbyheight(height):
    jsonResponse = json.loads(json_getblockheaderbyheight(height))
    nonce = jsonResponse["result"]["block_header"]["nonce"]
    reward = jsonResponse["result"]["block_header"]["reward"]
    hash = jsonResponse["result"]["block_header"]["hash"]
    timestamp = jsonResponse["result"]["block_header"]["timestamp"]
    major_version = jsonResponse["result"]["block_header"]["major_version"]
    heightx = jsonResponse["result"]["block_header"]["height"]
    difficulty = jsonResponse["result"]["block_header"]["difficulty"]
    depth = jsonResponse["result"]["block_header"]["depth"]
    prev_hash = jsonResponse["result"]["block_header"]["prev_hash"]
    orphan_status = jsonResponse["result"]["block_header"]["orphan_status"]
    block_size = jsonResponse["result"]["block_header"]["block_size"]
    minor_version = jsonResponse["result"]["block_header"]["minor_version"]
    num_txes = jsonResponse["result"]["block_header"]["num_txes"]
    #return blockheaderdata(nonce, reward, hash, timestamp, major_version, heightx, difficulty, depth, prev_hash, orphan_status, block_size, minor_version, num_txes)        
    return nonce, reward, hash, timestamp, major_version, heightx, difficulty, depth, prev_hash, orphan_status, block_size, minor_version, num_txes        
    
def main():
    #print json_getblockcount()
    #print getblockcount()
    #print miningstatus()
    
    height = 1
    print json_getblockheaderbyheight(height)
    nonce, reward, hash, timestamp, major_version, heightx, difficulty, depth, prev_hash, orphan_status, block_size, minor_version, num_txes = getblockheaderbyheight(height)
    print nonce, reward, hash, timestamp, major_version, heightx, difficulty, depth, prev_hash, orphan_status, block_size, minor_version, num_txes

if __name__ == "__main__":
    main()