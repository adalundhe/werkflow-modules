# werkflow-encryption

Version `0.3.0`

Asynchronous symmetric and asymmetric encryption module for [Werkflow](https://github.com/adalundhe/werkflow).

## Installation

```bash
pip install werkflow-encryption
```

## Features

- **Fernet (AES-128-CBC + HMAC-SHA256):** `generate_key()`, `encrypt()`, `decrypt()`.
- **AES-256-GCM (Authenticated Encryption):** `generate_aes_key()`, `encrypt_aes256gcm()`, `decrypt_aes256gcm()`.
  - Requires an explicit or previously loaded key (`MissingEncryptionKeyError` if unset).
  - Derives a 32-byte key and outputs **only** `nonce (12 bytes) + ciphertext + authentication tag (16 bytes)` — the encryption key is never embedded in the ciphertext.
- **NaCl SealedBox (Curve25519 / XSalsa20-Poly1305):** `generate_nacl_keypair()`, `encrypt_nacl()`, `decrypt_nacl()` (accepts raw 32-byte or base64-encoded keys; `pynacl` is declared as a dependency and guarded separately so Fernet/AES methods still function if PyNaCl is unavailable).
- **Key Persistence:** `dump_key_to_env()`, `load_key_from_env()`, `dump_key_to_file()`, and `load_key_from_file()`.

## Usage

```python
from werkflow_encryption import Encryption

async with Encryption() as enc:
    key = await enc.generate_aes_key()
    ciphertext = await enc.encrypt_aes256gcm(b"sensitive payload", key=key)
    plaintext = await enc.decrypt_aes256gcm(ciphertext, key=key)

    keypair = await enc.generate_nacl_keypair()
    sealed = await enc.encrypt_nacl(b"github-secret", public_key=keypair.public_key)
    opened = await enc.decrypt_nacl(sealed, private_key=keypair.private_key)
```

## Dependencies

- `werkflow-core`
- `werkflow-shell`
- `werkflow-system`
- `cryptography`
- `pynacl`

## Requirements

- Python `>=3.11`
