from werkflow_aws.models.mq import (
    MQCreateBrokerRequest,
    MQCreateBrokerResponse,
    MQCreateConfigurationRequest,
    MQCreateConfigurationResponse,
    MQCreateTagsRequest,
    MQCreateTagsResponse,
    MQCreateUserRequest,
    MQCreateUserResponse,
    MQDeleteBrokerRequest,
    MQDeleteBrokerResponse,
    MQDeleteConfigurationRequest,
    MQDeleteConfigurationResponse,
    MQDeleteTagsRequest,
    MQDeleteTagsResponse,
    MQDeleteUserRequest,
    MQDeleteUserResponse,
    MQDescribeBrokerEngineTypesRequest,
    MQDescribeBrokerEngineTypesResponse,
    MQDescribeBrokerInstanceOptionsRequest,
    MQDescribeBrokerInstanceOptionsResponse,
    MQDescribeBrokerRequest,
    MQDescribeBrokerResponse,
    MQDescribeConfigurationRequest,
    MQDescribeConfigurationResponse,
    MQDescribeConfigurationRevisionRequest,
    MQDescribeConfigurationRevisionResponse,
    MQDescribeSharedResourcesRequest,
    MQDescribeSharedResourcesResponse,
    MQDescribeUserRequest,
    MQDescribeUserResponse,
    MQListBrokersRequest,
    MQListBrokersResponse,
    MQListConfigurationRevisionsRequest,
    MQListConfigurationRevisionsResponse,
    MQListConfigurationsRequest,
    MQListConfigurationsResponse,
    MQListTagsRequest,
    MQListTagsResponse,
    MQListUsersRequest,
    MQListUsersResponse,
    MQPromoteRequest,
    MQPromoteResponse,
    MQRebootBrokerRequest,
    MQRebootBrokerResponse,
    MQUpdateBrokerRequest,
    MQUpdateBrokerResponse,
    MQUpdateConfigurationRequest,
    MQUpdateConfigurationResponse,
    MQUpdateUserRequest,
    MQUpdateUserResponse,
)
from werkflow_aws.types.mq_client import MQClient
from .base import AWSBaseService


