import asyncio
import functools
import hashlib
import os
import secrets
from base64 import b64decode, b64encode
from concurrent.futures import ThreadPoolExecutor
from typing import Any, NamedTuple, Optional, Union

from werkflow_core import Module
from werkflow_core.exceptions import MissingModuleError
from werkflow_shell import Shell
from werkflow_system import System

from .exceptions import MissingEncryptionKeyError

try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    _cryptography_available = True
except ImportError:
    _cryptography_available = False
    Fernet = None  # type: ignore[assignment,misc]
    AESGCM = None  # type: ignore[assignment,misc]

try:
    from nacl import encoding, public
    _pynacl_available = True
except ImportError:
    _pynacl_available = False
    encoding = None  # type: ignore[assignment]
    public = None  # type: ignore[assignment]

module_enabled = _cryptography_available


class NaClKeyPair(NamedTuple):
    public_key: bytes
    private_key: bytes


class Encryption(Module):
    module_enabled = module_enabled
    dependencies = [
        'cryptography',
        'pynacl',
        'werkflow-shell',
        'werkflow-system',
    ]

    def __init__(self) -> None:
        super().__init__()
        if (
            not self.module_enabled
            or Fernet is None
            or AESGCM is None
        ):
            raise MissingModuleError(self)

        self._system = System()
        self._shell = Shell()
        self._loop: Optional[asyncio.AbstractEventLoop] = None
        self._executor = ThreadPoolExecutor(
            max_workers=self._system.configuration.cores.physical
        )

        self.key: Optional[bytes] = None
        self.fernet: Optional[Fernet] = None

    def _ensure_enabled(self) -> None:
        if (
            not self.module_enabled
            or Fernet is None
            or AESGCM is None
        ):
            raise MissingModuleError(self)

    def _ensure_nacl_enabled(self) -> None:
        self._ensure_enabled()
        if not _pynacl_available or public is None or encoding is None:
            raise MissingModuleError(self)

    def _get_loop(self) -> asyncio.AbstractEventLoop:
        if self._loop is None or self._loop.is_closed():
            self._loop = asyncio.get_running_loop()
        return self._loop

    @staticmethod
    def _to_bytes(value: Union[bytes, str]) -> bytes:
        return value.encode('utf-8') if isinstance(value, str) else value

    @staticmethod
    def _derive_aes256_key(key: Union[bytes, str]) -> bytes:
        raw = key.encode('utf-8') if isinstance(key, str) else key
        if len(raw) == 32:
            return raw
        return hashlib.sha256(raw).digest()

    @staticmethod
    def _load_nacl_public_key(raw_key: Union[bytes, str]) -> Any:
        assert public is not None and encoding is not None
        key_bytes = raw_key.encode('utf-8') if isinstance(raw_key, str) else raw_key
        if len(key_bytes) == 32:
            return public.PublicKey(key_bytes)
        return public.PublicKey(key_bytes, encoder=encoding.Base64Encoder)

    @staticmethod
    def _load_nacl_private_key(raw_key: Union[bytes, str]) -> Any:
        assert public is not None and encoding is not None
        key_bytes = raw_key.encode('utf-8') if isinstance(raw_key, str) else raw_key
        if len(key_bytes) == 32:
            return public.PrivateKey(key_bytes)
        return public.PrivateKey(key_bytes, encoder=encoding.Base64Encoder)

    async def generate_key(self) -> bytes:
        self._ensure_enabled()
        assert Fernet is not None
        loop = self._get_loop()

        self.key = await loop.run_in_executor(
            self._executor,
            Fernet.generate_key,
        )
        self.fernet = Fernet(self.key)
        return self.key

    async def generate_aes_key(self) -> bytes:
        self._ensure_enabled()
        loop = self._get_loop()

        aes_key = await loop.run_in_executor(
            self._executor,
            lambda: b64encode(secrets.token_bytes(32)),
        )
        self.key = aes_key
        self.fernet = None
        return aes_key

    async def generate_nacl_keypair(self) -> NaClKeyPair:
        self._ensure_nacl_enabled()
        loop = self._get_loop()

        def _generate() -> NaClKeyPair:
            assert public is not None and encoding is not None
            private_key = public.PrivateKey.generate()
            public_key_bytes = private_key.public_key.encode(
                encoder=encoding.Base64Encoder
            )
            private_key_bytes = private_key.encode(
                encoder=encoding.Base64Encoder
            )
            return NaClKeyPair(
                public_key=public_key_bytes,
                private_key=private_key_bytes,
            )

        return await loop.run_in_executor(self._executor, _generate)

    async def load_key_from_env(
        self,
        key_name: str,
    ) -> bytes:
        self._ensure_enabled()
        assert Fernet is not None

        raw_key = await self._shell.get_envar(key_name)
        if raw_key is None:
            raise MissingEncryptionKeyError(
                f"No encryption key found in environment variable '{key_name}'."
            )

        self.key = raw_key.encode('utf-8') if isinstance(raw_key, str) else raw_key
        try:
            self.fernet = Fernet(self.key)
        except ValueError:
            self.fernet = None
        return self.key

    async def encrypt(
        self,
        secret: Union[bytes, str],
        key: Optional[Union[bytes, str]] = None,
    ) -> bytes:
        self._ensure_enabled()
        assert Fernet is not None
        loop = self._get_loop()

        secret_bytes = self._to_bytes(secret)

        if key is not None:
            fernet = Fernet(self._to_bytes(key))
        else:
            if self.fernet is None:
                if self.key is not None:
                    self.fernet = Fernet(self.key)
                else:
                    await self.generate_key()
            assert self.fernet is not None
            fernet = self.fernet

        return await loop.run_in_executor(
            self._executor,
            functools.partial(fernet.encrypt, secret_bytes),
        )

    async def decrypt(
        self,
        secret: Union[bytes, str],
        key: Optional[Union[bytes, str]] = None,
    ) -> bytes:
        self._ensure_enabled()
        assert Fernet is not None
        loop = self._get_loop()

        secret_bytes = self._to_bytes(secret)

        if key is not None:
            fernet = Fernet(self._to_bytes(key))
        else:
            if self.key is None:
                raise MissingEncryptionKeyError()
            if self.fernet is None:
                self.fernet = Fernet(self.key)
            fernet = self.fernet

        return await loop.run_in_executor(
            self._executor,
            functools.partial(fernet.decrypt, secret_bytes),
        )

    async def encrypt_nacl(
        self,
        secret: Union[bytes, str],
        public_key: Optional[Union[bytes, str]] = None,
    ) -> bytes:
        self._ensure_nacl_enabled()
        loop = self._get_loop()

        resolved_key = public_key if public_key is not None else self.key
        if resolved_key is None:
            raise MissingEncryptionKeyError()

        secret_bytes = self._to_bytes(secret)

        def _encrypt() -> bytes:
            assert public is not None
            pub_key = self._load_nacl_public_key(resolved_key)
            sealed_box = public.SealedBox(pub_key)
            encrypted = sealed_box.encrypt(secret_bytes)
            return b64encode(encrypted)

        return await loop.run_in_executor(self._executor, _encrypt)

    async def decrypt_nacl(
        self,
        secret: Union[bytes, str],
        private_key: Optional[Union[bytes, str]] = None,
        key: Optional[Union[bytes, str]] = None,
    ) -> bytes:
        self._ensure_nacl_enabled()
        loop = self._get_loop()

        resolved_key = (
            private_key
            if private_key is not None
            else (key if key is not None else self.key)
        )
        if resolved_key is None:
            raise MissingEncryptionKeyError()

        secret_bytes = self._to_bytes(secret)

        def _decrypt() -> bytes:
            assert public is not None
            priv_key = self._load_nacl_private_key(resolved_key)
            sealed_box = public.SealedBox(priv_key)
            decoded = b64decode(secret_bytes)
            return sealed_box.decrypt(decoded)

        return await loop.run_in_executor(self._executor, _decrypt)

    async def encrypt_aes256gcm(
        self,
        data: Union[bytes, str],
        key: Optional[Union[bytes, str]] = None,
    ) -> bytes:
        self._ensure_enabled()
        loop = self._get_loop()

        resolved_key = key if key is not None else self.key
        if resolved_key is None:
            raise MissingEncryptionKeyError()

        aes_key = self._derive_aes256_key(resolved_key)
        data_bytes = self._to_bytes(data)

        def _encrypt() -> bytes:
            assert AESGCM is not None
            nonce = secrets.token_bytes(12)
            ciphertext = AESGCM(aes_key).encrypt(nonce, data_bytes, b'')
            return nonce + ciphertext

        return await loop.run_in_executor(self._executor, _encrypt)

    async def decrypt_aes256gcm(
        self,
        secret: bytes,
        key: Optional[Union[bytes, str]] = None,
    ) -> bytes:
        self._ensure_enabled()
        loop = self._get_loop()

        resolved_key = key if key is not None else self.key
        if resolved_key is None:
            raise MissingEncryptionKeyError()

        if len(secret) < 28:
            raise ValueError(
                'Invalid AES-256-GCM ciphertext: payload must include 12-byte nonce and 16-byte tag.'
            )

        aes_key = self._derive_aes256_key(resolved_key)

        def _decrypt() -> bytes:
            assert AESGCM is not None
            nonce = secret[:12]
            ciphertext = secret[12:]
            return AESGCM(aes_key).decrypt(nonce, ciphertext, b'')

        return await loop.run_in_executor(self._executor, _decrypt)

    async def dump_key_to_file(
        self,
        key: Optional[Union[bytes, str]] = None,
        name: str = 'secret',
        path: Optional[str] = None,
        encoding: str = 'utf-8',
    ) -> None:
        self._ensure_enabled()

        if path is None:
            target_path = await self._shell.get_current_directory()
        else:
            target_path = await self._shell.to_absolute_path(path)

        key_filepath = os.path.join(target_path, f'{name}.key')

        resolved_key = key if key is not None else self.key
        if resolved_key is None:
            raise MissingEncryptionKeyError()

        payload: Union[str, bytes]
        if isinstance(resolved_key, bytes):
            try:
                payload = resolved_key.decode(encoding)
            except UnicodeDecodeError:
                payload = resolved_key
        else:
            payload = resolved_key

        await self._shell.pipe_to_file(
            key_filepath,
            payload,
            overwrite=True,
            silent=True,
        )

    async def dump_key_to_env(
        self,
        keyname: str,
        key: Optional[Union[bytes, str]] = None,
    ) -> None:
        self._ensure_enabled()

        resolved_key = key if key is not None else self.key
        if resolved_key is None:
            raise MissingEncryptionKeyError()

        if isinstance(resolved_key, bytes):
            try:
                key_value = resolved_key.decode('utf-8')
            except UnicodeDecodeError:
                key_value = b64encode(resolved_key).decode('ascii')
        else:
            key_value = resolved_key

        await self._shell.set_envar(keyname, key_value)

    async def load_key_from_file(
        self,
        key_filename: str = 'secret.key',
        path: Optional[str] = None,
        keyname: Optional[str] = None,
    ) -> bytes:
        self._ensure_enabled()
        assert Fernet is not None

        if path is None:
            target_path = await self._shell.get_current_directory()
        else:
            target_path = await self._shell.to_absolute_path(path)

        resolved_filename = key_filename
        if keyname is not None:
            candidate = os.path.join(target_path, keyname)
            if (
                not await self._shell.check_path_exists(candidate)
                and not keyname.endswith('.key')
                and await self._shell.check_path_exists(f'{candidate}.key')
            ):
                resolved_filename = f'{keyname}.key'
            else:
                resolved_filename = keyname

        key_filepath = os.path.join(target_path, resolved_filename)

        self.key = await self._shell.read_file_as_bytes(
            key_filepath,
            silent=True,
        )

        try:
            self.fernet = Fernet(self.key)
        except ValueError:
            self.fernet = None
        return self.key

    async def close(self) -> None:
        await self._shell.close()
        await self._system.close()
        try:
            loop = self._get_loop()
            await loop.run_in_executor(None, self._executor.shutdown, True)
        except RuntimeError:
            self._executor.shutdown(wait=True)

    def abort(self) -> None:
        self._shell.abort()
        self._system.abort()
        self._executor.shutdown(wait=False, cancel_futures=True)
