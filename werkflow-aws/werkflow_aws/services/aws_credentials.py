import asyncio
import boto3
import json
import functools
from werkflow_aws.models import AWSCredentialsSet
from werkflow_secrets import Secrets
from werkflow_shell import Shell
from typing import (
    Union, 
    Optional, 
    Dict, 
    Literal
)


class AWSCredentials:

    def __init__(self):

        self._error: Union[Exception, None] = None

        self._secrets = Secrets()
        self._shell = Shell()

        self.profile: Union[str, None] = None
        self.role: Union[str, None] = None
        self.account_id: Union[str, None] = None
        self.cache_filename: Union[str, None] = None
        self.access_token: Union[str, None] = None

        self.credentials: Union[AWSCredentialsSet, None] = None
    
    async def sso(
        self,
        profile_name: str,
    ):

        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        await self._loop.run_in_executor(
            None,
            functools.partial(
                boto3.setup_default_session,
                profile_name=profile_name
            )
        )

    async def get_credentials(
        self,
        profile: Optional[str]=None,
        cache_path: Optional[str]=None
    ) -> AWSCredentialsSet:
        if profile is None:
            profile = await self._shell.get_envar('AWS_PROFILE', 'dev')

        if not self.cache_filename:
            self.cache_filename = await self.get_cache_filename(
                cache_path=cache_path
            )

        role = await self.get_role(
            profile=profile
        )

        account_id = await self.get_account_id(
            profile=profile
        )

        access_token = await self.get_access_token(
            cache_path=cache_path
        )

        command_parameters = ' '.join([
            f'--account-id={account_id}',
            f'--access-token={access_token}',
            '--output json',
            f'--profile={profile}',
            f'--role-name={role}'
        ])


        aws_role_credentials: Dict[str, str] = await self._shell.run(
            f'aws --profile={profile} sso get-role-credentials {command_parameters}'
        )

        if isinstance(aws_role_credentials, dict) is False:
            aws_role_credentials = {}

        aws_access_key_id = aws_role_credentials.get('accessKeyId')

        aws_secret_access_key = aws_role_credentials.get('secretAccessKey')

        aws_session_token = aws_role_credentials.get('sessionToken')
        
        self.credentials = AWSCredentialsSet(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token
        )

        return self.credentials

    async def get_credentials_from_env(self) -> AWSCredentialsSet:

        aws_access_key_id = await self._shell.get_envar('AWS_ACCESS_KEY_ID')
        aws_secret_access_key = await self._shell.get_envar('AWS_SECRET_ACCESS_KEY')
        aws_session_token = await self._shell.get_envar('AWS_SESSION_TOKEN')

        self.credentials = AWSCredentialsSet(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token
        )

        return self.credentials

    async def get_encrypted_credentials_from_env(
        self,
        encryption_method: Literal['basic', 'aes256gcm']='basic'
    ):

        await self._secrets.load_key_from_env()

        aws_access_key_id = await self._secrets.load_from_env(
            'AWS_ACCESS_KEY_ID',
            method=encryption_method
        )

        aws_secret_access_key = await self._secrets.load_from_env(
            'AWS_SECRET_ACCESS_KEY',
            method=encryption_method
        )

        aws_session_token = await self._secrets.load_from_env(
            'AWS_SESSION_TOKEN',
            method=encryption_method
        )

        return AWSCredentialsSet(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token
        )
    
    async def get_encrypted_credentials_from_file(
        self,
        access_key_id_path: Optional[str]=None,
        secret_access_key_path: Optional[str]=None,
        session_token_path: Optional[str]=None,
        keyname: str='secret',
        key_filepath: Optional[str]=None,
        encryption_method: Literal['basic', 'aes256gcm']='basic'
    ):

        await self._secrets.load_key_from_file(
            keyname=keyname,
            path=key_filepath
        )

        aws_access_key_id = await self._secrets.load_from_file(
            path=access_key_id_path,
            method=encryption_method
        )

        aws_secret_access_key = await self._secrets.load_from_file(
            path=secret_access_key_path,
            method=encryption_method
        )

        aws_session_token = await self._secrets.load_from_file(
            path=session_token_path,
            method=encryption_method
        )

        return AWSCredentialsSet(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token
        )

    async def get_role(
        self,
        profile: Optional[str]=None
    ):
        
        if profile is None:
            profile = await self._shell.get_envar('AWS_PROFILE', 'dev')

        process_result = await self._shell.run(
            f'aws --profile={profile} configure get sso_role_name configure get sso_account_id',
            silent=True
        )

        self.role = process_result.stdout

        return self.role
    
    async def get_account_id(
        self,
        profile: Optional[str]=None
    ):
        
        if profile is None:
            profile = await self._shell.get_envar('AWS_PROFILE', 'dev')

        process_result = await self._shell.run(
            f'aws --profile={profile} configure get sso_account_id',
            silent=True
        )

        self.account_id = process_result.stdout

        return self.account_id
    
    async def get_cache_filename(
        self,
        cache_path: Optional[str]=None
    ):
        
        if cache_path is None:
            cache_path = '~/.aws/sso/cache'
        
        cache_path = await self._shell.to_absolute_path(cache_path)

        process_result = await self._shell.run(
            f'grep -rl "accessToken" {cache_path}',
            silent=True
        )

        self.cache_filename = process_result

        return self.cache_filename
    
    async def get_access_token(
        self,
        cache_path: Optional[str]=None
    ):
        
        if not self.cache_filename:
            self.cache_filename = await self.get_cache_filename(
                cache_path=cache_path
            )

        cache_data = await self._shell.read_file(
            self.cache_filename,
            silent=True
        )

        data: Dict[str, str] = json.loads(cache_data)

        self.access_token = data.get('accessToken')

        if self.access_token is None:
            raise Exception(f'Err. - Access token not found in cache file {self.cache_filename}')
        
        return self.access_token

    async def close(self):
        await self._secrets.close()
        await self._shell.close()

    def abort(self):
        self._secrets.abort()
        self._shell.abort()