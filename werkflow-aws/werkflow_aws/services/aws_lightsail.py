from werkflow_aws.models.lightsail import (
    LightsailAllocateStaticIpRequest,
    LightsailAllocateStaticIpResponse,
    LightsailAttachCertificateToDistributionRequest,
    LightsailAttachCertificateToDistributionResponse,
    LightsailAttachDiskRequest,
    LightsailAttachDiskResponse,
    LightsailAttachInstancesToLoadBalancerRequest,
    LightsailAttachInstancesToLoadBalancerResponse,
    LightsailAttachLoadBalancerTlsCertificateRequest,
    LightsailAttachLoadBalancerTlsCertificateResponse,
    LightsailAttachStaticIpRequest,
    LightsailAttachStaticIpResponse,
    LightsailCheckSubdomainAvailabilityRequest,
    LightsailCheckSubdomainAvailabilityResponse,
    LightsailCloseInstancePublicPortsRequest,
    LightsailCloseInstancePublicPortsResponse,
    LightsailCopySnapshotRequest,
    LightsailCopySnapshotResponse,
    LightsailCreateBucketAccessKeyRequest,
    LightsailCreateBucketAccessKeyResponse,
    LightsailCreateBucketRequest,
    LightsailCreateBucketResponse,
    LightsailCreateCertificateRequest,
    LightsailCreateCertificateResponse,
    LightsailCreateCloudFormationStackRequest,
    LightsailCreateCloudFormationStackResponse,
    LightsailCreateContactMethodRequest,
    LightsailCreateContactMethodResponse,
    LightsailCreateContainerServiceDeploymentRequest,
    LightsailCreateContainerServiceDeploymentResponse,
    LightsailCreateContainerServiceRegistryLoginRequest,
    LightsailCreateContainerServiceRegistryLoginResponse,
    LightsailCreateContainerServiceRequest,
    LightsailCreateContainerServiceResponse,
    LightsailCreateDiskFromSnapshotRequest,
    LightsailCreateDiskFromSnapshotResponse,
    LightsailCreateDiskRequest,
    LightsailCreateDiskResponse,
    LightsailCreateDiskSnapshotRequest,
    LightsailCreateDiskSnapshotResponse,
    LightsailCreateDistributionRequest,
    LightsailCreateDistributionResponse,
    LightsailCreateDomainEntryRequest,
    LightsailCreateDomainEntryResponse,
    LightsailCreateDomainRequest,
    LightsailCreateDomainResponse,
    LightsailCreateGUISessionAccessDetailsRequest,
    LightsailCreateGUISessionAccessDetailsResponse,
    LightsailCreateInstanceSnapshotRequest,
    LightsailCreateInstanceSnapshotResponse,
    LightsailCreateInstancesFromSnapshotRequest,
    LightsailCreateInstancesFromSnapshotResponse,
    LightsailCreateInstancesRequest,
    LightsailCreateInstancesResponse,
    LightsailCreateKeyPairRequest,
    LightsailCreateKeyPairResponse,
    LightsailCreateLoadBalancerRequest,
    LightsailCreateLoadBalancerResponse,
    LightsailCreateLoadBalancerTlsCertificateRequest,
    LightsailCreateLoadBalancerTlsCertificateResponse,
    LightsailCreateRelationalDatabaseFromSnapshotRequest,
    LightsailCreateRelationalDatabaseFromSnapshotResponse,
    LightsailCreateRelationalDatabaseRequest,
    LightsailCreateRelationalDatabaseResponse,
    LightsailCreateRelationalDatabaseSnapshotRequest,
    LightsailCreateRelationalDatabaseSnapshotResponse,
    LightsailCreateSubdomainRequest,
    LightsailCreateSubdomainResponse,
    LightsailDeleteAlarmRequest,
    LightsailDeleteAlarmResponse,
    LightsailDeleteAutoSnapshotRequest,
    LightsailDeleteAutoSnapshotResponse,
    LightsailDeleteBucketAccessKeyRequest,
    LightsailDeleteBucketAccessKeyResponse,
    LightsailDeleteBucketRequest,
    LightsailDeleteBucketResponse,
    LightsailDeleteCertificateRequest,
    LightsailDeleteCertificateResponse,
    LightsailDeleteContactMethodRequest,
    LightsailDeleteContactMethodResponse,
    LightsailDeleteContainerImageRequest,
    LightsailDeleteContainerImageResponse,
    LightsailDeleteContainerServiceRequest,
    LightsailDeleteContainerServiceResponse,
    LightsailDeleteDiskRequest,
    LightsailDeleteDiskResponse,
    LightsailDeleteDiskSnapshotRequest,
    LightsailDeleteDiskSnapshotResponse,
    LightsailDeleteDistributionRequest,
    LightsailDeleteDistributionResponse,
    LightsailDeleteDomainEntryRequest,
    LightsailDeleteDomainEntryResponse,
    LightsailDeleteDomainRequest,
    LightsailDeleteDomainResponse,
    LightsailDeleteInstanceRequest,
    LightsailDeleteInstanceResponse,
    LightsailDeleteInstanceSnapshotRequest,
    LightsailDeleteInstanceSnapshotResponse,
    LightsailDeleteKeyPairRequest,
    LightsailDeleteKeyPairResponse,
    LightsailDeleteKnownHostKeysRequest,
    LightsailDeleteKnownHostKeysResponse,
    LightsailDeleteLoadBalancerRequest,
    LightsailDeleteLoadBalancerResponse,
    LightsailDeleteLoadBalancerTlsCertificateRequest,
    LightsailDeleteLoadBalancerTlsCertificateResponse,
    LightsailDeleteRelationalDatabaseRequest,
    LightsailDeleteRelationalDatabaseResponse,
    LightsailDeleteRelationalDatabaseSnapshotRequest,
    LightsailDeleteRelationalDatabaseSnapshotResponse,
    LightsailDeleteSubdomainRequest,
    LightsailDeleteSubdomainResponse,
    LightsailDetachCertificateFromDistributionRequest,
    LightsailDetachCertificateFromDistributionResponse,
    LightsailDetachDiskRequest,
    LightsailDetachDiskResponse,
    LightsailDetachInstancesFromLoadBalancerRequest,
    LightsailDetachInstancesFromLoadBalancerResponse,
    LightsailDetachStaticIpRequest,
    LightsailDetachStaticIpResponse,
    LightsailDisableAddOnRequest,
    LightsailDisableAddOnResponse,
    LightsailDownloadDefaultKeyPairRequest,
    LightsailDownloadDefaultKeyPairResponse,
    LightsailEnableAddOnRequest,
    LightsailEnableAddOnResponse,
    LightsailExportSnapshotRequest,
    LightsailExportSnapshotResponse,
    LightsailGetActiveNamesRequest,
    LightsailGetActiveNamesResponse,
    LightsailGetAlarmsRequest,
    LightsailGetAlarmsResponse,
    LightsailGetAutoSnapshotsRequest,
    LightsailGetAutoSnapshotsResponse,
    LightsailGetBlueprintsRequest,
    LightsailGetBlueprintsResponse,
    LightsailGetBucketAccessKeysRequest,
    LightsailGetBucketAccessKeysResponse,
    LightsailGetBucketBundlesRequest,
    LightsailGetBucketBundlesResponse,
    LightsailGetBucketMetricDataRequest,
    LightsailGetBucketMetricDataResponse,
    LightsailGetBucketsRequest,
    LightsailGetBucketsResponse,
    LightsailGetBundlesRequest,
    LightsailGetBundlesResponse,
    LightsailGetCertificatesRequest,
    LightsailGetCertificatesResponse,
    LightsailGetCloudFormationStackRecordsRequest,
    LightsailGetCloudFormationStackRecordsResponse,
    LightsailGetContactMethodsRequest,
    LightsailGetContactMethodsResponse,
    LightsailGetContainerAPIMetadataRequest,
    LightsailGetContainerAPIMetadataResponse,
    LightsailGetContainerImagesRequest,
    LightsailGetContainerImagesResponse,
    LightsailGetContainerLogRequest,
    LightsailGetContainerLogResponse,
    LightsailGetContainerServiceDeploymentsRequest,
    LightsailGetContainerServiceDeploymentsResponse,
    LightsailGetContainerServiceMetricDataRequest,
    LightsailGetContainerServiceMetricDataResponse,
    LightsailGetContainerServicePowersRequest,
    LightsailGetContainerServicePowersResponse,
    LightsailGetContainerServicesRequest,
    LightsailGetContainerServicesResponse,
    LightsailGetCostEstimateRequest,
    LightsailGetCostEstimateResponse,
    LightsailGetDiskRequest,
    LightsailGetDiskResponse,
    LightsailGetDiskSnapshotRequest,
    LightsailGetDiskSnapshotResponse,
    LightsailGetDiskSnapshotsRequest,
    LightsailGetDiskSnapshotsResponse,
    LightsailGetDisksRequest,
    LightsailGetDisksResponse,
    LightsailGetDistributionBundlesRequest,
    LightsailGetDistributionBundlesResponse,
    LightsailGetDistributionLatestCacheResetRequest,
    LightsailGetDistributionLatestCacheResetResponse,
    LightsailGetDistributionMetricDataRequest,
    LightsailGetDistributionMetricDataResponse,
    LightsailGetDistributionsRequest,
    LightsailGetDistributionsResponse,
    LightsailGetDomainRequest,
    LightsailGetDomainResponse,
    LightsailGetDomainsRequest,
    LightsailGetDomainsResponse,
    LightsailGetExportSnapshotRecordsRequest,
    LightsailGetExportSnapshotRecordsResponse,
    LightsailGetInstanceAccessDetailsRequest,
    LightsailGetInstanceAccessDetailsResponse,
    LightsailGetInstanceMetricDataRequest,
    LightsailGetInstanceMetricDataResponse,
    LightsailGetInstancePortStatesRequest,
    LightsailGetInstancePortStatesResponse,
    LightsailGetInstanceRequest,
    LightsailGetInstanceResponse,
    LightsailGetInstanceSnapshotRequest,
    LightsailGetInstanceSnapshotResponse,
    LightsailGetInstanceSnapshotsRequest,
    LightsailGetInstanceSnapshotsResponse,
    LightsailGetInstanceStateRequest,
    LightsailGetInstanceStateResponse,
    LightsailGetInstancesRequest,
    LightsailGetInstancesResponse,
    LightsailGetKeyPairRequest,
    LightsailGetKeyPairResponse,
    LightsailGetKeyPairsRequest,
    LightsailGetKeyPairsResponse,
    LightsailGetLoadBalancerMetricDataRequest,
    LightsailGetLoadBalancerMetricDataResponse,
    LightsailGetLoadBalancerRequest,
    LightsailGetLoadBalancerResponse,
    LightsailGetLoadBalancerTlsCertificatesRequest,
    LightsailGetLoadBalancerTlsCertificatesResponse,
    LightsailGetLoadBalancerTlsPoliciesRequest,
    LightsailGetLoadBalancerTlsPoliciesResponse,
    LightsailGetLoadBalancersRequest,
    LightsailGetLoadBalancersResponse,
    LightsailGetOperationRequest,
    LightsailGetOperationResponse,
    LightsailGetOperationsForResourceRequest,
    LightsailGetOperationsForResourceResponse,
    LightsailGetOperationsRequest,
    LightsailGetOperationsResponse,
    LightsailGetProfileRequest,
    LightsailGetProfileResponse,
    LightsailGetRegionsRequest,
    LightsailGetRegionsResponse,
    LightsailGetRelationalDatabaseBlueprintsRequest,
    LightsailGetRelationalDatabaseBlueprintsResponse,
    LightsailGetRelationalDatabaseBundlesRequest,
    LightsailGetRelationalDatabaseBundlesResponse,
    LightsailGetRelationalDatabaseEventsRequest,
    LightsailGetRelationalDatabaseEventsResponse,
    LightsailGetRelationalDatabaseLogEventsRequest,
    LightsailGetRelationalDatabaseLogEventsResponse,
    LightsailGetRelationalDatabaseLogStreamsRequest,
    LightsailGetRelationalDatabaseLogStreamsResponse,
    LightsailGetRelationalDatabaseMasterUserPasswordRequest,
    LightsailGetRelationalDatabaseMasterUserPasswordResponse,
    LightsailGetRelationalDatabaseMetricDataRequest,
    LightsailGetRelationalDatabaseMetricDataResponse,
    LightsailGetRelationalDatabaseParametersRequest,
    LightsailGetRelationalDatabaseParametersResponse,
    LightsailGetRelationalDatabaseRequest,
    LightsailGetRelationalDatabaseResponse,
    LightsailGetRelationalDatabaseSnapshotRequest,
    LightsailGetRelationalDatabaseSnapshotResponse,
    LightsailGetRelationalDatabaseSnapshotsRequest,
    LightsailGetRelationalDatabaseSnapshotsResponse,
    LightsailGetRelationalDatabasesRequest,
    LightsailGetRelationalDatabasesResponse,
    LightsailGetSetupHistoryRequest,
    LightsailGetSetupHistoryResponse,
    LightsailGetStaticIpRequest,
    LightsailGetStaticIpResponse,
    LightsailGetStaticIpsRequest,
    LightsailGetStaticIpsResponse,
    LightsailGetSubdomainsRequest,
    LightsailGetSubdomainsResponse,
    LightsailImportKeyPairRequest,
    LightsailImportKeyPairResponse,
    LightsailIsVpcPeeredRequest,
    LightsailIsVpcPeeredResponse,
    LightsailOpenInstancePublicPortsRequest,
    LightsailOpenInstancePublicPortsResponse,
    LightsailPeerVpcRequest,
    LightsailPeerVpcResponse,
    LightsailPutAlarmRequest,
    LightsailPutAlarmResponse,
    LightsailPutInstancePublicPortsRequest,
    LightsailPutInstancePublicPortsResponse,
    LightsailRebootInstanceRequest,
    LightsailRebootInstanceResponse,
    LightsailRebootRelationalDatabaseRequest,
    LightsailRebootRelationalDatabaseResponse,
    LightsailRegisterContainerImageRequest,
    LightsailRegisterContainerImageResponse,
    LightsailReleaseStaticIpRequest,
    LightsailReleaseStaticIpResponse,
    LightsailResetDistributionCacheRequest,
    LightsailResetDistributionCacheResponse,
    LightsailSendContactMethodVerificationRequest,
    LightsailSendContactMethodVerificationResponse,
    LightsailSetIpAddressTypeRequest,
    LightsailSetIpAddressTypeResponse,
    LightsailSetResourceAccessForBucketRequest,
    LightsailSetResourceAccessForBucketResponse,
    LightsailSetupInstanceHttpsRequest,
    LightsailSetupInstanceHttpsResponse,
    LightsailStartGUISessionRequest,
    LightsailStartGUISessionResponse,
    LightsailStartInstanceRequest,
    LightsailStartInstanceResponse,
    LightsailStartRelationalDatabaseRequest,
    LightsailStartRelationalDatabaseResponse,
    LightsailStopGUISessionRequest,
    LightsailStopGUISessionResponse,
    LightsailStopInstanceRequest,
    LightsailStopInstanceResponse,
    LightsailStopRelationalDatabaseRequest,
    LightsailStopRelationalDatabaseResponse,
    LightsailTagResourceRequest,
    LightsailTagResourceResponse,
    LightsailTestAlarmRequest,
    LightsailTestAlarmResponse,
    LightsailUnpeerVpcRequest,
    LightsailUnpeerVpcResponse,
    LightsailUntagResourceRequest,
    LightsailUntagResourceResponse,
    LightsailUpdateBucketBundleRequest,
    LightsailUpdateBucketBundleResponse,
    LightsailUpdateBucketRequest,
    LightsailUpdateBucketResponse,
    LightsailUpdateContainerServiceRequest,
    LightsailUpdateContainerServiceResponse,
    LightsailUpdateDistributionBundleRequest,
    LightsailUpdateDistributionBundleResponse,
    LightsailUpdateDistributionRequest,
    LightsailUpdateDistributionResponse,
    LightsailUpdateDomainEntryRequest,
    LightsailUpdateDomainEntryResponse,
    LightsailUpdateInstanceMetadataOptionsRequest,
    LightsailUpdateInstanceMetadataOptionsResponse,
    LightsailUpdateLoadBalancerAttributeRequest,
    LightsailUpdateLoadBalancerAttributeResponse,
    LightsailUpdateRelationalDatabaseParametersRequest,
    LightsailUpdateRelationalDatabaseParametersResponse,
    LightsailUpdateRelationalDatabaseRequest,
    LightsailUpdateRelationalDatabaseResponse,
    LightsailUpdateSubdomainAssociationRequest,
    LightsailUpdateSubdomainAssociationResponse,
)
from werkflow_aws.types.lightsail_client import LightsailClient
from .base import AWSBaseService


