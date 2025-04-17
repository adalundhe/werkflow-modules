import asyncio
import os
import functools
import secrets
from base64 import b64encode, b64decode
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from concurrent.futures import ThreadPoolExecutor
from werkflow_core import Module
from werkflow_shell import Shell
from werkflow_system import System
from typing import Optional
from .exceptions import MissingEncryptionKeyError

try:
    module_enabled=True
    from cryptography.fernet import Fernet
    from nacl import encoding, public
except ImportError:
    module_enabled=False
    Fernet=None
    encoding=None
    public=None


class Encryption(Module):
    module_enabled=module_enabled

    def __init__(self) -> None:
        super().__init__()

        self._system = System()
        self._shell = Shell()
        self._loop: asyncio.AbstractEventLoop = None
        self._executor = ThreadPoolExecutor(
            max_workers=self._system.configuration.cores.physical
        )

        self.key: bytes = None
        self.fernet: Fernet = None

    async def generate_key(self):

        if self._loop is None:
            self._loop = asyncio.get_running_loop()

        self.key = await self._loop.run_in_executor(
            self._executor,
            Fernet.generate_key
        )

        self.fernet = Fernet(self.key)

    async def load_key_from_env(
        self,
        key_name: str
    ):
        self.key = await self._shell.get_envar(key_name)

        self.fernet = Fernet(self.key)

    async def encrypt(
        self,
        secret: bytes
    ) -> bytes:
        
        if self._loop is None:
            self._loop = asyncio.get_running_loop()

        if self.fernet is None:
            await self.generate_key()
            self.fernet = Fernet(self.key)

        encrypted_secret = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self.fernet.encrypt,
                secret
            )
        )

        return encrypted_secret
    
    async def decrypt(
        self,
        secret: bytes,
        key: Optional[str]=None
    ) -> bytes:
        
        if self._loop is None:
            self._loop = asyncio.get_running_loop()

        if key is None and self.key is None:
            raise MissingEncryptionKeyError()
        
        elif key is None:
            key = self.key
        
        if self.fernet is None:
            self.fernet = Fernet(key)
        
        decrypted_secret = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self.fernet.decrypt,
                secret
            )
        )

        return decrypted_secret
    
    async def encrypt_nacl(
        self,
        secret: bytes
    ) -> bytes:
        if self._loop is None:
            self._loop = asyncio.get_running_loop()

        if self.key is None:
            raise MissingEncryptionKeyError()
        
        public_key = public.PublicKey(self.key, encoding.Base64Encoder())
        sealed_box = public.SealedBox(public_key)
        
        encrypted = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                sealed_box.encrypt,
                secret
            )
        )

        base64_secret = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                b64encode,
                encrypted
            )
        )

        return base64_secret
    
    async def decrypt_nacl(
        self,
        secret: bytes
    ) -> bytes:
        
        if self._loop is None:
            self._loop = asyncio.get_running_loop()

        if key is None and self.key is None:
            raise MissingEncryptionKeyError()
        
        elif key is None:
            key = self.key
        
        public_key = public.PublicKey(key, encoding.Base64Encoder())
        sealed_box = public.SealedBox(public_key)

        base64_secret = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                b64decode,
                secret
            )
        )
        
        decrypted = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                sealed_box.decrypt,
                base64_secret
            )
        )

        return decrypted

    async def encrypt_aes256gcm(
        self,
        secret: bytes
    ) -> bytes:
        key = secrets.token_bytes(32)
        nonce = secrets.token_bytes(12)
        return key + nonce + AESGCM(key).encrypt(
            nonce, 
            secret, 
            b""
        )

    async def decrypt_aes256gcm(
        self,
        secret: bytes
    ) -> bytes:
        key = secret[:32]
        nonce = secret[32:44]
        return AESGCM(key).decrypt(
            nonce, 
            secret[44:], 
            b""
        )
    
    async def dump_key_to_file(
        self,
        key: Optional[bytes]=None,
        name: str='secret',
        path: str=None,
        encoding: str='utf-8'
    ) -> None:
        
        if self._loop is None:
            self._loop = asyncio.get_running_loop()


        if path is None:
            path = await self._shell.get_current_directory()

        key_filepath = os.path.join(
            path,
            f'{name}.key'
        )
        
        if key is None and self.key is None:
            raise MissingEncryptionKeyError()
        
        elif key is None:
            key = self.key

        await self._shell.pipe_to_file(
            key_filepath,
            key.decode(encoding),
            overwrite=True,
            silent=True
        )

    async def dump_key_to_env(
        self,
        keyname: str,
        key: Optional[bytes]=None,
    ):
        if self._loop is None:
            self._loop = asyncio.get_running_loop()

        if key is None and self.key is None:
            raise MissingEncryptionKeyError()
        
        elif key is None:
            key = self.key

        await self._shell.set_envar(
            keyname,
            key
        )

    async def load_key_from_file(
        self,
        key_filename: str='secret.key',
        path: str=None,  
    ) -> None:
        
        if self._loop is None:
            self._loop = asyncio.get_running_loop()

        if path is None:
            path = await self._shell.get_current_directory()

        key_filepath = os.path.join(
            path,
            key_filename
        )

        self.key = await self._shell.read_file_as_bytes(
            key_filepath,
            silent=True
        )

        self.fernet = Fernet(self.key)

    async def close(self):
        await self._shell.close()
        await self._system.close()
        self._executor.shutdown()

    def abort(self):
        self._shell.abort()
        self._system.abort()
        self._executor.shutdown()

