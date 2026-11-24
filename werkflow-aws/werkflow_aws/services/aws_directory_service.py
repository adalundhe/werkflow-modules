from werkflow_aws.models.directory_service import (
    DirectoryServiceAcceptSharedDirectoryRequest,
    DirectoryServiceAcceptSharedDirectoryResponse,
    DirectoryServiceAddIpRoutesRequest,
    DirectoryServiceAddIpRoutesResponse,
    DirectoryServiceAddRegionRequest,
    DirectoryServiceAddRegionResponse,
    DirectoryServiceAddTagsToResourceRequest,
    DirectoryServiceAddTagsToResourceResponse,
    DirectoryServiceCancelSchemaExtensionRequest,
    DirectoryServiceCancelSchemaExtensionResponse,
    DirectoryServiceConnectDirectoryRequest,
    DirectoryServiceConnectDirectoryResponse,
    DirectoryServiceCreateAliasRequest,
    DirectoryServiceCreateAliasResponse,
    DirectoryServiceCreateComputerRequest,
    DirectoryServiceCreateComputerResponse,
    DirectoryServiceCreateConditionalForwarderRequest,
    DirectoryServiceCreateConditionalForwarderResponse,
    DirectoryServiceCreateDirectoryRequest,
    DirectoryServiceCreateDirectoryResponse,
    DirectoryServiceCreateHybridADRequest,
    DirectoryServiceCreateHybridADResponse,
    DirectoryServiceCreateLogSubscriptionRequest,
    DirectoryServiceCreateLogSubscriptionResponse,
    DirectoryServiceCreateMicrosoftADRequest,
    DirectoryServiceCreateMicrosoftADResponse,
    DirectoryServiceCreateSnapshotRequest,
    DirectoryServiceCreateSnapshotResponse,
    DirectoryServiceCreateTrustRequest,
    DirectoryServiceCreateTrustResponse,
    DirectoryServiceDeleteADAssessmentRequest,
    DirectoryServiceDeleteADAssessmentResponse,
    DirectoryServiceDeleteConditionalForwarderRequest,
    DirectoryServiceDeleteConditionalForwarderResponse,
    DirectoryServiceDeleteDirectoryRequest,
    DirectoryServiceDeleteDirectoryResponse,
    DirectoryServiceDeleteLogSubscriptionRequest,
    DirectoryServiceDeleteLogSubscriptionResponse,
    DirectoryServiceDeleteSnapshotRequest,
    DirectoryServiceDeleteSnapshotResponse,
    DirectoryServiceDeleteTrustRequest,
    DirectoryServiceDeleteTrustResponse,
    DirectoryServiceDeregisterCertificateRequest,
    DirectoryServiceDeregisterCertificateResponse,
    DirectoryServiceDeregisterEventTopicRequest,
    DirectoryServiceDeregisterEventTopicResponse,
    DirectoryServiceDescribeADAssessmentRequest,
    DirectoryServiceDescribeADAssessmentResponse,
    DirectoryServiceDescribeCAEnrollmentPolicyRequest,
    DirectoryServiceDescribeCAEnrollmentPolicyResponse,
    DirectoryServiceDescribeCertificateRequest,
    DirectoryServiceDescribeCertificateResponse,
    DirectoryServiceDescribeClientAuthenticationSettingsRequest,
    DirectoryServiceDescribeClientAuthenticationSettingsResponse,
    DirectoryServiceDescribeConditionalForwardersRequest,
    DirectoryServiceDescribeConditionalForwardersResponse,
    DirectoryServiceDescribeDirectoriesRequest,
    DirectoryServiceDescribeDirectoriesResponse,
    DirectoryServiceDescribeDirectoryDataAccessRequest,
    DirectoryServiceDescribeDirectoryDataAccessResponse,
    DirectoryServiceDescribeDomainControllersRequest,
    DirectoryServiceDescribeDomainControllersResponse,
    DirectoryServiceDescribeEventTopicsRequest,
    DirectoryServiceDescribeEventTopicsResponse,
    DirectoryServiceDescribeHybridADUpdateRequest,
    DirectoryServiceDescribeHybridADUpdateResponse,
    DirectoryServiceDescribeLDAPSSettingsRequest,
    DirectoryServiceDescribeLDAPSSettingsResponse,
    DirectoryServiceDescribeRegionsRequest,
    DirectoryServiceDescribeRegionsResponse,
    DirectoryServiceDescribeSettingsRequest,
    DirectoryServiceDescribeSettingsResponse,
    DirectoryServiceDescribeSharedDirectoriesRequest,
    DirectoryServiceDescribeSharedDirectoriesResponse,
    DirectoryServiceDescribeSnapshotsRequest,
    DirectoryServiceDescribeSnapshotsResponse,
    DirectoryServiceDescribeTrustsRequest,
    DirectoryServiceDescribeTrustsResponse,
    DirectoryServiceDescribeUpdateDirectoryRequest,
    DirectoryServiceDescribeUpdateDirectoryResponse,
    DirectoryServiceDisableCAEnrollmentPolicyRequest,
    DirectoryServiceDisableCAEnrollmentPolicyResponse,
    DirectoryServiceDisableClientAuthenticationRequest,
    DirectoryServiceDisableClientAuthenticationResponse,
    DirectoryServiceDisableDirectoryDataAccessRequest,
    DirectoryServiceDisableDirectoryDataAccessResponse,
    DirectoryServiceDisableLDAPSRequest,
    DirectoryServiceDisableLDAPSResponse,
    DirectoryServiceDisableRadiusRequest,
    DirectoryServiceDisableRadiusResponse,
    DirectoryServiceDisableSsoRequest,
    DirectoryServiceDisableSsoResponse,
    DirectoryServiceEnableCAEnrollmentPolicyRequest,
    DirectoryServiceEnableCAEnrollmentPolicyResponse,
    DirectoryServiceEnableClientAuthenticationRequest,
    DirectoryServiceEnableClientAuthenticationResponse,
    DirectoryServiceEnableDirectoryDataAccessRequest,
    DirectoryServiceEnableDirectoryDataAccessResponse,
    DirectoryServiceEnableLDAPSRequest,
    DirectoryServiceEnableLDAPSResponse,
    DirectoryServiceEnableRadiusRequest,
    DirectoryServiceEnableRadiusResponse,
    DirectoryServiceEnableSsoRequest,
    DirectoryServiceEnableSsoResponse,
    DirectoryServiceGetDirectoryLimitsRequest,
    DirectoryServiceGetDirectoryLimitsResponse,
    DirectoryServiceGetSnapshotLimitsRequest,
    DirectoryServiceGetSnapshotLimitsResponse,
    DirectoryServiceListADAssessmentsRequest,
    DirectoryServiceListADAssessmentsResponse,
    DirectoryServiceListCertificatesRequest,
    DirectoryServiceListCertificatesResponse,
    DirectoryServiceListIpRoutesRequest,
    DirectoryServiceListIpRoutesResponse,
    DirectoryServiceListLogSubscriptionsRequest,
    DirectoryServiceListLogSubscriptionsResponse,
    DirectoryServiceListSchemaExtensionsRequest,
    DirectoryServiceListSchemaExtensionsResponse,
    DirectoryServiceListTagsForResourceRequest,
    DirectoryServiceListTagsForResourceResponse,
    DirectoryServiceRegisterCertificateRequest,
    DirectoryServiceRegisterCertificateResponse,
    DirectoryServiceRegisterEventTopicRequest,
    DirectoryServiceRegisterEventTopicResponse,
    DirectoryServiceRejectSharedDirectoryRequest,
    DirectoryServiceRejectSharedDirectoryResponse,
    DirectoryServiceRemoveIpRoutesRequest,
    DirectoryServiceRemoveIpRoutesResponse,
    DirectoryServiceRemoveRegionRequest,
    DirectoryServiceRemoveRegionResponse,
    DirectoryServiceRemoveTagsFromResourceRequest,
    DirectoryServiceRemoveTagsFromResourceResponse,
    DirectoryServiceResetUserPasswordRequest,
    DirectoryServiceResetUserPasswordResponse,
    DirectoryServiceRestoreFromSnapshotRequest,
    DirectoryServiceRestoreFromSnapshotResponse,
    DirectoryServiceShareDirectoryRequest,
    DirectoryServiceShareDirectoryResponse,
    DirectoryServiceStartADAssessmentRequest,
    DirectoryServiceStartADAssessmentResponse,
    DirectoryServiceStartSchemaExtensionRequest,
    DirectoryServiceStartSchemaExtensionResponse,
    DirectoryServiceUnshareDirectoryRequest,
    DirectoryServiceUnshareDirectoryResponse,
    DirectoryServiceUpdateConditionalForwarderRequest,
    DirectoryServiceUpdateConditionalForwarderResponse,
    DirectoryServiceUpdateDirectorySetupRequest,
    DirectoryServiceUpdateDirectorySetupResponse,
    DirectoryServiceUpdateHybridADRequest,
    DirectoryServiceUpdateHybridADResponse,
    DirectoryServiceUpdateNumberOfDomainControllersRequest,
    DirectoryServiceUpdateNumberOfDomainControllersResponse,
    DirectoryServiceUpdateRadiusRequest,
    DirectoryServiceUpdateRadiusResponse,
    DirectoryServiceUpdateSettingsRequest,
    DirectoryServiceUpdateSettingsResponse,
    DirectoryServiceUpdateTrustRequest,
    DirectoryServiceUpdateTrustResponse,
    DirectoryServiceVerifyTrustRequest,
    DirectoryServiceVerifyTrustResponse,
)
from werkflow_aws.types.directory_service_client import DirectoryServiceClient
from .base import AWSBaseService