class AWSMQ(AWSBaseService[MQClient]):
    service_name = 'mq'
    boto3_service_name = 'mq'

    def __init__(self) -> None:
        super().__init__(service_name='mq', boto3_service_name='mq')

    async def create_broker(
        self,
        request: MQCreateBrokerRequest,
    ) -> MQCreateBrokerResponse:
        client = self._require_client()
        return await self._execute(client.create_broker, request, MQCreateBrokerResponse)

    async def create_configuration(
        self,
        request: MQCreateConfigurationRequest,
    ) -> MQCreateConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_configuration, request, MQCreateConfigurationResponse)

    async def create_tags(
        self,
        request: MQCreateTagsRequest,
    ) -> MQCreateTagsResponse:
        client = self._require_client()
        return await self._execute(client.create_tags, request, MQCreateTagsResponse)

    async def create_user(
        self,
        request: MQCreateUserRequest,
    ) -> MQCreateUserResponse:
        client = self._require_client()
        return await self._execute(client.create_user, request, MQCreateUserResponse)

    async def delete_broker(
        self,
        request: MQDeleteBrokerRequest,
    ) -> MQDeleteBrokerResponse:
        client = self._require_client()
        return await self._execute(client.delete_broker, request, MQDeleteBrokerResponse)

    async def delete_configuration(
        self,
        request: MQDeleteConfigurationRequest,
    ) -> MQDeleteConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_configuration, request, MQDeleteConfigurationResponse)

    async def delete_tags(
        self,
        request: MQDeleteTagsRequest,
    ) -> MQDeleteTagsResponse:
        client = self._require_client()
        return await self._execute(client.delete_tags, request, MQDeleteTagsResponse)

    async def delete_user(
        self,
        request: MQDeleteUserRequest,
    ) -> MQDeleteUserResponse:
        client = self._require_client()
        return await self._execute(client.delete_user, request, MQDeleteUserResponse)

    async def describe_broker(
        self,
        request: MQDescribeBrokerRequest,
    ) -> MQDescribeBrokerResponse:
        client = self._require_client()
        return await self._execute(client.describe_broker, request, MQDescribeBrokerResponse)

    async def describe_broker_engine_types(
        self,
        request: MQDescribeBrokerEngineTypesRequest | None = None,
    ) -> MQDescribeBrokerEngineTypesResponse:
        client = self._require_client()
        return await self._execute(client.describe_broker_engine_types, request, MQDescribeBrokerEngineTypesResponse)

    async def describe_broker_instance_options(
        self,
        request: MQDescribeBrokerInstanceOptionsRequest | None = None,
    ) -> MQDescribeBrokerInstanceOptionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_broker_instance_options, request, MQDescribeBrokerInstanceOptionsResponse)

    async def describe_configuration(
        self,
        request: MQDescribeConfigurationRequest,
    ) -> MQDescribeConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_configuration, request, MQDescribeConfigurationResponse)

    async def describe_configuration_revision(
        self,
        request: MQDescribeConfigurationRevisionRequest,
    ) -> MQDescribeConfigurationRevisionResponse:
        client = self._require_client()
        return await self._execute(client.describe_configuration_revision, request, MQDescribeConfigurationRevisionResponse)

    async def describe_shared_resources(
        self,
        request: MQDescribeSharedResourcesRequest,
    ) -> MQDescribeSharedResourcesResponse:
        client = self._require_client()
        return await self._execute(client.describe_shared_resources, request, MQDescribeSharedResourcesResponse)

    async def describe_shared_resources_paginated(
        self,
        request: MQDescribeSharedResourcesRequest,
    ) -> list[MQDescribeSharedResourcesResponse]:
        return await self._paginate('describe_shared_resources', request, MQDescribeSharedResourcesResponse)

    async def describe_user(
        self,
        request: MQDescribeUserRequest,
    ) -> MQDescribeUserResponse:
        client = self._require_client()
        return await self._execute(client.describe_user, request, MQDescribeUserResponse)

    async def list_brokers(
        self,
        request: MQListBrokersRequest | None = None,
    ) -> MQListBrokersResponse:
        client = self._require_client()
        return await self._execute(client.list_brokers, request, MQListBrokersResponse)

    async def list_brokers_paginated(
        self,
        request: MQListBrokersRequest | None = None,
    ) -> list[MQListBrokersResponse]:
        return await self._paginate('list_brokers', request, MQListBrokersResponse)

    async def list_configuration_revisions(
        self,
        request: MQListConfigurationRevisionsRequest,
    ) -> MQListConfigurationRevisionsResponse:
        client = self._require_client()
        return await self._execute(client.list_configuration_revisions, request, MQListConfigurationRevisionsResponse)

    async def list_configurations(
        self,
        request: MQListConfigurationsRequest | None = None,
    ) -> MQListConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.list_configurations, request, MQListConfigurationsResponse)

    async def list_tags(
        self,
        request: MQListTagsRequest,
    ) -> MQListTagsResponse:
        client = self._require_client()
        return await self._execute(client.list_tags, request, MQListTagsResponse)

    async def list_users(
        self,
        request: MQListUsersRequest,
    ) -> MQListUsersResponse:
        client = self._require_client()
        return await self._execute(client.list_users, request, MQListUsersResponse)

    async def promote(
        self,
        request: MQPromoteRequest,
    ) -> MQPromoteResponse:
        client = self._require_client()
        return await self._execute(client.promote, request, MQPromoteResponse)

    async def reboot_broker(
        self,
        request: MQRebootBrokerRequest,
    ) -> MQRebootBrokerResponse:
        client = self._require_client()
        return await self._execute(client.reboot_broker, request, MQRebootBrokerResponse)

    async def update_broker(
        self,
        request: MQUpdateBrokerRequest,
    ) -> MQUpdateBrokerResponse:
        client = self._require_client()
        return await self._execute(client.update_broker, request, MQUpdateBrokerResponse)

    async def update_configuration(
        self,
        request: MQUpdateConfigurationRequest,
    ) -> MQUpdateConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_configuration, request, MQUpdateConfigurationResponse)

    async def update_user(
        self,
        request: MQUpdateUserRequest,
    ) -> MQUpdateUserResponse:
        client = self._require_client()
        return await self._execute(client.update_user, request, MQUpdateUserResponse)
