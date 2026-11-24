from werkflow_aws.models.mwa import (
    MWAACreateCliTokenRequest,
    MWAACreateCliTokenResponse,
    MWAACreateEnvironmentRequest,
    MWAACreateEnvironmentResponse,
    MWAACreateWebLoginTokenRequest,
    MWAACreateWebLoginTokenResponse,
    MWAADeleteEnvironmentRequest,
    MWAADeleteEnvironmentResponse,
    MWAAGetEnvironmentRequest,
    MWAAGetEnvironmentResponse,
    MWAAInvokeRestApiRequest,
    MWAAInvokeRestApiResponse,
    MWAAListEnvironmentsRequest,
    MWAAListEnvironmentsResponse,
    MWAAListTagsForResourceRequest,
    MWAAListTagsForResourceResponse,
    MWAAPublishMetricsRequest,
    MWAAPublishMetricsResponse,
    MWAATagResourceRequest,
    MWAATagResourceResponse,
    MWAAUntagResourceRequest,
    MWAAUntagResourceResponse,
    MWAAUpdateEnvironmentRequest,
    MWAAUpdateEnvironmentResponse,
)
from werkflow_aws.types.mwa_client import MWAAClient
from .base import AWSBaseService


class AWSMWAA(AWSBaseService[MWAAClient]):
    service_name = 'mwa'
    boto3_service_name = 'mwaa'

    def __init__(self) -> None:
        super().__init__(service_name='mwa', boto3_service_name='mwaa')

    async def create_cli_token(
        self,
        request: MWAACreateCliTokenRequest,
    ) -> MWAACreateCliTokenResponse:
        client = self._require_client()
        return await self._execute(client.create_cli_token, request, MWAACreateCliTokenResponse)

    async def create_environment(
        self,
        request: MWAACreateEnvironmentRequest,
    ) -> MWAACreateEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.create_environment, request, MWAACreateEnvironmentResponse)

    async def create_web_login_token(
        self,
        request: MWAACreateWebLoginTokenRequest,
    ) -> MWAACreateWebLoginTokenResponse:
        client = self._require_client()
        return await self._execute(client.create_web_login_token, request, MWAACreateWebLoginTokenResponse)

    async def delete_environment(
        self,
        request: MWAADeleteEnvironmentRequest,
    ) -> MWAADeleteEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_environment, request, MWAADeleteEnvironmentResponse)

    async def get_environment(
        self,
        request: MWAAGetEnvironmentRequest,
    ) -> MWAAGetEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.get_environment, request, MWAAGetEnvironmentResponse)

    async def invoke_rest_api(
        self,
        request: MWAAInvokeRestApiRequest,
    ) -> MWAAInvokeRestApiResponse:
        client = self._require_client()
        return await self._execute(client.invoke_rest_api, request, MWAAInvokeRestApiResponse)

    async def list_environments(
        self,
        request: MWAAListEnvironmentsRequest | None = None,
    ) -> MWAAListEnvironmentsResponse:
        client = self._require_client()
        return await self._execute(client.list_environments, request, MWAAListEnvironmentsResponse)

    async def list_environments_paginated(
        self,
        request: MWAAListEnvironmentsRequest | None = None,
    ) -> list[MWAAListEnvironmentsResponse]:
        return await self._paginate('list_environments', request, MWAAListEnvironmentsResponse)

    async def list_tags_for_resource(
        self,
        request: MWAAListTagsForResourceRequest,
    ) -> MWAAListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, MWAAListTagsForResourceResponse)

    async def publish_metrics(
        self,
        request: MWAAPublishMetricsRequest,
    ) -> MWAAPublishMetricsResponse:
        client = self._require_client()
        return await self._execute(client.publish_metrics, request, MWAAPublishMetricsResponse)

    async def tag_resource(
        self,
        request: MWAATagResourceRequest,
    ) -> MWAATagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, MWAATagResourceResponse)

    async def untag_resource(
        self,
        request: MWAAUntagResourceRequest,
    ) -> MWAAUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, MWAAUntagResourceResponse)

    async def update_environment(
        self,
        request: MWAAUpdateEnvironmentRequest,
    ) -> MWAAUpdateEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.update_environment, request, MWAAUpdateEnvironmentResponse)
