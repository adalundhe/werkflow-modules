from werkflow_aws.models.dms import (
    DMSAddTagsToResourceRequest,
    DMSAddTagsToResourceResponse,
    DMSApplyPendingMaintenanceActionRequest,
    DMSApplyPendingMaintenanceActionResponse,
    DMSBatchStartRecommendationsRequest,
    DMSBatchStartRecommendationsResponse,
    DMSCancelMetadataModelConversionRequest,
    DMSCancelMetadataModelConversionResponse,
    DMSCancelMetadataModelCreationRequest,
    DMSCancelMetadataModelCreationResponse,
    DMSCancelReplicationTaskAssessmentRunRequest,
    DMSCancelReplicationTaskAssessmentRunResponse,
    DMSCreateDataMigrationRequest,
    DMSCreateDataMigrationResponse,
    DMSCreateDataProviderRequest,
    DMSCreateDataProviderResponse,
    DMSCreateEndpointRequest,
    DMSCreateEndpointResponse,
    DMSCreateEventSubscriptionRequest,
    DMSCreateEventSubscriptionResponse,
    DMSCreateFleetAdvisorCollectorRequest,
    DMSCreateFleetAdvisorCollectorResponse,
    DMSCreateInstanceProfileRequest,
    DMSCreateInstanceProfileResponse,
    DMSCreateMigrationProjectRequest,
    DMSCreateMigrationProjectResponse,
    DMSCreateReplicationConfigRequest,
    DMSCreateReplicationConfigResponse,
    DMSCreateReplicationInstanceRequest,
    DMSCreateReplicationInstanceResponse,
    DMSCreateReplicationSubnetGroupRequest,
    DMSCreateReplicationSubnetGroupResponse,
    DMSCreateReplicationTaskRequest,
    DMSCreateReplicationTaskResponse,
    DMSDeleteCertificateRequest,
    DMSDeleteCertificateResponse,
    DMSDeleteConnectionRequest,
    DMSDeleteConnectionResponse,
    DMSDeleteDataMigrationRequest,
    DMSDeleteDataMigrationResponse,
    DMSDeleteDataProviderRequest,
    DMSDeleteDataProviderResponse,
    DMSDeleteEndpointRequest,
    DMSDeleteEndpointResponse,
    DMSDeleteEventSubscriptionRequest,
    DMSDeleteEventSubscriptionResponse,
    DMSDeleteFleetAdvisorCollectorRequest,
    DMSDeleteFleetAdvisorCollectorResponse,
    DMSDeleteFleetAdvisorDatabasesRequest,
    DMSDeleteFleetAdvisorDatabasesResponse,
    DMSDeleteInstanceProfileRequest,
    DMSDeleteInstanceProfileResponse,
    DMSDeleteMigrationProjectRequest,
    DMSDeleteMigrationProjectResponse,
    DMSDeleteReplicationConfigRequest,
    DMSDeleteReplicationConfigResponse,
    DMSDeleteReplicationInstanceRequest,
    DMSDeleteReplicationInstanceResponse,
    DMSDeleteReplicationSubnetGroupRequest,
    DMSDeleteReplicationSubnetGroupResponse,
    DMSDeleteReplicationTaskAssessmentRunRequest,
    DMSDeleteReplicationTaskAssessmentRunResponse,
    DMSDeleteReplicationTaskRequest,
    DMSDeleteReplicationTaskResponse,
    DMSDescribeAccountAttributesRequest,
    DMSDescribeAccountAttributesResponse,
    DMSDescribeApplicableIndividualAssessmentsRequest,
    DMSDescribeApplicableIndividualAssessmentsResponse,
    DMSDescribeCertificatesRequest,
    DMSDescribeCertificatesResponse,
    DMSDescribeConnectionsRequest,
    DMSDescribeConnectionsResponse,
    DMSDescribeConversionConfigurationRequest,
    DMSDescribeConversionConfigurationResponse,
    DMSDescribeDataMigrationsRequest,
    DMSDescribeDataMigrationsResponse,
    DMSDescribeDataProvidersRequest,
    DMSDescribeDataProvidersResponse,
    DMSDescribeEndpointSettingsRequest,
    DMSDescribeEndpointSettingsResponse,
    DMSDescribeEndpointTypesRequest,
    DMSDescribeEndpointTypesResponse,
    DMSDescribeEndpointsRequest,
    DMSDescribeEndpointsResponse,
    DMSDescribeEngineVersionsRequest,
    DMSDescribeEngineVersionsResponse,
    DMSDescribeEventCategoriesRequest,
    DMSDescribeEventCategoriesResponse,
    DMSDescribeEventSubscriptionsRequest,
    DMSDescribeEventSubscriptionsResponse,
    DMSDescribeEventsRequest,
    DMSDescribeEventsResponse,
    DMSDescribeExtensionPackAssociationsRequest,
    DMSDescribeExtensionPackAssociationsResponse,
    DMSDescribeFleetAdvisorCollectorsRequest,
    DMSDescribeFleetAdvisorCollectorsResponse,
    DMSDescribeFleetAdvisorDatabasesRequest,
    DMSDescribeFleetAdvisorDatabasesResponse,
    DMSDescribeFleetAdvisorLsaAnalysisRequest,
    DMSDescribeFleetAdvisorLsaAnalysisResponse,
    DMSDescribeFleetAdvisorSchemaObjectSummaryRequest,
    DMSDescribeFleetAdvisorSchemaObjectSummaryResponse,
    DMSDescribeFleetAdvisorSchemasRequest,
    DMSDescribeFleetAdvisorSchemasResponse,
    DMSDescribeInstanceProfilesRequest,
    DMSDescribeInstanceProfilesResponse,
    DMSDescribeMetadataModelAssessmentsRequest,
    DMSDescribeMetadataModelAssessmentsResponse,
    DMSDescribeMetadataModelChildrenRequest,
    DMSDescribeMetadataModelChildrenResponse,
    DMSDescribeMetadataModelConversionsRequest,
    DMSDescribeMetadataModelConversionsResponse,
    DMSDescribeMetadataModelCreationsRequest,
    DMSDescribeMetadataModelCreationsResponse,
    DMSDescribeMetadataModelExportsAsScriptRequest,
    DMSDescribeMetadataModelExportsAsScriptResponse,
    DMSDescribeMetadataModelExportsToTargetRequest,
    DMSDescribeMetadataModelExportsToTargetResponse,
    DMSDescribeMetadataModelImportsRequest,
    DMSDescribeMetadataModelImportsResponse,
    DMSDescribeMetadataModelRequest,
    DMSDescribeMetadataModelResponse,
    DMSDescribeMigrationProjectsRequest,
    DMSDescribeMigrationProjectsResponse,
    DMSDescribeOrderableReplicationInstancesRequest,
    DMSDescribeOrderableReplicationInstancesResponse,
    DMSDescribePendingMaintenanceActionsRequest,
    DMSDescribePendingMaintenanceActionsResponse,
    DMSDescribeRecommendationLimitationsRequest,
    DMSDescribeRecommendationLimitationsResponse,
    DMSDescribeRecommendationsRequest,
    DMSDescribeRecommendationsResponse,
    DMSDescribeRefreshSchemasStatusRequest,
    DMSDescribeRefreshSchemasStatusResponse,
    DMSDescribeReplicationConfigsRequest,
    DMSDescribeReplicationConfigsResponse,
    DMSDescribeReplicationInstanceTaskLogsRequest,
    DMSDescribeReplicationInstanceTaskLogsResponse,
    DMSDescribeReplicationInstancesRequest,
    DMSDescribeReplicationInstancesResponse,
    DMSDescribeReplicationSubnetGroupsRequest,
    DMSDescribeReplicationSubnetGroupsResponse,
    DMSDescribeReplicationTableStatisticsRequest,
    DMSDescribeReplicationTableStatisticsResponse,
    DMSDescribeReplicationTaskAssessmentResultsRequest,
    DMSDescribeReplicationTaskAssessmentResultsResponse,
    DMSDescribeReplicationTaskAssessmentRunsRequest,
    DMSDescribeReplicationTaskAssessmentRunsResponse,
    DMSDescribeReplicationTaskIndividualAssessmentsRequest,
    DMSDescribeReplicationTaskIndividualAssessmentsResponse,
    DMSDescribeReplicationTasksRequest,
    DMSDescribeReplicationTasksResponse,
    DMSDescribeReplicationsRequest,
    DMSDescribeReplicationsResponse,
    DMSDescribeSchemasRequest,
    DMSDescribeSchemasResponse,
    DMSDescribeTableStatisticsRequest,
    DMSDescribeTableStatisticsResponse,
    DMSExportMetadataModelAssessmentRequest,
    DMSExportMetadataModelAssessmentResponse,
    DMSGetTargetSelectionRulesRequest,
    DMSGetTargetSelectionRulesResponse,
    DMSImportCertificateRequest,
    DMSImportCertificateResponse,
    DMSListTagsForResourceRequest,
    DMSListTagsForResourceResponse,
    DMSModifyConversionConfigurationRequest,
    DMSModifyConversionConfigurationResponse,
    DMSModifyDataMigrationRequest,
    DMSModifyDataMigrationResponse,
    DMSModifyDataProviderRequest,
    DMSModifyDataProviderResponse,
    DMSModifyEndpointRequest,
    DMSModifyEndpointResponse,
    DMSModifyEventSubscriptionRequest,
    DMSModifyEventSubscriptionResponse,
    DMSModifyInstanceProfileRequest,
    DMSModifyInstanceProfileResponse,
    DMSModifyMigrationProjectRequest,
    DMSModifyMigrationProjectResponse,
    DMSModifyReplicationConfigRequest,
    DMSModifyReplicationConfigResponse,
    DMSModifyReplicationInstanceRequest,
    DMSModifyReplicationInstanceResponse,
    DMSModifyReplicationSubnetGroupRequest,
    DMSModifyReplicationSubnetGroupResponse,
    DMSModifyReplicationTaskRequest,
    DMSModifyReplicationTaskResponse,
    DMSMoveReplicationTaskRequest,
    DMSMoveReplicationTaskResponse,
    DMSRebootReplicationInstanceRequest,
    DMSRebootReplicationInstanceResponse,
    DMSRefreshSchemasRequest,
    DMSRefreshSchemasResponse,
    DMSReloadReplicationTablesRequest,
    DMSReloadReplicationTablesResponse,
    DMSReloadTablesRequest,
    DMSReloadTablesResponse,
    DMSRemoveTagsFromResourceRequest,
    DMSRemoveTagsFromResourceResponse,
    DMSRunFleetAdvisorLsaAnalysisRequest,
    DMSRunFleetAdvisorLsaAnalysisResponse,
    DMSStartDataMigrationRequest,
    DMSStartDataMigrationResponse,
    DMSStartExtensionPackAssociationRequest,
    DMSStartExtensionPackAssociationResponse,
    DMSStartMetadataModelAssessmentRequest,
    DMSStartMetadataModelAssessmentResponse,
    DMSStartMetadataModelConversionRequest,
    DMSStartMetadataModelConversionResponse,
    DMSStartMetadataModelCreationRequest,
    DMSStartMetadataModelCreationResponse,
    DMSStartMetadataModelExportAsScriptRequest,
    DMSStartMetadataModelExportAsScriptResponse,
    DMSStartMetadataModelExportToTargetRequest,
    DMSStartMetadataModelExportToTargetResponse,
    DMSStartMetadataModelImportRequest,
    DMSStartMetadataModelImportResponse,
    DMSStartRecommendationsRequest,
    DMSStartRecommendationsResponse,
    DMSStartReplicationRequest,
    DMSStartReplicationResponse,
    DMSStartReplicationTaskAssessmentRequest,
    DMSStartReplicationTaskAssessmentResponse,
    DMSStartReplicationTaskAssessmentRunRequest,
    DMSStartReplicationTaskAssessmentRunResponse,
    DMSStartReplicationTaskRequest,
    DMSStartReplicationTaskResponse,
    DMSStopDataMigrationRequest,
    DMSStopDataMigrationResponse,
    DMSStopReplicationRequest,
    DMSStopReplicationResponse,
    DMSStopReplicationTaskRequest,
    DMSStopReplicationTaskResponse,
    DMSTestConnectionRequest,
    DMSTestConnectionResponse,
    DMSUpdateSubscriptionsToEventBridgeRequest,
    DMSUpdateSubscriptionsToEventBridgeResponse,
)
from werkflow_aws.types.dms_client import DMSClient
from .base import AWSBaseService


