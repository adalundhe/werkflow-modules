from werkflow_aws.models.app_stream import (
    AppStreamAssociateAppBlockBuilderAppBlockRequest,
    AppStreamAssociateAppBlockBuilderAppBlockResponse,
    AppStreamAssociateApplicationFleetRequest,
    AppStreamAssociateApplicationFleetResponse,
    AppStreamAssociateApplicationToEntitlementRequest,
    AppStreamAssociateApplicationToEntitlementResponse,
    AppStreamAssociateFleetRequest,
    AppStreamAssociateFleetResponse,
    AppStreamAssociateSoftwareToImageBuilderRequest,
    AppStreamAssociateSoftwareToImageBuilderResponse,
    AppStreamBatchAssociateUserStackRequest,
    AppStreamBatchAssociateUserStackResponse,
    AppStreamBatchDisassociateUserStackRequest,
    AppStreamBatchDisassociateUserStackResponse,
    AppStreamCopyImageRequest,
    AppStreamCopyImageResponse,
    AppStreamCreateAppBlockBuilderRequest,
    AppStreamCreateAppBlockBuilderResponse,
    AppStreamCreateAppBlockBuilderStreamingURLRequest,
    AppStreamCreateAppBlockBuilderStreamingURLResponse,
    AppStreamCreateAppBlockRequest,
    AppStreamCreateAppBlockResponse,
    AppStreamCreateApplicationRequest,
    AppStreamCreateApplicationResponse,
    AppStreamCreateDirectoryConfigRequest,
    AppStreamCreateDirectoryConfigResponse,
    AppStreamCreateEntitlementRequest,
    AppStreamCreateEntitlementResponse,
    AppStreamCreateExportImageTaskRequest,
    AppStreamCreateExportImageTaskResponse,
    AppStreamCreateFleetRequest,
    AppStreamCreateFleetResponse,
    AppStreamCreateImageBuilderRequest,
    AppStreamCreateImageBuilderResponse,
    AppStreamCreateImageBuilderStreamingURLRequest,
    AppStreamCreateImageBuilderStreamingURLResponse,
    AppStreamCreateImportedImageRequest,
    AppStreamCreateImportedImageResponse,
    AppStreamCreateStackRequest,
    AppStreamCreateStackResponse,
    AppStreamCreateStreamingURLRequest,
    AppStreamCreateStreamingURLResponse,
    AppStreamCreateThemeForStackRequest,
    AppStreamCreateThemeForStackResponse,
    AppStreamCreateUpdatedImageRequest,
    AppStreamCreateUpdatedImageResponse,
    AppStreamCreateUsageReportSubscriptionRequest,
    AppStreamCreateUsageReportSubscriptionResponse,
    AppStreamCreateUserRequest,
    AppStreamCreateUserResponse,
    AppStreamDeleteAppBlockBuilderRequest,
    AppStreamDeleteAppBlockBuilderResponse,
    AppStreamDeleteAppBlockRequest,
    AppStreamDeleteAppBlockResponse,
    AppStreamDeleteApplicationRequest,
    AppStreamDeleteApplicationResponse,
    AppStreamDeleteDirectoryConfigRequest,
    AppStreamDeleteDirectoryConfigResponse,
    AppStreamDeleteEntitlementRequest,
    AppStreamDeleteEntitlementResponse,
    AppStreamDeleteFleetRequest,
    AppStreamDeleteFleetResponse,
    AppStreamDeleteImageBuilderRequest,
    AppStreamDeleteImageBuilderResponse,
    AppStreamDeleteImagePermissionsRequest,
    AppStreamDeleteImagePermissionsResponse,
    AppStreamDeleteImageRequest,
    AppStreamDeleteImageResponse,
    AppStreamDeleteStackRequest,
    AppStreamDeleteStackResponse,
    AppStreamDeleteThemeForStackRequest,
    AppStreamDeleteThemeForStackResponse,
    AppStreamDeleteUsageReportSubscriptionRequest,
    AppStreamDeleteUsageReportSubscriptionResponse,
    AppStreamDeleteUserRequest,
    AppStreamDeleteUserResponse,
    AppStreamDescribeAppBlockBuilderAppBlockAssociationsRequest,
    AppStreamDescribeAppBlockBuilderAppBlockAssociationsResponse,
    AppStreamDescribeAppBlockBuildersRequest,
    AppStreamDescribeAppBlockBuildersResponse,
    AppStreamDescribeAppBlocksRequest,
    AppStreamDescribeAppBlocksResponse,
    AppStreamDescribeAppLicenseUsageRequest,
    AppStreamDescribeAppLicenseUsageResponse,
    AppStreamDescribeApplicationFleetAssociationsRequest,
    AppStreamDescribeApplicationFleetAssociationsResponse,
    AppStreamDescribeApplicationsRequest,
    AppStreamDescribeApplicationsResponse,
    AppStreamDescribeDirectoryConfigsRequest,
    AppStreamDescribeDirectoryConfigsResponse,
    AppStreamDescribeEntitlementsRequest,
    AppStreamDescribeEntitlementsResponse,
    AppStreamDescribeFleetsRequest,
    AppStreamDescribeFleetsResponse,
    AppStreamDescribeImageBuildersRequest,
    AppStreamDescribeImageBuildersResponse,
    AppStreamDescribeImagePermissionsRequest,
    AppStreamDescribeImagePermissionsResponse,
    AppStreamDescribeImagesRequest,
    AppStreamDescribeImagesResponse,
    AppStreamDescribeSessionsRequest,
    AppStreamDescribeSessionsResponse,
    AppStreamDescribeSoftwareAssociationsRequest,
    AppStreamDescribeSoftwareAssociationsResponse,
    AppStreamDescribeStacksRequest,
    AppStreamDescribeStacksResponse,
    AppStreamDescribeThemeForStackRequest,
    AppStreamDescribeThemeForStackResponse,
    AppStreamDescribeUsageReportSubscriptionsRequest,
    AppStreamDescribeUsageReportSubscriptionsResponse,
    AppStreamDescribeUserStackAssociationsRequest,
    AppStreamDescribeUserStackAssociationsResponse,
    AppStreamDescribeUsersRequest,
    AppStreamDescribeUsersResponse,
    AppStreamDisableUserRequest,
    AppStreamDisableUserResponse,
    AppStreamDisassociateAppBlockBuilderAppBlockRequest,
    AppStreamDisassociateAppBlockBuilderAppBlockResponse,
    AppStreamDisassociateApplicationFleetRequest,
    AppStreamDisassociateApplicationFleetResponse,
    AppStreamDisassociateApplicationFromEntitlementRequest,
    AppStreamDisassociateApplicationFromEntitlementResponse,
    AppStreamDisassociateFleetRequest,
    AppStreamDisassociateFleetResponse,
    AppStreamDisassociateSoftwareFromImageBuilderRequest,
    AppStreamDisassociateSoftwareFromImageBuilderResponse,
    AppStreamDrainSessionInstanceRequest,
    AppStreamDrainSessionInstanceResponse,
    AppStreamEnableUserRequest,
    AppStreamEnableUserResponse,
    AppStreamExpireSessionRequest,
    AppStreamExpireSessionResponse,
    AppStreamGetExportImageTaskRequest,
    AppStreamGetExportImageTaskResponse,
    AppStreamListAssociatedFleetsRequest,
    AppStreamListAssociatedFleetsResponse,
    AppStreamListAssociatedStacksRequest,
    AppStreamListAssociatedStacksResponse,
    AppStreamListEntitledApplicationsRequest,
    AppStreamListEntitledApplicationsResponse,
    AppStreamListExportImageTasksRequest,
    AppStreamListExportImageTasksResponse,
    AppStreamListTagsForResourceRequest,
    AppStreamListTagsForResourceResponse,
    AppStreamStartAppBlockBuilderRequest,
    AppStreamStartAppBlockBuilderResponse,
    AppStreamStartFleetRequest,
    AppStreamStartFleetResponse,
    AppStreamStartImageBuilderRequest,
    AppStreamStartImageBuilderResponse,
    AppStreamStartSoftwareDeploymentToImageBuilderRequest,
    AppStreamStartSoftwareDeploymentToImageBuilderResponse,
    AppStreamStopAppBlockBuilderRequest,
    AppStreamStopAppBlockBuilderResponse,
    AppStreamStopFleetRequest,
    AppStreamStopFleetResponse,
    AppStreamStopImageBuilderRequest,
    AppStreamStopImageBuilderResponse,
    AppStreamTagResourceRequest,
    AppStreamTagResourceResponse,
    AppStreamUntagResourceRequest,
    AppStreamUntagResourceResponse,
    AppStreamUpdateAppBlockBuilderRequest,
    AppStreamUpdateAppBlockBuilderResponse,
    AppStreamUpdateApplicationRequest,
    AppStreamUpdateApplicationResponse,
    AppStreamUpdateDirectoryConfigRequest,
    AppStreamUpdateDirectoryConfigResponse,
    AppStreamUpdateEntitlementRequest,
    AppStreamUpdateEntitlementResponse,
    AppStreamUpdateFleetRequest,
    AppStreamUpdateFleetResponse,
    AppStreamUpdateImageBuilderRequest,
    AppStreamUpdateImageBuilderResponse,
    AppStreamUpdateImagePermissionsRequest,
    AppStreamUpdateImagePermissionsResponse,
    AppStreamUpdateStackRequest,
    AppStreamUpdateStackResponse,
    AppStreamUpdateThemeForStackRequest,
    AppStreamUpdateThemeForStackResponse,
)
from werkflow_aws.types.app_stream_client import AppStreamClient
from .base import AWSBaseService


