from werkflow_aws.models.opensearch import (
    OpenSearchAcceptInboundConnectionRequest,
    OpenSearchAcceptInboundConnectionResponse,
    OpenSearchAddDataSourceRequest,
    OpenSearchAddDataSourceResponse,
    OpenSearchAddDirectQueryDataSourceRequest,
    OpenSearchAddDirectQueryDataSourceResponse,
    OpenSearchAddReplicationPeerRequest,
    OpenSearchAddReplicationPeerResponse,
    OpenSearchAddTagsRequest,
    OpenSearchAddTagsResponse,
    OpenSearchAssociatePackageRequest,
    OpenSearchAssociatePackageResponse,
    OpenSearchAssociatePackagesRequest,
    OpenSearchAssociatePackagesResponse,
    OpenSearchAttachDataSourceRequest,
    OpenSearchAttachDataSourceResponse,
    OpenSearchAuthorizeVpcEndpointAccessRequest,
    OpenSearchAuthorizeVpcEndpointAccessResponse,
    OpenSearchCancelDomainConfigChangeRequest,
    OpenSearchCancelDomainConfigChangeResponse,
    OpenSearchCancelServiceSoftwareUpdateRequest,
    OpenSearchCancelServiceSoftwareUpdateResponse,
    OpenSearchCompareDomainConfigurationRequest,
    OpenSearchCompareDomainConfigurationResponse,
    OpenSearchCreateApplicationRequest,
    OpenSearchCreateApplicationResponse,
    OpenSearchCreateDomainRequest,
    OpenSearchCreateDomainResponse,
    OpenSearchCreateIndexRequest,
    OpenSearchCreateIndexResponse,
    OpenSearchCreateOutboundConnectionRequest,
    OpenSearchCreateOutboundConnectionResponse,
    OpenSearchCreatePackageRequest,
    OpenSearchCreatePackageResponse,
    OpenSearchCreateVpcEndpointRequest,
    OpenSearchCreateVpcEndpointResponse,
    OpenSearchDeleteApplicationRequest,
    OpenSearchDeleteApplicationResponse,
    OpenSearchDeleteDataSourceRequest,
    OpenSearchDeleteDataSourceResponse,
    OpenSearchDeleteDirectQueryDataSourceRequest,
    OpenSearchDeleteDirectQueryDataSourceResponse,
    OpenSearchDeleteDomainRequest,
    OpenSearchDeleteDomainResponse,
    OpenSearchDeleteInboundConnectionRequest,
    OpenSearchDeleteInboundConnectionResponse,
    OpenSearchDeleteIndexRequest,
    OpenSearchDeleteIndexResponse,
    OpenSearchDeleteOutboundConnectionRequest,
    OpenSearchDeleteOutboundConnectionResponse,
    OpenSearchDeletePackageRequest,
    OpenSearchDeletePackageResponse,
    OpenSearchDeleteVpcEndpointRequest,
    OpenSearchDeleteVpcEndpointResponse,
    OpenSearchDeregisterCapabilityRequest,
    OpenSearchDeregisterCapabilityResponse,
    OpenSearchDescribeDataSourceAttachmentRequest,
    OpenSearchDescribeDataSourceAttachmentResponse,
    OpenSearchDescribeDomainAutoTunesRequest,
    OpenSearchDescribeDomainAutoTunesResponse,
    OpenSearchDescribeDomainChangeProgressRequest,
    OpenSearchDescribeDomainChangeProgressResponse,
    OpenSearchDescribeDomainConfigRequest,
    OpenSearchDescribeDomainConfigResponse,
    OpenSearchDescribeDomainHealthRequest,
    OpenSearchDescribeDomainHealthResponse,
    OpenSearchDescribeDomainNodesRequest,
    OpenSearchDescribeDomainNodesResponse,
    OpenSearchDescribeDomainReplicationRequest,
    OpenSearchDescribeDomainReplicationResponse,
    OpenSearchDescribeDomainRequest,
    OpenSearchDescribeDomainResponse,
    OpenSearchDescribeDomainsRequest,
    OpenSearchDescribeDomainsResponse,
    OpenSearchDescribeDryRunProgressRequest,
    OpenSearchDescribeDryRunProgressResponse,
    OpenSearchDescribeInboundConnectionsRequest,
    OpenSearchDescribeInboundConnectionsResponse,
    OpenSearchDescribeInsightDetailsRequest,
    OpenSearchDescribeInsightDetailsResponse,
    OpenSearchDescribeInstanceTypeLimitsRequest,
    OpenSearchDescribeInstanceTypeLimitsResponse,
    OpenSearchDescribeOutboundConnectionsRequest,
    OpenSearchDescribeOutboundConnectionsResponse,
    OpenSearchDescribePackagesRequest,
    OpenSearchDescribePackagesResponse,
    OpenSearchDescribeReservedInstanceOfferingsRequest,
    OpenSearchDescribeReservedInstanceOfferingsResponse,
    OpenSearchDescribeReservedInstancesRequest,
    OpenSearchDescribeReservedInstancesResponse,
    OpenSearchDescribeVpcEndpointsRequest,
    OpenSearchDescribeVpcEndpointsResponse,
    OpenSearchDetachDataSourceRequest,
    OpenSearchDetachDataSourceResponse,
    OpenSearchDissociatePackageRequest,
    OpenSearchDissociatePackageResponse,
    OpenSearchDissociatePackagesRequest,
    OpenSearchDissociatePackagesResponse,
    OpenSearchFailoverReplicationRequest,
    OpenSearchFailoverReplicationResponse,
    OpenSearchGetApplicationRequest,
    OpenSearchGetApplicationResponse,
    OpenSearchGetCapabilityRequest,
    OpenSearchGetCapabilityResponse,
    OpenSearchGetCompatibleVersionsRequest,
    OpenSearchGetCompatibleVersionsResponse,
    OpenSearchGetDataSourceRequest,
    OpenSearchGetDataSourceResponse,
    OpenSearchGetDefaultApplicationSettingRequest,
    OpenSearchGetDefaultApplicationSettingResponse,
    OpenSearchGetDirectQueryDataSourceRequest,
    OpenSearchGetDirectQueryDataSourceResponse,
    OpenSearchGetDomainMaintenanceStatusRequest,
    OpenSearchGetDomainMaintenanceStatusResponse,
    OpenSearchGetIndexRequest,
    OpenSearchGetIndexResponse,
    OpenSearchGetMigrationRequest,
    OpenSearchGetMigrationResponse,
    OpenSearchGetPackageVersionHistoryRequest,
    OpenSearchGetPackageVersionHistoryResponse,
    OpenSearchGetUpgradeHistoryRequest,
    OpenSearchGetUpgradeHistoryResponse,
    OpenSearchGetUpgradeStatusRequest,
    OpenSearchGetUpgradeStatusResponse,
    OpenSearchInsightFeedbackRequest,
    OpenSearchInsightFeedbackResponse,
    OpenSearchListApplicationsRequest,
    OpenSearchListApplicationsResponse,
    OpenSearchListDataSourceAttachmentsRequest,
    OpenSearchListDataSourceAttachmentsResponse,
    OpenSearchListDataSourcesRequest,
    OpenSearchListDataSourcesResponse,
    OpenSearchListDirectQueryDataSourcesRequest,
    OpenSearchListDirectQueryDataSourcesResponse,
    OpenSearchListDomainMaintenancesRequest,
    OpenSearchListDomainMaintenancesResponse,
    OpenSearchListDomainNamesRequest,
    OpenSearchListDomainNamesResponse,
    OpenSearchListDomainsForPackageRequest,
    OpenSearchListDomainsForPackageResponse,
    OpenSearchListInsightsRequest,
    OpenSearchListInsightsResponse,
    OpenSearchListInstanceTypeDetailsRequest,
    OpenSearchListInstanceTypeDetailsResponse,
    OpenSearchListMigrationsRequest,
    OpenSearchListMigrationsResponse,
    OpenSearchListPackagesForDomainRequest,
    OpenSearchListPackagesForDomainResponse,
    OpenSearchListScheduledActionsRequest,
    OpenSearchListScheduledActionsResponse,
    OpenSearchListTagsRequest,
    OpenSearchListTagsResponse,
    OpenSearchListVersionsRequest,
    OpenSearchListVersionsResponse,
    OpenSearchListVpcEndpointAccessRequest,
    OpenSearchListVpcEndpointAccessResponse,
    OpenSearchListVpcEndpointsForDomainRequest,
    OpenSearchListVpcEndpointsForDomainResponse,
    OpenSearchListVpcEndpointsRequest,
    OpenSearchListVpcEndpointsResponse,
    OpenSearchPurchaseReservedInstanceOfferingRequest,
    OpenSearchPurchaseReservedInstanceOfferingResponse,
    OpenSearchPutDefaultApplicationSettingRequest,
    OpenSearchPutDefaultApplicationSettingResponse,
    OpenSearchRegisterCapabilityRequest,
    OpenSearchRegisterCapabilityResponse,
    OpenSearchRejectInboundConnectionRequest,
    OpenSearchRejectInboundConnectionResponse,
    OpenSearchRemoveReplicationPeerRequest,
    OpenSearchRemoveReplicationPeerResponse,
    OpenSearchRemoveTagsRequest,
    OpenSearchRemoveTagsResponse,
    OpenSearchRevokeVpcEndpointAccessRequest,
    OpenSearchRevokeVpcEndpointAccessResponse,
    OpenSearchRollbackServiceSoftwareUpdateRequest,
    OpenSearchRollbackServiceSoftwareUpdateResponse,
    OpenSearchStartDomainMaintenanceRequest,
    OpenSearchStartDomainMaintenanceResponse,
    OpenSearchStartMigrationRequest,
    OpenSearchStartMigrationResponse,
    OpenSearchStartServiceSoftwareUpdateRequest,
    OpenSearchStartServiceSoftwareUpdateResponse,
    OpenSearchSwitchoverReplicationRequest,
    OpenSearchSwitchoverReplicationResponse,
    OpenSearchUpdateApplicationRequest,
    OpenSearchUpdateApplicationResponse,
    OpenSearchUpdateCloneRequest,
    OpenSearchUpdateCloneResponse,
    OpenSearchUpdateDataSourceRequest,
    OpenSearchUpdateDataSourceResponse,
    OpenSearchUpdateDirectQueryDataSourceRequest,
    OpenSearchUpdateDirectQueryDataSourceResponse,
    OpenSearchUpdateDomainConfigRequest,
    OpenSearchUpdateDomainConfigResponse,
    OpenSearchUpdateIndexRequest,
    OpenSearchUpdateIndexResponse,
    OpenSearchUpdatePackageRequest,
    OpenSearchUpdatePackageResponse,
    OpenSearchUpdatePackageScopeRequest,
    OpenSearchUpdatePackageScopeResponse,
    OpenSearchUpdateScheduledActionRequest,
    OpenSearchUpdateScheduledActionResponse,
    OpenSearchUpdateVpcEndpointRequest,
    OpenSearchUpdateVpcEndpointResponse,
    OpenSearchUpgradeDomainRequest,
    OpenSearchUpgradeDomainResponse,
)
from werkflow_aws.types.opensearch_client import OpenSearchClient
from .base import AWSBaseService