class AWSLightsail(AWSBaseService[LightsailClient]):
    service_name = 'lightsail'
    boto3_service_name = 'lightsail'

    def __init__(self) -> None:
        super().__init__(service_name='lightsail', boto3_service_name='lightsail')

    async def allocate_static_ip(
        self,
        request: LightsailAllocateStaticIpRequest,
    ) -> LightsailAllocateStaticIpResponse:
        client = self._require_client()
        return await self._execute(client.allocate_static_ip, request, LightsailAllocateStaticIpResponse)

    async def attach_certificate_to_distribution(
        self,
        request: LightsailAttachCertificateToDistributionRequest,
    ) -> LightsailAttachCertificateToDistributionResponse:
        client = self._require_client()
        return await self._execute(client.attach_certificate_to_distribution, request, LightsailAttachCertificateToDistributionResponse)

    async def attach_disk(
        self,
        request: LightsailAttachDiskRequest,
    ) -> LightsailAttachDiskResponse:
        client = self._require_client()
        return await self._execute(client.attach_disk, request, LightsailAttachDiskResponse)

    async def attach_instances_to_load_balancer(
        self,
        request: LightsailAttachInstancesToLoadBalancerRequest,
    ) -> LightsailAttachInstancesToLoadBalancerResponse:
        client = self._require_client()
        return await self._execute(client.attach_instances_to_load_balancer, request, LightsailAttachInstancesToLoadBalancerResponse)

    async def attach_load_balancer_tls_certificate(
        self,
        request: LightsailAttachLoadBalancerTlsCertificateRequest,
    ) -> LightsailAttachLoadBalancerTlsCertificateResponse:
        client = self._require_client()
        return await self._execute(client.attach_load_balancer_tls_certificate, request, LightsailAttachLoadBalancerTlsCertificateResponse)

    async def attach_static_ip(
        self,
        request: LightsailAttachStaticIpRequest,
    ) -> LightsailAttachStaticIpResponse:
        client = self._require_client()
        return await self._execute(client.attach_static_ip, request, LightsailAttachStaticIpResponse)

    async def check_subdomain_availability(
        self,
        request: LightsailCheckSubdomainAvailabilityRequest,
    ) -> LightsailCheckSubdomainAvailabilityResponse:
        client = self._require_client()
        return await self._execute(client.check_subdomain_availability, request, LightsailCheckSubdomainAvailabilityResponse)

    async def close_instance_public_ports(
        self,
        request: LightsailCloseInstancePublicPortsRequest,
    ) -> LightsailCloseInstancePublicPortsResponse:
        client = self._require_client()
        return await self._execute(client.close_instance_public_ports, request, LightsailCloseInstancePublicPortsResponse)

    async def copy_snapshot(
        self,
        request: LightsailCopySnapshotRequest,
    ) -> LightsailCopySnapshotResponse:
        client = self._require_client()
        return await self._execute(client.copy_snapshot, request, LightsailCopySnapshotResponse)

    async def create_bucket(
        self,
        request: LightsailCreateBucketRequest,
    ) -> LightsailCreateBucketResponse:
        client = self._require_client()
        return await self._execute(client.create_bucket, request, LightsailCreateBucketResponse)

    async def create_bucket_access_key(
        self,
        request: LightsailCreateBucketAccessKeyRequest,
    ) -> LightsailCreateBucketAccessKeyResponse:
        client = self._require_client()
        return await self._execute(client.create_bucket_access_key, request, LightsailCreateBucketAccessKeyResponse)

    async def create_certificate(
        self,
        request: LightsailCreateCertificateRequest,
    ) -> LightsailCreateCertificateResponse:
        client = self._require_client()
        return await self._execute(client.create_certificate, request, LightsailCreateCertificateResponse)

    async def create_cloud_formation_stack(
        self,
        request: LightsailCreateCloudFormationStackRequest,
    ) -> LightsailCreateCloudFormationStackResponse:
        client = self._require_client()
        return await self._execute(client.create_cloud_formation_stack, request, LightsailCreateCloudFormationStackResponse)

    async def create_contact_method(
        self,
        request: LightsailCreateContactMethodRequest,
    ) -> LightsailCreateContactMethodResponse:
        client = self._require_client()
        return await self._execute(client.create_contact_method, request, LightsailCreateContactMethodResponse)

    async def create_container_service(
        self,
        request: LightsailCreateContainerServiceRequest,
    ) -> LightsailCreateContainerServiceResponse:
        client = self._require_client()
        return await self._execute(client.create_container_service, request, LightsailCreateContainerServiceResponse)

    async def create_container_service_deployment(
        self,
        request: LightsailCreateContainerServiceDeploymentRequest,
    ) -> LightsailCreateContainerServiceDeploymentResponse:
        client = self._require_client()
        return await self._execute(client.create_container_service_deployment, request, LightsailCreateContainerServiceDeploymentResponse)

    async def create_container_service_registry_login(
        self,
        request: LightsailCreateContainerServiceRegistryLoginRequest | None = None,
    ) -> LightsailCreateContainerServiceRegistryLoginResponse:
        client = self._require_client()
        return await self._execute(client.create_container_service_registry_login, request, LightsailCreateContainerServiceRegistryLoginResponse)

    async def create_disk(
        self,
        request: LightsailCreateDiskRequest,
    ) -> LightsailCreateDiskResponse:
        client = self._require_client()
        return await self._execute(client.create_disk, request, LightsailCreateDiskResponse)

    async def create_disk_from_snapshot(
        self,
        request: LightsailCreateDiskFromSnapshotRequest,
    ) -> LightsailCreateDiskFromSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.create_disk_from_snapshot, request, LightsailCreateDiskFromSnapshotResponse)

    async def create_disk_snapshot(
        self,
        request: LightsailCreateDiskSnapshotRequest,
    ) -> LightsailCreateDiskSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.create_disk_snapshot, request, LightsailCreateDiskSnapshotResponse)

    async def create_distribution(
        self,
        request: LightsailCreateDistributionRequest,
    ) -> LightsailCreateDistributionResponse:
        client = self._require_client()
        return await self._execute(client.create_distribution, request, LightsailCreateDistributionResponse)

    async def create_domain(
        self,
        request: LightsailCreateDomainRequest,
    ) -> LightsailCreateDomainResponse:
        client = self._require_client()
        return await self._execute(client.create_domain, request, LightsailCreateDomainResponse)

    async def create_domain_entry(
        self,
        request: LightsailCreateDomainEntryRequest,
    ) -> LightsailCreateDomainEntryResponse:
        client = self._require_client()
        return await self._execute(client.create_domain_entry, request, LightsailCreateDomainEntryResponse)

    async def create_gui_session_access_details(
        self,
        request: LightsailCreateGUISessionAccessDetailsRequest,
    ) -> LightsailCreateGUISessionAccessDetailsResponse:
        client = self._require_client()
        return await self._execute(client.create_gui_session_access_details, request, LightsailCreateGUISessionAccessDetailsResponse)

    async def create_instance_snapshot(
        self,
        request: LightsailCreateInstanceSnapshotRequest,
    ) -> LightsailCreateInstanceSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.create_instance_snapshot, request, LightsailCreateInstanceSnapshotResponse)

    async def create_instances(
        self,
        request: LightsailCreateInstancesRequest,
    ) -> LightsailCreateInstancesResponse:
        client = self._require_client()
        return await self._execute(client.create_instances, request, LightsailCreateInstancesResponse)

    async def create_instances_from_snapshot(
        self,
        request: LightsailCreateInstancesFromSnapshotRequest,
    ) -> LightsailCreateInstancesFromSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.create_instances_from_snapshot, request, LightsailCreateInstancesFromSnapshotResponse)

    async def create_key_pair(
        self,
        request: LightsailCreateKeyPairRequest,
    ) -> LightsailCreateKeyPairResponse:
        client = self._require_client()
        return await self._execute(client.create_key_pair, request, LightsailCreateKeyPairResponse)

    async def create_load_balancer(
        self,
        request: LightsailCreateLoadBalancerRequest,
    ) -> LightsailCreateLoadBalancerResponse:
        client = self._require_client()
        return await self._execute(client.create_load_balancer, request, LightsailCreateLoadBalancerResponse)

    async def create_load_balancer_tls_certificate(
        self,
        request: LightsailCreateLoadBalancerTlsCertificateRequest,
    ) -> LightsailCreateLoadBalancerTlsCertificateResponse:
        client = self._require_client()
        return await self._execute(client.create_load_balancer_tls_certificate, request, LightsailCreateLoadBalancerTlsCertificateResponse)

    async def create_relational_database(
        self,
        request: LightsailCreateRelationalDatabaseRequest,
    ) -> LightsailCreateRelationalDatabaseResponse:
        client = self._require_client()
        return await self._execute(client.create_relational_database, request, LightsailCreateRelationalDatabaseResponse)

    async def create_relational_database_from_snapshot(
        self,
        request: LightsailCreateRelationalDatabaseFromSnapshotRequest,
    ) -> LightsailCreateRelationalDatabaseFromSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.create_relational_database_from_snapshot, request, LightsailCreateRelationalDatabaseFromSnapshotResponse)

    async def create_relational_database_snapshot(
        self,
        request: LightsailCreateRelationalDatabaseSnapshotRequest,
    ) -> LightsailCreateRelationalDatabaseSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.create_relational_database_snapshot, request, LightsailCreateRelationalDatabaseSnapshotResponse)

    async def create_subdomain(
        self,
        request: LightsailCreateSubdomainRequest,
    ) -> LightsailCreateSubdomainResponse:
        client = self._require_client()
        return await self._execute(client.create_subdomain, request, LightsailCreateSubdomainResponse)

    async def delete_alarm(
        self,
        request: LightsailDeleteAlarmRequest,
    ) -> LightsailDeleteAlarmResponse:
        client = self._require_client()
        return await self._execute(client.delete_alarm, request, LightsailDeleteAlarmResponse)

    async def delete_auto_snapshot(
        self,
        request: LightsailDeleteAutoSnapshotRequest,
    ) -> LightsailDeleteAutoSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.delete_auto_snapshot, request, LightsailDeleteAutoSnapshotResponse)

    async def delete_bucket(
        self,
        request: LightsailDeleteBucketRequest,
    ) -> LightsailDeleteBucketResponse:
        client = self._require_client()
        return await self._execute(client.delete_bucket, request, LightsailDeleteBucketResponse)

    async def delete_bucket_access_key(
        self,
        request: LightsailDeleteBucketAccessKeyRequest,
    ) -> LightsailDeleteBucketAccessKeyResponse:
        client = self._require_client()
        return await self._execute(client.delete_bucket_access_key, request, LightsailDeleteBucketAccessKeyResponse)

    async def delete_certificate(
        self,
        request: LightsailDeleteCertificateRequest,
    ) -> LightsailDeleteCertificateResponse:
        client = self._require_client()
        return await self._execute(client.delete_certificate, request, LightsailDeleteCertificateResponse)

    async def delete_contact_method(
        self,
        request: LightsailDeleteContactMethodRequest,
    ) -> LightsailDeleteContactMethodResponse:
        client = self._require_client()
        return await self._execute(client.delete_contact_method, request, LightsailDeleteContactMethodResponse)

    async def delete_container_image(
        self,
        request: LightsailDeleteContainerImageRequest,
    ) -> LightsailDeleteContainerImageResponse:
        client = self._require_client()
        return await self._execute(client.delete_container_image, request, LightsailDeleteContainerImageResponse)

    async def delete_container_service(
        self,
        request: LightsailDeleteContainerServiceRequest,
    ) -> LightsailDeleteContainerServiceResponse:
        client = self._require_client()
        return await self._execute(client.delete_container_service, request, LightsailDeleteContainerServiceResponse)

    async def delete_disk(
        self,
        request: LightsailDeleteDiskRequest,
    ) -> LightsailDeleteDiskResponse:
        client = self._require_client()
        return await self._execute(client.delete_disk, request, LightsailDeleteDiskResponse)

    async def delete_disk_snapshot(
        self,
        request: LightsailDeleteDiskSnapshotRequest,
    ) -> LightsailDeleteDiskSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.delete_disk_snapshot, request, LightsailDeleteDiskSnapshotResponse)

    async def delete_distribution(
        self,
        request: LightsailDeleteDistributionRequest | None = None,
    ) -> LightsailDeleteDistributionResponse:
        client = self._require_client()
        return await self._execute(client.delete_distribution, request, LightsailDeleteDistributionResponse)

    async def delete_domain(
        self,
        request: LightsailDeleteDomainRequest,
    ) -> LightsailDeleteDomainResponse:
        client = self._require_client()
        return await self._execute(client.delete_domain, request, LightsailDeleteDomainResponse)

    async def delete_domain_entry(
        self,
        request: LightsailDeleteDomainEntryRequest,
    ) -> LightsailDeleteDomainEntryResponse:
        client = self._require_client()
        return await self._execute(client.delete_domain_entry, request, LightsailDeleteDomainEntryResponse)

    async def delete_instance(
        self,
        request: LightsailDeleteInstanceRequest,
    ) -> LightsailDeleteInstanceResponse:
        client = self._require_client()
        return await self._execute(client.delete_instance, request, LightsailDeleteInstanceResponse)

    async def delete_instance_snapshot(
        self,
        request: LightsailDeleteInstanceSnapshotRequest,
    ) -> LightsailDeleteInstanceSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.delete_instance_snapshot, request, LightsailDeleteInstanceSnapshotResponse)

    async def delete_key_pair(
        self,
        request: LightsailDeleteKeyPairRequest,
    ) -> LightsailDeleteKeyPairResponse:
        client = self._require_client()
        return await self._execute(client.delete_key_pair, request, LightsailDeleteKeyPairResponse)

    async def delete_known_host_keys(
        self,
        request: LightsailDeleteKnownHostKeysRequest,
    ) -> LightsailDeleteKnownHostKeysResponse:
        client = self._require_client()
        return await self._execute(client.delete_known_host_keys, request, LightsailDeleteKnownHostKeysResponse)

    async def delete_load_balancer(
        self,
        request: LightsailDeleteLoadBalancerRequest,
    ) -> LightsailDeleteLoadBalancerResponse:
        client = self._require_client()
        return await self._execute(client.delete_load_balancer, request, LightsailDeleteLoadBalancerResponse)

    async def delete_load_balancer_tls_certificate(
        self,
        request: LightsailDeleteLoadBalancerTlsCertificateRequest,
    ) -> LightsailDeleteLoadBalancerTlsCertificateResponse:
        client = self._require_client()
        return await self._execute(client.delete_load_balancer_tls_certificate, request, LightsailDeleteLoadBalancerTlsCertificateResponse)

    async def delete_relational_database(
        self,
        request: LightsailDeleteRelationalDatabaseRequest,
    ) -> LightsailDeleteRelationalDatabaseResponse:
        client = self._require_client()
        return await self._execute(client.delete_relational_database, request, LightsailDeleteRelationalDatabaseResponse)

    async def delete_relational_database_snapshot(
        self,
        request: LightsailDeleteRelationalDatabaseSnapshotRequest,
    ) -> LightsailDeleteRelationalDatabaseSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.delete_relational_database_snapshot, request, LightsailDeleteRelationalDatabaseSnapshotResponse)

    async def delete_subdomain(
        self,
        request: LightsailDeleteSubdomainRequest,
    ) -> LightsailDeleteSubdomainResponse:
        client = self._require_client()
        return await self._execute(client.delete_subdomain, request, LightsailDeleteSubdomainResponse)

    async def detach_certificate_from_distribution(
        self,
        request: LightsailDetachCertificateFromDistributionRequest,
    ) -> LightsailDetachCertificateFromDistributionResponse:
        client = self._require_client()
        return await self._execute(client.detach_certificate_from_distribution, request, LightsailDetachCertificateFromDistributionResponse)

    async def detach_disk(
        self,
        request: LightsailDetachDiskRequest,
    ) -> LightsailDetachDiskResponse:
        client = self._require_client()
        return await self._execute(client.detach_disk, request, LightsailDetachDiskResponse)

    async def detach_instances_from_load_balancer(
        self,
        request: LightsailDetachInstancesFromLoadBalancerRequest,
    ) -> LightsailDetachInstancesFromLoadBalancerResponse:
        client = self._require_client()
        return await self._execute(client.detach_instances_from_load_balancer, request, LightsailDetachInstancesFromLoadBalancerResponse)

    async def detach_static_ip(
        self,
        request: LightsailDetachStaticIpRequest,
    ) -> LightsailDetachStaticIpResponse:
        client = self._require_client()
        return await self._execute(client.detach_static_ip, request, LightsailDetachStaticIpResponse)

    async def disable_add_on(
        self,
        request: LightsailDisableAddOnRequest,
    ) -> LightsailDisableAddOnResponse:
        client = self._require_client()
        return await self._execute(client.disable_add_on, request, LightsailDisableAddOnResponse)

    async def download_default_key_pair(
        self,
        request: LightsailDownloadDefaultKeyPairRequest | None = None,
    ) -> LightsailDownloadDefaultKeyPairResponse:
        client = self._require_client()
        return await self._execute(client.download_default_key_pair, request, LightsailDownloadDefaultKeyPairResponse)

    async def enable_add_on(
        self,
        request: LightsailEnableAddOnRequest,
    ) -> LightsailEnableAddOnResponse:
        client = self._require_client()
        return await self._execute(client.enable_add_on, request, LightsailEnableAddOnResponse)

    async def export_snapshot(
        self,
        request: LightsailExportSnapshotRequest,
    ) -> LightsailExportSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.export_snapshot, request, LightsailExportSnapshotResponse)

    async def get_active_names(
        self,
        request: LightsailGetActiveNamesRequest | None = None,
    ) -> LightsailGetActiveNamesResponse:
        client = self._require_client()
        return await self._execute(client.get_active_names, request, LightsailGetActiveNamesResponse)

    async def get_active_names_paginated(
        self,
        request: LightsailGetActiveNamesRequest | None = None,
    ) -> list[LightsailGetActiveNamesResponse]:
        return await self._paginate('get_active_names', request, LightsailGetActiveNamesResponse)

    async def get_alarms(
        self,
        request: LightsailGetAlarmsRequest | None = None,
    ) -> LightsailGetAlarmsResponse:
        client = self._require_client()
        return await self._execute(client.get_alarms, request, LightsailGetAlarmsResponse)

    async def get_auto_snapshots(
        self,
        request: LightsailGetAutoSnapshotsRequest,
    ) -> LightsailGetAutoSnapshotsResponse:
        client = self._require_client()
        return await self._execute(client.get_auto_snapshots, request, LightsailGetAutoSnapshotsResponse)

    async def get_blueprints(
        self,
        request: LightsailGetBlueprintsRequest | None = None,
    ) -> LightsailGetBlueprintsResponse:
        client = self._require_client()
        return await self._execute(client.get_blueprints, request, LightsailGetBlueprintsResponse)

    async def get_blueprints_paginated(
        self,
        request: LightsailGetBlueprintsRequest | None = None,
    ) -> list[LightsailGetBlueprintsResponse]:
        return await self._paginate('get_blueprints', request, LightsailGetBlueprintsResponse)

    async def get_bucket_access_keys(
        self,
        request: LightsailGetBucketAccessKeysRequest,
    ) -> LightsailGetBucketAccessKeysResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_access_keys, request, LightsailGetBucketAccessKeysResponse)

    async def get_bucket_bundles(
        self,
        request: LightsailGetBucketBundlesRequest | None = None,
    ) -> LightsailGetBucketBundlesResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_bundles, request, LightsailGetBucketBundlesResponse)

    async def get_bucket_metric_data(
        self,
        request: LightsailGetBucketMetricDataRequest,
    ) -> LightsailGetBucketMetricDataResponse:
        client = self._require_client()
        return await self._execute(client.get_bucket_metric_data, request, LightsailGetBucketMetricDataResponse)

    async def get_buckets(
        self,
        request: LightsailGetBucketsRequest | None = None,
    ) -> LightsailGetBucketsResponse:
        client = self._require_client()
        return await self._execute(client.get_buckets, request, LightsailGetBucketsResponse)

    async def get_bundles(
        self,
        request: LightsailGetBundlesRequest | None = None,
    ) -> LightsailGetBundlesResponse:
        client = self._require_client()
        return await self._execute(client.get_bundles, request, LightsailGetBundlesResponse)

    async def get_bundles_paginated(
        self,
        request: LightsailGetBundlesRequest | None = None,
    ) -> list[LightsailGetBundlesResponse]:
        return await self._paginate('get_bundles', request, LightsailGetBundlesResponse)

    async def get_certificates(
        self,
        request: LightsailGetCertificatesRequest | None = None,
    ) -> LightsailGetCertificatesResponse:
        client = self._require_client()
        return await self._execute(client.get_certificates, request, LightsailGetCertificatesResponse)

    async def get_cloud_formation_stack_records(
        self,
        request: LightsailGetCloudFormationStackRecordsRequest | None = None,
    ) -> LightsailGetCloudFormationStackRecordsResponse:
        client = self._require_client()
        return await self._execute(client.get_cloud_formation_stack_records, request, LightsailGetCloudFormationStackRecordsResponse)

    async def get_cloud_formation_stack_records_paginated(
        self,
        request: LightsailGetCloudFormationStackRecordsRequest | None = None,
    ) -> list[LightsailGetCloudFormationStackRecordsResponse]:
        return await self._paginate('get_cloud_formation_stack_records', request, LightsailGetCloudFormationStackRecordsResponse)

    async def get_contact_methods(
        self,
        request: LightsailGetContactMethodsRequest | None = None,
    ) -> LightsailGetContactMethodsResponse:
        client = self._require_client()
        return await self._execute(client.get_contact_methods, request, LightsailGetContactMethodsResponse)

    async def get_container_api_metadata(
        self,
        request: LightsailGetContainerAPIMetadataRequest | None = None,
    ) -> LightsailGetContainerAPIMetadataResponse:
        client = self._require_client()
        return await self._execute(client.get_container_api_metadata, request, LightsailGetContainerAPIMetadataResponse)

    async def get_container_images(
        self,
        request: LightsailGetContainerImagesRequest,
    ) -> LightsailGetContainerImagesResponse:
        client = self._require_client()
        return await self._execute(client.get_container_images, request, LightsailGetContainerImagesResponse)

    async def get_container_log(
        self,
        request: LightsailGetContainerLogRequest,
    ) -> LightsailGetContainerLogResponse:
        client = self._require_client()
        return await self._execute(client.get_container_log, request, LightsailGetContainerLogResponse)

    async def get_container_service_deployments(
        self,
        request: LightsailGetContainerServiceDeploymentsRequest,
    ) -> LightsailGetContainerServiceDeploymentsResponse:
        client = self._require_client()
        return await self._execute(client.get_container_service_deployments, request, LightsailGetContainerServiceDeploymentsResponse)

    async def get_container_service_metric_data(
        self,
        request: LightsailGetContainerServiceMetricDataRequest,
    ) -> LightsailGetContainerServiceMetricDataResponse:
        client = self._require_client()
        return await self._execute(client.get_container_service_metric_data, request, LightsailGetContainerServiceMetricDataResponse)

    async def get_container_service_powers(
        self,
        request: LightsailGetContainerServicePowersRequest | None = None,
    ) -> LightsailGetContainerServicePowersResponse:
        client = self._require_client()
        return await self._execute(client.get_container_service_powers, request, LightsailGetContainerServicePowersResponse)

    async def get_container_services(
        self,
        request: LightsailGetContainerServicesRequest | None = None,
    ) -> LightsailGetContainerServicesResponse:
        client = self._require_client()
        return await self._execute(client.get_container_services, request, LightsailGetContainerServicesResponse)

    async def get_cost_estimate(
        self,
        request: LightsailGetCostEstimateRequest,
    ) -> LightsailGetCostEstimateResponse:
        client = self._require_client()
        return await self._execute(client.get_cost_estimate, request, LightsailGetCostEstimateResponse)

    async def get_disk(
        self,
        request: LightsailGetDiskRequest,
    ) -> LightsailGetDiskResponse:
        client = self._require_client()
        return await self._execute(client.get_disk, request, LightsailGetDiskResponse)

    async def get_disk_snapshot(
        self,
        request: LightsailGetDiskSnapshotRequest,
    ) -> LightsailGetDiskSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.get_disk_snapshot, request, LightsailGetDiskSnapshotResponse)

    async def get_disk_snapshots(
        self,
        request: LightsailGetDiskSnapshotsRequest | None = None,
    ) -> LightsailGetDiskSnapshotsResponse:
        client = self._require_client()
        return await self._execute(client.get_disk_snapshots, request, LightsailGetDiskSnapshotsResponse)

    async def get_disk_snapshots_paginated(
        self,
        request: LightsailGetDiskSnapshotsRequest | None = None,
    ) -> list[LightsailGetDiskSnapshotsResponse]:
        return await self._paginate('get_disk_snapshots', request, LightsailGetDiskSnapshotsResponse)

    async def get_disks(
        self,
        request: LightsailGetDisksRequest | None = None,
    ) -> LightsailGetDisksResponse:
        client = self._require_client()
        return await self._execute(client.get_disks, request, LightsailGetDisksResponse)

    async def get_disks_paginated(
        self,
        request: LightsailGetDisksRequest | None = None,
    ) -> list[LightsailGetDisksResponse]:
        return await self._paginate('get_disks', request, LightsailGetDisksResponse)

    async def get_distribution_bundles(
        self,
        request: LightsailGetDistributionBundlesRequest | None = None,
    ) -> LightsailGetDistributionBundlesResponse:
        client = self._require_client()
        return await self._execute(client.get_distribution_bundles, request, LightsailGetDistributionBundlesResponse)

    async def get_distribution_latest_cache_reset(
        self,
        request: LightsailGetDistributionLatestCacheResetRequest | None = None,
    ) -> LightsailGetDistributionLatestCacheResetResponse:
        client = self._require_client()
        return await self._execute(client.get_distribution_latest_cache_reset, request, LightsailGetDistributionLatestCacheResetResponse)

    async def get_distribution_metric_data(
        self,
        request: LightsailGetDistributionMetricDataRequest,
    ) -> LightsailGetDistributionMetricDataResponse:
        client = self._require_client()
        return await self._execute(client.get_distribution_metric_data, request, LightsailGetDistributionMetricDataResponse)

    async def get_distributions(
        self,
        request: LightsailGetDistributionsRequest | None = None,
    ) -> LightsailGetDistributionsResponse:
        client = self._require_client()
        return await self._execute(client.get_distributions, request, LightsailGetDistributionsResponse)

    async def get_domain(
        self,
        request: LightsailGetDomainRequest,
    ) -> LightsailGetDomainResponse:
        client = self._require_client()
        return await self._execute(client.get_domain, request, LightsailGetDomainResponse)

    async def get_domains(
        self,
        request: LightsailGetDomainsRequest | None = None,
    ) -> LightsailGetDomainsResponse:
        client = self._require_client()
        return await self._execute(client.get_domains, request, LightsailGetDomainsResponse)

    async def get_domains_paginated(
        self,
        request: LightsailGetDomainsRequest | None = None,
    ) -> list[LightsailGetDomainsResponse]:
        return await self._paginate('get_domains', request, LightsailGetDomainsResponse)

    async def get_export_snapshot_records(
        self,
        request: LightsailGetExportSnapshotRecordsRequest | None = None,
    ) -> LightsailGetExportSnapshotRecordsResponse:
        client = self._require_client()
        return await self._execute(client.get_export_snapshot_records, request, LightsailGetExportSnapshotRecordsResponse)

    async def get_export_snapshot_records_paginated(
        self,
        request: LightsailGetExportSnapshotRecordsRequest | None = None,
    ) -> list[LightsailGetExportSnapshotRecordsResponse]:
        return await self._paginate('get_export_snapshot_records', request, LightsailGetExportSnapshotRecordsResponse)

    async def get_instance(
        self,
        request: LightsailGetInstanceRequest,
    ) -> LightsailGetInstanceResponse:
        client = self._require_client()
        return await self._execute(client.get_instance, request, LightsailGetInstanceResponse)

    async def get_instance_access_details(
        self,
        request: LightsailGetInstanceAccessDetailsRequest,
    ) -> LightsailGetInstanceAccessDetailsResponse:
        client = self._require_client()
        return await self._execute(client.get_instance_access_details, request, LightsailGetInstanceAccessDetailsResponse)

    async def get_instance_metric_data(
        self,
        request: LightsailGetInstanceMetricDataRequest,
    ) -> LightsailGetInstanceMetricDataResponse:
        client = self._require_client()
        return await self._execute(client.get_instance_metric_data, request, LightsailGetInstanceMetricDataResponse)

    async def get_instance_port_states(
        self,
        request: LightsailGetInstancePortStatesRequest,
    ) -> LightsailGetInstancePortStatesResponse:
        client = self._require_client()
        return await self._execute(client.get_instance_port_states, request, LightsailGetInstancePortStatesResponse)

    async def get_instance_snapshot(
        self,
        request: LightsailGetInstanceSnapshotRequest,
    ) -> LightsailGetInstanceSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.get_instance_snapshot, request, LightsailGetInstanceSnapshotResponse)

    async def get_instance_snapshots(
        self,
        request: LightsailGetInstanceSnapshotsRequest | None = None,
    ) -> LightsailGetInstanceSnapshotsResponse:
        client = self._require_client()
        return await self._execute(client.get_instance_snapshots, request, LightsailGetInstanceSnapshotsResponse)

    async def get_instance_snapshots_paginated(
        self,
        request: LightsailGetInstanceSnapshotsRequest | None = None,
    ) -> list[LightsailGetInstanceSnapshotsResponse]:
        return await self._paginate('get_instance_snapshots', request, LightsailGetInstanceSnapshotsResponse)

    async def get_instance_state(
        self,
        request: LightsailGetInstanceStateRequest,
    ) -> LightsailGetInstanceStateResponse:
        client = self._require_client()
        return await self._execute(client.get_instance_state, request, LightsailGetInstanceStateResponse)

    async def get_instances(
        self,
        request: LightsailGetInstancesRequest | None = None,
    ) -> LightsailGetInstancesResponse:
        client = self._require_client()
        return await self._execute(client.get_instances, request, LightsailGetInstancesResponse)

    async def get_instances_paginated(
        self,
        request: LightsailGetInstancesRequest | None = None,
    ) -> list[LightsailGetInstancesResponse]:
        return await self._paginate('get_instances', request, LightsailGetInstancesResponse)

    async def get_key_pair(
        self,
        request: LightsailGetKeyPairRequest,
    ) -> LightsailGetKeyPairResponse:
        client = self._require_client()
        return await self._execute(client.get_key_pair, request, LightsailGetKeyPairResponse)

    async def get_key_pairs(
        self,
        request: LightsailGetKeyPairsRequest | None = None,
    ) -> LightsailGetKeyPairsResponse:
        client = self._require_client()
        return await self._execute(client.get_key_pairs, request, LightsailGetKeyPairsResponse)

    async def get_key_pairs_paginated(
        self,
        request: LightsailGetKeyPairsRequest | None = None,
    ) -> list[LightsailGetKeyPairsResponse]:
        return await self._paginate('get_key_pairs', request, LightsailGetKeyPairsResponse)

    async def get_load_balancer(
        self,
        request: LightsailGetLoadBalancerRequest,
    ) -> LightsailGetLoadBalancerResponse:
        client = self._require_client()
        return await self._execute(client.get_load_balancer, request, LightsailGetLoadBalancerResponse)

    async def get_load_balancer_metric_data(
        self,
        request: LightsailGetLoadBalancerMetricDataRequest,
    ) -> LightsailGetLoadBalancerMetricDataResponse:
        client = self._require_client()
        return await self._execute(client.get_load_balancer_metric_data, request, LightsailGetLoadBalancerMetricDataResponse)

    async def get_load_balancer_tls_certificates(
        self,
        request: LightsailGetLoadBalancerTlsCertificatesRequest,
    ) -> LightsailGetLoadBalancerTlsCertificatesResponse:
        client = self._require_client()
        return await self._execute(client.get_load_balancer_tls_certificates, request, LightsailGetLoadBalancerTlsCertificatesResponse)

    async def get_load_balancer_tls_policies(
        self,
        request: LightsailGetLoadBalancerTlsPoliciesRequest | None = None,
    ) -> LightsailGetLoadBalancerTlsPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.get_load_balancer_tls_policies, request, LightsailGetLoadBalancerTlsPoliciesResponse)

    async def get_load_balancers(
        self,
        request: LightsailGetLoadBalancersRequest | None = None,
    ) -> LightsailGetLoadBalancersResponse:
        client = self._require_client()
        return await self._execute(client.get_load_balancers, request, LightsailGetLoadBalancersResponse)

    async def get_load_balancers_paginated(
        self,
        request: LightsailGetLoadBalancersRequest | None = None,
    ) -> list[LightsailGetLoadBalancersResponse]:
        return await self._paginate('get_load_balancers', request, LightsailGetLoadBalancersResponse)

    async def get_operation(
        self,
        request: LightsailGetOperationRequest,
    ) -> LightsailGetOperationResponse:
        client = self._require_client()
        return await self._execute(client.get_operation, request, LightsailGetOperationResponse)

    async def get_operations(
        self,
        request: LightsailGetOperationsRequest | None = None,
    ) -> LightsailGetOperationsResponse:
        client = self._require_client()
        return await self._execute(client.get_operations, request, LightsailGetOperationsResponse)

    async def get_operations_paginated(
        self,
        request: LightsailGetOperationsRequest | None = None,
    ) -> list[LightsailGetOperationsResponse]:
        return await self._paginate('get_operations', request, LightsailGetOperationsResponse)

    async def get_operations_for_resource(
        self,
        request: LightsailGetOperationsForResourceRequest,
    ) -> LightsailGetOperationsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.get_operations_for_resource, request, LightsailGetOperationsForResourceResponse)

    async def get_profile(
        self,
        request: LightsailGetProfileRequest | None = None,
    ) -> LightsailGetProfileResponse:
        client = self._require_client()
        return await self._execute(client.get_profile, request, LightsailGetProfileResponse)

    async def get_regions(
        self,
        request: LightsailGetRegionsRequest | None = None,
    ) -> LightsailGetRegionsResponse:
        client = self._require_client()
        return await self._execute(client.get_regions, request, LightsailGetRegionsResponse)

    async def get_relational_database(
        self,
        request: LightsailGetRelationalDatabaseRequest,
    ) -> LightsailGetRelationalDatabaseResponse:
        client = self._require_client()
        return await self._execute(client.get_relational_database, request, LightsailGetRelationalDatabaseResponse)

    async def get_relational_database_blueprints(
        self,
        request: LightsailGetRelationalDatabaseBlueprintsRequest | None = None,
    ) -> LightsailGetRelationalDatabaseBlueprintsResponse:
        client = self._require_client()
        return await self._execute(client.get_relational_database_blueprints, request, LightsailGetRelationalDatabaseBlueprintsResponse)

    async def get_relational_database_blueprints_paginated(
        self,
        request: LightsailGetRelationalDatabaseBlueprintsRequest | None = None,
    ) -> list[LightsailGetRelationalDatabaseBlueprintsResponse]:
        return await self._paginate('get_relational_database_blueprints', request, LightsailGetRelationalDatabaseBlueprintsResponse)

    async def get_relational_database_bundles(
        self,
        request: LightsailGetRelationalDatabaseBundlesRequest | None = None,
    ) -> LightsailGetRelationalDatabaseBundlesResponse:
        client = self._require_client()
        return await self._execute(client.get_relational_database_bundles, request, LightsailGetRelationalDatabaseBundlesResponse)

    async def get_relational_database_bundles_paginated(
        self,
        request: LightsailGetRelationalDatabaseBundlesRequest | None = None,
    ) -> list[LightsailGetRelationalDatabaseBundlesResponse]:
        return await self._paginate('get_relational_database_bundles', request, LightsailGetRelationalDatabaseBundlesResponse)

    async def get_relational_database_events(
        self,
        request: LightsailGetRelationalDatabaseEventsRequest,
    ) -> LightsailGetRelationalDatabaseEventsResponse:
        client = self._require_client()
        return await self._execute(client.get_relational_database_events, request, LightsailGetRelationalDatabaseEventsResponse)

    async def get_relational_database_events_paginated(
        self,
        request: LightsailGetRelationalDatabaseEventsRequest,
    ) -> list[LightsailGetRelationalDatabaseEventsResponse]:
        return await self._paginate('get_relational_database_events', request, LightsailGetRelationalDatabaseEventsResponse)

    async def get_relational_database_log_events(
        self,
        request: LightsailGetRelationalDatabaseLogEventsRequest,
    ) -> LightsailGetRelationalDatabaseLogEventsResponse:
        client = self._require_client()
        return await self._execute(client.get_relational_database_log_events, request, LightsailGetRelationalDatabaseLogEventsResponse)

    async def get_relational_database_log_streams(
        self,
        request: LightsailGetRelationalDatabaseLogStreamsRequest,
    ) -> LightsailGetRelationalDatabaseLogStreamsResponse:
        client = self._require_client()
        return await self._execute(client.get_relational_database_log_streams, request, LightsailGetRelationalDatabaseLogStreamsResponse)

    async def get_relational_database_master_user_password(
        self,
        request: LightsailGetRelationalDatabaseMasterUserPasswordRequest,
    ) -> LightsailGetRelationalDatabaseMasterUserPasswordResponse:
        client = self._require_client()
        return await self._execute(client.get_relational_database_master_user_password, request, LightsailGetRelationalDatabaseMasterUserPasswordResponse)

    async def get_relational_database_metric_data(
        self,
        request: LightsailGetRelationalDatabaseMetricDataRequest,
    ) -> LightsailGetRelationalDatabaseMetricDataResponse:
        client = self._require_client()
        return await self._execute(client.get_relational_database_metric_data, request, LightsailGetRelationalDatabaseMetricDataResponse)

    async def get_relational_database_parameters(
        self,
        request: LightsailGetRelationalDatabaseParametersRequest,
    ) -> LightsailGetRelationalDatabaseParametersResponse:
        client = self._require_client()
        return await self._execute(client.get_relational_database_parameters, request, LightsailGetRelationalDatabaseParametersResponse)

    async def get_relational_database_parameters_paginated(
        self,
        request: LightsailGetRelationalDatabaseParametersRequest,
    ) -> list[LightsailGetRelationalDatabaseParametersResponse]:
        return await self._paginate('get_relational_database_parameters', request, LightsailGetRelationalDatabaseParametersResponse)

    async def get_relational_database_snapshot(
        self,
        request: LightsailGetRelationalDatabaseSnapshotRequest,
    ) -> LightsailGetRelationalDatabaseSnapshotResponse:
        client = self._require_client()
        return await self._execute(client.get_relational_database_snapshot, request, LightsailGetRelationalDatabaseSnapshotResponse)

    async def get_relational_database_snapshots(
        self,
        request: LightsailGetRelationalDatabaseSnapshotsRequest | None = None,
    ) -> LightsailGetRelationalDatabaseSnapshotsResponse:
        client = self._require_client()
        return await self._execute(client.get_relational_database_snapshots, request, LightsailGetRelationalDatabaseSnapshotsResponse)

    async def get_relational_database_snapshots_paginated(
        self,
        request: LightsailGetRelationalDatabaseSnapshotsRequest | None = None,
    ) -> list[LightsailGetRelationalDatabaseSnapshotsResponse]:
        return await self._paginate('get_relational_database_snapshots', request, LightsailGetRelationalDatabaseSnapshotsResponse)

    async def get_relational_databases(
        self,
        request: LightsailGetRelationalDatabasesRequest | None = None,
    ) -> LightsailGetRelationalDatabasesResponse:
        client = self._require_client()
        return await self._execute(client.get_relational_databases, request, LightsailGetRelationalDatabasesResponse)

    async def get_relational_databases_paginated(
        self,
        request: LightsailGetRelationalDatabasesRequest | None = None,
    ) -> list[LightsailGetRelationalDatabasesResponse]:
        return await self._paginate('get_relational_databases', request, LightsailGetRelationalDatabasesResponse)

    async def get_setup_history(
        self,
        request: LightsailGetSetupHistoryRequest,
    ) -> LightsailGetSetupHistoryResponse:
        client = self._require_client()
        return await self._execute(client.get_setup_history, request, LightsailGetSetupHistoryResponse)

    async def get_static_ip(
        self,
        request: LightsailGetStaticIpRequest,
    ) -> LightsailGetStaticIpResponse:
        client = self._require_client()
        return await self._execute(client.get_static_ip, request, LightsailGetStaticIpResponse)

    async def get_static_ips(
        self,
        request: LightsailGetStaticIpsRequest | None = None,
    ) -> LightsailGetStaticIpsResponse:
        client = self._require_client()
        return await self._execute(client.get_static_ips, request, LightsailGetStaticIpsResponse)

    async def get_static_ips_paginated(
        self,
        request: LightsailGetStaticIpsRequest | None = None,
    ) -> list[LightsailGetStaticIpsResponse]:
        return await self._paginate('get_static_ips', request, LightsailGetStaticIpsResponse)

    async def get_subdomains(
        self,
        request: LightsailGetSubdomainsRequest | None = None,
    ) -> LightsailGetSubdomainsResponse:
        client = self._require_client()
        return await self._execute(client.get_subdomains, request, LightsailGetSubdomainsResponse)

    async def import_key_pair(
        self,
        request: LightsailImportKeyPairRequest,
    ) -> LightsailImportKeyPairResponse:
        client = self._require_client()
        return await self._execute(client.import_key_pair, request, LightsailImportKeyPairResponse)

    async def is_vpc_peered(
        self,
        request: LightsailIsVpcPeeredRequest | None = None,
    ) -> LightsailIsVpcPeeredResponse:
        client = self._require_client()
        return await self._execute(client.is_vpc_peered, request, LightsailIsVpcPeeredResponse)

    async def open_instance_public_ports(
        self,
        request: LightsailOpenInstancePublicPortsRequest,
    ) -> LightsailOpenInstancePublicPortsResponse:
        client = self._require_client()
        return await self._execute(client.open_instance_public_ports, request, LightsailOpenInstancePublicPortsResponse)

    async def peer_vpc(
        self,
        request: LightsailPeerVpcRequest | None = None,
    ) -> LightsailPeerVpcResponse:
        client = self._require_client()
        return await self._execute(client.peer_vpc, request, LightsailPeerVpcResponse)

    async def put_alarm(
        self,
        request: LightsailPutAlarmRequest,
    ) -> LightsailPutAlarmResponse:
        client = self._require_client()
        return await self._execute(client.put_alarm, request, LightsailPutAlarmResponse)

    async def put_instance_public_ports(
        self,
        request: LightsailPutInstancePublicPortsRequest,
    ) -> LightsailPutInstancePublicPortsResponse:
        client = self._require_client()
        return await self._execute(client.put_instance_public_ports, request, LightsailPutInstancePublicPortsResponse)

    async def reboot_instance(
        self,
        request: LightsailRebootInstanceRequest,
    ) -> LightsailRebootInstanceResponse:
        client = self._require_client()
        return await self._execute(client.reboot_instance, request, LightsailRebootInstanceResponse)

    async def reboot_relational_database(
        self,
        request: LightsailRebootRelationalDatabaseRequest,
    ) -> LightsailRebootRelationalDatabaseResponse:
        client = self._require_client()
        return await self._execute(client.reboot_relational_database, request, LightsailRebootRelationalDatabaseResponse)

    async def register_container_image(
        self,
        request: LightsailRegisterContainerImageRequest,
    ) -> LightsailRegisterContainerImageResponse:
        client = self._require_client()
        return await self._execute(client.register_container_image, request, LightsailRegisterContainerImageResponse)

    async def release_static_ip(
        self,
        request: LightsailReleaseStaticIpRequest,
    ) -> LightsailReleaseStaticIpResponse:
        client = self._require_client()
        return await self._execute(client.release_static_ip, request, LightsailReleaseStaticIpResponse)

    async def reset_distribution_cache(
        self,
        request: LightsailResetDistributionCacheRequest | None = None,
    ) -> LightsailResetDistributionCacheResponse:
        client = self._require_client()
        return await self._execute(client.reset_distribution_cache, request, LightsailResetDistributionCacheResponse)

    async def send_contact_method_verification(
        self,
        request: LightsailSendContactMethodVerificationRequest,
    ) -> LightsailSendContactMethodVerificationResponse:
        client = self._require_client()
        return await self._execute(client.send_contact_method_verification, request, LightsailSendContactMethodVerificationResponse)

    async def set_ip_address_type(
        self,
        request: LightsailSetIpAddressTypeRequest,
    ) -> LightsailSetIpAddressTypeResponse:
        client = self._require_client()
        return await self._execute(client.set_ip_address_type, request, LightsailSetIpAddressTypeResponse)

    async def set_resource_access_for_bucket(
        self,
        request: LightsailSetResourceAccessForBucketRequest,
    ) -> LightsailSetResourceAccessForBucketResponse:
        client = self._require_client()
        return await self._execute(client.set_resource_access_for_bucket, request, LightsailSetResourceAccessForBucketResponse)

    async def setup_instance_https(
        self,
        request: LightsailSetupInstanceHttpsRequest,
    ) -> LightsailSetupInstanceHttpsResponse:
        client = self._require_client()
        return await self._execute(client.setup_instance_https, request, LightsailSetupInstanceHttpsResponse)

    async def start_gui_session(
        self,
        request: LightsailStartGUISessionRequest,
    ) -> LightsailStartGUISessionResponse:
        client = self._require_client()
        return await self._execute(client.start_gui_session, request, LightsailStartGUISessionResponse)

    async def start_instance(
        self,
        request: LightsailStartInstanceRequest,
    ) -> LightsailStartInstanceResponse:
        client = self._require_client()
        return await self._execute(client.start_instance, request, LightsailStartInstanceResponse)

    async def start_relational_database(
        self,
        request: LightsailStartRelationalDatabaseRequest,
    ) -> LightsailStartRelationalDatabaseResponse:
        client = self._require_client()
        return await self._execute(client.start_relational_database, request, LightsailStartRelationalDatabaseResponse)

    async def stop_gui_session(
        self,
        request: LightsailStopGUISessionRequest,
    ) -> LightsailStopGUISessionResponse:
        client = self._require_client()
        return await self._execute(client.stop_gui_session, request, LightsailStopGUISessionResponse)

    async def stop_instance(
        self,
        request: LightsailStopInstanceRequest,
    ) -> LightsailStopInstanceResponse:
        client = self._require_client()
        return await self._execute(client.stop_instance, request, LightsailStopInstanceResponse)

    async def stop_relational_database(
        self,
        request: LightsailStopRelationalDatabaseRequest,
    ) -> LightsailStopRelationalDatabaseResponse:
        client = self._require_client()
        return await self._execute(client.stop_relational_database, request, LightsailStopRelationalDatabaseResponse)

    async def tag_resource(
        self,
        request: LightsailTagResourceRequest,
    ) -> LightsailTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, LightsailTagResourceResponse)

    async def test_alarm(
        self,
        request: LightsailTestAlarmRequest,
    ) -> LightsailTestAlarmResponse:
        client = self._require_client()
        return await self._execute(client.test_alarm, request, LightsailTestAlarmResponse)

    async def unpeer_vpc(
        self,
        request: LightsailUnpeerVpcRequest | None = None,
    ) -> LightsailUnpeerVpcResponse:
        client = self._require_client()
        return await self._execute(client.unpeer_vpc, request, LightsailUnpeerVpcResponse)

    async def untag_resource(
        self,
        request: LightsailUntagResourceRequest,
    ) -> LightsailUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, LightsailUntagResourceResponse)

    async def update_bucket(
        self,
        request: LightsailUpdateBucketRequest,
    ) -> LightsailUpdateBucketResponse:
        client = self._require_client()
        return await self._execute(client.update_bucket, request, LightsailUpdateBucketResponse)

    async def update_bucket_bundle(
        self,
        request: LightsailUpdateBucketBundleRequest,
    ) -> LightsailUpdateBucketBundleResponse:
        client = self._require_client()
        return await self._execute(client.update_bucket_bundle, request, LightsailUpdateBucketBundleResponse)

    async def update_container_service(
        self,
        request: LightsailUpdateContainerServiceRequest,
    ) -> LightsailUpdateContainerServiceResponse:
        client = self._require_client()
        return await self._execute(client.update_container_service, request, LightsailUpdateContainerServiceResponse)

    async def update_distribution(
        self,
        request: LightsailUpdateDistributionRequest,
    ) -> LightsailUpdateDistributionResponse:
        client = self._require_client()
        return await self._execute(client.update_distribution, request, LightsailUpdateDistributionResponse)

    async def update_distribution_bundle(
        self,
        request: LightsailUpdateDistributionBundleRequest | None = None,
    ) -> LightsailUpdateDistributionBundleResponse:
        client = self._require_client()
        return await self._execute(client.update_distribution_bundle, request, LightsailUpdateDistributionBundleResponse)

    async def update_domain_entry(
        self,
        request: LightsailUpdateDomainEntryRequest,
    ) -> LightsailUpdateDomainEntryResponse:
        client = self._require_client()
        return await self._execute(client.update_domain_entry, request, LightsailUpdateDomainEntryResponse)

    async def update_instance_metadata_options(
        self,
        request: LightsailUpdateInstanceMetadataOptionsRequest,
    ) -> LightsailUpdateInstanceMetadataOptionsResponse:
        client = self._require_client()
        return await self._execute(client.update_instance_metadata_options, request, LightsailUpdateInstanceMetadataOptionsResponse)

    async def update_load_balancer_attribute(
        self,
        request: LightsailUpdateLoadBalancerAttributeRequest,
    ) -> LightsailUpdateLoadBalancerAttributeResponse:
        client = self._require_client()
        return await self._execute(client.update_load_balancer_attribute, request, LightsailUpdateLoadBalancerAttributeResponse)

    async def update_relational_database(
        self,
        request: LightsailUpdateRelationalDatabaseRequest,
    ) -> LightsailUpdateRelationalDatabaseResponse:
        client = self._require_client()
        return await self._execute(client.update_relational_database, request, LightsailUpdateRelationalDatabaseResponse)

    async def update_relational_database_parameters(
        self,
        request: LightsailUpdateRelationalDatabaseParametersRequest,
    ) -> LightsailUpdateRelationalDatabaseParametersResponse:
        client = self._require_client()
        return await self._execute(client.update_relational_database_parameters, request, LightsailUpdateRelationalDatabaseParametersResponse)

    async def update_subdomain_association(
        self,
        request: LightsailUpdateSubdomainAssociationRequest,
    ) -> LightsailUpdateSubdomainAssociationResponse:
        client = self._require_client()
        return await self._execute(client.update_subdomain_association, request, LightsailUpdateSubdomainAssociationResponse)
