require('dotenv').config();
const express = require('express');
const { CeramicClient } = require('@ceramicnetwork/http-client');
const { TileDocument } = require('@ceramicnetwork/stream-tile');
const { Ed25519Provider } = require('key-did-provider-ed25519');
const { DID } = require('dids');
const { fromString } = require('uint8arrays/from-string');

const CERAMIC_NODE_URL = process.env.CERAMIC_NODE_URL || 'https://ceramic-clay.3boxlabs.com';
const SEED = process.env.SEED || '0000000000000000000000000000000000000000000000000000000000000000'; // Replace in .env for real use

const app = express();
app.use(express.json());

async function getCeramic() {
  const ceramic = new CeramicClient(CERAMIC_NODE_URL);
  const provider = new Ed25519Provider(fromString(SEED, 'base16'));
  const did = new DID({ provider });
  await did.authenticate();
  ceramic.did = did;
  return ceramic;
}

app.post('/create-profile', async (req, res) => {
  try {
    const { did, profile } = req.body;
    const ceramic = await getCeramic();
    const doc = await TileDocument.create(ceramic, { ...profile, did }, { family: 'userProfile' });
    res.json({ streamId: doc.id.toString() });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.post('/update-profile', async (req, res) => {
  try {
    const { streamId, profile } = req.body;
    const ceramic = await getCeramic();
    const doc = await TileDocument.load(ceramic, streamId);
    await doc.update(profile);
    res.json({ ok: true });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.get('/profile/:streamId', async (req, res) => {
  try {
    const { streamId } = req.params;
    const ceramic = await getCeramic();
    const doc = await TileDocument.load(ceramic, streamId);
    res.json(doc.content);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Ceramic microservice running on port ${PORT}`);
}); 