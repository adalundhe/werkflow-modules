import functools
from typing import Any

import boto3
from botocore.config import Config

from werkflow_aws.models import (
    RegionName,
)
from werkflow_aws.models.sts import (
    AssumeRoleRequest,
    AssumedRoleResponse,
    AssumeRoleWithWebIdentityRequest,
    AssumeRoleWithWebIdentityResponse,
    DecodeAuthorizationMessageRequest,
    DecodeAuthorizationMessageResponse,
    GetAccessKeyInfoRequest,
    GetAccessKeyInfoResponse,
    GetCallerIdentityRequest,
    GetCallerIdentityResponse,
    GetSessionTokenRequest,
    GetSessionTokenResponse,
)
from werkflow_aws.types import STSClient
from .base import AWSBaseService
from werkflow_aws.models.sts import (
    STSAssumeRoleWithSAMLRequest,
    STSAssumeRoleWithSAMLResponse,
    STSAssumeRootRequest,
    STSAssumeRootResponse,
    STSGetDelegatedAccessTokenRequest,
    STSGetDelegatedAccessTokenResponse,
    STSGetFederationTokenRequest,
    STSGetFederationTokenResponse,
    STSGetScopedCredentialsRequest,
    STSGetScopedCredentialsResponse,
    STSGetWebIdentityTokenRequest,
    STSGetWebIdentityTokenResponse,
)


class AWSSTS(AWSBaseService[STSClient]):
    service_name = 'STS'
    boto3_service_name = 'sts'

    def __init__(self) -> None:
        super().__init__(service_name='STS', boto3_service_name='sts')
        self._proxy_client: STSClient | None = None

    async def connect_unauthorized(
        self,
        region: RegionName,
    ) -> None:
        await self.connect(region=region, credentials=None)

    async def assume_role_by_proxy(
        self,
        assume_role_request: AssumeRoleRequest,
        assume_proxy_role_request: AssumeRoleRequest,
        region: RegionName,
    ) -> AssumedRoleResponse:
        client = self._require_client()
        loop = self._get_loop()
        aws_region = self._regions.get(region)

        proxy_response = await loop.run_in_executor(
            self._executor,
            functools.partial(
                client.assume_role,
                **assume_proxy_role_request.model_dump(exclude_none=True),
            ),
        )
        assumed_proxy_response = AssumedRoleResponse(**proxy_response)
        if assumed_proxy_response.Credentials is None:
            raise RuntimeError('STS assume_role returned no proxy credentials.')

        proxy_client: Any = await loop.run_in_executor(
            self._executor,
            functools.partial(
                boto3.client,
                'sts',
                aws_access_key_id=assumed_proxy_response.Credentials.AccessKeyId,
                aws_secret_access_key=assumed_proxy_response.Credentials.SecretAccessKey,
                aws_session_token=assumed_proxy_response.Credentials.SessionToken,
                config=Config(region_name=aws_region.value),
            ),
        )
        self._proxy_client = proxy_client

        try:
            assume_response = await loop.run_in_executor(
                self._executor,
                functools.partial(
                    proxy_client.assume_role,
                    **assume_role_request.model_dump(exclude_none=True),
                ),
            )
            return AssumedRoleResponse(**assume_response)
        finally:
            await loop.run_in_executor(None, proxy_client.close)
            if self._proxy_client is proxy_client:
                self._proxy_client = None

    async def assume_role(
        self,
        assume_role_request: AssumeRoleRequest,
    ) -> AssumedRoleResponse:
        client = self._require_client()
        return await self._execute(
            client.assume_role,
            assume_role_request,
            AssumedRoleResponse,
        )

    async def assume_role_with_web_identity(
        self,
        request: AssumeRoleWithWebIdentityRequest,
    ) -> AssumeRoleWithWebIdentityResponse:
        client = self._require_client()
        return await self._execute(
            client.assume_role_with_web_identity,
            request,
            AssumeRoleWithWebIdentityResponse,
        )

    async def get_caller_identity(
        self,
        request: GetCallerIdentityRequest | None = None,
    ) -> GetCallerIdentityResponse:
        client = self._require_client()
        return await self._execute(
            client.get_caller_identity,
            request,
            GetCallerIdentityResponse,
        )

    async def get_session_token(
        self,
        request: GetSessionTokenRequest | None = None,
    ) -> GetSessionTokenResponse:
        client = self._require_client()
        return await self._execute(
            client.get_session_token,
            request or GetSessionTokenRequest(),
            GetSessionTokenResponse,
        )

    async def decode_authorization_message(
        self,
        request: DecodeAuthorizationMessageRequest,
    ) -> DecodeAuthorizationMessageResponse:
        client = self._require_client()
        return await self._execute(
            client.decode_authorization_message,
            request,
            DecodeAuthorizationMessageResponse,
        )

    async def get_access_key_info(
        self,
        request: GetAccessKeyInfoRequest,
    ) -> GetAccessKeyInfoResponse:
        client = self._require_client()
        return await self._execute(
            client.get_access_key_info,
            request,
            GetAccessKeyInfoResponse,
        )

    async def close(self) -> None:
        if self._proxy_client is not None:
            proxy_client: Any = self._proxy_client
            self._proxy_client = None
            try:
                loop = self._get_loop()
                await loop.run_in_executor(None, proxy_client.close)
            except RuntimeError:
                proxy_client.close()
        await super().close()

    def abort(self) -> None:
        if self._proxy_client is not None:
            proxy_client: Any = self._proxy_client
            self._proxy_client = None
            proxy_client.close()
        super().abort()

    async def assume_role_with_saml(
        self,
        request: STSAssumeRoleWithSAMLRequest,
    ) -> STSAssumeRoleWithSAMLResponse:
        client = self._require_client()
        return await self._execute(client.assume_role_with_saml, request, STSAssumeRoleWithSAMLResponse)

    async def assume_root(
        self,
        request: STSAssumeRootRequest,
    ) -> STSAssumeRootResponse:
        client = self._require_client()
        return await self._execute(client.assume_root, request, STSAssumeRootResponse)

    async def get_delegated_access_token(
        self,
        request: STSGetDelegatedAccessTokenRequest,
    ) -> STSGetDelegatedAccessTokenResponse:
        client = self._require_client()
        return await self._execute(client.get_delegated_access_token, request, STSGetDelegatedAccessTokenResponse)

    async def get_federation_token(
        self,
        request: STSGetFederationTokenRequest,
    ) -> STSGetFederationTokenResponse:
        client = self._require_client()
        return await self._execute(client.get_federation_token, request, STSGetFederationTokenResponse)

    async def get_scoped_credentials(
        self,
        request: STSGetScopedCredentialsRequest | None = None,
    ) -> STSGetScopedCredentialsResponse:
        client = self._require_client()
        return await self._execute(client.get_scoped_credentials, request, STSGetScopedCredentialsResponse)

    async def get_web_identity_token(
        self,
        request: STSGetWebIdentityTokenRequest,
    ) -> STSGetWebIdentityTokenResponse:
        client = self._require_client()
        return await self._execute(client.get_web_identity_token, request, STSGetWebIdentityTokenResponse)

