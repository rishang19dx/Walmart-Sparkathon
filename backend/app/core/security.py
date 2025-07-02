import subprocess
import json
from fastapi import HTTPException, status, Request

async def verify_did_jwt(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing or invalid Authorization header")
    token = auth_header.split(" ", 1)[1]
    try:
        # Call DIDKit CLI to verify JWT
        result = subprocess.run(
            ["didkit", "vc-verify-jwt", token],
            capture_output=True,
            text=True,
            check=True
        )
        verification = json.loads(result.stdout)
        if verification.get('errors'):
            raise Exception(verification['errors'])
        # Optionally, extract the DID (issuer)
        did = verification.get('issuer')
        return did
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"DID verification failed: {str(e)}")