class AWSDMS(AWSBaseService[DMSClient]):
    service_name = 'dms'
    boto3_service_name = 'dms'

    def __init__(self) -> None:
        super().__init__(service_name='dms', boto3_service_name='dms')

    async def add_tags_to_resource(
        self,
        request: DMSAddTagsToResourceRequest,
    ) -> DMSAddTagsToResourceResponse:
        client = self._require_client()
        return await self._execute(client.add_tags_to_resource, request, DMSAddTagsToResourceResponse)

    async def apply_pending_maintenance_action(
        self,
        request: DMSApplyPendingMaintenanceActionRequest,
    ) -> DMSApplyPendingMaintenanceActionResponse:
        client = self._require_client()
        return await self._execute(client.apply_pending_maintenance_action, request, DMSApplyPendingMaintenanceActionResponse)

    async def batch_start_recommendations(
        self,
        request: DMSBatchStartRecommendationsRequest | None = None,
    ) -> DMSBatchStartRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.batch_start_recommendations, request, DMSBatchStartRecommendationsResponse)

    async def cancel_metadata_model_conversion(
        self,
        request: DMSCancelMetadataModelConversionRequest,
    ) -> DMSCancelMetadataModelConversionResponse:
        client = self._require_client()
        return await self._execute(client.cancel_metadata_model_conversion, request, DMSCancelMetadataModelConversionResponse)

    async def cancel_metadata_model_creation(
        self,
        request: DMSCancelMetadataModelCreationRequest,
    ) -> DMSCancelMetadataModelCreationResponse:
        client = self._require_client()
        return await self._execute(client.cancel_metadata_model_creation, request, DMSCancelMetadataModelCreationResponse)

    async def cancel_replication_task_assessment_run(
        self,
        request: DMSCancelReplicationTaskAssessmentRunRequest,
    ) -> DMSCancelReplicationTaskAssessmentRunResponse:
        client = self._require_client()
        return await self._execute(client.cancel_replication_task_assessment_run, request, DMSCancelReplicationTaskAssessmentRunResponse)

    async def create_data_migration(
        self,
        request: DMSCreateDataMigrationRequest,
    ) -> DMSCreateDataMigrationResponse:
        client = self._require_client()
        return await self._execute(client.create_data_migration, request, DMSCreateDataMigrationResponse)

    async def create_data_provider(
        self,
        request: DMSCreateDataProviderRequest,
    ) -> DMSCreateDataProviderResponse:
        client = self._require_client()
        return await self._execute(client.create_data_provider, request, DMSCreateDataProviderResponse)

    async def create_endpoint(
        self,
        request: DMSCreateEndpointRequest,
    ) -> DMSCreateEndpointResponse:
        client = self._require_client()
        return await self._execute(client.create_endpoint, request, DMSCreateEndpointResponse)

    async def create_event_subscription(
        self,
        request: DMSCreateEventSubscriptionRequest,
    ) -> DMSCreateEventSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.create_event_subscription, request, DMSCreateEventSubscriptionResponse)

    async def create_fleet_advisor_collector(
        self,
        request: DMSCreateFleetAdvisorCollectorRequest,
    ) -> DMSCreateFleetAdvisorCollectorResponse:
        client = self._require_client()
        return await self._execute(client.create_fleet_advisor_collector, request, DMSCreateFleetAdvisorCollectorResponse)

    async def create_instance_profile(
        self,
        request: DMSCreateInstanceProfileRequest | None = None,
    ) -> DMSCreateInstanceProfileResponse:
        client = self._require_client()
        return await self._execute(client.create_instance_profile, request, DMSCreateInstanceProfileResponse)

    async def create_migration_project(
        self,
        request: DMSCreateMigrationProjectRequest,
    ) -> DMSCreateMigrationProjectResponse:
        client = self._require_client()
        return await self._execute(client.create_migration_project, request, DMSCreateMigrationProjectResponse)

    async def create_replication_config(
        self,
        request: DMSCreateReplicationConfigRequest,
    ) -> DMSCreateReplicationConfigResponse:
        client = self._require_client()
        return await self._execute(client.create_replication_config, request, DMSCreateReplicationConfigResponse)

    async def create_replication_instance(
        self,
        request: DMSCreateReplicationInstanceRequest,
    ) -> DMSCreateReplicationInstanceResponse:
        client = self._require_client()
        return await self._execute(client.create_replication_instance, request, DMSCreateReplicationInstanceResponse)

    async def create_replication_subnet_group(
        self,
        request: DMSCreateReplicationSubnetGroupRequest,
    ) -> DMSCreateReplicationSubnetGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_replication_subnet_group, request, DMSCreateReplicationSubnetGroupResponse)

    async def create_replication_task(
        self,
        request: DMSCreateReplicationTaskRequest,
    ) -> DMSCreateReplicationTaskResponse:
        client = self._require_client()
        return await self._execute(client.create_replication_task, request, DMSCreateReplicationTaskResponse)

    async def delete_certificate(
        self,
        request: DMSDeleteCertificateRequest,
    ) -> DMSDeleteCertificateResponse:
        client = self._require_client()
        return await self._execute(client.delete_certificate, request, DMSDeleteCertificateResponse)

    async def delete_connection(
        self,
        request: DMSDeleteConnectionRequest,
    ) -> DMSDeleteConnectionResponse:
        client = self._require_client()
        return await self._execute(client.delete_connection, request, DMSDeleteConnectionResponse)

    async def delete_data_migration(
        self,
        request: DMSDeleteDataMigrationRequest,
    ) -> DMSDeleteDataMigrationResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_migration, request, DMSDeleteDataMigrationResponse)

    async def delete_data_provider(
        self,
        request: DMSDeleteDataProviderRequest,
    ) -> DMSDeleteDataProviderResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_provider, request, DMSDeleteDataProviderResponse)

    async def delete_endpoint(
        self,
        request: DMSDeleteEndpointRequest,
    ) -> DMSDeleteEndpointResponse:
        client = self._require_client()
        return await self._execute(client.delete_endpoint, request, DMSDeleteEndpointResponse)

    async def delete_event_subscription(
        self,
        request: DMSDeleteEventSubscriptionRequest,
    ) -> DMSDeleteEventSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.delete_event_subscription, request, DMSDeleteEventSubscriptionResponse)

    async def delete_fleet_advisor_collector(
        self,
        request: DMSDeleteFleetAdvisorCollectorRequest,
    ) -> DMSDeleteFleetAdvisorCollectorResponse:
        client = self._require_client()
        return await self._execute(client.delete_fleet_advisor_collector, request, DMSDeleteFleetAdvisorCollectorResponse)

    async def delete_fleet_advisor_databases(
        self,
        request: DMSDeleteFleetAdvisorDatabasesRequest,
    ) -> DMSDeleteFleetAdvisorDatabasesResponse:
        client = self._require_client()
        return await self._execute(client.delete_fleet_advisor_databases, request, DMSDeleteFleetAdvisorDatabasesResponse)

    async def delete_instance_profile(
        self,
        request: DMSDeleteInstanceProfileRequest,
    ) -> DMSDeleteInstanceProfileResponse:
        client = self._require_client()
        return await self._execute(client.delete_instance_profile, request, DMSDeleteInstanceProfileResponse)

    async def delete_migration_project(
        self,
        request: DMSDeleteMigrationProjectRequest,
    ) -> DMSDeleteMigrationProjectResponse:
        client = self._require_client()
        return await self._execute(client.delete_migration_project, request, DMSDeleteMigrationProjectResponse)

    async def delete_replication_config(
        self,
        request: DMSDeleteReplicationConfigRequest,
    ) -> DMSDeleteReplicationConfigResponse:
        client = self._require_client()
        return await self._execute(client.delete_replication_config, request, DMSDeleteReplicationConfigResponse)

    async def delete_replication_instance(
        self,
        request: DMSDeleteReplicationInstanceRequest,
    ) -> DMSDeleteReplicationInstanceResponse:
        client = self._require_client()
        return await self._execute(client.delete_replication_instance, request, DMSDeleteReplicationInstanceResponse)

    async def delete_replication_subnet_group(
        self,
        request: DMSDeleteReplicationSubnetGroupRequest,
    ) -> DMSDeleteReplicationSubnetGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_replication_subnet_group, request, DMSDeleteReplicationSubnetGroupResponse)

    async def delete_replication_task(
        self,
        request: DMSDeleteReplicationTaskRequest,
    ) -> DMSDeleteReplicationTaskResponse:
        client = self._require_client()
        return await self._execute(client.delete_replication_task, request, DMSDeleteReplicationTaskResponse)

    async def delete_replication_task_assessment_run(
        self,
        request: DMSDeleteReplicationTaskAssessmentRunRequest,
    ) -> DMSDeleteReplicationTaskAssessmentRunResponse:
        client = self._require_client()
        return await self._execute(client.delete_replication_task_assessment_run, request, DMSDeleteReplicationTaskAssessmentRunResponse)

    async def describe_account_attributes(
        self,
        request: DMSDescribeAccountAttributesRequest | None = None,
    ) -> DMSDescribeAccountAttributesResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_attributes, request, DMSDescribeAccountAttributesResponse)

    async def describe_applicable_individual_assessments(
        self,
        request: DMSDescribeApplicableIndividualAssessmentsRequest | None = None,
    ) -> DMSDescribeApplicableIndividualAssessmentsResponse:
        client = self._require_client()
        return await self._execute(client.describe_applicable_individual_assessments, request, DMSDescribeApplicableIndividualAssessmentsResponse)

    async def describe_certificates(
        self,
        request: DMSDescribeCertificatesRequest | None = None,
    ) -> DMSDescribeCertificatesResponse:
        client = self._require_client()
        return await self._execute(client.describe_certificates, request, DMSDescribeCertificatesResponse)

    async def describe_certificates_paginated(
        self,
        request: DMSDescribeCertificatesRequest | None = None,
    ) -> list[DMSDescribeCertificatesResponse]:
        return await self._paginate('describe_certificates', request, DMSDescribeCertificatesResponse)

    async def describe_connections(
        self,
        request: DMSDescribeConnectionsRequest | None = None,
    ) -> DMSDescribeConnectionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_connections, request, DMSDescribeConnectionsResponse)

    async def describe_connections_paginated(
        self,
        request: DMSDescribeConnectionsRequest | None = None,
    ) -> list[DMSDescribeConnectionsResponse]:
        return await self._paginate('describe_connections', request, DMSDescribeConnectionsResponse)

    async def describe_conversion_configuration(
        self,
        request: DMSDescribeConversionConfigurationRequest,
    ) -> DMSDescribeConversionConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.describe_conversion_configuration, request, DMSDescribeConversionConfigurationResponse)

    async def describe_data_migrations(
        self,
        request: DMSDescribeDataMigrationsRequest | None = None,
    ) -> DMSDescribeDataMigrationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_data_migrations, request, DMSDescribeDataMigrationsResponse)

    async def describe_data_migrations_paginated(
        self,
        request: DMSDescribeDataMigrationsRequest | None = None,
    ) -> list[DMSDescribeDataMigrationsResponse]:
        return await self._paginate('describe_data_migrations', request, DMSDescribeDataMigrationsResponse)

    async def describe_data_providers(
        self,
        request: DMSDescribeDataProvidersRequest | None = None,
    ) -> DMSDescribeDataProvidersResponse:
        client = self._require_client()
        return await self._execute(client.describe_data_providers, request, DMSDescribeDataProvidersResponse)

    async def describe_endpoint_settings(
        self,
        request: DMSDescribeEndpointSettingsRequest,
    ) -> DMSDescribeEndpointSettingsResponse:
        client = self._require_client()
        return await self._execute(client.describe_endpoint_settings, request, DMSDescribeEndpointSettingsResponse)

    async def describe_endpoint_types(
        self,
        request: DMSDescribeEndpointTypesRequest | None = None,
    ) -> DMSDescribeEndpointTypesResponse:
        client = self._require_client()
        return await self._execute(client.describe_endpoint_types, request, DMSDescribeEndpointTypesResponse)

    async def describe_endpoint_types_paginated(
        self,
        request: DMSDescribeEndpointTypesRequest | None = None,
    ) -> list[DMSDescribeEndpointTypesResponse]:
        return await self._paginate('describe_endpoint_types', request, DMSDescribeEndpointTypesResponse)

    async def describe_endpoints(
        self,
        request: DMSDescribeEndpointsRequest | None = None,
    ) -> DMSDescribeEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.describe_endpoints, request, DMSDescribeEndpointsResponse)

    async def describe_endpoints_paginated(
        self,
        request: DMSDescribeEndpointsRequest | None = None,
    ) -> list[DMSDescribeEndpointsResponse]:
        return await self._paginate('describe_endpoints', request, DMSDescribeEndpointsResponse)

    async def describe_engine_versions(
        self,
        request: DMSDescribeEngineVersionsRequest | None = None,
    ) -> DMSDescribeEngineVersionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_engine_versions, request, DMSDescribeEngineVersionsResponse)

    async def describe_event_categories(
        self,
        request: DMSDescribeEventCategoriesRequest | None = None,
    ) -> DMSDescribeEventCategoriesResponse:
        client = self._require_client()
        return await self._execute(client.describe_event_categories, request, DMSDescribeEventCategoriesResponse)

    async def describe_event_subscriptions(
        self,
        request: DMSDescribeEventSubscriptionsRequest | None = None,
    ) -> DMSDescribeEventSubscriptionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_event_subscriptions, request, DMSDescribeEventSubscriptionsResponse)

    async def describe_event_subscriptions_paginated(
        self,
        request: DMSDescribeEventSubscriptionsRequest | None = None,
    ) -> list[DMSDescribeEventSubscriptionsResponse]:
        return await self._paginate('describe_event_subscriptions', request, DMSDescribeEventSubscriptionsResponse)

    async def describe_events(
        self,
        request: DMSDescribeEventsRequest | None = None,
    ) -> DMSDescribeEventsResponse:
        client = self._require_client()
        return await self._execute(client.describe_events, request, DMSDescribeEventsResponse)

    async def describe_events_paginated(
        self,
        request: DMSDescribeEventsRequest | None = None,
    ) -> list[DMSDescribeEventsResponse]:
        return await self._paginate('describe_events', request, DMSDescribeEventsResponse)

    async def describe_extension_pack_associations(
        self,
        request: DMSDescribeExtensionPackAssociationsRequest,
    ) -> DMSDescribeExtensionPackAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_extension_pack_associations, request, DMSDescribeExtensionPackAssociationsResponse)

    async def describe_fleet_advisor_collectors(
        self,
        request: DMSDescribeFleetAdvisorCollectorsRequest | None = None,
    ) -> DMSDescribeFleetAdvisorCollectorsResponse:
        client = self._require_client()
        return await self._execute(client.describe_fleet_advisor_collectors, request, DMSDescribeFleetAdvisorCollectorsResponse)

    async def describe_fleet_advisor_databases(
        self,
        request: DMSDescribeFleetAdvisorDatabasesRequest | None = None,
    ) -> DMSDescribeFleetAdvisorDatabasesResponse:
        client = self._require_client()
        return await self._execute(client.describe_fleet_advisor_databases, request, DMSDescribeFleetAdvisorDatabasesResponse)

    async def describe_fleet_advisor_lsa_analysis(
        self,
        request: DMSDescribeFleetAdvisorLsaAnalysisRequest | None = None,
    ) -> DMSDescribeFleetAdvisorLsaAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.describe_fleet_advisor_lsa_analysis, request, DMSDescribeFleetAdvisorLsaAnalysisResponse)

    async def describe_fleet_advisor_schema_object_summary(
        self,
        request: DMSDescribeFleetAdvisorSchemaObjectSummaryRequest | None = None,
    ) -> DMSDescribeFleetAdvisorSchemaObjectSummaryResponse:
        client = self._require_client()
        return await self._execute(client.describe_fleet_advisor_schema_object_summary, request, DMSDescribeFleetAdvisorSchemaObjectSummaryResponse)

    async def describe_fleet_advisor_schemas(
        self,
        request: DMSDescribeFleetAdvisorSchemasRequest | None = None,
    ) -> DMSDescribeFleetAdvisorSchemasResponse:
        client = self._require_client()
        return await self._execute(client.describe_fleet_advisor_schemas, request, DMSDescribeFleetAdvisorSchemasResponse)

    async def describe_instance_profiles(
        self,
        request: DMSDescribeInstanceProfilesRequest | None = None,
    ) -> DMSDescribeInstanceProfilesResponse:
        client = self._require_client()
        return await self._execute(client.describe_instance_profiles, request, DMSDescribeInstanceProfilesResponse)

    async def describe_metadata_model(
        self,
        request: DMSDescribeMetadataModelRequest,
    ) -> DMSDescribeMetadataModelResponse:
        client = self._require_client()
        return await self._execute(client.describe_metadata_model, request, DMSDescribeMetadataModelResponse)

    async def describe_metadata_model_assessments(
        self,
        request: DMSDescribeMetadataModelAssessmentsRequest,
    ) -> DMSDescribeMetadataModelAssessmentsResponse:
        client = self._require_client()
        return await self._execute(client.describe_metadata_model_assessments, request, DMSDescribeMetadataModelAssessmentsResponse)

    async def describe_metadata_model_children(
        self,
        request: DMSDescribeMetadataModelChildrenRequest,
    ) -> DMSDescribeMetadataModelChildrenResponse:
        client = self._require_client()
        return await self._execute(client.describe_metadata_model_children, request, DMSDescribeMetadataModelChildrenResponse)

    async def describe_metadata_model_children_paginated(
        self,
        request: DMSDescribeMetadataModelChildrenRequest,
    ) -> list[DMSDescribeMetadataModelChildrenResponse]:
        return await self._paginate('describe_metadata_model_children', request, DMSDescribeMetadataModelChildrenResponse)

    async def describe_metadata_model_conversions(
        self,
        request: DMSDescribeMetadataModelConversionsRequest,
    ) -> DMSDescribeMetadataModelConversionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_metadata_model_conversions, request, DMSDescribeMetadataModelConversionsResponse)

    async def describe_metadata_model_creations(
        self,
        request: DMSDescribeMetadataModelCreationsRequest,
    ) -> DMSDescribeMetadataModelCreationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_metadata_model_creations, request, DMSDescribeMetadataModelCreationsResponse)

    async def describe_metadata_model_creations_paginated(
        self,
        request: DMSDescribeMetadataModelCreationsRequest,
    ) -> list[DMSDescribeMetadataModelCreationsResponse]:
        return await self._paginate('describe_metadata_model_creations', request, DMSDescribeMetadataModelCreationsResponse)

    async def describe_metadata_model_exports_as_script(
        self,
        request: DMSDescribeMetadataModelExportsAsScriptRequest,
    ) -> DMSDescribeMetadataModelExportsAsScriptResponse:
        client = self._require_client()
        return await self._execute(client.describe_metadata_model_exports_as_script, request, DMSDescribeMetadataModelExportsAsScriptResponse)

    async def describe_metadata_model_exports_to_target(
        self,
        request: DMSDescribeMetadataModelExportsToTargetRequest,
    ) -> DMSDescribeMetadataModelExportsToTargetResponse:
        client = self._require_client()
        return await self._execute(client.describe_metadata_model_exports_to_target, request, DMSDescribeMetadataModelExportsToTargetResponse)

    async def describe_metadata_model_imports(
        self,
        request: DMSDescribeMetadataModelImportsRequest,
    ) -> DMSDescribeMetadataModelImportsResponse:
        client = self._require_client()
        return await self._execute(client.describe_metadata_model_imports, request, DMSDescribeMetadataModelImportsResponse)

    async def describe_migration_projects(
        self,
        request: DMSDescribeMigrationProjectsRequest | None = None,
    ) -> DMSDescribeMigrationProjectsResponse:
        client = self._require_client()
        return await self._execute(client.describe_migration_projects, request, DMSDescribeMigrationProjectsResponse)

    async def describe_orderable_replication_instances(
        self,
        request: DMSDescribeOrderableReplicationInstancesRequest | None = None,
    ) -> DMSDescribeOrderableReplicationInstancesResponse:
        client = self._require_client()
        return await self._execute(client.describe_orderable_replication_instances, request, DMSDescribeOrderableReplicationInstancesResponse)

    async def describe_orderable_replication_instances_paginated(
        self,
        request: DMSDescribeOrderableReplicationInstancesRequest | None = None,
    ) -> list[DMSDescribeOrderableReplicationInstancesResponse]:
        return await self._paginate('describe_orderable_replication_instances', request, DMSDescribeOrderableReplicationInstancesResponse)

    async def describe_pending_maintenance_actions(
        self,
        request: DMSDescribePendingMaintenanceActionsRequest | None = None,
    ) -> DMSDescribePendingMaintenanceActionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_pending_maintenance_actions, request, DMSDescribePendingMaintenanceActionsResponse)

    async def describe_recommendation_limitations(
        self,
        request: DMSDescribeRecommendationLimitationsRequest | None = None,
    ) -> DMSDescribeRecommendationLimitationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_recommendation_limitations, request, DMSDescribeRecommendationLimitationsResponse)

    async def describe_recommendations(
        self,
        request: DMSDescribeRecommendationsRequest | None = None,
    ) -> DMSDescribeRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_recommendations, request, DMSDescribeRecommendationsResponse)

    async def describe_refresh_schemas_status(
        self,
        request: DMSDescribeRefreshSchemasStatusRequest,
    ) -> DMSDescribeRefreshSchemasStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_refresh_schemas_status, request, DMSDescribeRefreshSchemasStatusResponse)

    async def describe_replication_configs(
        self,
        request: DMSDescribeReplicationConfigsRequest | None = None,
    ) -> DMSDescribeReplicationConfigsResponse:
        client = self._require_client()
        return await self._execute(client.describe_replication_configs, request, DMSDescribeReplicationConfigsResponse)

    async def describe_replication_instance_task_logs(
        self,
        request: DMSDescribeReplicationInstanceTaskLogsRequest,
    ) -> DMSDescribeReplicationInstanceTaskLogsResponse:
        client = self._require_client()
        return await self._execute(client.describe_replication_instance_task_logs, request, DMSDescribeReplicationInstanceTaskLogsResponse)

    async def describe_replication_instances(
        self,
        request: DMSDescribeReplicationInstancesRequest | None = None,
    ) -> DMSDescribeReplicationInstancesResponse:
        client = self._require_client()
        return await self._execute(client.describe_replication_instances, request, DMSDescribeReplicationInstancesResponse)

    async def describe_replication_instances_paginated(
        self,
        request: DMSDescribeReplicationInstancesRequest | None = None,
    ) -> list[DMSDescribeReplicationInstancesResponse]:
        return await self._paginate('describe_replication_instances', request, DMSDescribeReplicationInstancesResponse)

    async def describe_replication_subnet_groups(
        self,
        request: DMSDescribeReplicationSubnetGroupsRequest | None = None,
    ) -> DMSDescribeReplicationSubnetGroupsResponse:
        client = self._require_client()
        return await self._execute(client.describe_replication_subnet_groups, request, DMSDescribeReplicationSubnetGroupsResponse)

    async def describe_replication_subnet_groups_paginated(
        self,
        request: DMSDescribeReplicationSubnetGroupsRequest | None = None,
    ) -> list[DMSDescribeReplicationSubnetGroupsResponse]:
        return await self._paginate('describe_replication_subnet_groups', request, DMSDescribeReplicationSubnetGroupsResponse)

    async def describe_replication_table_statistics(
        self,
        request: DMSDescribeReplicationTableStatisticsRequest,
    ) -> DMSDescribeReplicationTableStatisticsResponse:
        client = self._require_client()
        return await self._execute(client.describe_replication_table_statistics, request, DMSDescribeReplicationTableStatisticsResponse)

    async def describe_replication_task_assessment_results(
        self,
        request: DMSDescribeReplicationTaskAssessmentResultsRequest | None = None,
    ) -> DMSDescribeReplicationTaskAssessmentResultsResponse:
        client = self._require_client()
        return await self._execute(client.describe_replication_task_assessment_results, request, DMSDescribeReplicationTaskAssessmentResultsResponse)

    async def describe_replication_task_assessment_results_paginated(
        self,
        request: DMSDescribeReplicationTaskAssessmentResultsRequest | None = None,
    ) -> list[DMSDescribeReplicationTaskAssessmentResultsResponse]:
        return await self._paginate('describe_replication_task_assessment_results', request, DMSDescribeReplicationTaskAssessmentResultsResponse)

    async def describe_replication_task_assessment_runs(
        self,
        request: DMSDescribeReplicationTaskAssessmentRunsRequest | None = None,
    ) -> DMSDescribeReplicationTaskAssessmentRunsResponse:
        client = self._require_client()
        return await self._execute(client.describe_replication_task_assessment_runs, request, DMSDescribeReplicationTaskAssessmentRunsResponse)

    async def describe_replication_task_individual_assessments(
        self,
        request: DMSDescribeReplicationTaskIndividualAssessmentsRequest | None = None,
    ) -> DMSDescribeReplicationTaskIndividualAssessmentsResponse:
        client = self._require_client()
        return await self._execute(client.describe_replication_task_individual_assessments, request, DMSDescribeReplicationTaskIndividualAssessmentsResponse)

    async def describe_replication_tasks(
        self,
        request: DMSDescribeReplicationTasksRequest | None = None,
    ) -> DMSDescribeReplicationTasksResponse:
        client = self._require_client()
        return await self._execute(client.describe_replication_tasks, request, DMSDescribeReplicationTasksResponse)

    async def describe_replication_tasks_paginated(
        self,
        request: DMSDescribeReplicationTasksRequest | None = None,
    ) -> list[DMSDescribeReplicationTasksResponse]:
        return await self._paginate('describe_replication_tasks', request, DMSDescribeReplicationTasksResponse)

    async def describe_replications(
        self,
        request: DMSDescribeReplicationsRequest | None = None,
    ) -> DMSDescribeReplicationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_replications, request, DMSDescribeReplicationsResponse)

    async def describe_schemas(
        self,
        request: DMSDescribeSchemasRequest,
    ) -> DMSDescribeSchemasResponse:
        client = self._require_client()
        return await self._execute(client.describe_schemas, request, DMSDescribeSchemasResponse)

    async def describe_schemas_paginated(
        self,
        request: DMSDescribeSchemasRequest,
    ) -> list[DMSDescribeSchemasResponse]:
        return await self._paginate('describe_schemas', request, DMSDescribeSchemasResponse)

    async def describe_table_statistics(
        self,
        request: DMSDescribeTableStatisticsRequest,
    ) -> DMSDescribeTableStatisticsResponse:
        client = self._require_client()
        return await self._execute(client.describe_table_statistics, request, DMSDescribeTableStatisticsResponse)

    async def describe_table_statistics_paginated(
        self,
        request: DMSDescribeTableStatisticsRequest,
    ) -> list[DMSDescribeTableStatisticsResponse]:
        return await self._paginate('describe_table_statistics', request, DMSDescribeTableStatisticsResponse)

    async def export_metadata_model_assessment(
        self,
        request: DMSExportMetadataModelAssessmentRequest,
    ) -> DMSExportMetadataModelAssessmentResponse:
        client = self._require_client()
        return await self._execute(client.export_metadata_model_assessment, request, DMSExportMetadataModelAssessmentResponse)

    async def get_target_selection_rules(
        self,
        request: DMSGetTargetSelectionRulesRequest,
    ) -> DMSGetTargetSelectionRulesResponse:
        client = self._require_client()
        return await self._execute(client.get_target_selection_rules, request, DMSGetTargetSelectionRulesResponse)

    async def import_certificate(
        self,
        request: DMSImportCertificateRequest,
    ) -> DMSImportCertificateResponse:
        client = self._require_client()
        return await self._execute(client.import_certificate, request, DMSImportCertificateResponse)

    async def list_tags_for_resource(
        self,
        request: DMSListTagsForResourceRequest | None = None,
    ) -> DMSListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, DMSListTagsForResourceResponse)

    async def modify_conversion_configuration(
        self,
        request: DMSModifyConversionConfigurationRequest,
    ) -> DMSModifyConversionConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.modify_conversion_configuration, request, DMSModifyConversionConfigurationResponse)

    async def modify_data_migration(
        self,
        request: DMSModifyDataMigrationRequest,
    ) -> DMSModifyDataMigrationResponse:
        client = self._require_client()
        return await self._execute(client.modify_data_migration, request, DMSModifyDataMigrationResponse)

    async def modify_data_provider(
        self,
        request: DMSModifyDataProviderRequest,
    ) -> DMSModifyDataProviderResponse:
        client = self._require_client()
        return await self._execute(client.modify_data_provider, request, DMSModifyDataProviderResponse)

    async def modify_endpoint(
        self,
        request: DMSModifyEndpointRequest,
    ) -> DMSModifyEndpointResponse:
        client = self._require_client()
        return await self._execute(client.modify_endpoint, request, DMSModifyEndpointResponse)

    async def modify_event_subscription(
        self,
        request: DMSModifyEventSubscriptionRequest,
    ) -> DMSModifyEventSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.modify_event_subscription, request, DMSModifyEventSubscriptionResponse)

    async def modify_instance_profile(
        self,
        request: DMSModifyInstanceProfileRequest,
    ) -> DMSModifyInstanceProfileResponse:
        client = self._require_client()
        return await self._execute(client.modify_instance_profile, request, DMSModifyInstanceProfileResponse)

    async def modify_migration_project(
        self,
        request: DMSModifyMigrationProjectRequest,
    ) -> DMSModifyMigrationProjectResponse:
        client = self._require_client()
        return await self._execute(client.modify_migration_project, request, DMSModifyMigrationProjectResponse)

    async def modify_replication_config(
        self,
        request: DMSModifyReplicationConfigRequest,
    ) -> DMSModifyReplicationConfigResponse:
        client = self._require_client()
        return await self._execute(client.modify_replication_config, request, DMSModifyReplicationConfigResponse)

    async def modify_replication_instance(
        self,
        request: DMSModifyReplicationInstanceRequest,
    ) -> DMSModifyReplicationInstanceResponse:
        client = self._require_client()
        return await self._execute(client.modify_replication_instance, request, DMSModifyReplicationInstanceResponse)

    async def modify_replication_subnet_group(
        self,
        request: DMSModifyReplicationSubnetGroupRequest,
    ) -> DMSModifyReplicationSubnetGroupResponse:
        client = self._require_client()
        return await self._execute(client.modify_replication_subnet_group, request, DMSModifyReplicationSubnetGroupResponse)

    async def modify_replication_task(
        self,
        request: DMSModifyReplicationTaskRequest,
    ) -> DMSModifyReplicationTaskResponse:
        client = self._require_client()
        return await self._execute(client.modify_replication_task, request, DMSModifyReplicationTaskResponse)

    async def move_replication_task(
        self,
        request: DMSMoveReplicationTaskRequest,
    ) -> DMSMoveReplicationTaskResponse:
        client = self._require_client()
        return await self._execute(client.move_replication_task, request, DMSMoveReplicationTaskResponse)

    async def reboot_replication_instance(
        self,
        request: DMSRebootReplicationInstanceRequest,
    ) -> DMSRebootReplicationInstanceResponse:
        client = self._require_client()
        return await self._execute(client.reboot_replication_instance, request, DMSRebootReplicationInstanceResponse)

    async def refresh_schemas(
        self,
        request: DMSRefreshSchemasRequest,
    ) -> DMSRefreshSchemasResponse:
        client = self._require_client()
        return await self._execute(client.refresh_schemas, request, DMSRefreshSchemasResponse)

    async def reload_replication_tables(
        self,
        request: DMSReloadReplicationTablesRequest,
    ) -> DMSReloadReplicationTablesResponse:
        client = self._require_client()
        return await self._execute(client.reload_replication_tables, request, DMSReloadReplicationTablesResponse)

    async def reload_tables(
        self,
        request: DMSReloadTablesRequest,
    ) -> DMSReloadTablesResponse:
        client = self._require_client()
        return await self._execute(client.reload_tables, request, DMSReloadTablesResponse)

    async def remove_tags_from_resource(
        self,
        request: DMSRemoveTagsFromResourceRequest,
    ) -> DMSRemoveTagsFromResourceResponse:
        client = self._require_client()
        return await self._execute(client.remove_tags_from_resource, request, DMSRemoveTagsFromResourceResponse)

    async def run_fleet_advisor_lsa_analysis(
        self,
        request: DMSRunFleetAdvisorLsaAnalysisRequest | None = None,
    ) -> DMSRunFleetAdvisorLsaAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.run_fleet_advisor_lsa_analysis, request, DMSRunFleetAdvisorLsaAnalysisResponse)

    async def start_data_migration(
        self,
        request: DMSStartDataMigrationRequest,
    ) -> DMSStartDataMigrationResponse:
        client = self._require_client()
        return await self._execute(client.start_data_migration, request, DMSStartDataMigrationResponse)

    async def start_extension_pack_association(
        self,
        request: DMSStartExtensionPackAssociationRequest,
    ) -> DMSStartExtensionPackAssociationResponse:
        client = self._require_client()
        return await self._execute(client.start_extension_pack_association, request, DMSStartExtensionPackAssociationResponse)

    async def start_metadata_model_assessment(
        self,
        request: DMSStartMetadataModelAssessmentRequest,
    ) -> DMSStartMetadataModelAssessmentResponse:
        client = self._require_client()
        return await self._execute(client.start_metadata_model_assessment, request, DMSStartMetadataModelAssessmentResponse)

    async def start_metadata_model_conversion(
        self,
        request: DMSStartMetadataModelConversionRequest,
    ) -> DMSStartMetadataModelConversionResponse:
        client = self._require_client()
        return await self._execute(client.start_metadata_model_conversion, request, DMSStartMetadataModelConversionResponse)

    async def start_metadata_model_creation(
        self,
        request: DMSStartMetadataModelCreationRequest,
    ) -> DMSStartMetadataModelCreationResponse:
        client = self._require_client()
        return await self._execute(client.start_metadata_model_creation, request, DMSStartMetadataModelCreationResponse)

    async def start_metadata_model_export_as_script(
        self,
        request: DMSStartMetadataModelExportAsScriptRequest,
    ) -> DMSStartMetadataModelExportAsScriptResponse:
        client = self._require_client()
        return await self._execute(client.start_metadata_model_export_as_script, request, DMSStartMetadataModelExportAsScriptResponse)

    async def start_metadata_model_export_to_target(
        self,
        request: DMSStartMetadataModelExportToTargetRequest,
    ) -> DMSStartMetadataModelExportToTargetResponse:
        client = self._require_client()
        return await self._execute(client.start_metadata_model_export_to_target, request, DMSStartMetadataModelExportToTargetResponse)

    async def start_metadata_model_import(
        self,
        request: DMSStartMetadataModelImportRequest,
    ) -> DMSStartMetadataModelImportResponse:
        client = self._require_client()
        return await self._execute(client.start_metadata_model_import, request, DMSStartMetadataModelImportResponse)

    async def start_recommendations(
        self,
        request: DMSStartRecommendationsRequest,
    ) -> DMSStartRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.start_recommendations, request, DMSStartRecommendationsResponse)

    async def start_replication(
        self,
        request: DMSStartReplicationRequest,
    ) -> DMSStartReplicationResponse:
        client = self._require_client()
        return await self._execute(client.start_replication, request, DMSStartReplicationResponse)

    async def start_replication_task(
        self,
        request: DMSStartReplicationTaskRequest,
    ) -> DMSStartReplicationTaskResponse:
        client = self._require_client()
        return await self._execute(client.start_replication_task, request, DMSStartReplicationTaskResponse)

    async def start_replication_task_assessment(
        self,
        request: DMSStartReplicationTaskAssessmentRequest,
    ) -> DMSStartReplicationTaskAssessmentResponse:
        client = self._require_client()
        return await self._execute(client.start_replication_task_assessment, request, DMSStartReplicationTaskAssessmentResponse)

    async def start_replication_task_assessment_run(
        self,
        request: DMSStartReplicationTaskAssessmentRunRequest,
    ) -> DMSStartReplicationTaskAssessmentRunResponse:
        client = self._require_client()
        return await self._execute(client.start_replication_task_assessment_run, request, DMSStartReplicationTaskAssessmentRunResponse)

    async def stop_data_migration(
        self,
        request: DMSStopDataMigrationRequest,
    ) -> DMSStopDataMigrationResponse:
        client = self._require_client()
        return await self._execute(client.stop_data_migration, request, DMSStopDataMigrationResponse)

    async def stop_replication(
        self,
        request: DMSStopReplicationRequest,
    ) -> DMSStopReplicationResponse:
        client = self._require_client()
        return await self._execute(client.stop_replication, request, DMSStopReplicationResponse)

    async def stop_replication_task(
        self,
        request: DMSStopReplicationTaskRequest,
    ) -> DMSStopReplicationTaskResponse:
        client = self._require_client()
        return await self._execute(client.stop_replication_task, request, DMSStopReplicationTaskResponse)

    async def test_connection(
        self,
        request: DMSTestConnectionRequest,
    ) -> DMSTestConnectionResponse:
        client = self._require_client()
        return await self._execute(client.test_connection, request, DMSTestConnectionResponse)

    async def update_subscriptions_to_event_bridge(
        self,
        request: DMSUpdateSubscriptionsToEventBridgeRequest | None = None,
    ) -> DMSUpdateSubscriptionsToEventBridgeResponse:
        client = self._require_client()
        return await self._execute(client.update_subscriptions_to_event_bridge, request, DMSUpdateSubscriptionsToEventBridgeResponse)
