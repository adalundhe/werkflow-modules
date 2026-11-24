import json
import os
from base64 import b64decode, b64encode
from typing import Dict, Literal, Optional

from werkflow_core import Module
from werkflow_encryption import Encryption
from werkflow_shell import Shell

EncryptionMethod = Literal['basic', 'aes256gcm']


class Secrets(Module):
    dependencies = ['werkflow-encryption', 'werkflow-shell']

    def __init__(self) -> None:
        super().__init__()

        self._shell = Shell()
        self.encryption = Encryption()
        self.default_file: str = '.secrets.json'

    async def generate_key(self) -> bytes:
        return await self.encryption.generate_key()

    async def dump_key_to_env(
        self,
        name: str,
    ) -> None:
        await self.encryption.dump_key_to_env(name)

    async def dump_key_to_file(
        self,
        name: str = 'secret',
        path: Optional[str] = None,
    ) -> None:
        await self.encryption.dump_key_to_file(
            name=name,
            path=path,
        )

    async def dump_secret_to_env(
        self,
        name: str,
        secret: str,
        method: EncryptionMethod = 'basic',
    ) -> None:
        secret_bytes = secret.encode('utf-8')
        if method == 'aes256gcm':
            encrypted_bytes = await self.encryption.encrypt_aes256gcm(secret_bytes)
            encoded_secret = b64encode(encrypted_bytes).decode('ascii')
        else:
            encrypted_bytes = await self.encryption.encrypt(secret_bytes)
            encoded_secret = encrypted_bytes.decode('utf-8')

        await self._shell.set_envar(name, encoded_secret)

    async def dump_secret_to_file(
        self,
        secret: str,
        path: str,
        method: EncryptionMethod = 'basic',
    ) -> None:
        secret_bytes = secret.encode('utf-8')
        if method == 'aes256gcm':
            encrypted_secret = await self.encryption.encrypt_aes256gcm(secret_bytes)
        else:
            encrypted_secret = await self.encryption.encrypt(secret_bytes)

        await self._shell.pipe_to_file(
            path,
            encrypted_secret,
            overwrite=True,
            silent=True,
        )

    async def dump_secrets_json(
        self,
        secrets: Dict[str, str],
        path: str,
        method: EncryptionMethod = 'basic',
    ) -> None:
        encrypted_secrets: Dict[str, str] = {}

        if method == 'aes256gcm':
            for key, value in secrets.items():
                encrypted = await self.encryption.encrypt_aes256gcm(
                    value.encode('utf-8')
                )
                encrypted_secrets[key] = b64encode(encrypted).decode('ascii')
        else:
            for key, value in secrets.items():
                encrypted = await self.encryption.encrypt(
                    value.encode('utf-8')
                )
                encrypted_secrets[key] = encrypted.decode('utf-8')

        json_data = json.dumps(encrypted_secrets)

        await self._shell.pipe_to_file(
            path,
            json_data,
            overwrite=True,
            silent=True,
        )

    async def load_key(
        self,
        name: str,
        path: Optional[str] = None,
    ) -> bytes:
        if path is None:
            target_path = await self._shell.get_current_directory()
        else:
            target_path = await self._shell.to_absolute_path(path)

        resolved_filename = name
        candidate = os.path.join(target_path, name)
        if (
            not await self._shell.check_path_exists(candidate)
            and not name.endswith('.key')
            and await self._shell.check_path_exists(f'{candidate}.key')
        ):
            resolved_filename = f'{name}.key'

        return await self.encryption.load_key_from_file(
            key_filename=resolved_filename,
            path=target_path,
        )

    async def load_key_from_env(
        self,
        name: str = 'WERKFLOW_ENCRYPTION_KEY',
    ) -> bytes:
        return await self.encryption.load_key_from_env(name)

    async def load_key_from_file(
        self,
        key_filename: str = 'secret.key',
        path: Optional[str] = None,
        keyname: Optional[str] = None,
    ) -> bytes:
        return await self.encryption.load_key_from_file(
            key_filename=key_filename,
            path=path,
            keyname=keyname,
        )

    async def load_from_env(
        self,
        name: str,
        method: EncryptionMethod = 'basic',
    ) -> bytes:
        envar = await self._shell.get_envar(name)
        if envar is None:
            raise KeyError(f"Environment variable '{name}' is not set.")

        if method == 'aes256gcm':
            encrypted_bytes = b64decode(envar.encode('ascii'))
            return await self.encryption.decrypt_aes256gcm(encrypted_bytes)

        return await self.encryption.decrypt(envar.encode('utf-8'))

    async def load_from_file(
        self,
        path: Optional[str] = None,
        json_key: Optional[str] = None,
        method: EncryptionMethod = 'basic',
    ) -> bytes:
        if path is None and json_key is None:
            current_directory = await self._shell.get_current_directory()
            path = os.path.join(current_directory, 'secret.txt')
        elif path is None:
            current_directory = await self._shell.get_current_directory()
            path = os.path.join(current_directory, 'secret.json')

        raw_content = await self._shell.read_file_as_bytes(
            path,
            silent=True,
        )

        if json_key is not None:
            secret_data: Dict[str, str] = json.loads(raw_content.decode('utf-8'))
            if json_key not in secret_data:
                raise KeyError(f"Secret key '{json_key}' not found in '{path}'.")
            raw_value = secret_data[json_key]
            if method == 'aes256gcm':
                encrypted_secret = b64decode(raw_value.encode('ascii'))
            else:
                encrypted_secret = raw_value.encode('utf-8')
        else:
            encrypted_secret = raw_content

        if method == 'aes256gcm':
            return await self.encryption.decrypt_aes256gcm(encrypted_secret)

        return await self.encryption.decrypt(encrypted_secret)

    async def load_from_json(
        self,
        path: Optional[str] = None,
        method: EncryptionMethod = 'basic',
    ) -> Dict[str, str]:
        if path is None:
            current_directory = await self._shell.get_current_directory()
            path = os.path.join(current_directory, 'secrets.json')

        secrets_file = await self._shell.read_file(
            path,
            silent=True,
        )

        encrypted_secrets: Dict[str, str] = json.loads(secrets_file)
        decrypted_secrets: Dict[str, str] = {}

        if method == 'aes256gcm':
            for key, value in encrypted_secrets.items():
                decrypted = await self.encryption.decrypt_aes256gcm(
                    b64decode(value.encode('ascii'))
                )
                decrypted_secrets[key] = decrypted.decode('utf-8')
        else:
            for key, value in encrypted_secrets.items():
                decrypted = await self.encryption.decrypt(
                    value.encode('utf-8')
                )
                decrypted_secrets[key] = decrypted.decode('utf-8')

        return decrypted_secrets

    async def close(self) -> None:
        await self.encryption.close()
        await self._shell.close()

    def abort(self) -> None:
        self.encryption.abort()
        self._shell.abort()
