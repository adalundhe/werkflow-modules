from werkflow_aws.models.security_lake import (
    SecurityLakeCreateAwsLogSourceRequest,
    SecurityLakeCreateAwsLogSourceResponse,
    SecurityLakeCreateCustomLogSourceRequest,
    SecurityLakeCreateCustomLogSourceResponse,
    SecurityLakeCreateDataLakeExceptionSubscriptionRequest,
    SecurityLakeCreateDataLakeExceptionSubscriptionResponse,
    SecurityLakeCreateDataLakeOrganizationConfigurationRequest,
    SecurityLakeCreateDataLakeOrganizationConfigurationResponse,
    SecurityLakeCreateDataLakeRequest,
    SecurityLakeCreateDataLakeResponse,
    SecurityLakeCreateSubscriberNotificationRequest,
    SecurityLakeCreateSubscriberNotificationResponse,
    SecurityLakeCreateSubscriberRequest,
    SecurityLakeCreateSubscriberResponse,
    SecurityLakeDeleteAwsLogSourceRequest,
    SecurityLakeDeleteAwsLogSourceResponse,
    SecurityLakeDeleteCustomLogSourceRequest,
    SecurityLakeDeleteCustomLogSourceResponse,
    SecurityLakeDeleteDataLakeExceptionSubscriptionRequest,
    SecurityLakeDeleteDataLakeExceptionSubscriptionResponse,
    SecurityLakeDeleteDataLakeOrganizationConfigurationRequest,
    SecurityLakeDeleteDataLakeOrganizationConfigurationResponse,
    SecurityLakeDeleteDataLakeRequest,
    SecurityLakeDeleteDataLakeResponse,
    SecurityLakeDeleteSubscriberNotificationRequest,
    SecurityLakeDeleteSubscriberNotificationResponse,
    SecurityLakeDeleteSubscriberRequest,
    SecurityLakeDeleteSubscriberResponse,
    SecurityLakeDeregisterDataLakeDelegatedAdministratorRequest,
    SecurityLakeDeregisterDataLakeDelegatedAdministratorResponse,
    SecurityLakeGetDataLakeExceptionSubscriptionRequest,
    SecurityLakeGetDataLakeExceptionSubscriptionResponse,
    SecurityLakeGetDataLakeOrganizationConfigurationRequest,
    SecurityLakeGetDataLakeOrganizationConfigurationResponse,
    SecurityLakeGetDataLakeSourcesRequest,
    SecurityLakeGetDataLakeSourcesResponse,
    SecurityLakeGetSubscriberRequest,
    SecurityLakeGetSubscriberResponse,
    SecurityLakeListDataLakeExceptionsRequest,
    SecurityLakeListDataLakeExceptionsResponse,
    SecurityLakeListDataLakesRequest,
    SecurityLakeListDataLakesResponse,
    SecurityLakeListLogSourcesRequest,
    SecurityLakeListLogSourcesResponse,
    SecurityLakeListSubscribersRequest,
    SecurityLakeListSubscribersResponse,
    SecurityLakeListTagsForResourceRequest,
    SecurityLakeListTagsForResourceResponse,
    SecurityLakeRegisterDataLakeDelegatedAdministratorRequest,
    SecurityLakeRegisterDataLakeDelegatedAdministratorResponse,
    SecurityLakeTagResourceRequest,
    SecurityLakeTagResourceResponse,
    SecurityLakeUntagResourceRequest,
    SecurityLakeUntagResourceResponse,
    SecurityLakeUpdateDataLakeExceptionSubscriptionRequest,
    SecurityLakeUpdateDataLakeExceptionSubscriptionResponse,
    SecurityLakeUpdateDataLakeRequest,
    SecurityLakeUpdateDataLakeResponse,
    SecurityLakeUpdateSubscriberNotificationRequest,
    SecurityLakeUpdateSubscriberNotificationResponse,
    SecurityLakeUpdateSubscriberRequest,
    SecurityLakeUpdateSubscriberResponse,
)
from werkflow_aws.types.security_lake_client import SecurityLakeClient
from .base import AWSBaseService


