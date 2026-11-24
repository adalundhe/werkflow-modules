from werkflow_aws.models.cognito_sync import (
    CognitoSyncBulkPublishRequest,
    CognitoSyncBulkPublishResponse,
    CognitoSyncDeleteDatasetRequest,
    CognitoSyncDeleteDatasetResponse,
    CognitoSyncDescribeDatasetRequest,
    CognitoSyncDescribeDatasetResponse,
    CognitoSyncDescribeIdentityPoolUsageRequest,
    CognitoSyncDescribeIdentityPoolUsageResponse,
    CognitoSyncDescribeIdentityUsageRequest,
    CognitoSyncDescribeIdentityUsageResponse,
    CognitoSyncGetBulkPublishDetailsRequest,
    CognitoSyncGetBulkPublishDetailsResponse,
    CognitoSyncGetCognitoEventsRequest,
    CognitoSyncGetCognitoEventsResponse,
    CognitoSyncGetIdentityPoolConfigurationRequest,
    CognitoSyncGetIdentityPoolConfigurationResponse,
    CognitoSyncListDatasetsRequest,
    CognitoSyncListDatasetsResponse,
    CognitoSyncListIdentityPoolUsageRequest,
    CognitoSyncListIdentityPoolUsageResponse,
    CognitoSyncListRecordsRequest,
    CognitoSyncListRecordsResponse,
    CognitoSyncRegisterDeviceRequest,
    CognitoSyncRegisterDeviceResponse,
    CognitoSyncSetCognitoEventsRequest,
    CognitoSyncSetCognitoEventsResponse,
    CognitoSyncSetIdentityPoolConfigurationRequest,
    CognitoSyncSetIdentityPoolConfigurationResponse,
    CognitoSyncSubscribeToDatasetRequest,
    CognitoSyncSubscribeToDatasetResponse,
    CognitoSyncUnsubscribeFromDatasetRequest,
    CognitoSyncUnsubscribeFromDatasetResponse,
    CognitoSyncUpdateRecordsRequest,
    CognitoSyncUpdateRecordsResponse,
)
from werkflow_aws.types.cognito_sync_client import CognitoSyncClient
from .base import AWSBaseService


class AWSCognitoSync(AWSBaseService[CognitoSyncClient]):
    service_name = 'cognito-sync'
    boto3_service_name = 'cognito-sync'

    def __init__(self) -> None:
        super().__init__(service_name='cognito-sync', boto3_service_name='cognito-sync')

    async def bulk_publish(
        self,
        request: CognitoSyncBulkPublishRequest,
    ) -> CognitoSyncBulkPublishResponse:
        client = self._require_client()
        return await self._execute(client.bulk_publish, request, CognitoSyncBulkPublishResponse)

    async def delete_dataset(
        self,
        request: CognitoSyncDeleteDatasetRequest,
    ) -> CognitoSyncDeleteDatasetResponse:
        client = self._require_client()
        return await self._execute(client.delete_dataset, request, CognitoSyncDeleteDatasetResponse)

    async def describe_dataset(
        self,
        request: CognitoSyncDescribeDatasetRequest,
    ) -> CognitoSyncDescribeDatasetResponse:
        client = self._require_client()
        return await self._execute(client.describe_dataset, request, CognitoSyncDescribeDatasetResponse)

    async def describe_identity_pool_usage(
        self,
        request: CognitoSyncDescribeIdentityPoolUsageRequest,
    ) -> CognitoSyncDescribeIdentityPoolUsageResponse:
        client = self._require_client()
        return await self._execute(client.describe_identity_pool_usage, request, CognitoSyncDescribeIdentityPoolUsageResponse)

    async def describe_identity_usage(
        self,
        request: CognitoSyncDescribeIdentityUsageRequest,
    ) -> CognitoSyncDescribeIdentityUsageResponse:
        client = self._require_client()
        return await self._execute(client.describe_identity_usage, request, CognitoSyncDescribeIdentityUsageResponse)

    async def get_bulk_publish_details(
        self,
        request: CognitoSyncGetBulkPublishDetailsRequest,
    ) -> CognitoSyncGetBulkPublishDetailsResponse:
        client = self._require_client()
        return await self._execute(client.get_bulk_publish_details, request, CognitoSyncGetBulkPublishDetailsResponse)

    async def get_cognito_events(
        self,
        request: CognitoSyncGetCognitoEventsRequest,
    ) -> CognitoSyncGetCognitoEventsResponse:
        client = self._require_client()
        return await self._execute(client.get_cognito_events, request, CognitoSyncGetCognitoEventsResponse)

    async def get_identity_pool_configuration(
        self,
        request: CognitoSyncGetIdentityPoolConfigurationRequest,
    ) -> CognitoSyncGetIdentityPoolConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_identity_pool_configuration, request, CognitoSyncGetIdentityPoolConfigurationResponse)

    async def list_datasets(
        self,
        request: CognitoSyncListDatasetsRequest,
    ) -> CognitoSyncListDatasetsResponse:
        client = self._require_client()
        return await self._execute(client.list_datasets, request, CognitoSyncListDatasetsResponse)

    async def list_identity_pool_usage(
        self,
        request: CognitoSyncListIdentityPoolUsageRequest | None = None,
    ) -> CognitoSyncListIdentityPoolUsageResponse:
        client = self._require_client()
        return await self._execute(client.list_identity_pool_usage, request, CognitoSyncListIdentityPoolUsageResponse)

    async def list_records(
        self,
        request: CognitoSyncListRecordsRequest,
    ) -> CognitoSyncListRecordsResponse:
        client = self._require_client()
        return await self._execute(client.list_records, request, CognitoSyncListRecordsResponse)

    async def register_device(
        self,
        request: CognitoSyncRegisterDeviceRequest,
    ) -> CognitoSyncRegisterDeviceResponse:
        client = self._require_client()
        return await self._execute(client.register_device, request, CognitoSyncRegisterDeviceResponse)

    async def set_cognito_events(
        self,
        request: CognitoSyncSetCognitoEventsRequest,
    ) -> CognitoSyncSetCognitoEventsResponse:
        client = self._require_client()
        return await self._execute(client.set_cognito_events, request, CognitoSyncSetCognitoEventsResponse)

    async def set_identity_pool_configuration(
        self,
        request: CognitoSyncSetIdentityPoolConfigurationRequest,
    ) -> CognitoSyncSetIdentityPoolConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.set_identity_pool_configuration, request, CognitoSyncSetIdentityPoolConfigurationResponse)

    async def subscribe_to_dataset(
        self,
        request: CognitoSyncSubscribeToDatasetRequest,
    ) -> CognitoSyncSubscribeToDatasetResponse:
        client = self._require_client()
        return await self._execute(client.subscribe_to_dataset, request, CognitoSyncSubscribeToDatasetResponse)

    async def unsubscribe_from_dataset(
        self,
        request: CognitoSyncUnsubscribeFromDatasetRequest,
    ) -> CognitoSyncUnsubscribeFromDatasetResponse:
        client = self._require_client()
        return await self._execute(client.unsubscribe_from_dataset, request, CognitoSyncUnsubscribeFromDatasetResponse)

    async def update_records(
        self,
        request: CognitoSyncUpdateRecordsRequest,
    ) -> CognitoSyncUpdateRecordsResponse:
        client = self._require_client()
        return await self._execute(client.update_records, request, CognitoSyncUpdateRecordsResponse)