class AWSOpenSearch(AWSBaseService[OpenSearchClient]):
    service_name = 'opensearch'
    boto3_service_name = 'opensearch'

    def __init__(self) -> None:
        super().__init__(service_name='opensearch', boto3_service_name='opensearch')

    async def accept_inbound_connection(
        self,
        request: OpenSearchAcceptInboundConnectionRequest,
    ) -> OpenSearchAcceptInboundConnectionResponse:
        client = self._require_client()
        return await self._execute(client.accept_inbound_connection, request, OpenSearchAcceptInboundConnectionResponse)

    async def add_data_source(
        self,
        request: OpenSearchAddDataSourceRequest,
    ) -> OpenSearchAddDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.add_data_source, request, OpenSearchAddDataSourceResponse)

    async def add_direct_query_data_source(
        self,
        request: OpenSearchAddDirectQueryDataSourceRequest,
    ) -> OpenSearchAddDirectQueryDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.add_direct_query_data_source, request, OpenSearchAddDirectQueryDataSourceResponse)

    async def add_replication_peer(
        self,
        request: OpenSearchAddReplicationPeerRequest,
    ) -> OpenSearchAddReplicationPeerResponse:
        client = self._require_client()
        return await self._execute(client.add_replication_peer, request, OpenSearchAddReplicationPeerResponse)

    async def add_tags(
        self,
        request: OpenSearchAddTagsRequest,
    ) -> OpenSearchAddTagsResponse:
        client = self._require_client()
        return await self._execute(client.add_tags, request, OpenSearchAddTagsResponse)

    async def associate_package(
        self,
        request: OpenSearchAssociatePackageRequest,
    ) -> OpenSearchAssociatePackageResponse:
        client = self._require_client()
        return await self._execute(client.associate_package, request, OpenSearchAssociatePackageResponse)

    async def associate_packages(
        self,
        request: OpenSearchAssociatePackagesRequest,
    ) -> OpenSearchAssociatePackagesResponse:
        client = self._require_client()
        return await self._execute(client.associate_packages, request, OpenSearchAssociatePackagesResponse)

    async def attach_data_source(
        self,
        request: OpenSearchAttachDataSourceRequest,
    ) -> OpenSearchAttachDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.attach_data_source, request, OpenSearchAttachDataSourceResponse)

    async def authorize_vpc_endpoint_access(
        self,
        request: OpenSearchAuthorizeVpcEndpointAccessRequest,
    ) -> OpenSearchAuthorizeVpcEndpointAccessResponse:
        client = self._require_client()
        return await self._execute(client.authorize_vpc_endpoint_access, request, OpenSearchAuthorizeVpcEndpointAccessResponse)

    async def cancel_domain_config_change(
        self,
        request: OpenSearchCancelDomainConfigChangeRequest,
    ) -> OpenSearchCancelDomainConfigChangeResponse:
        client = self._require_client()
        return await self._execute(client.cancel_domain_config_change, request, OpenSearchCancelDomainConfigChangeResponse)

    async def cancel_service_software_update(
        self,
        request: OpenSearchCancelServiceSoftwareUpdateRequest,
    ) -> OpenSearchCancelServiceSoftwareUpdateResponse:
        client = self._require_client()
        return await self._execute(client.cancel_service_software_update, request, OpenSearchCancelServiceSoftwareUpdateResponse)

    async def compare_domain_configuration(
        self,
        request: OpenSearchCompareDomainConfigurationRequest,
    ) -> OpenSearchCompareDomainConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.compare_domain_configuration, request, OpenSearchCompareDomainConfigurationResponse)

    async def create_application(
        self,
        request: OpenSearchCreateApplicationRequest,
    ) -> OpenSearchCreateApplicationResponse:
        client = self._require_client()
        return await self._execute(client.create_application, request, OpenSearchCreateApplicationResponse)

    async def create_domain(
        self,
        request: OpenSearchCreateDomainRequest,
    ) -> OpenSearchCreateDomainResponse:
        client = self._require_client()
        return await self._execute(client.create_domain, request, OpenSearchCreateDomainResponse)

    async def create_index(
        self,
        request: OpenSearchCreateIndexRequest,
    ) -> OpenSearchCreateIndexResponse:
        client = self._require_client()
        return await self._execute(client.create_index, request, OpenSearchCreateIndexResponse)

    async def create_outbound_connection(
        self,
        request: OpenSearchCreateOutboundConnectionRequest,
    ) -> OpenSearchCreateOutboundConnectionResponse:
        client = self._require_client()
        return await self._execute(client.create_outbound_connection, request, OpenSearchCreateOutboundConnectionResponse)

    async def create_package(
        self,
        request: OpenSearchCreatePackageRequest,
    ) -> OpenSearchCreatePackageResponse:
        client = self._require_client()
        return await self._execute(client.create_package, request, OpenSearchCreatePackageResponse)

    async def create_vpc_endpoint(
        self,
        request: OpenSearchCreateVpcEndpointRequest,
    ) -> OpenSearchCreateVpcEndpointResponse:
        client = self._require_client()
        return await self._execute(client.create_vpc_endpoint, request, OpenSearchCreateVpcEndpointResponse)

    async def delete_application(
        self,
        request: OpenSearchDeleteApplicationRequest,
    ) -> OpenSearchDeleteApplicationResponse:
        client = self._require_client()
        return await self._execute(client.delete_application, request, OpenSearchDeleteApplicationResponse)

    async def delete_data_source(
        self,
        request: OpenSearchDeleteDataSourceRequest,
    ) -> OpenSearchDeleteDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_source, request, OpenSearchDeleteDataSourceResponse)

    async def delete_direct_query_data_source(
        self,
        request: OpenSearchDeleteDirectQueryDataSourceRequest,
    ) -> OpenSearchDeleteDirectQueryDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.delete_direct_query_data_source, request, OpenSearchDeleteDirectQueryDataSourceResponse)

    async def delete_domain(
        self,
        request: OpenSearchDeleteDomainRequest,
    ) -> OpenSearchDeleteDomainResponse:
        client = self._require_client()
        return await self._execute(client.delete_domain, request, OpenSearchDeleteDomainResponse)

    async def delete_inbound_connection(
        self,
        request: OpenSearchDeleteInboundConnectionRequest,
    ) -> OpenSearchDeleteInboundConnectionResponse:
        client = self._require_client()
        return await self._execute(client.delete_inbound_connection, request, OpenSearchDeleteInboundConnectionResponse)

    async def delete_index(
        self,
        request: OpenSearchDeleteIndexRequest,
    ) -> OpenSearchDeleteIndexResponse:
        client = self._require_client()
        return await self._execute(client.delete_index, request, OpenSearchDeleteIndexResponse)

    async def delete_outbound_connection(
        self,
        request: OpenSearchDeleteOutboundConnectionRequest,
    ) -> OpenSearchDeleteOutboundConnectionResponse:
        client = self._require_client()
        return await self._execute(client.delete_outbound_connection, request, OpenSearchDeleteOutboundConnectionResponse)

    async def delete_package(
        self,
        request: OpenSearchDeletePackageRequest,
    ) -> OpenSearchDeletePackageResponse:
        client = self._require_client()
        return await self._execute(client.delete_package, request, OpenSearchDeletePackageResponse)

    async def delete_vpc_endpoint(
        self,
        request: OpenSearchDeleteVpcEndpointRequest,
    ) -> OpenSearchDeleteVpcEndpointResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpc_endpoint, request, OpenSearchDeleteVpcEndpointResponse)

    async def deregister_capability(
        self,
        request: OpenSearchDeregisterCapabilityRequest,
    ) -> OpenSearchDeregisterCapabilityResponse:
        client = self._require_client()
        return await self._execute(client.deregister_capability, request, OpenSearchDeregisterCapabilityResponse)

    async def describe_data_source_attachment(
        self,
        request: OpenSearchDescribeDataSourceAttachmentRequest,
    ) -> OpenSearchDescribeDataSourceAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.describe_data_source_attachment, request, OpenSearchDescribeDataSourceAttachmentResponse)

    async def describe_domain(
        self,
        request: OpenSearchDescribeDomainRequest,
    ) -> OpenSearchDescribeDomainResponse:
        client = self._require_client()
        return await self._execute(client.describe_domain, request, OpenSearchDescribeDomainResponse)

    async def describe_domain_auto_tunes(
        self,
        request: OpenSearchDescribeDomainAutoTunesRequest,
    ) -> OpenSearchDescribeDomainAutoTunesResponse:
        client = self._require_client()
        return await self._execute(client.describe_domain_auto_tunes, request, OpenSearchDescribeDomainAutoTunesResponse)

    async def describe_domain_change_progress(
        self,
        request: OpenSearchDescribeDomainChangeProgressRequest,
    ) -> OpenSearchDescribeDomainChangeProgressResponse:
        client = self._require_client()
        return await self._execute(client.describe_domain_change_progress, request, OpenSearchDescribeDomainChangeProgressResponse)

    async def describe_domain_config(
        self,
        request: OpenSearchDescribeDomainConfigRequest,
    ) -> OpenSearchDescribeDomainConfigResponse:
        client = self._require_client()
        return await self._execute(client.describe_domain_config, request, OpenSearchDescribeDomainConfigResponse)

    async def describe_domain_health(
        self,
        request: OpenSearchDescribeDomainHealthRequest,
    ) -> OpenSearchDescribeDomainHealthResponse:
        client = self._require_client()
        return await self._execute(client.describe_domain_health, request, OpenSearchDescribeDomainHealthResponse)

    async def describe_domain_nodes(
        self,
        request: OpenSearchDescribeDomainNodesRequest,
    ) -> OpenSearchDescribeDomainNodesResponse:
        client = self._require_client()
        return await self._execute(client.describe_domain_nodes, request, OpenSearchDescribeDomainNodesResponse)

    async def describe_domain_replication(
        self,
        request: OpenSearchDescribeDomainReplicationRequest,
    ) -> OpenSearchDescribeDomainReplicationResponse:
        client = self._require_client()
        return await self._execute(client.describe_domain_replication, request, OpenSearchDescribeDomainReplicationResponse)

    async def describe_domains(
        self,
        request: OpenSearchDescribeDomainsRequest,
    ) -> OpenSearchDescribeDomainsResponse:
        client = self._require_client()
        return await self._execute(client.describe_domains, request, OpenSearchDescribeDomainsResponse)

    async def describe_dry_run_progress(
        self,
        request: OpenSearchDescribeDryRunProgressRequest,
    ) -> OpenSearchDescribeDryRunProgressResponse:
        client = self._require_client()
        return await self._execute(client.describe_dry_run_progress, request, OpenSearchDescribeDryRunProgressResponse)

    async def describe_inbound_connections(
        self,
        request: OpenSearchDescribeInboundConnectionsRequest | None = None,
    ) -> OpenSearchDescribeInboundConnectionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_inbound_connections, request, OpenSearchDescribeInboundConnectionsResponse)

    async def describe_insight_details(
        self,
        request: OpenSearchDescribeInsightDetailsRequest,
    ) -> OpenSearchDescribeInsightDetailsResponse:
        client = self._require_client()
        return await self._execute(client.describe_insight_details, request, OpenSearchDescribeInsightDetailsResponse)

    async def describe_instance_type_limits(
        self,
        request: OpenSearchDescribeInstanceTypeLimitsRequest,
    ) -> OpenSearchDescribeInstanceTypeLimitsResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_type_limits, request, OpenSearchDescribeInstanceTypeLimitsResponse)

    async def describe_outbound_connections(
        self,
        request: OpenSearchDescribeOutboundConnectionsRequest | None = None,
    ) -> OpenSearchDescribeOutboundConnectionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_outbound_connections, request, OpenSearchDescribeOutboundConnectionsResponse)

    async def describe_packages(
        self,
        request: OpenSearchDescribePackagesRequest | None = None,
    ) -> OpenSearchDescribePackagesResponse:
        client = self._require_client()
        return await self._execute(client.describe_packages, request, OpenSearchDescribePackagesResponse)

    async def describe_reserved_instance_offerings(
        self,
        request: OpenSearchDescribeReservedInstanceOfferingsRequest | None = None,
    ) -> OpenSearchDescribeReservedInstanceOfferingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_reserved_instance_offerings, request, OpenSearchDescribeReservedInstanceOfferingsResponse)

    async def describe_reserved_instances(
        self,
        request: OpenSearchDescribeReservedInstancesRequest | None = None,
    ) -> OpenSearchDescribeReservedInstancesResponse:
        client = self._require_client()
        return await self._execute(client.describe_reserved_instances, request, OpenSearchDescribeReservedInstancesResponse)

    async def describe_vpc_endpoints(
        self,
        request: OpenSearchDescribeVpcEndpointsRequest,
    ) -> OpenSearchDescribeVpcEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpc_endpoints, request, OpenSearchDescribeVpcEndpointsResponse)

    async def detach_data_source(
        self,
        request: OpenSearchDetachDataSourceRequest,
    ) -> OpenSearchDetachDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.detach_data_source, request, OpenSearchDetachDataSourceResponse)

    async def dissociate_package(
        self,
        request: OpenSearchDissociatePackageRequest,
    ) -> OpenSearchDissociatePackageResponse:
        client = self._require_client()
        return await self._execute(client.dissociate_package, request, OpenSearchDissociatePackageResponse)

    async def dissociate_packages(
        self,
        request: OpenSearchDissociatePackagesRequest,
    ) -> OpenSearchDissociatePackagesResponse:
        client = self._require_client()
        return await self._execute(client.dissociate_packages, request, OpenSearchDissociatePackagesResponse)

    async def failover_replication(
        self,
        request: OpenSearchFailoverReplicationRequest,
    ) -> OpenSearchFailoverReplicationResponse:
        client = self._require_client()
        return await self._execute(client.failover_replication, request, OpenSearchFailoverReplicationResponse)

    async def get_application(
        self,
        request: OpenSearchGetApplicationRequest,
    ) -> OpenSearchGetApplicationResponse:
        client = self._require_client()
        return await self._execute(client.get_application, request, OpenSearchGetApplicationResponse)

    async def get_capability(
        self,
        request: OpenSearchGetCapabilityRequest,
    ) -> OpenSearchGetCapabilityResponse:
        client = self._require_client()
        return await self._execute(client.get_capability, request, OpenSearchGetCapabilityResponse)

    async def get_compatible_versions(
        self,
        request: OpenSearchGetCompatibleVersionsRequest | None = None,
    ) -> OpenSearchGetCompatibleVersionsResponse:
        client = self._require_client()
        return await self._execute(client.get_compatible_versions, request, OpenSearchGetCompatibleVersionsResponse)

    async def get_data_source(
        self,
        request: OpenSearchGetDataSourceRequest,
    ) -> OpenSearchGetDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.get_data_source, request, OpenSearchGetDataSourceResponse)

    async def get_default_application_setting(
        self,
        request: OpenSearchGetDefaultApplicationSettingRequest | None = None,
    ) -> OpenSearchGetDefaultApplicationSettingResponse:
        client = self._require_client()
        return await self._execute(client.get_default_application_setting, request, OpenSearchGetDefaultApplicationSettingResponse)

    async def get_direct_query_data_source(
        self,
        request: OpenSearchGetDirectQueryDataSourceRequest,
    ) -> OpenSearchGetDirectQueryDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.get_direct_query_data_source, request, OpenSearchGetDirectQueryDataSourceResponse)

    async def get_domain_maintenance_status(
        self,
        request: OpenSearchGetDomainMaintenanceStatusRequest,
    ) -> OpenSearchGetDomainMaintenanceStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_domain_maintenance_status, request, OpenSearchGetDomainMaintenanceStatusResponse)

    async def get_index(
        self,
        request: OpenSearchGetIndexRequest,
    ) -> OpenSearchGetIndexResponse:
        client = self._require_client()
        return await self._execute(client.get_index, request, OpenSearchGetIndexResponse)

    async def get_migration(
        self,
        request: OpenSearchGetMigrationRequest,
    ) -> OpenSearchGetMigrationResponse:
        client = self._require_client()
        return await self._execute(client.get_migration, request, OpenSearchGetMigrationResponse)

    async def get_package_version_history(
        self,
        request: OpenSearchGetPackageVersionHistoryRequest,
    ) -> OpenSearchGetPackageVersionHistoryResponse:
        client = self._require_client()
        return await self._execute(client.get_package_version_history, request, OpenSearchGetPackageVersionHistoryResponse)

    async def get_upgrade_history(
        self,
        request: OpenSearchGetUpgradeHistoryRequest,
    ) -> OpenSearchGetUpgradeHistoryResponse:
        client = self._require_client()
        return await self._execute(client.get_upgrade_history, request, OpenSearchGetUpgradeHistoryResponse)

    async def get_upgrade_status(
        self,
        request: OpenSearchGetUpgradeStatusRequest,
    ) -> OpenSearchGetUpgradeStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_upgrade_status, request, OpenSearchGetUpgradeStatusResponse)

    async def insight_feedback(
        self,
        request: OpenSearchInsightFeedbackRequest,
    ) -> OpenSearchInsightFeedbackResponse:
        client = self._require_client()
        return await self._execute(client.insight_feedback, request, OpenSearchInsightFeedbackResponse)

    async def list_applications(
        self,
        request: OpenSearchListApplicationsRequest | None = None,
    ) -> OpenSearchListApplicationsResponse:
        client = self._require_client()
        return await self._execute(client.list_applications, request, OpenSearchListApplicationsResponse)

    async def list_applications_paginated(
        self,
        request: OpenSearchListApplicationsRequest | None = None,
    ) -> list[OpenSearchListApplicationsResponse]:
        return await self._paginate('list_applications', request, OpenSearchListApplicationsResponse)

    async def list_data_source_attachments(
        self,
        request: OpenSearchListDataSourceAttachmentsRequest,
    ) -> OpenSearchListDataSourceAttachmentsResponse:
        client = self._require_client()
        return await self._execute(client.list_data_source_attachments, request, OpenSearchListDataSourceAttachmentsResponse)

    async def list_data_sources(
        self,
        request: OpenSearchListDataSourcesRequest,
    ) -> OpenSearchListDataSourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_data_sources, request, OpenSearchListDataSourcesResponse)

    async def list_direct_query_data_sources(
        self,
        request: OpenSearchListDirectQueryDataSourcesRequest | None = None,
    ) -> OpenSearchListDirectQueryDataSourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_direct_query_data_sources, request, OpenSearchListDirectQueryDataSourcesResponse)

    async def list_domain_maintenances(
        self,
        request: OpenSearchListDomainMaintenancesRequest,
    ) -> OpenSearchListDomainMaintenancesResponse:
        client = self._require_client()
        return await self._execute(client.list_domain_maintenances, request, OpenSearchListDomainMaintenancesResponse)

    async def list_domain_names(
        self,
        request: OpenSearchListDomainNamesRequest | None = None,
    ) -> OpenSearchListDomainNamesResponse:
        client = self._require_client()
        return await self._execute(client.list_domain_names, request, OpenSearchListDomainNamesResponse)

    async def list_domains_for_package(
        self,
        request: OpenSearchListDomainsForPackageRequest,
    ) -> OpenSearchListDomainsForPackageResponse:
        client = self._require_client()
        return await self._execute(client.list_domains_for_package, request, OpenSearchListDomainsForPackageResponse)

    async def list_insights(
        self,
        request: OpenSearchListInsightsRequest,
    ) -> OpenSearchListInsightsResponse:
        client = self._require_client()
        return await self._execute(client.list_insights, request, OpenSearchListInsightsResponse)

    async def list_instance_type_details(
        self,
        request: OpenSearchListInstanceTypeDetailsRequest,
    ) -> OpenSearchListInstanceTypeDetailsResponse:
        client = self._require_client()
        return await self._execute(client.list_instance_type_details, request, OpenSearchListInstanceTypeDetailsResponse)

    async def list_migrations(
        self,
        request: OpenSearchListMigrationsRequest,
    ) -> OpenSearchListMigrationsResponse:
        client = self._require_client()
        return await self._execute(client.list_migrations, request, OpenSearchListMigrationsResponse)

    async def list_packages_for_domain(
        self,
        request: OpenSearchListPackagesForDomainRequest,
    ) -> OpenSearchListPackagesForDomainResponse:
        client = self._require_client()
        return await self._execute(client.list_packages_for_domain, request, OpenSearchListPackagesForDomainResponse)

    async def list_scheduled_actions(
        self,
        request: OpenSearchListScheduledActionsRequest,
    ) -> OpenSearchListScheduledActionsResponse:
        client = self._require_client()
        return await self._execute(client.list_scheduled_actions, request, OpenSearchListScheduledActionsResponse)

    async def list_tags(
        self,
        request: OpenSearchListTagsRequest,
    ) -> OpenSearchListTagsResponse:
        client = self._require_client()
        return await self._execute(client.list_tags, request, OpenSearchListTagsResponse)

    async def list_versions(
        self,
        request: OpenSearchListVersionsRequest | None = None,
    ) -> OpenSearchListVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_versions, request, OpenSearchListVersionsResponse)

    async def list_vpc_endpoint_access(
        self,
        request: OpenSearchListVpcEndpointAccessRequest,
    ) -> OpenSearchListVpcEndpointAccessResponse:
        client = self._require_client()
        return await self._execute(client.list_vpc_endpoint_access, request, OpenSearchListVpcEndpointAccessResponse)

    async def list_vpc_endpoints(
        self,
        request: OpenSearchListVpcEndpointsRequest | None = None,
    ) -> OpenSearchListVpcEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.list_vpc_endpoints, request, OpenSearchListVpcEndpointsResponse)

    async def list_vpc_endpoints_for_domain(
        self,
        request: OpenSearchListVpcEndpointsForDomainRequest,
    ) -> OpenSearchListVpcEndpointsForDomainResponse:
        client = self._require_client()
        return await self._execute(client.list_vpc_endpoints_for_domain, request, OpenSearchListVpcEndpointsForDomainResponse)

    async def purchase_reserved_instance_offering(
        self,
        request: OpenSearchPurchaseReservedInstanceOfferingRequest,
    ) -> OpenSearchPurchaseReservedInstanceOfferingResponse:
        client = self._require_client()
        return await self._execute(client.purchase_reserved_instance_offering, request, OpenSearchPurchaseReservedInstanceOfferingResponse)

    async def put_default_application_setting(
        self,
        request: OpenSearchPutDefaultApplicationSettingRequest,
    ) -> OpenSearchPutDefaultApplicationSettingResponse:
        client = self._require_client()
        return await self._execute(client.put_default_application_setting, request, OpenSearchPutDefaultApplicationSettingResponse)

    async def register_capability(
        self,
        request: OpenSearchRegisterCapabilityRequest,
    ) -> OpenSearchRegisterCapabilityResponse:
        client = self._require_client()
        return await self._execute(client.register_capability, request, OpenSearchRegisterCapabilityResponse)

    async def reject_inbound_connection(
        self,
        request: OpenSearchRejectInboundConnectionRequest,
    ) -> OpenSearchRejectInboundConnectionResponse:
        client = self._require_client()
        return await self._execute(client.reject_inbound_connection, request, OpenSearchRejectInboundConnectionResponse)

    async def remove_replication_peer(
        self,
        request: OpenSearchRemoveReplicationPeerRequest,
    ) -> OpenSearchRemoveReplicationPeerResponse:
        client = self._require_client()
        return await self._execute(client.remove_replication_peer, request, OpenSearchRemoveReplicationPeerResponse)

    async def remove_tags(
        self,
        request: OpenSearchRemoveTagsRequest,
    ) -> OpenSearchRemoveTagsResponse:
        client = self._require_client()
        return await self._execute(client.remove_tags, request, OpenSearchRemoveTagsResponse)

    async def revoke_vpc_endpoint_access(
        self,
        request: OpenSearchRevokeVpcEndpointAccessRequest,
    ) -> OpenSearchRevokeVpcEndpointAccessResponse:
        client = self._require_client()
        return await self._execute(client.revoke_vpc_endpoint_access, request, OpenSearchRevokeVpcEndpointAccessResponse)

    async def rollback_service_software_update(
        self,
        request: OpenSearchRollbackServiceSoftwareUpdateRequest,
    ) -> OpenSearchRollbackServiceSoftwareUpdateResponse:
        client = self._require_client()
        return await self._execute(client.rollback_service_software_update, request, OpenSearchRollbackServiceSoftwareUpdateResponse)

    async def start_domain_maintenance(
        self,
        request: OpenSearchStartDomainMaintenanceRequest,
    ) -> OpenSearchStartDomainMaintenanceResponse:
        client = self._require_client()
        return await self._execute(client.start_domain_maintenance, request, OpenSearchStartDomainMaintenanceResponse)

    async def start_migration(
        self,
        request: OpenSearchStartMigrationRequest,
    ) -> OpenSearchStartMigrationResponse:
        client = self._require_client()
        return await self._execute(client.start_migration, request, OpenSearchStartMigrationResponse)

    async def start_service_software_update(
        self,
        request: OpenSearchStartServiceSoftwareUpdateRequest,
    ) -> OpenSearchStartServiceSoftwareUpdateResponse:
        client = self._require_client()
        return await self._execute(client.start_service_software_update, request, OpenSearchStartServiceSoftwareUpdateResponse)

    async def switchover_replication(
        self,
        request: OpenSearchSwitchoverReplicationRequest,
    ) -> OpenSearchSwitchoverReplicationResponse:
        client = self._require_client()
        return await self._execute(client.switchover_replication, request, OpenSearchSwitchoverReplicationResponse)

    async def update_application(
        self,
        request: OpenSearchUpdateApplicationRequest,
    ) -> OpenSearchUpdateApplicationResponse:
        client = self._require_client()
        return await self._execute(client.update_application, request, OpenSearchUpdateApplicationResponse)

    async def update_clone(
        self,
        request: OpenSearchUpdateCloneRequest,
    ) -> OpenSearchUpdateCloneResponse:
        client = self._require_client()
        return await self._execute(client.update_clone, request, OpenSearchUpdateCloneResponse)

    async def update_data_source(
        self,
        request: OpenSearchUpdateDataSourceRequest,
    ) -> OpenSearchUpdateDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.update_data_source, request, OpenSearchUpdateDataSourceResponse)

    async def update_direct_query_data_source(
        self,
        request: OpenSearchUpdateDirectQueryDataSourceRequest,
    ) -> OpenSearchUpdateDirectQueryDataSourceResponse:
        client = self._require_client()
        return await self._execute(client.update_direct_query_data_source, request, OpenSearchUpdateDirectQueryDataSourceResponse)

    async def update_domain_config(
        self,
        request: OpenSearchUpdateDomainConfigRequest,
    ) -> OpenSearchUpdateDomainConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_domain_config, request, OpenSearchUpdateDomainConfigResponse)

    async def update_index(
        self,
        request: OpenSearchUpdateIndexRequest,
    ) -> OpenSearchUpdateIndexResponse:
        client = self._require_client()
        return await self._execute(client.update_index, request, OpenSearchUpdateIndexResponse)

    async def update_package(
        self,
        request: OpenSearchUpdatePackageRequest,
    ) -> OpenSearchUpdatePackageResponse:
        client = self._require_client()
        return await self._execute(client.update_package, request, OpenSearchUpdatePackageResponse)

    async def update_package_scope(
        self,
        request: OpenSearchUpdatePackageScopeRequest,
    ) -> OpenSearchUpdatePackageScopeResponse:
        client = self._require_client()
        return await self._execute(client.update_package_scope, request, OpenSearchUpdatePackageScopeResponse)

    async def update_scheduled_action(
        self,
        request: OpenSearchUpdateScheduledActionRequest,
    ) -> OpenSearchUpdateScheduledActionResponse:
        client = self._require_client()
        return await self._execute(client.update_scheduled_action, request, OpenSearchUpdateScheduledActionResponse)

    async def update_vpc_endpoint(
        self,
        request: OpenSearchUpdateVpcEndpointRequest,
    ) -> OpenSearchUpdateVpcEndpointResponse:
        client = self._require_client()
        return await self._execute(client.update_vpc_endpoint, request, OpenSearchUpdateVpcEndpointResponse)

    async def upgrade_domain(
        self,
        request: OpenSearchUpgradeDomainRequest,
    ) -> OpenSearchUpgradeDomainResponse:
        client = self._require_client()
        return await self._execute(client.upgrade_domain, request, OpenSearchUpgradeDomainResponse)
