import didkit

# Generate a new key and DID (using did:key method)
def generate_did_key():
    key = didkit.generate_ed25519_key()
    did = didkit.key_to_did("key", key)
    return {"did": did, "key": key}

# Resolve a DID to its DID Document
def resolve_did(did):
    did_document = didkit.resolve_did(did, '{}')
    return did_document 