class AWSSecurityLake(AWSBaseService[SecurityLakeClient]):
    service_name = 'security-lake'
    boto3_service_name = 'securitylake'

    def __init__(self) -> None:
        super().__init__(service_name='security-lake', boto3_service_name='securitylake')

    async def create_aws_log_source(
        self,
        request: SecurityLakeCreateAwsLogSourceRequest,
    ) -> SecurityLakeCreateAwsLogSourceResponse:
        client = self._require_client()
        return await self._execute(client.create_aws_log_source, request, SecurityLakeCreateAwsLogSourceResponse)

    async def create_custom_log_source(
        self,
        request: SecurityLakeCreateCustomLogSourceRequest,
    ) -> SecurityLakeCreateCustomLogSourceResponse:
        client = self._require_client()
        return await self._execute(client.create_custom_log_source, request, SecurityLakeCreateCustomLogSourceResponse)

    async def create_data_lake(
        self,
        request: SecurityLakeCreateDataLakeRequest,
    ) -> SecurityLakeCreateDataLakeResponse:
        client = self._require_client()
        return await self._execute(client.create_data_lake, request, SecurityLakeCreateDataLakeResponse)

    async def create_data_lake_exception_subscription(
        self,
        request: SecurityLakeCreateDataLakeExceptionSubscriptionRequest,
    ) -> SecurityLakeCreateDataLakeExceptionSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.create_data_lake_exception_subscription, request, SecurityLakeCreateDataLakeExceptionSubscriptionResponse)

    async def create_data_lake_organization_configuration(
        self,
        request: SecurityLakeCreateDataLakeOrganizationConfigurationRequest | None = None,
    ) -> SecurityLakeCreateDataLakeOrganizationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_data_lake_organization_configuration, request, SecurityLakeCreateDataLakeOrganizationConfigurationResponse)

    async def create_subscriber(
        self,
        request: SecurityLakeCreateSubscriberRequest,
    ) -> SecurityLakeCreateSubscriberResponse:
        client = self._require_client()
        return await self._execute(client.create_subscriber, request, SecurityLakeCreateSubscriberResponse)

    async def create_subscriber_notification(
        self,
        request: SecurityLakeCreateSubscriberNotificationRequest,
    ) -> SecurityLakeCreateSubscriberNotificationResponse:
        client = self._require_client()
        return await self._execute(client.create_subscriber_notification, request, SecurityLakeCreateSubscriberNotificationResponse)

    async def delete_aws_log_source(
        self,
        request: SecurityLakeDeleteAwsLogSourceRequest,
    ) -> SecurityLakeDeleteAwsLogSourceResponse:
        client = self._require_client()
        return await self._execute(client.delete_aws_log_source, request, SecurityLakeDeleteAwsLogSourceResponse)

    async def delete_custom_log_source(
        self,
        request: SecurityLakeDeleteCustomLogSourceRequest,
    ) -> SecurityLakeDeleteCustomLogSourceResponse:
        client = self._require_client()
        return await self._execute(client.delete_custom_log_source, request, SecurityLakeDeleteCustomLogSourceResponse)

    async def delete_data_lake(
        self,
        request: SecurityLakeDeleteDataLakeRequest,
    ) -> SecurityLakeDeleteDataLakeResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_lake, request, SecurityLakeDeleteDataLakeResponse)

    async def delete_data_lake_exception_subscription(
        self,
        request: SecurityLakeDeleteDataLakeExceptionSubscriptionRequest | None = None,
    ) -> SecurityLakeDeleteDataLakeExceptionSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_lake_exception_subscription, request, SecurityLakeDeleteDataLakeExceptionSubscriptionResponse)

    async def delete_data_lake_organization_configuration(
        self,
        request: SecurityLakeDeleteDataLakeOrganizationConfigurationRequest | None = None,
    ) -> SecurityLakeDeleteDataLakeOrganizationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_lake_organization_configuration, request, SecurityLakeDeleteDataLakeOrganizationConfigurationResponse)

    async def delete_subscriber(
        self,
        request: SecurityLakeDeleteSubscriberRequest,
    ) -> SecurityLakeDeleteSubscriberResponse:
        client = self._require_client()
        return await self._execute(client.delete_subscriber, request, SecurityLakeDeleteSubscriberResponse)

    async def delete_subscriber_notification(
        self,
        request: SecurityLakeDeleteSubscriberNotificationRequest,
    ) -> SecurityLakeDeleteSubscriberNotificationResponse:
        client = self._require_client()
        return await self._execute(client.delete_subscriber_notification, request, SecurityLakeDeleteSubscriberNotificationResponse)

    async def deregister_data_lake_delegated_administrator(
        self,
        request: SecurityLakeDeregisterDataLakeDelegatedAdministratorRequest | None = None,
    ) -> SecurityLakeDeregisterDataLakeDelegatedAdministratorResponse:
        client = self._require_client()
        return await self._execute(client.deregister_data_lake_delegated_administrator, request, SecurityLakeDeregisterDataLakeDelegatedAdministratorResponse)

    async def get_data_lake_exception_subscription(
        self,
        request: SecurityLakeGetDataLakeExceptionSubscriptionRequest | None = None,
    ) -> SecurityLakeGetDataLakeExceptionSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.get_data_lake_exception_subscription, request, SecurityLakeGetDataLakeExceptionSubscriptionResponse)

    async def get_data_lake_organization_configuration(
        self,
        request: SecurityLakeGetDataLakeOrganizationConfigurationRequest | None = None,
    ) -> SecurityLakeGetDataLakeOrganizationConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_data_lake_organization_configuration, request, SecurityLakeGetDataLakeOrganizationConfigurationResponse)

    async def get_data_lake_sources(
        self,
        request: SecurityLakeGetDataLakeSourcesRequest | None = None,
    ) -> SecurityLakeGetDataLakeSourcesResponse:
        client = self._require_client()
        return await self._execute(client.get_data_lake_sources, request, SecurityLakeGetDataLakeSourcesResponse)

    async def get_data_lake_sources_paginated(
        self,
        request: SecurityLakeGetDataLakeSourcesRequest | None = None,
    ) -> list[SecurityLakeGetDataLakeSourcesResponse]:
        return await self._paginate('get_data_lake_sources', request, SecurityLakeGetDataLakeSourcesResponse)

    async def get_subscriber(
        self,
        request: SecurityLakeGetSubscriberRequest,
    ) -> SecurityLakeGetSubscriberResponse:
        client = self._require_client()
        return await self._execute(client.get_subscriber, request, SecurityLakeGetSubscriberResponse)

    async def list_data_lake_exceptions(
        self,
        request: SecurityLakeListDataLakeExceptionsRequest | None = None,
    ) -> SecurityLakeListDataLakeExceptionsResponse:
        client = self._require_client()
        return await self._execute(client.list_data_lake_exceptions, request, SecurityLakeListDataLakeExceptionsResponse)

    async def list_data_lake_exceptions_paginated(
        self,
        request: SecurityLakeListDataLakeExceptionsRequest | None = None,
    ) -> list[SecurityLakeListDataLakeExceptionsResponse]:
        return await self._paginate('list_data_lake_exceptions', request, SecurityLakeListDataLakeExceptionsResponse)

    async def list_data_lakes(
        self,
        request: SecurityLakeListDataLakesRequest | None = None,
    ) -> SecurityLakeListDataLakesResponse:
        client = self._require_client()
        return await self._execute(client.list_data_lakes, request, SecurityLakeListDataLakesResponse)

    async def list_log_sources(
        self,
        request: SecurityLakeListLogSourcesRequest | None = None,
    ) -> SecurityLakeListLogSourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_log_sources, request, SecurityLakeListLogSourcesResponse)

    async def list_log_sources_paginated(
        self,
        request: SecurityLakeListLogSourcesRequest | None = None,
    ) -> list[SecurityLakeListLogSourcesResponse]:
        return await self._paginate('list_log_sources', request, SecurityLakeListLogSourcesResponse)

    async def list_subscribers(
        self,
        request: SecurityLakeListSubscribersRequest | None = None,
    ) -> SecurityLakeListSubscribersResponse:
        client = self._require_client()
        return await self._execute(client.list_subscribers, request, SecurityLakeListSubscribersResponse)

    async def list_subscribers_paginated(
        self,
        request: SecurityLakeListSubscribersRequest | None = None,
    ) -> list[SecurityLakeListSubscribersResponse]:
        return await self._paginate('list_subscribers', request, SecurityLakeListSubscribersResponse)

    async def list_tags_for_resource(
        self,
        request: SecurityLakeListTagsForResourceRequest,
    ) -> SecurityLakeListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, SecurityLakeListTagsForResourceResponse)

    async def register_data_lake_delegated_administrator(
        self,
        request: SecurityLakeRegisterDataLakeDelegatedAdministratorRequest,
    ) -> SecurityLakeRegisterDataLakeDelegatedAdministratorResponse:
        client = self._require_client()
        return await self._execute(client.register_data_lake_delegated_administrator, request, SecurityLakeRegisterDataLakeDelegatedAdministratorResponse)

    async def tag_resource(
        self,
        request: SecurityLakeTagResourceRequest,
    ) -> SecurityLakeTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, SecurityLakeTagResourceResponse)

    async def untag_resource(
        self,
        request: SecurityLakeUntagResourceRequest,
    ) -> SecurityLakeUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, SecurityLakeUntagResourceResponse)

    async def update_data_lake(
        self,
        request: SecurityLakeUpdateDataLakeRequest,
    ) -> SecurityLakeUpdateDataLakeResponse:
        client = self._require_client()
        return await self._execute(client.update_data_lake, request, SecurityLakeUpdateDataLakeResponse)

    async def update_data_lake_exception_subscription(
        self,
        request: SecurityLakeUpdateDataLakeExceptionSubscriptionRequest,
    ) -> SecurityLakeUpdateDataLakeExceptionSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.update_data_lake_exception_subscription, request, SecurityLakeUpdateDataLakeExceptionSubscriptionResponse)

    async def update_subscriber(
        self,
        request: SecurityLakeUpdateSubscriberRequest,
    ) -> SecurityLakeUpdateSubscriberResponse:
        client = self._require_client()
        return await self._execute(client.update_subscriber, request, SecurityLakeUpdateSubscriberResponse)

    async def update_subscriber_notification(
        self,
        request: SecurityLakeUpdateSubscriberNotificationRequest,
    ) -> SecurityLakeUpdateSubscriberNotificationResponse:
        client = self._require_client()
        return await self._execute(client.update_subscriber_notification, request, SecurityLakeUpdateSubscriberNotificationResponse)