class AWSDirectoryService(AWSBaseService[DirectoryServiceClient]):
    service_name = 'directory-service'
    boto3_service_name = 'ds'

    def __init__(self) -> None:
        super().__init__(service_name='directory-service', boto3_service_name='ds')

    async def accept_shared_directory(
        self,
        request: DirectoryServiceAcceptSharedDirectoryRequest,
    ) -> DirectoryServiceAcceptSharedDirectoryResponse:
        client = self._require_client()
        return await self._execute(client.accept_shared_directory, request, DirectoryServiceAcceptSharedDirectoryResponse)

    async def add_ip_routes(
        self,
        request: DirectoryServiceAddIpRoutesRequest,
    ) -> DirectoryServiceAddIpRoutesResponse:
        client = self._require_client()
        return await self._execute(client.add_ip_routes, request, DirectoryServiceAddIpRoutesResponse)

    async def add_region(
        self,
        request: DirectoryServiceAddRegionRequest,
    ) -> DirectoryServiceAddRegionResponse:
        client = self._require_client()
        return await self._execute(client.add_region, request, DirectoryServiceAddRegionResponse)

    async def add_tags_to_resource(
        self,
        request: DirectoryServiceAddTagsToResourceRequest,
    ) -> DirectoryServiceAddTagsToResourceResponse:
        client = self._require_client()
        return await self._execute(client.add_tags_to_resource, request, DirectoryServiceAddTagsToResourceResponse)

    async def cancel_schema_extension(
        self,
        request: DirectoryServiceCancelSchemaExtensionRequest,
    ) -> DirectoryServiceCancelSchemaExtensionResponse:
        client = self._require_client()
        return await self._execute(client.cancel_schema_extension, request, DirectoryServiceCancelSchemaExtensionResponse)

    async def connect_directory(
        self,
        request: DirectoryServiceConnectDirectoryRequest,
    ) -> DirectoryServiceConnectDirectoryResponse:
        client = self._require_client()
        return await self._execute(client.connect_directory, request, DirectoryServiceConnectDirectoryResponse)

    async def create_alias(
        self,
        request: DirectoryServiceCreateAliasRequest,
    ) -> DirectoryServiceCreateAliasResponse:
        client = self._require_client()
        return await self._execute(client.create_alias, request, DirectoryServiceCreateAliasResponse)

    async def create_computer(
        self,
        request: DirectoryServiceCreateComputerRequest,
    ) -> DirectoryServiceCreateComputerResponse:
        client = self._require_client()
        return await self._execute(client.create_computer, request, DirectoryServiceCreateComputerResponse)

    async def create_conditional_forwarder(
        self,
        request: DirectoryServiceCreateConditionalForwarderRequest,
    ) -> DirectoryServiceCreateConditionalForwarderResponse:
        client = self._require_client()
        return await self._execute(client.create_conditional_forwarder, request, DirectoryServiceCreateConditionalForwarderResponse)

    async def create_directory(
        self,
        request: DirectoryServiceCreateDirectoryRequest,
    ) -> DirectoryServiceCreateDirectoryResponse:
        client = self._require_client()
        return await self._execute(client.create_directory, request, DirectoryServiceCreateDirectoryResponse)

    async def create_hybrid_ad(
        self,
        request: DirectoryServiceCreateHybridADRequest,
    ) -> DirectoryServiceCreateHybridADResponse:
        client = self._require_client()
        return await self._execute(client.create_hybrid_ad, request, DirectoryServiceCreateHybridADResponse)

    async def create_log_subscription(
        self,
        request: DirectoryServiceCreateLogSubscriptionRequest,
    ) -> DirectoryServiceCreateLogSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.create_log_subscription, request, DirectoryServiceCreateLogSubscriptionResponse)

    async def create_microsoft_ad(
        self,
        request: DirectoryServiceCreateMicrosoftADRequest,
    ) -> DirectoryServiceCreateMicrosoftADResponse:
        client = self._require_client()
        return await self._execute(client.create_microsoft_ad, request, DirectoryServiceCreateMicrosoftADResponse)

    async def create_snapshot(
        self,
        request: DirectoryServiceCreateSnapshotRequest,
    ) -> DirectoryServiceCreateSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.create_snapshot, request, DirectoryServiceCreateSnapshotResponse)

    async def create_trust(
        self,
        request: DirectoryServiceCreateTrustRequest,
    ) -> DirectoryServiceCreateTrustResponse:
        client = self._require_client()
        return await self._execute(client.create_trust, request, DirectoryServiceCreateTrustResponse)

    async def delete_ad_assessment(
        self,
        request: DirectoryServiceDeleteADAssessmentRequest,
    ) -> DirectoryServiceDeleteADAssessmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_ad_assessment, request, DirectoryServiceDeleteADAssessmentResponse)

    async def delete_conditional_forwarder(
        self,
        request: DirectoryServiceDeleteConditionalForwarderRequest,
    ) -> DirectoryServiceDeleteConditionalForwarderResponse:
        client = self._require_client()
        return await self._execute(client.delete_conditional_forwarder, request, DirectoryServiceDeleteConditionalForwarderResponse)

    async def delete_directory(
        self,
        request: DirectoryServiceDeleteDirectoryRequest,
    ) -> DirectoryServiceDeleteDirectoryResponse:
        client = self._require_client()
        return await self._execute(client.delete_directory, request, DirectoryServiceDeleteDirectoryResponse)

    async def delete_log_subscription(
        self,
        request: DirectoryServiceDeleteLogSubscriptionRequest,
    ) -> DirectoryServiceDeleteLogSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.delete_log_subscription, request, DirectoryServiceDeleteLogSubscriptionResponse)

    async def delete_snapshot(
        self,
        request: DirectoryServiceDeleteSnapshotRequest,
    ) -> DirectoryServiceDeleteSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.delete_snapshot, request, DirectoryServiceDeleteSnapshotResponse)

    async def delete_trust(
        self,
        request: DirectoryServiceDeleteTrustRequest,
    ) -> DirectoryServiceDeleteTrustResponse:
        client = self._require_client()
        return await self._execute(client.delete_trust, request, DirectoryServiceDeleteTrustResponse)

    async def deregister_certificate(
        self,
        request: DirectoryServiceDeregisterCertificateRequest,
    ) -> DirectoryServiceDeregisterCertificateResponse:
        client = self._require_client()
        return await self._execute(client.deregister_certificate, request, DirectoryServiceDeregisterCertificateResponse)

    async def deregister_event_topic(
        self,
        request: DirectoryServiceDeregisterEventTopicRequest,
    ) -> DirectoryServiceDeregisterEventTopicResponse:
        client = self._require_client()
        return await self._execute(client.deregister_event_topic, request, DirectoryServiceDeregisterEventTopicResponse)

    async def describe_ad_assessment(
        self,
        request: DirectoryServiceDescribeADAssessmentRequest,
    ) -> DirectoryServiceDescribeADAssessmentResponse:
        client = self._require_client()
        return await self._execute(client.describe_ad_assessment, request, DirectoryServiceDescribeADAssessmentResponse)

    async def describe_ca_enrollment_policy(
        self,
        request: DirectoryServiceDescribeCAEnrollmentPolicyRequest,
    ) -> DirectoryServiceDescribeCAEnrollmentPolicyResponse:
        client = self._require_client()
        return await self._execute(client.describe_ca_enrollment_policy, request, DirectoryServiceDescribeCAEnrollmentPolicyResponse)

    async def describe_certificate(
        self,
        request: DirectoryServiceDescribeCertificateRequest,
    ) -> DirectoryServiceDescribeCertificateResponse:
        client = self._require_client()
        return await self._execute(client.describe_certificate, request, DirectoryServiceDescribeCertificateResponse)

    async def describe_client_authentication_settings(
        self,
        request: DirectoryServiceDescribeClientAuthenticationSettingsRequest,
    ) -> DirectoryServiceDescribeClientAuthenticationSettingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_client_authentication_settings, request, DirectoryServiceDescribeClientAuthenticationSettingsResponse)

    async def describe_client_authentication_settings_paginated(
        self,
        request: DirectoryServiceDescribeClientAuthenticationSettingsRequest,
    ) -> list[DirectoryServiceDescribeClientAuthenticationSettingsResponse]:
        return await self._paginate('describe_client_authentication_settings', request, DirectoryServiceDescribeClientAuthenticationSettingsResponse)

    async def describe_conditional_forwarders(
        self,
        request: DirectoryServiceDescribeConditionalForwardersRequest,
    ) -> DirectoryServiceDescribeConditionalForwardersResponse:
        client = self._require_client()
        return await self._execute(client.describe_conditional_forwarders, request, DirectoryServiceDescribeConditionalForwardersResponse)

    async def describe_directories(
        self,
        request: DirectoryServiceDescribeDirectoriesRequest | None = None,
    ) -> DirectoryServiceDescribeDirectoriesResponse:
        client = self._require_client()
        return await self._execute(client.describe_directories, request, DirectoryServiceDescribeDirectoriesResponse)

    async def describe_directories_paginated(
        self,
        request: DirectoryServiceDescribeDirectoriesRequest | None = None,
    ) -> list[DirectoryServiceDescribeDirectoriesResponse]:
        return await self._paginate('describe_directories', request, DirectoryServiceDescribeDirectoriesResponse)

    async def describe_directory_data_access(
        self,
        request: DirectoryServiceDescribeDirectoryDataAccessRequest,
    ) -> DirectoryServiceDescribeDirectoryDataAccessResponse:
        client = self._require_client()
        return await self._execute(client.describe_directory_data_access, request, DirectoryServiceDescribeDirectoryDataAccessResponse)

    async def describe_domain_controllers(
        self,
        request: DirectoryServiceDescribeDomainControllersRequest,
    ) -> DirectoryServiceDescribeDomainControllersResponse:
        client = self._require_client()
        return await self._execute(client.describe_domain_controllers, request, DirectoryServiceDescribeDomainControllersResponse)

    async def describe_domain_controllers_paginated(
        self,
        request: DirectoryServiceDescribeDomainControllersRequest,
    ) -> list[DirectoryServiceDescribeDomainControllersResponse]:
        return await self._paginate('describe_domain_controllers', request, DirectoryServiceDescribeDomainControllersResponse)

    async def describe_event_topics(
        self,
        request: DirectoryServiceDescribeEventTopicsRequest | None = None,
    ) -> DirectoryServiceDescribeEventTopicsResponse:
        client = self._require_client()
        return await self._execute(client.describe_event_topics, request, DirectoryServiceDescribeEventTopicsResponse)

    async def describe_hybrid_ad_update(
        self,
        request: DirectoryServiceDescribeHybridADUpdateRequest,
    ) -> DirectoryServiceDescribeHybridADUpdateResponse:
        client = self._require_client()
        return await self._execute(client.describe_hybrid_ad_update, request, DirectoryServiceDescribeHybridADUpdateResponse)

    async def describe_ldaps_settings(
        self,
        request: DirectoryServiceDescribeLDAPSSettingsRequest,
    ) -> DirectoryServiceDescribeLDAPSSettingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_ldaps_settings, request, DirectoryServiceDescribeLDAPSSettingsResponse)

    async def describe_ldaps_settings_paginated(
        self,
        request: DirectoryServiceDescribeLDAPSSettingsRequest,
    ) -> list[DirectoryServiceDescribeLDAPSSettingsResponse]:
        return await self._paginate('describe_ldaps_settings', request, DirectoryServiceDescribeLDAPSSettingsResponse)

    async def describe_regions(
        self,
        request: DirectoryServiceDescribeRegionsRequest,
    ) -> DirectoryServiceDescribeRegionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_regions, request, DirectoryServiceDescribeRegionsResponse)

    async def describe_regions_paginated(
        self,
        request: DirectoryServiceDescribeRegionsRequest,
    ) -> list[DirectoryServiceDescribeRegionsResponse]:
        return await self._paginate('describe_regions', request, DirectoryServiceDescribeRegionsResponse)

    async def describe_settings(
        self,
        request: DirectoryServiceDescribeSettingsRequest,
    ) -> DirectoryServiceDescribeSettingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_settings, request, DirectoryServiceDescribeSettingsResponse)

    async def describe_shared_directories(
        self,
        request: DirectoryServiceDescribeSharedDirectoriesRequest,
    ) -> DirectoryServiceDescribeSharedDirectoriesResponse:
        client = self._require_client()
        return await self._execute(client.describe_shared_directories, request, DirectoryServiceDescribeSharedDirectoriesResponse)

    async def describe_shared_directories_paginated(
        self,
        request: DirectoryServiceDescribeSharedDirectoriesRequest,
    ) -> list[DirectoryServiceDescribeSharedDirectoriesResponse]:
        return await self._paginate('describe_shared_directories', request, DirectoryServiceDescribeSharedDirectoriesResponse)

    async def describe_snapshots(
        self,
        request: DirectoryServiceDescribeSnapshotsRequest | None = None,
    ) -> DirectoryServiceDescribeSnapshotsResponse:
        client = self._require_client()
        return await self._execute(client.describe_snapshots, request, DirectoryServiceDescribeSnapshotsResponse)

    async def describe_snapshots_paginated(
        self,
        request: DirectoryServiceDescribeSnapshotsRequest | None = None,
    ) -> list[DirectoryServiceDescribeSnapshotsResponse]:
        return await self._paginate('describe_snapshots', request, DirectoryServiceDescribeSnapshotsResponse)

    async def describe_trusts(
        self,
        request: DirectoryServiceDescribeTrustsRequest | None = None,
    ) -> DirectoryServiceDescribeTrustsResponse:
        client = self._require_client()
        return await self._execute(client.describe_trusts, request, DirectoryServiceDescribeTrustsResponse)

    async def describe_trusts_paginated(
        self,
        request: DirectoryServiceDescribeTrustsRequest | None = None,
    ) -> list[DirectoryServiceDescribeTrustsResponse]:
        return await self._paginate('describe_trusts', request, DirectoryServiceDescribeTrustsResponse)

    async def describe_update_directory(
        self,
        request: DirectoryServiceDescribeUpdateDirectoryRequest,
    ) -> DirectoryServiceDescribeUpdateDirectoryResponse:
        client = self._require_client()
        return await self._execute(client.describe_update_directory, request, DirectoryServiceDescribeUpdateDirectoryResponse)

    async def describe_update_directory_paginated(
        self,
        request: DirectoryServiceDescribeUpdateDirectoryRequest,
    ) -> list[DirectoryServiceDescribeUpdateDirectoryResponse]:
        return await self._paginate('describe_update_directory', request, DirectoryServiceDescribeUpdateDirectoryResponse)

    async def disable_ca_enrollment_policy(
        self,
        request: DirectoryServiceDisableCAEnrollmentPolicyRequest,
    ) -> DirectoryServiceDisableCAEnrollmentPolicyResponse:
        client = self._require_client()
        return await self._execute(client.disable_ca_enrollment_policy, request, DirectoryServiceDisableCAEnrollmentPolicyResponse)

    async def disable_client_authentication(
        self,
        request: DirectoryServiceDisableClientAuthenticationRequest,
    ) -> DirectoryServiceDisableClientAuthenticationResponse:
        client = self._require_client()
        return await self._execute(client.disable_client_authentication, request, DirectoryServiceDisableClientAuthenticationResponse)

    async def disable_directory_data_access(
        self,
        request: DirectoryServiceDisableDirectoryDataAccessRequest,
    ) -> DirectoryServiceDisableDirectoryDataAccessResponse:
        client = self._require_client()
        return await self._execute(client.disable_directory_data_access, request, DirectoryServiceDisableDirectoryDataAccessResponse)

    async def disable_ldaps(
        self,
        request: DirectoryServiceDisableLDAPSRequest,
    ) -> DirectoryServiceDisableLDAPSResponse:
        client = self._require_client()
        return await self._execute(client.disable_ldaps, request, DirectoryServiceDisableLDAPSResponse)

    async def disable_radius(
        self,
        request: DirectoryServiceDisableRadiusRequest,
    ) -> DirectoryServiceDisableRadiusResponse:
        client = self._require_client()
        return await self._execute(client.disable_radius, request, DirectoryServiceDisableRadiusResponse)

    async def disable_sso(
        self,
        request: DirectoryServiceDisableSsoRequest,
    ) -> DirectoryServiceDisableSsoResponse:
        client = self._require_client()
        return await self._execute(client.disable_sso, request, DirectoryServiceDisableSsoResponse)

    async def enable_ca_enrollment_policy(
        self,
        request: DirectoryServiceEnableCAEnrollmentPolicyRequest,
    ) -> DirectoryServiceEnableCAEnrollmentPolicyResponse:
        client = self._require_client()
        return await self._execute(client.enable_ca_enrollment_policy, request, DirectoryServiceEnableCAEnrollmentPolicyResponse)

    async def enable_client_authentication(
        self,
        request: DirectoryServiceEnableClientAuthenticationRequest,
    ) -> DirectoryServiceEnableClientAuthenticationResponse:
        client = self._require_client()
        return await self._execute(client.enable_client_authentication, request, DirectoryServiceEnableClientAuthenticationResponse)

    async def enable_directory_data_access(
        self,
        request: DirectoryServiceEnableDirectoryDataAccessRequest,
    ) -> DirectoryServiceEnableDirectoryDataAccessResponse:
        client = self._require_client()
        return await self._execute(client.enable_directory_data_access, request, DirectoryServiceEnableDirectoryDataAccessResponse)

    async def enable_ldaps(
        self,
        request: DirectoryServiceEnableLDAPSRequest,
    ) -> DirectoryServiceEnableLDAPSResponse:
        client = self._require_client()
        return await self._execute(client.enable_ldaps, request, DirectoryServiceEnableLDAPSResponse)

    async def enable_radius(
        self,
        request: DirectoryServiceEnableRadiusRequest,
    ) -> DirectoryServiceEnableRadiusResponse:
        client = self._require_client()
        return await self._execute(client.enable_radius, request, DirectoryServiceEnableRadiusResponse)

    async def enable_sso(
        self,
        request: DirectoryServiceEnableSsoRequest,
    ) -> DirectoryServiceEnableSsoResponse:
        client = self._require_client()
        return await self._execute(client.enable_sso, request, DirectoryServiceEnableSsoResponse)

    async def get_directory_limits(
        self,
        request: DirectoryServiceGetDirectoryLimitsRequest | None = None,
    ) -> DirectoryServiceGetDirectoryLimitsResponse:
        client = self._require_client()
        return await self._execute(client.get_directory_limits, request, DirectoryServiceGetDirectoryLimitsResponse)

    async def get_snapshot_limits(
        self,
        request: DirectoryServiceGetSnapshotLimitsRequest,
    ) -> DirectoryServiceGetSnapshotLimitsResponse:
        client = self._require_client()
        return await self._execute(client.get_snapshot_limits, request, DirectoryServiceGetSnapshotLimitsResponse)

    async def list_ad_assessments(
        self,
        request: DirectoryServiceListADAssessmentsRequest | None = None,
    ) -> DirectoryServiceListADAssessmentsResponse:
        client = self._require_client()
        return await self._execute(client.list_ad_assessments, request, DirectoryServiceListADAssessmentsResponse)

    async def list_ad_assessments_paginated(
        self,
        request: DirectoryServiceListADAssessmentsRequest | None = None,
    ) -> list[DirectoryServiceListADAssessmentsResponse]:
        return await self._paginate('list_ad_assessments', request, DirectoryServiceListADAssessmentsResponse)

    async def list_certificates(
        self,
        request: DirectoryServiceListCertificatesRequest,
    ) -> DirectoryServiceListCertificatesResponse:
        client = self._require_client()
        return await self._execute(client.list_certificates, request, DirectoryServiceListCertificatesResponse)

    async def list_certificates_paginated(
        self,
        request: DirectoryServiceListCertificatesRequest,
    ) -> list[DirectoryServiceListCertificatesResponse]:
        return await self._paginate('list_certificates', request, DirectoryServiceListCertificatesResponse)

    async def list_ip_routes(
        self,
        request: DirectoryServiceListIpRoutesRequest,
    ) -> DirectoryServiceListIpRoutesResponse:
        client = self._require_client()
        return await self._execute(client.list_ip_routes, request, DirectoryServiceListIpRoutesResponse)

    async def list_ip_routes_paginated(
        self,
        request: DirectoryServiceListIpRoutesRequest,
    ) -> list[DirectoryServiceListIpRoutesResponse]:
        return await self._paginate('list_ip_routes', request, DirectoryServiceListIpRoutesResponse)

    async def list_log_subscriptions(
        self,
        request: DirectoryServiceListLogSubscriptionsRequest | None = None,
    ) -> DirectoryServiceListLogSubscriptionsResponse:
        client = self._require_client()
        return await self._execute(client.list_log_subscriptions, request, DirectoryServiceListLogSubscriptionsResponse)

    async def list_log_subscriptions_paginated(
        self,
        request: DirectoryServiceListLogSubscriptionsRequest | None = None,
    ) -> list[DirectoryServiceListLogSubscriptionsResponse]:
        return await self._paginate('list_log_subscriptions', request, DirectoryServiceListLogSubscriptionsResponse)

    async def list_schema_extensions(
        self,
        request: DirectoryServiceListSchemaExtensionsRequest,
    ) -> DirectoryServiceListSchemaExtensionsResponse:
        client = self._require_client()
        return await self._execute(client.list_schema_extensions, request, DirectoryServiceListSchemaExtensionsResponse)

    async def list_schema_extensions_paginated(
        self,
        request: DirectoryServiceListSchemaExtensionsRequest,
    ) -> list[DirectoryServiceListSchemaExtensionsResponse]:
        return await self._paginate('list_schema_extensions', request, DirectoryServiceListSchemaExtensionsResponse)

    async def list_tags_for_resource(
        self,
        request: DirectoryServiceListTagsForResourceRequest,
    ) -> DirectoryServiceListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, DirectoryServiceListTagsForResourceResponse)

    async def list_tags_for_resource_paginated(
        self,
        request: DirectoryServiceListTagsForResourceRequest,
    ) -> list[DirectoryServiceListTagsForResourceResponse]:
        return await self._paginate('list_tags_for_resource', request, DirectoryServiceListTagsForResourceResponse)

    async def register_certificate(
        self,
        request: DirectoryServiceRegisterCertificateRequest,
    ) -> DirectoryServiceRegisterCertificateResponse:
        client = self._require_client()
        return await self._execute(client.register_certificate, request, DirectoryServiceRegisterCertificateResponse)

    async def register_event_topic(
        self,
        request: DirectoryServiceRegisterEventTopicRequest,
    ) -> DirectoryServiceRegisterEventTopicResponse:
        client = self._require_client()
        return await self._execute(client.register_event_topic, request, DirectoryServiceRegisterEventTopicResponse)

    async def reject_shared_directory(
        self,
        request: DirectoryServiceRejectSharedDirectoryRequest,
    ) -> DirectoryServiceRejectSharedDirectoryResponse:
        client = self._require_client()
        return await self._execute(client.reject_shared_directory, request, DirectoryServiceRejectSharedDirectoryResponse)

    async def remove_ip_routes(
        self,
        request: DirectoryServiceRemoveIpRoutesRequest,
    ) -> DirectoryServiceRemoveIpRoutesResponse:
        client = self._require_client()
        return await self._execute(client.remove_ip_routes, request, DirectoryServiceRemoveIpRoutesResponse)

    async def remove_region(
        self,
        request: DirectoryServiceRemoveRegionRequest,
    ) -> DirectoryServiceRemoveRegionResponse:
        client = self._require_client()
        return await self._execute(client.remove_region, request, DirectoryServiceRemoveRegionResponse)

    async def remove_tags_from_resource(
        self,
        request: DirectoryServiceRemoveTagsFromResourceRequest,
    ) -> DirectoryServiceRemoveTagsFromResourceResponse:
        client = self._require_client()
        return await self._execute(client.remove_tags_from_resource, request, DirectoryServiceRemoveTagsFromResourceResponse)

    async def reset_user_password(
        self,
        request: DirectoryServiceResetUserPasswordRequest,
    ) -> DirectoryServiceResetUserPasswordResponse:
        client = self._require_client()
        return await self._execute(client.reset_user_password, request, DirectoryServiceResetUserPasswordResponse)

    async def restore_from_snapshot(
        self,
        request: DirectoryServiceRestoreFromSnapshotRequest,
    ) -> DirectoryServiceRestoreFromSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.restore_from_snapshot, request, DirectoryServiceRestoreFromSnapshotResponse)

    async def share_directory(
        self,
        request: DirectoryServiceShareDirectoryRequest,
    ) -> DirectoryServiceShareDirectoryResponse:
        client = self._require_client()
        return await self._execute(client.share_directory, request, DirectoryServiceShareDirectoryResponse)

    async def start_ad_assessment(
        self,
        request: DirectoryServiceStartADAssessmentRequest | None = None,
    ) -> DirectoryServiceStartADAssessmentResponse:
        client = self._require_client()
        return await self._execute(client.start_ad_assessment, request, DirectoryServiceStartADAssessmentResponse)

    async def start_schema_extension(
        self,
        request: DirectoryServiceStartSchemaExtensionRequest,
    ) -> DirectoryServiceStartSchemaExtensionResponse:
        client = self._require_client()
        return await self._execute(client.start_schema_extension, request, DirectoryServiceStartSchemaExtensionResponse)

    async def unshare_directory(
        self,
        request: DirectoryServiceUnshareDirectoryRequest,
    ) -> DirectoryServiceUnshareDirectoryResponse:
        client = self._require_client()
        return await self._execute(client.unshare_directory, request, DirectoryServiceUnshareDirectoryResponse)

    async def update_conditional_forwarder(
        self,
        request: DirectoryServiceUpdateConditionalForwarderRequest,
    ) -> DirectoryServiceUpdateConditionalForwarderResponse:
        client = self._require_client()
        return await self._execute(client.update_conditional_forwarder, request, DirectoryServiceUpdateConditionalForwarderResponse)

    async def update_directory_setup(
        self,
        request: DirectoryServiceUpdateDirectorySetupRequest,
    ) -> DirectoryServiceUpdateDirectorySetupResponse:
        client = self._require_client()
        return await self._execute(client.update_directory_setup, request, DirectoryServiceUpdateDirectorySetupResponse)

    async def update_hybrid_ad(
        self,
        request: DirectoryServiceUpdateHybridADRequest,
    ) -> DirectoryServiceUpdateHybridADResponse:
        client = self._require_client()
        return await self._execute(client.update_hybrid_ad, request, DirectoryServiceUpdateHybridADResponse)

    async def update_number_of_domain_controllers(
        self,
        request: DirectoryServiceUpdateNumberOfDomainControllersRequest,
    ) -> DirectoryServiceUpdateNumberOfDomainControllersResponse:
        client = self._require_client()
        return await self._execute(client.update_number_of_domain_controllers, request, DirectoryServiceUpdateNumberOfDomainControllersResponse)

    async def update_radius(
        self,
        request: DirectoryServiceUpdateRadiusRequest,
    ) -> DirectoryServiceUpdateRadiusResponse:
        client = self._require_client()
        return await self._execute(client.update_radius, request, DirectoryServiceUpdateRadiusResponse)

    async def update_settings(
        self,
        request: DirectoryServiceUpdateSettingsRequest,
    ) -> DirectoryServiceUpdateSettingsResponse:
        client = self._require_client()
        return await self._execute(client.update_settings, request, DirectoryServiceUpdateSettingsResponse)

    async def update_trust(
        self,
        request: DirectoryServiceUpdateTrustRequest,
    ) -> DirectoryServiceUpdateTrustResponse:
        client = self._require_client()
        return await self._execute(client.update_trust, request, DirectoryServiceUpdateTrustResponse)

    async def verify_trust(
        self,
        request: DirectoryServiceVerifyTrustRequest,
    ) -> DirectoryServiceVerifyTrustResponse:
        client = self._require_client()
        return await self._execute(client.verify_trust, request, DirectoryServiceVerifyTrustResponse)
