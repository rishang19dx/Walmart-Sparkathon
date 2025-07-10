# Ceramic Microservice

This Node.js microservice provides HTTP endpoints to interact with the Ceramic Network for decentralized user profile management. It is designed to be called by the main backend (Python/FastAPI) to create, update, and fetch user profiles stored on Ceramic.

## Features
- Create a new user profile (returns Ceramic stream ID)
- Update an existing profile
- Fetch a profile by stream ID

## Prerequisites
- Node.js (v16+ recommended)
- npm or yarn
- Access to a Ceramic node (e.g., https://ceramic-clay.3boxlabs.com)

## Setup
```bash
cd ceramic-microservice
npm install
```

## Running the Service
```bash
node index.js
```

## API Endpoints
- `POST /create-profile` — Create a new profile. Body: `{ did, profile }`
- `POST /update-profile` — Update a profile. Body: `{ streamId, profile }`
- `GET /profile/:streamId` — Fetch a profile by stream ID.

## Environment Variables
- `CERAMIC_NODE_URL` — URL of the Ceramic node (default: https://ceramic-clay.3boxlabs.com)
- `SEED` — 32-byte hex string for the Ed25519 key (for demo/dev only; use secure key management in production)

## Notes
- This service is for demo/prototyping. For production, use secure key management and authentication. 