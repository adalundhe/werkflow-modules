import asyncio
import functools
import json
import pathlib
from typing import Any, Dict, Literal, Optional, Union

import boto3
from werkflow_aws.models import AWSCredentialsSet
from werkflow_secrets import Secrets
from werkflow_shell import Shell


class AWSCredentials:

    def __init__(self) -> None:
        self._error: Union[Exception, None] = None
        self._loop: Optional[asyncio.AbstractEventLoop] = None

        self._secrets = Secrets()
        self._shell = Shell()

        self.profile: Union[str, None] = None
        self.role: Union[str, None] = None
        self.account_id: Union[str, None] = None
        self.cache_filename: Union[str, None] = None
        self.access_token: Union[str, None] = None

        self.credentials: Union[AWSCredentialsSet, None] = None

    def _get_loop(self) -> asyncio.AbstractEventLoop:
        if self._loop is None or self._loop.is_closed():
            self._loop = asyncio.get_running_loop()
        return self._loop

    async def sso(
        self,
        profile_name: str,
    ) -> None:
        loop = self._get_loop()
        await loop.run_in_executor(
            None,
            functools.partial(
                boto3.setup_default_session,
                profile_name=profile_name,
            ),
        )

    async def get_credentials(
        self,
        profile: Optional[str] = None,
        cache_path: Optional[str] = None,
    ) -> AWSCredentialsSet:
        if profile is None:
            profile = await self._shell.get_envar('AWS_PROFILE', 'dev') or 'dev'

        self.profile = profile

        if not self.cache_filename:
            self.cache_filename = await self.get_cache_filename(
                cache_path=cache_path,
            )

        role = await self.get_role(profile=profile)
        account_id = await self.get_account_id(profile=profile)
        access_token = await self.get_access_token(cache_path=cache_path)

        command_parameters = ' '.join([
            f'--account-id={account_id}',
            f'--access-token={access_token}',
            '--output json',
            f'--profile={profile}',
            f'--role-name={role}',
        ])

        process_result = await self._shell.run(
            f'aws --profile={profile} sso get-role-credentials {command_parameters}',
            silent=True,
        )

        raw_stdout = (process_result.stdout or '').strip()
        parsed_payload: Dict[str, Any] = json.loads(raw_stdout) if raw_stdout else {}
        role_creds: Dict[str, Any] = parsed_payload.get('roleCredentials', parsed_payload)

        self.credentials = AWSCredentialsSet(
            aws_access_key_id=role_creds.get('accessKeyId'),
            aws_secret_access_key=role_creds.get('secretAccessKey'),
            aws_session_token=role_creds.get('sessionToken'),
            aws_profile=profile,
        )

        return self.credentials

    async def get_credentials_from_env(self) -> AWSCredentialsSet:
        aws_access_key_id = await self._shell.get_envar('AWS_ACCESS_KEY_ID')
        aws_secret_access_key = await self._shell.get_envar('AWS_SECRET_ACCESS_KEY')
        aws_session_token = await self._shell.get_envar('AWS_SESSION_TOKEN')
        aws_profile = await self._shell.get_envar('AWS_PROFILE')

        self.credentials = AWSCredentialsSet(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token,
            aws_profile=aws_profile,
        )

        return self.credentials

    @staticmethod
    def _decode_secret_value(value: Union[str, bytes, None]) -> Optional[str]:
        if value is None:
            return None
        if isinstance(value, bytes):
            return value.decode('utf-8')
        return value

    async def get_encrypted_credentials_from_env(
        self,
        encryption_method: Literal['basic', 'aes256gcm'] = 'basic',
        key_name: str = 'WERKFLOW_ENCRYPTION_KEY',
    ) -> AWSCredentialsSet:
        await self._secrets.load_key_from_env(key_name)

        aws_access_key_id = self._decode_secret_value(
            await self._secrets.load_from_env(
                'AWS_ACCESS_KEY_ID',
                method=encryption_method,
            )
        )
        aws_secret_access_key = self._decode_secret_value(
            await self._secrets.load_from_env(
                'AWS_SECRET_ACCESS_KEY',
                method=encryption_method,
            )
        )
        aws_session_token = self._decode_secret_value(
            await self._secrets.load_from_env(
                'AWS_SESSION_TOKEN',
                method=encryption_method,
            )
        )

        self.credentials = AWSCredentialsSet(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token,
        )
        return self.credentials

    async def get_encrypted_credentials_from_file(
        self,
        access_key_id_path: Optional[str] = None,
        secret_access_key_path: Optional[str] = None,
        session_token_path: Optional[str] = None,
        keyname: str = 'secret',
        key_filepath: Optional[str] = None,
        encryption_method: Literal['basic', 'aes256gcm'] = 'basic',
    ) -> AWSCredentialsSet:
        await self._secrets.load_key(
            name=keyname,
            path=key_filepath,
        )

        aws_access_key_id = self._decode_secret_value(
            await self._secrets.load_from_file(
                path=access_key_id_path,
                method=encryption_method,
            )
        ) if access_key_id_path is not None else None

        aws_secret_access_key = self._decode_secret_value(
            await self._secrets.load_from_file(
                path=secret_access_key_path,
                method=encryption_method,
            )
        ) if secret_access_key_path is not None else None

        aws_session_token = self._decode_secret_value(
            await self._secrets.load_from_file(
                path=session_token_path,
                method=encryption_method,
            )
        ) if session_token_path is not None else None

        self.credentials = AWSCredentialsSet(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token,
        )
        return self.credentials

    async def get_role(
        self,
        profile: Optional[str] = None,
    ) -> str:
        if profile is None:
            profile = await self._shell.get_envar('AWS_PROFILE', 'dev') or 'dev'

        process_result = await self._shell.run(
            f'aws --profile={profile} configure get sso_role_name',
            silent=True,
        )

        self.role = (process_result.stdout or '').strip()
        return self.role

    async def get_account_id(
        self,
        profile: Optional[str] = None,
    ) -> str:
        if profile is None:
            profile = await self._shell.get_envar('AWS_PROFILE', 'dev') or 'dev'

        process_result = await self._shell.run(
            f'aws --profile={profile} configure get sso_account_id',
            silent=True,
        )

        self.account_id = (process_result.stdout or '').strip()
        return self.account_id

    async def get_cache_filename(
        self,
        cache_path: Optional[str] = None,
    ) -> str:
        if cache_path is None:
            cache_path = '~/.aws/sso/cache'

        resolved_dir = await self._shell.to_absolute_path(cache_path)
        loop = self._get_loop()

        def _find_cache_file() -> str:
            cache_dir = pathlib.Path(resolved_dir)
            if not cache_dir.is_dir():
                raise FileNotFoundError(f'AWS SSO cache directory not found: {resolved_dir}')

            json_files = sorted(
                cache_dir.glob('*.json'),
                key=lambda p: p.stat().st_mtime,
                reverse=True,
            )
            for candidate in json_files:
                try:
                    content = json.loads(candidate.read_text(encoding='utf-8'))
                except (OSError, json.JSONDecodeError):
                    continue
                if isinstance(content, dict) and 'accessToken' in content:
                    return str(candidate)

            raise FileNotFoundError(
                f'No AWS SSO cache file containing accessToken found in {resolved_dir}'
            )

        self.cache_filename = await loop.run_in_executor(None, _find_cache_file)
        return self.cache_filename

    async def get_access_token(
        self,
        cache_path: Optional[str] = None,
    ) -> str:
        if not self.cache_filename:
            self.cache_filename = await self.get_cache_filename(
                cache_path=cache_path,
            )

        cache_data = await self._shell.read_file(
            self.cache_filename,
            silent=True,
        )

        data: Dict[str, Any] = json.loads(cache_data)
        self.access_token = data.get('accessToken')

        if self.access_token is None:
            raise ValueError(
                f'Err. - Access token not found in cache file {self.cache_filename}'
            )

        return self.access_token

    async def close(self) -> None:
        await self._secrets.close()
        await self._shell.close()

    def abort(self) -> None:
        self._secrets.abort()
        self._shell.abort()
