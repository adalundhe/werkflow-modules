# werkflow-secrets

Version `0.3.0`

Encrypted secret storage and retrieval for environment variables, files, and JSON key/value stores in [Werkflow](https://github.com/adalundhe/werkflow).

## Installation

```bash
pip install werkflow-secrets
```

## Features

- **Multiple Encryption Modes (`EncryptionMethod`):**
  - `'basic'`: Fernet authenticated encryption.
  - `'aes256gcm'`: AES-256-GCM authenticated encryption with base64-safe transport for env vars and JSON files (key is always stored separately, never inside the ciphertext).
- **Key Management:** `generate_key()`, `dump_key_to_env()`, `load_key_from_env()`, `dump_key_to_file()`, `load_key_from_file()`, and `load_key()`.
- **Secret Storage & Loading:**
  - Environment variables: `dump_secret_to_env()`, `load_from_env()`.
  - Files: `dump_secret_to_file()`, `load_from_file()` (including single-key lookup via `json_key`).
  - JSON dictionaries: `dump_secrets_json()` (does not mutate caller dictionaries) and `load_from_json()`.

## Usage

```python
from werkflow_secrets import Secrets

async with Secrets() as secrets:
    await secrets.generate_key()
    await secrets.dump_key_to_file(name="app", path="./keys")

    await secrets.dump_secret_to_env("DB_PASSWORD", "s3cr3t", method="aes256gcm")
    password = await secrets.load_from_env("DB_PASSWORD", method="aes256gcm")

    await secrets.dump_secrets_json({"api_key": "abc"}, "./secrets.json", method="aes256gcm")
    loaded = await secrets.load_from_json("./secrets.json", method="aes256gcm")
```

## Dependencies

- `werkflow-core`
- `werkflow-encryption`
- `werkflow-shell`

## Requirements

- Python `>=3.11`
