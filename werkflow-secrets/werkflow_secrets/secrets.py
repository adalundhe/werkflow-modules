import orjson
import os
from werkflow_core import Module
from werkflow_encryption import Encryption
from werkflow_shell import Shell
from typing import Dict, Literal, Optional

class Secrets(Module):

    def __init__(self) -> None:
        super().__init__()
        
        self._shell = Shell()
        self.encryption = Encryption()
        self.default_file = '.secrets.json'

    async def generate_key(self):
        await self.encryption.generate_key()

    async def dump_key_to_env(
        self,
        name: str
    ):
        await self.encryption.dump_key_to_env(name)

    async def dump_key_to_file(
        self,
        name: str='secret',
        path: str=None
    ):
        await self.encryption.dump_key_to_file(
            name=name,
            path=path
        )

    async def dump_key_to_env(
        self,
        name: str
    ):
        await self.encryption.dump_key_to_env(
            name
        )

    async def dump_secret_to_env(
        self,
        name: str,
        secret: str,
        method: Literal['basic', 'aes256gcm']='basic'
    ):
        
        if method == 'aes256gcm':
            encrypted_secret = await self.encryption.encrypt_aes256gcm(secret)
        
        else:
            encrypted_secret = await self.encryption.encrypt(secret)
        
        await self._shell.set_envar(
            name,
            encrypted_secret
        )

    async def dump_secret_to_file(
        self,
        secret: str,
        path: str,
        method: Literal['basic', 'aes256gcm']='basic'
    ):
        
        if method == 'aes256gcm':
            encrypted_secret = await self.encryption.encrypt_aes256gcm(
                secret.encode()
            )

        else: 
            encrypted_secret = await self.encryption.encrypt(
                secret.encode()
            )

        await self._shell.pipe_to_file(
            path,
            encrypted_secret,
            overwrite=True,
            silent=True
        )

    async def dump_secrets_json(
        self,
        secrets: Dict[str, str],
        path: str,
        method: Literal['basic', 'aes256gcm']='basic'
    ):
        
        if method == 'aes256gcm':
            for key, value in secrets.items():
                secret = await self.encryption.encrypt_aes256gcm(
                    value.encode()
                )

                secrets[key] = secret.decode()

        else:
            for key, value in secrets.items():
                secret = await self.encryption.encrypt(
                    value.encode()
                )

                secrets[key] = secret.decode()

        json_data = orjson.dumps(secrets).decode()
        
        await self._shell.pipe_to_file(
            path,
            json_data,
            overwrite=True,
            silent=True
        )

    async def load_key(
        self,
        name: str,
        path: Optional[str]=None
    ) -> None:
        
        if path is None:
            path = await self._shell.get_current_directory()

        await self.encryption.load_key_from_file(
            keyname=name,
            path=path
        )

    async def load_key_from_env(
        self,
        name: str
    ):
        await self.encryption.load_key_from_env(
            name
        )  

    async def load_key_from_file(
        self,
        key_filename: str='secret.key',
        path: Optional[str]=None
    ):
        await self.encryption.load_key_from_file(
            key_filename=key_filename,
            path=path
        )

    async def load_from_env( 
        self,
        name: str,
        method: Literal['basic', 'aes256gcm']='basic'
    ):
        envar = await self._shell.get_envar(name)

        if method == 'aes256gcm':
            secret = await self.encryption.decrypt_aes256gcm(envar)

        else:
            secret = await self.encryption.decrypt(envar)

        return secret
    
    async def load_from_file(
        self,
        path: str=None,
        json_key: Optional[str]=None,
        method: Literal['basic', 'aes256gcm']='basic'
    ):
        if path is None and json_key is False:
            current_directory = await self._shell.get_current_directory()
            path = os.path.join(
                current_directory,
                'secret.txt'
            )

        elif path is None:
            current_directory = await self._shell.get_current_directory()
            path = os.path.join(
                current_directory,
                'secret.json'
            )

        encrypted_secret = await self._shell.read_file_as_bytes(
            path,
            silent=True
        )

        if json_key:
            secret_data: Dict[str, str] = json.loads(encrypted_secret)
            encrypted_secret = secret_data.get(json_key, '').encode()

        if method == 'aes256gcm':
            secret = await self.encryption.decrypt_aes256gcm(encrypted_secret)
        
        else:
            secret = await self.encryption.decrypt(encrypted_secret)

        return secret

    async def load_from_json(
        self,
        path: str=None,
        method: Literal['basic', 'aes256gcm']='basic'
    ) -> Dict[str, str]:
        
        if path is None:
            current_directory = await self._shell.get_current_directory()
            path = os.path.join(
                current_directory,
                'secrets.json'
            )

        secrets_file = await self._shell.read_file(
            path,
            silent=True
        )

        secrets: Dict[str, str] = orjson.loads(secrets_file)

        if method == 'aes256gcm':
            for key, value in secrets.items():
                secret = await self.encryption.decrypt_aes256gcm(
                    value.encode()
                )

                secrets[key] = secret.decode()

        else:
            for key, value in secrets.items():
                secret = await self.encryption.decrypt(
                    value.encode()
                )

                secrets[key] = secret.decode()

        return secrets
    
    async def close(self):
        await self.encryption.close()
        await self._shell.close()

    def abort(self):
        self.encryption.abort()
        self._shell.abort()

    

