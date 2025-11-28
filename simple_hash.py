import pprint
import time

# explain birthday problem

def tiny_hash(msg):
    h = 0
    for i in range(len(msg)):
        h = (h + ord(msg[i])) % 65536 # 17-bit hash
    return h

def verifyMessageHash(message, expectedHash) :
    return tiny_hash(message) == expectedHash


def brute_force_tiny_hash(target_hash, charset, max_length):

    start = time.time()  # Start timer
    
    def search(prefix, depth):
        if depth == 0:
            if tiny_hash(prefix) == target_hash:
                return prefix
            return None
        
        for char in charset:
            result = search(prefix + char, depth - 1)
            print(f'Trying: "{prefix + char}"')
            if result is not None:
                return result
        
        return None
    
    # Try increasing lengths
    for length in range(1, max_length + 1):
        result = search("", length)
        if result is not None:
            end = time.time()
            return {
                'match': result,
                'time_seconds': end - start,
                'length': length
            }
    
    # No match found
    end = time.time()
    return {
        'match': None,
        'time_seconds': end - start,
        'length': None
    }

def example_hash():

    msgs = [
        "A bat",
        "Li Europan lingues es membres del sam familie. Lor separat existentie es un myth.",
        "A quick brown fox jumps over the lazy dog",
        "A tab"
    ]

    msgsWithHash = [
        {
            'message': msg,
            'hash': tiny_hash(msg)
        } for msg in msgs 
    ]


    pprint.pprint(msgsWithHash,indent=4, width=40, depth=2)

    # man in the middle changes data
    msgs[0] = "B test"
    msgsWithHash[0]['message'] = "Changed message"

    print("Messages with their hashes:")
    pprint.pprint(msgsWithHash,indent=4, width=40, depth=2)

    for entry in msgsWithHash:
        msg = entry['message']
        expectedHash = entry['hash']
        isValid = verifyMessageHash(msg, expectedHash)
        print(f"Message: '{msg}' | Expected Hash: {expectedHash} | Valid: {isValid}")

def brute_force_example():
    charset = "1234567890abcdefghijklmnopqrstuvwxyz"
    target = tiny_hash("12345")
    # target = tiny_hash("12345678")
    # target = tiny_hash("hello")
    # target = tiny_hash("test@")
    # target = tiny_hash("hello1") # last test result : seconds 53.11 
    # target = tiny_hash("hellow") # last test result: closed the vscode
    # target = tiny_hash("A quick brown fox jumps over the lazy dog") # exponential time
    result = brute_force_tiny_hash(target, charset, 10)
    print("target hash:", target)
    pprint.pprint(result, indent=4, width=40, depth=2)

# example_hash()
brute_force_example()