class AWSAppStream(AWSBaseService[AppStreamClient]):
    service_name = 'app-stream'
    boto3_service_name = 'appstream'

    def __init__(self) -> None:
        super().__init__(service_name='app-stream', boto3_service_name='appstream')

    async def associate_app_block_builder_app_block(
        self,
        request: AppStreamAssociateAppBlockBuilderAppBlockRequest,
    ) -> AppStreamAssociateAppBlockBuilderAppBlockResponse:
        client = self._require_client()
        return await self._execute(client.associate_app_block_builder_app_block, request, AppStreamAssociateAppBlockBuilderAppBlockResponse)

    async def associate_application_fleet(
        self,
        request: AppStreamAssociateApplicationFleetRequest,
    ) -> AppStreamAssociateApplicationFleetResponse:
        client = self._require_client()
        return await self._execute(client.associate_application_fleet, request, AppStreamAssociateApplicationFleetResponse)

    async def associate_application_to_entitlement(
        self,
        request: AppStreamAssociateApplicationToEntitlementRequest,
    ) -> AppStreamAssociateApplicationToEntitlementResponse:
        client = self._require_client()
        return await self._execute(client.associate_application_to_entitlement, request, AppStreamAssociateApplicationToEntitlementResponse)

    async def associate_fleet(
        self,
        request: AppStreamAssociateFleetRequest,
    ) -> AppStreamAssociateFleetResponse:
        client = self._require_client()
        return await self._execute(client.associate_fleet, request, AppStreamAssociateFleetResponse)

    async def associate_software_to_image_builder(
        self,
        request: AppStreamAssociateSoftwareToImageBuilderRequest,
    ) -> AppStreamAssociateSoftwareToImageBuilderResponse:
        client = self._require_client()
        return await self._execute(client.associate_software_to_image_builder, request, AppStreamAssociateSoftwareToImageBuilderResponse)

    async def batch_associate_user_stack(
        self,
        request: AppStreamBatchAssociateUserStackRequest,
    ) -> AppStreamBatchAssociateUserStackResponse:
        client = self._require_client()
        return await self._execute(client.batch_associate_user_stack, request, AppStreamBatchAssociateUserStackResponse)

    async def batch_disassociate_user_stack(
        self,
        request: AppStreamBatchDisassociateUserStackRequest,
    ) -> AppStreamBatchDisassociateUserStackResponse:
        client = self._require_client()
        return await self._execute(client.batch_disassociate_user_stack, request, AppStreamBatchDisassociateUserStackResponse)

    async def copy_image(
        self,
        request: AppStreamCopyImageRequest,
    ) -> AppStreamCopyImageResponse:
        client = self._require_client()
        return await self._execute(client.copy_image, request, AppStreamCopyImageResponse)

    async def create_app_block(
        self,
        request: AppStreamCreateAppBlockRequest,
    ) -> AppStreamCreateAppBlockResponse:
        client = self._require_client()
        return await self._execute(client.create_app_block, request, AppStreamCreateAppBlockResponse)

    async def create_app_block_builder(
        self,
        request: AppStreamCreateAppBlockBuilderRequest,
    ) -> AppStreamCreateAppBlockBuilderResponse:
        client = self._require_client()
        return await self._execute(client.create_app_block_builder, request, AppStreamCreateAppBlockBuilderResponse)

    async def create_app_block_builder_streaming_url(
        self,
        request: AppStreamCreateAppBlockBuilderStreamingURLRequest,
    ) -> AppStreamCreateAppBlockBuilderStreamingURLResponse:
        client = self._require_client()
        return await self._execute(client.create_app_block_builder_streaming_url, request, AppStreamCreateAppBlockBuilderStreamingURLResponse)

    async def create_application(
        self,
        request: AppStreamCreateApplicationRequest,
    ) -> AppStreamCreateApplicationResponse:
        client = self._require_client()
        return await self._execute(client.create_application, request, AppStreamCreateApplicationResponse)

    async def create_directory_config(
        self,
        request: AppStreamCreateDirectoryConfigRequest,
    ) -> AppStreamCreateDirectoryConfigResponse:
        client = self._require_client()
        return await self._execute(client.create_directory_config, request, AppStreamCreateDirectoryConfigResponse)

    async def create_entitlement(
        self,
        request: AppStreamCreateEntitlementRequest,
    ) -> AppStreamCreateEntitlementResponse:
        client = self._require_client()
        return await self._execute(client.create_entitlement, request, AppStreamCreateEntitlementResponse)

    async def create_export_image_task(
        self,
        request: AppStreamCreateExportImageTaskRequest,
    ) -> AppStreamCreateExportImageTaskResponse:
        client = self._require_client()
        return await self._execute(client.create_export_image_task, request, AppStreamCreateExportImageTaskResponse)

    async def create_fleet(
        self,
        request: AppStreamCreateFleetRequest,
    ) -> AppStreamCreateFleetResponse:
        client = self._require_client()
        return await self._execute(client.create_fleet, request, AppStreamCreateFleetResponse)

    async def create_image_builder(
        self,
        request: AppStreamCreateImageBuilderRequest,
    ) -> AppStreamCreateImageBuilderResponse:
        client = self._require_client()
        return await self._execute(client.create_image_builder, request, AppStreamCreateImageBuilderResponse)

    async def create_image_builder_streaming_url(
        self,
        request: AppStreamCreateImageBuilderStreamingURLRequest,
    ) -> AppStreamCreateImageBuilderStreamingURLResponse:
        client = self._require_client()
        return await self._execute(client.create_image_builder_streaming_url, request, AppStreamCreateImageBuilderStreamingURLResponse)

    async def create_imported_image(
        self,
        request: AppStreamCreateImportedImageRequest,
    ) -> AppStreamCreateImportedImageResponse:
        client = self._require_client()
        return await self._execute(client.create_imported_image, request, AppStreamCreateImportedImageResponse)

    async def create_stack(
        self,
        request: AppStreamCreateStackRequest,
    ) -> AppStreamCreateStackResponse:
        client = self._require_client()
        return await self._execute(client.create_stack, request, AppStreamCreateStackResponse)

    async def create_streaming_url(
        self,
        request: AppStreamCreateStreamingURLRequest,
    ) -> AppStreamCreateStreamingURLResponse:
        client = self._require_client()
        return await self._execute(client.create_streaming_url, request, AppStreamCreateStreamingURLResponse)

    async def create_theme_for_stack(
        self,
        request: AppStreamCreateThemeForStackRequest,
    ) -> AppStreamCreateThemeForStackResponse:
        client = self._require_client()
        return await self._execute(client.create_theme_for_stack, request, AppStreamCreateThemeForStackResponse)

    async def create_updated_image(
        self,
        request: AppStreamCreateUpdatedImageRequest,
    ) -> AppStreamCreateUpdatedImageResponse:
        client = self._require_client()
        return await self._execute(client.create_updated_image, request, AppStreamCreateUpdatedImageResponse)

    async def create_usage_report_subscription(
        self,
        request: AppStreamCreateUsageReportSubscriptionRequest | None = None,
    ) -> AppStreamCreateUsageReportSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.create_usage_report_subscription, request, AppStreamCreateUsageReportSubscriptionResponse)

    async def create_user(
        self,
        request: AppStreamCreateUserRequest,
    ) -> AppStreamCreateUserResponse:
        client = self._require_client()
        return await self._execute(client.create_user, request, AppStreamCreateUserResponse)

    async def delete_app_block(
        self,
        request: AppStreamDeleteAppBlockRequest,
    ) -> AppStreamDeleteAppBlockResponse:
        client = self._require_client()
        return await self._execute(client.delete_app_block, request, AppStreamDeleteAppBlockResponse)

    async def delete_app_block_builder(
        self,
        request: AppStreamDeleteAppBlockBuilderRequest,
    ) -> AppStreamDeleteAppBlockBuilderResponse:
        client = self._require_client()
        return await self._execute(client.delete_app_block_builder, request, AppStreamDeleteAppBlockBuilderResponse)

    async def delete_application(
        self,
        request: AppStreamDeleteApplicationRequest,
    ) -> AppStreamDeleteApplicationResponse:
        client = self._require_client()
        return await self._execute(client.delete_application, request, AppStreamDeleteApplicationResponse)

    async def delete_directory_config(
        self,
        request: AppStreamDeleteDirectoryConfigRequest,
    ) -> AppStreamDeleteDirectoryConfigResponse:
        client = self._require_client()
        return await self._execute(client.delete_directory_config, request, AppStreamDeleteDirectoryConfigResponse)

    async def delete_entitlement(
        self,
        request: AppStreamDeleteEntitlementRequest,
    ) -> AppStreamDeleteEntitlementResponse:
        client = self._require_client()
        return await self._execute(client.delete_entitlement, request, AppStreamDeleteEntitlementResponse)

    async def delete_fleet(
        self,
        request: AppStreamDeleteFleetRequest,
    ) -> AppStreamDeleteFleetResponse:
        client = self._require_client()
        return await self._execute(client.delete_fleet, request, AppStreamDeleteFleetResponse)

    async def delete_image(
        self,
        request: AppStreamDeleteImageRequest,
    ) -> AppStreamDeleteImageResponse:
        client = self._require_client()
        return await self._execute(client.delete_image, request, AppStreamDeleteImageResponse)

    async def delete_image_builder(
        self,
        request: AppStreamDeleteImageBuilderRequest,
    ) -> AppStreamDeleteImageBuilderResponse:
        client = self._require_client()
        return await self._execute(client.delete_image_builder, request, AppStreamDeleteImageBuilderResponse)

    async def delete_image_permissions(
        self,
        request: AppStreamDeleteImagePermissionsRequest,
    ) -> AppStreamDeleteImagePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.delete_image_permissions, request, AppStreamDeleteImagePermissionsResponse)

    async def delete_stack(
        self,
        request: AppStreamDeleteStackRequest,
    ) -> AppStreamDeleteStackResponse:
        client = self._require_client()
        return await self._execute(client.delete_stack, request, AppStreamDeleteStackResponse)

    async def delete_theme_for_stack(
        self,
        request: AppStreamDeleteThemeForStackRequest,
    ) -> AppStreamDeleteThemeForStackResponse:
        client = self._require_client()
        return await self._execute(client.delete_theme_for_stack, request, AppStreamDeleteThemeForStackResponse)

    async def delete_usage_report_subscription(
        self,
        request: AppStreamDeleteUsageReportSubscriptionRequest | None = None,
    ) -> AppStreamDeleteUsageReportSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.delete_usage_report_subscription, request, AppStreamDeleteUsageReportSubscriptionResponse)

    async def delete_user(
        self,
        request: AppStreamDeleteUserRequest,
    ) -> AppStreamDeleteUserResponse:
        client = self._require_client()
        return await self._execute(client.delete_user, request, AppStreamDeleteUserResponse)

    async def describe_app_block_builder_app_block_associations(
        self,
        request: AppStreamDescribeAppBlockBuilderAppBlockAssociationsRequest | None = None,
    ) -> AppStreamDescribeAppBlockBuilderAppBlockAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_app_block_builder_app_block_associations, request, AppStreamDescribeAppBlockBuilderAppBlockAssociationsResponse)

    async def describe_app_block_builders(
        self,
        request: AppStreamDescribeAppBlockBuildersRequest | None = None,
    ) -> AppStreamDescribeAppBlockBuildersResponse:
        client = self._require_client()
        return await self._execute(client.describe_app_block_builders, request, AppStreamDescribeAppBlockBuildersResponse)

    async def describe_app_blocks(
        self,
        request: AppStreamDescribeAppBlocksRequest | None = None,
    ) -> AppStreamDescribeAppBlocksResponse:
        client = self._require_client()
        return await self._execute(client.describe_app_blocks, request, AppStreamDescribeAppBlocksResponse)

    async def describe_app_license_usage(
        self,
        request: AppStreamDescribeAppLicenseUsageRequest,
    ) -> AppStreamDescribeAppLicenseUsageResponse:
        client = self._require_client()
        return await self._execute(client.describe_app_license_usage, request, AppStreamDescribeAppLicenseUsageResponse)

    async def describe_application_fleet_associations(
        self,
        request: AppStreamDescribeApplicationFleetAssociationsRequest | None = None,
    ) -> AppStreamDescribeApplicationFleetAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_application_fleet_associations, request, AppStreamDescribeApplicationFleetAssociationsResponse)

    async def describe_applications(
        self,
        request: AppStreamDescribeApplicationsRequest | None = None,
    ) -> AppStreamDescribeApplicationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_applications, request, AppStreamDescribeApplicationsResponse)

    async def describe_directory_configs(
        self,
        request: AppStreamDescribeDirectoryConfigsRequest | None = None,
    ) -> AppStreamDescribeDirectoryConfigsResponse:
        client = self._require_client()
        return await self._execute(client.describe_directory_configs, request, AppStreamDescribeDirectoryConfigsResponse)

    async def describe_directory_configs_paginated(
        self,
        request: AppStreamDescribeDirectoryConfigsRequest | None = None,
    ) -> list[AppStreamDescribeDirectoryConfigsResponse]:
        return await self._paginate('describe_directory_configs', request, AppStreamDescribeDirectoryConfigsResponse)

    async def describe_entitlements(
        self,
        request: AppStreamDescribeEntitlementsRequest,
    ) -> AppStreamDescribeEntitlementsResponse:
        client = self._require_client()
        return await self._execute(client.describe_entitlements, request, AppStreamDescribeEntitlementsResponse)

    async def describe_fleets(
        self,
        request: AppStreamDescribeFleetsRequest | None = None,
    ) -> AppStreamDescribeFleetsResponse:
        client = self._require_client()
        return await self._execute(client.describe_fleets, request, AppStreamDescribeFleetsResponse)

    async def describe_fleets_paginated(
        self,
        request: AppStreamDescribeFleetsRequest | None = None,
    ) -> list[AppStreamDescribeFleetsResponse]:
        return await self._paginate('describe_fleets', request, AppStreamDescribeFleetsResponse)

    async def describe_image_builders(
        self,
        request: AppStreamDescribeImageBuildersRequest | None = None,
    ) -> AppStreamDescribeImageBuildersResponse:
        client = self._require_client()
        return await self._execute(client.describe_image_builders, request, AppStreamDescribeImageBuildersResponse)

    async def describe_image_builders_paginated(
        self,
        request: AppStreamDescribeImageBuildersRequest | None = None,
    ) -> list[AppStreamDescribeImageBuildersResponse]:
        return await self._paginate('describe_image_builders', request, AppStreamDescribeImageBuildersResponse)

    async def describe_image_permissions(
        self,
        request: AppStreamDescribeImagePermissionsRequest,
    ) -> AppStreamDescribeImagePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_image_permissions, request, AppStreamDescribeImagePermissionsResponse)

    async def describe_images(
        self,
        request: AppStreamDescribeImagesRequest | None = None,
    ) -> AppStreamDescribeImagesResponse:
        client = self._require_client()
        return await self._execute(client.describe_images, request, AppStreamDescribeImagesResponse)

    async def describe_images_paginated(
        self,
        request: AppStreamDescribeImagesRequest | None = None,
    ) -> list[AppStreamDescribeImagesResponse]:
        return await self._paginate('describe_images', request, AppStreamDescribeImagesResponse)

    async def describe_sessions(
        self,
        request: AppStreamDescribeSessionsRequest,
    ) -> AppStreamDescribeSessionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_sessions, request, AppStreamDescribeSessionsResponse)

    async def describe_sessions_paginated(
        self,
        request: AppStreamDescribeSessionsRequest,
    ) -> list[AppStreamDescribeSessionsResponse]:
        return await self._paginate('describe_sessions', request, AppStreamDescribeSessionsResponse)

    async def describe_software_associations(
        self,
        request: AppStreamDescribeSoftwareAssociationsRequest,
    ) -> AppStreamDescribeSoftwareAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_software_associations, request, AppStreamDescribeSoftwareAssociationsResponse)

    async def describe_stacks(
        self,
        request: AppStreamDescribeStacksRequest | None = None,
    ) -> AppStreamDescribeStacksResponse:
        client = self._require_client()
        return await self._execute(client.describe_stacks, request, AppStreamDescribeStacksResponse)

    async def describe_stacks_paginated(
        self,
        request: AppStreamDescribeStacksRequest | None = None,
    ) -> list[AppStreamDescribeStacksResponse]:
        return await self._paginate('describe_stacks', request, AppStreamDescribeStacksResponse)

    async def describe_theme_for_stack(
        self,
        request: AppStreamDescribeThemeForStackRequest,
    ) -> AppStreamDescribeThemeForStackResponse:
        client = self._require_client()
        return await self._execute(client.describe_theme_for_stack, request, AppStreamDescribeThemeForStackResponse)

    async def describe_usage_report_subscriptions(
        self,
        request: AppStreamDescribeUsageReportSubscriptionsRequest | None = None,
    ) -> AppStreamDescribeUsageReportSubscriptionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_usage_report_subscriptions, request, AppStreamDescribeUsageReportSubscriptionsResponse)

    async def describe_user_stack_associations(
        self,
        request: AppStreamDescribeUserStackAssociationsRequest | None = None,
    ) -> AppStreamDescribeUserStackAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_user_stack_associations, request, AppStreamDescribeUserStackAssociationsResponse)

    async def describe_user_stack_associations_paginated(
        self,
        request: AppStreamDescribeUserStackAssociationsRequest | None = None,
    ) -> list[AppStreamDescribeUserStackAssociationsResponse]:
        return await self._paginate('describe_user_stack_associations', request, AppStreamDescribeUserStackAssociationsResponse)

    async def describe_users(
        self,
        request: AppStreamDescribeUsersRequest,
    ) -> AppStreamDescribeUsersResponse:
        client = self._require_client()
        return await self._execute(client.describe_users, request, AppStreamDescribeUsersResponse)

    async def describe_users_paginated(
        self,
        request: AppStreamDescribeUsersRequest,
    ) -> list[AppStreamDescribeUsersResponse]:
        return await self._paginate('describe_users', request, AppStreamDescribeUsersResponse)

    async def disable_user(
        self,
        request: AppStreamDisableUserRequest,
    ) -> AppStreamDisableUserResponse:
        client = self._require_client()
        return await self._execute(client.disable_user, request, AppStreamDisableUserResponse)

    async def disassociate_app_block_builder_app_block(
        self,
        request: AppStreamDisassociateAppBlockBuilderAppBlockRequest,
    ) -> AppStreamDisassociateAppBlockBuilderAppBlockResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_app_block_builder_app_block, request, AppStreamDisassociateAppBlockBuilderAppBlockResponse)

    async def disassociate_application_fleet(
        self,
        request: AppStreamDisassociateApplicationFleetRequest,
    ) -> AppStreamDisassociateApplicationFleetResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_application_fleet, request, AppStreamDisassociateApplicationFleetResponse)

    async def disassociate_application_from_entitlement(
        self,
        request: AppStreamDisassociateApplicationFromEntitlementRequest,
    ) -> AppStreamDisassociateApplicationFromEntitlementResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_application_from_entitlement, request, AppStreamDisassociateApplicationFromEntitlementResponse)

    async def disassociate_fleet(
        self,
        request: AppStreamDisassociateFleetRequest,
    ) -> AppStreamDisassociateFleetResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_fleet, request, AppStreamDisassociateFleetResponse)

    async def disassociate_software_from_image_builder(
        self,
        request: AppStreamDisassociateSoftwareFromImageBuilderRequest,
    ) -> AppStreamDisassociateSoftwareFromImageBuilderResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_software_from_image_builder, request, AppStreamDisassociateSoftwareFromImageBuilderResponse)

    async def drain_session_instance(
        self,
        request: AppStreamDrainSessionInstanceRequest,
    ) -> AppStreamDrainSessionInstanceResponse:
        client = self._require_client()
        return await self._execute(client.drain_session_instance, request, AppStreamDrainSessionInstanceResponse)

    async def enable_user(
        self,
        request: AppStreamEnableUserRequest,
    ) -> AppStreamEnableUserResponse:
        client = self._require_client()
        return await self._execute(client.enable_user, request, AppStreamEnableUserResponse)

    async def expire_session(
        self,
        request: AppStreamExpireSessionRequest,
    ) -> AppStreamExpireSessionResponse:
        client = self._require_client()
        return await self._execute(client.expire_session, request, AppStreamExpireSessionResponse)

    async def get_export_image_task(
        self,
        request: AppStreamGetExportImageTaskRequest | None = None,
    ) -> AppStreamGetExportImageTaskResponse:
        client = self._require_client()
        return await self._execute(client.get_export_image_task, request, AppStreamGetExportImageTaskResponse)

    async def list_associated_fleets(
        self,
        request: AppStreamListAssociatedFleetsRequest,
    ) -> AppStreamListAssociatedFleetsResponse:
        client = self._require_client()
        return await self._execute(client.list_associated_fleets, request, AppStreamListAssociatedFleetsResponse)

    async def list_associated_fleets_paginated(
        self,
        request: AppStreamListAssociatedFleetsRequest,
    ) -> list[AppStreamListAssociatedFleetsResponse]:
        return await self._paginate('list_associated_fleets', request, AppStreamListAssociatedFleetsResponse)

    async def list_associated_stacks(
        self,
        request: AppStreamListAssociatedStacksRequest,
    ) -> AppStreamListAssociatedStacksResponse:
        client = self._require_client()
        return await self._execute(client.list_associated_stacks, request, AppStreamListAssociatedStacksResponse)

    async def list_associated_stacks_paginated(
        self,
        request: AppStreamListAssociatedStacksRequest,
    ) -> list[AppStreamListAssociatedStacksResponse]:
        return await self._paginate('list_associated_stacks', request, AppStreamListAssociatedStacksResponse)

    async def list_entitled_applications(
        self,
        request: AppStreamListEntitledApplicationsRequest,
    ) -> AppStreamListEntitledApplicationsResponse:
        client = self._require_client()
        return await self._execute(client.list_entitled_applications, request, AppStreamListEntitledApplicationsResponse)

    async def list_export_image_tasks(
        self,
        request: AppStreamListExportImageTasksRequest | None = None,
    ) -> AppStreamListExportImageTasksResponse:
        client = self._require_client()
        return await self._execute(client.list_export_image_tasks, request, AppStreamListExportImageTasksResponse)

    async def list_tags_for_resource(
        self,
        request: AppStreamListTagsForResourceRequest,
    ) -> AppStreamListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, AppStreamListTagsForResourceResponse)

    async def start_app_block_builder(
        self,
        request: AppStreamStartAppBlockBuilderRequest,
    ) -> AppStreamStartAppBlockBuilderResponse:
        client = self._require_client()
        return await self._execute(client.start_app_block_builder, request, AppStreamStartAppBlockBuilderResponse)

    async def start_fleet(
        self,
        request: AppStreamStartFleetRequest,
    ) -> AppStreamStartFleetResponse:
        client = self._require_client()
        return await self._execute(client.start_fleet, request, AppStreamStartFleetResponse)

    async def start_image_builder(
        self,
        request: AppStreamStartImageBuilderRequest,
    ) -> AppStreamStartImageBuilderResponse:
        client = self._require_client()
        return await self._execute(client.start_image_builder, request, AppStreamStartImageBuilderResponse)

    async def start_software_deployment_to_image_builder(
        self,
        request: AppStreamStartSoftwareDeploymentToImageBuilderRequest,
    ) -> AppStreamStartSoftwareDeploymentToImageBuilderResponse:
        client = self._require_client()
        return await self._execute(client.start_software_deployment_to_image_builder, request, AppStreamStartSoftwareDeploymentToImageBuilderResponse)

    async def stop_app_block_builder(
        self,
        request: AppStreamStopAppBlockBuilderRequest,
    ) -> AppStreamStopAppBlockBuilderResponse:
        client = self._require_client()
        return await self._execute(client.stop_app_block_builder, request, AppStreamStopAppBlockBuilderResponse)

    async def stop_fleet(
        self,
        request: AppStreamStopFleetRequest,
    ) -> AppStreamStopFleetResponse:
        client = self._require_client()
        return await self._execute(client.stop_fleet, request, AppStreamStopFleetResponse)

    async def stop_image_builder(
        self,
        request: AppStreamStopImageBuilderRequest,
    ) -> AppStreamStopImageBuilderResponse:
        client = self._require_client()
        return await self._execute(client.stop_image_builder, request, AppStreamStopImageBuilderResponse)

    async def tag_resource(
        self,
        request: AppStreamTagResourceRequest,
    ) -> AppStreamTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, AppStreamTagResourceResponse)

    async def untag_resource(
        self,
        request: AppStreamUntagResourceRequest,
    ) -> AppStreamUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, AppStreamUntagResourceResponse)

    async def update_app_block_builder(
        self,
        request: AppStreamUpdateAppBlockBuilderRequest,
    ) -> AppStreamUpdateAppBlockBuilderResponse:
        client = self._require_client()
        return await self._execute(client.update_app_block_builder, request, AppStreamUpdateAppBlockBuilderResponse)

    async def update_application(
        self,
        request: AppStreamUpdateApplicationRequest,
    ) -> AppStreamUpdateApplicationResponse:
        client = self._require_client()
        return await self._execute(client.update_application, request, AppStreamUpdateApplicationResponse)

    async def update_directory_config(
        self,
        request: AppStreamUpdateDirectoryConfigRequest,
    ) -> AppStreamUpdateDirectoryConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_directory_config, request, AppStreamUpdateDirectoryConfigResponse)

    async def update_entitlement(
        self,
        request: AppStreamUpdateEntitlementRequest,
    ) -> AppStreamUpdateEntitlementResponse:
        client = self._require_client()
        return await self._execute(client.update_entitlement, request, AppStreamUpdateEntitlementResponse)

    async def update_fleet(
        self,
        request: AppStreamUpdateFleetRequest | None = None,
    ) -> AppStreamUpdateFleetResponse:
        client = self._require_client()
        return await self._execute(client.update_fleet, request, AppStreamUpdateFleetResponse)

    async def update_image_builder(
        self,
        request: AppStreamUpdateImageBuilderRequest,
    ) -> AppStreamUpdateImageBuilderResponse:
        client = self._require_client()
        return await self._execute(client.update_image_builder, request, AppStreamUpdateImageBuilderResponse)

    async def update_image_permissions(
        self,
        request: AppStreamUpdateImagePermissionsRequest,
    ) -> AppStreamUpdateImagePermissionsResponse:
        client = self._require_client()
        return await self._execute(client.update_image_permissions, request, AppStreamUpdateImagePermissionsResponse)

    async def update_stack(
        self,
        request: AppStreamUpdateStackRequest,
    ) -> AppStreamUpdateStackResponse:
        client = self._require_client()
        return await self._execute(client.update_stack, request, AppStreamUpdateStackResponse)

    async def update_theme_for_stack(
        self,
        request: AppStreamUpdateThemeForStackRequest,
    ) -> AppStreamUpdateThemeForStackResponse:
        client = self._require_client()
        return await self._execute(client.update_theme_for_stack, request, AppStreamUpdateThemeForStackResponse)
