from werkflow_aws.models.glue import (
    GlueAssociateGlossaryTermsRequest,
    GlueAssociateGlossaryTermsResponse,
    GlueBatchCreatePartitionRequest,
    GlueBatchCreatePartitionResponse,
    GlueBatchDeleteConnectionRequest,
    GlueBatchDeleteConnectionResponse,
    GlueBatchDeletePartitionRequest,
    GlueBatchDeletePartitionResponse,
    GlueBatchDeleteTableRequest,
    GlueBatchDeleteTableResponse,
    GlueBatchDeleteTableVersionRequest,
    GlueBatchDeleteTableVersionResponse,
    GlueBatchGetBlueprintsRequest,
    GlueBatchGetBlueprintsResponse,
    GlueBatchGetCrawlersRequest,
    GlueBatchGetCrawlersResponse,
    GlueBatchGetCustomEntityTypesRequest,
    GlueBatchGetCustomEntityTypesResponse,
    GlueBatchGetDataQualityResultRequest,
    GlueBatchGetDataQualityResultResponse,
    GlueBatchGetDataQualityResultV2Request,
    GlueBatchGetDataQualityResultV2Response,
    GlueBatchGetDataQualityRulesetEvaluationRunRequest,
    GlueBatchGetDataQualityRulesetEvaluationRunResponse,
    GlueBatchGetDevEndpointsRequest,
    GlueBatchGetDevEndpointsResponse,
    GlueBatchGetIterableFormsRequest,
    GlueBatchGetIterableFormsResponse,
    GlueBatchGetJobsRequest,
    GlueBatchGetJobsResponse,
    GlueBatchGetPartitionRequest,
    GlueBatchGetPartitionResponse,
    GlueBatchGetTableOptimizerRequest,
    GlueBatchGetTableOptimizerResponse,
    GlueBatchGetTriggersRequest,
    GlueBatchGetTriggersResponse,
    GlueBatchGetWorkflowsRequest,
    GlueBatchGetWorkflowsResponse,
    GlueBatchPutDataQualityStatisticAnnotationRequest,
    GlueBatchPutDataQualityStatisticAnnotationResponse,
    GlueBatchStopJobRunRequest,
    GlueBatchStopJobRunResponse,
    GlueBatchUpdatePartitionRequest,
    GlueBatchUpdatePartitionResponse,
    GlueCancelDataQualityRuleRecommendationRunRequest,
    GlueCancelDataQualityRuleRecommendationRunResponse,
    GlueCancelDataQualityRulesetEvaluationRunRequest,
    GlueCancelDataQualityRulesetEvaluationRunResponse,
    GlueCancelMLTaskRunRequest,
    GlueCancelMLTaskRunResponse,
    GlueCancelStatementRequest,
    GlueCancelStatementResponse,
    GlueCheckSchemaVersionValidityRequest,
    GlueCheckSchemaVersionValidityResponse,
    GlueCreateBlueprintRequest,
    GlueCreateBlueprintResponse,
    GlueCreateCatalogRequest,
    GlueCreateCatalogResponse,
    GlueCreateClassifierRequest,
    GlueCreateClassifierResponse,
    GlueCreateColumnStatisticsTaskSettingsRequest,
    GlueCreateColumnStatisticsTaskSettingsResponse,
    GlueCreateConnectionRequest,
    GlueCreateConnectionResponse,
    GlueCreateCrawlerRequest,
    GlueCreateCrawlerResponse,
    GlueCreateCustomEntityTypeRequest,
    GlueCreateCustomEntityTypeResponse,
    GlueCreateDataQualityEvaluationConfigRequest,
    GlueCreateDataQualityEvaluationConfigResponse,
    GlueCreateDataQualityRulesetRequest,
    GlueCreateDataQualityRulesetResponse,
    GlueCreateDatabaseRequest,
    GlueCreateDatabaseResponse,
    GlueCreateDevEndpointRequest,
    GlueCreateDevEndpointResponse,
    GlueCreateGlossaryRequest,
    GlueCreateGlossaryResponse,
    GlueCreateGlossaryTermRequest,
    GlueCreateGlossaryTermResponse,
    GlueCreateGlueIdentityCenterConfigurationRequest,
    GlueCreateGlueIdentityCenterConfigurationResponse,
    GlueCreateIntegrationRequest,
    GlueCreateIntegrationResourcePropertyRequest,
    GlueCreateIntegrationResourcePropertyResponse,
    GlueCreateIntegrationResponse,
    GlueCreateIntegrationTablePropertiesRequest,
    GlueCreateIntegrationTablePropertiesResponse,
    GlueCreateJobRequest,
    GlueCreateJobResponse,
    GlueCreateMLTransformRequest,
    GlueCreateMLTransformResponse,
    GlueCreatePartitionIndexRequest,
    GlueCreatePartitionIndexResponse,
    GlueCreatePartitionRequest,
    GlueCreatePartitionResponse,
    GlueCreateRegistryRequest,
    GlueCreateRegistryResponse,
    GlueCreateSchemaRequest,
    GlueCreateSchemaResponse,
    GlueCreateScriptRequest,
    GlueCreateScriptResponse,
    GlueCreateSecurityConfigurationRequest,
    GlueCreateSecurityConfigurationResponse,
    GlueCreateSessionRequest,
    GlueCreateSessionResponse,
    GlueCreateTableOptimizerRequest,
    GlueCreateTableOptimizerResponse,
    GlueCreateTableRequest,
    GlueCreateTableResponse,
    GlueCreateTriggerRequest,
    GlueCreateTriggerResponse,
    GlueCreateUsageProfileRequest,
    GlueCreateUsageProfileResponse,
    GlueCreateUserDefinedFunctionRequest,
    GlueCreateUserDefinedFunctionResponse,
    GlueCreateWorkflowRequest,
    GlueCreateWorkflowResponse,
    GlueDeleteAssetRequest,
    GlueDeleteAssetResponse,
    GlueDeleteAttachmentRequest,
    GlueDeleteAttachmentResponse,
    GlueDeleteBlueprintRequest,
    GlueDeleteBlueprintResponse,
    GlueDeleteCatalogRequest,
    GlueDeleteCatalogResponse,
    GlueDeleteClassifierRequest,
    GlueDeleteClassifierResponse,
    GlueDeleteColumnStatisticsForPartitionRequest,
    GlueDeleteColumnStatisticsForPartitionResponse,
    GlueDeleteColumnStatisticsForTableRequest,
    GlueDeleteColumnStatisticsForTableResponse,
    GlueDeleteColumnStatisticsTaskSettingsRequest,
    GlueDeleteColumnStatisticsTaskSettingsResponse,
    GlueDeleteConnectionRequest,
    GlueDeleteConnectionResponse,
    GlueDeleteConnectionTypeRequest,
    GlueDeleteConnectionTypeResponse,
    GlueDeleteCrawlerRequest,
    GlueDeleteCrawlerResponse,
    GlueDeleteCustomEntityTypeRequest,
    GlueDeleteCustomEntityTypeResponse,
    GlueDeleteDataQualityEvaluationConfigRequest,
    GlueDeleteDataQualityEvaluationConfigResponse,
    GlueDeleteDataQualityRulesetRequest,
    GlueDeleteDataQualityRulesetResponse,
    GlueDeleteDatabaseRequest,
    GlueDeleteDatabaseResponse,
    GlueDeleteDevEndpointRequest,
    GlueDeleteDevEndpointResponse,
    GlueDeleteFormTypeRequest,
    GlueDeleteFormTypeResponse,
    GlueDeleteGlossaryRequest,
    GlueDeleteGlossaryResponse,
    GlueDeleteGlossaryTermRequest,
    GlueDeleteGlossaryTermResponse,
    GlueDeleteGlueIdentityCenterConfigurationRequest,
    GlueDeleteGlueIdentityCenterConfigurationResponse,
    GlueDeleteIntegrationRequest,
    GlueDeleteIntegrationResourcePropertyRequest,
    GlueDeleteIntegrationResourcePropertyResponse,
    GlueDeleteIntegrationResponse,
    GlueDeleteIntegrationTablePropertiesRequest,
    GlueDeleteIntegrationTablePropertiesResponse,
    GlueDeleteJobRequest,
    GlueDeleteJobResponse,
    GlueDeleteMLTransformRequest,
    GlueDeleteMLTransformResponse,
    GlueDeletePartitionIndexRequest,
    GlueDeletePartitionIndexResponse,
    GlueDeletePartitionRequest,
    GlueDeletePartitionResponse,
    GlueDeleteRegistryRequest,
    GlueDeleteRegistryResponse,
    GlueDeleteResourcePolicyRequest,
    GlueDeleteResourcePolicyResponse,
    GlueDeleteSchemaRequest,
    GlueDeleteSchemaResponse,
    GlueDeleteSchemaVersionsRequest,
    GlueDeleteSchemaVersionsResponse,
    GlueDeleteSecurityConfigurationRequest,
    GlueDeleteSecurityConfigurationResponse,
    GlueDeleteSessionRequest,
    GlueDeleteSessionResponse,
    GlueDeleteTableOptimizerRequest,
    GlueDeleteTableOptimizerResponse,
    GlueDeleteTableRequest,
    GlueDeleteTableResponse,
    GlueDeleteTableVersionRequest,
    GlueDeleteTableVersionResponse,
    GlueDeleteTriggerRequest,
    GlueDeleteTriggerResponse,
    GlueDeleteUsageProfileRequest,
    GlueDeleteUsageProfileResponse,
    GlueDeleteUserDefinedFunctionRequest,
    GlueDeleteUserDefinedFunctionResponse,
    GlueDeleteWorkflowRequest,
    GlueDeleteWorkflowResponse,
    GlueDescribeConnectionTypeRequest,
    GlueDescribeConnectionTypeResponse,
    GlueDescribeEntityRequest,
    GlueDescribeEntityResponse,
    GlueDescribeInboundIntegrationsRequest,
    GlueDescribeInboundIntegrationsResponse,
    GlueDescribeIntegrationsRequest,
    GlueDescribeIntegrationsResponse,
    GlueDisassociateGlossaryTermsRequest,
    GlueDisassociateGlossaryTermsResponse,
    GlueGetAssetRequest,
    GlueGetAssetResponse,
    GlueGetAssetTypeRequest,
    GlueGetAssetTypeResponse,
    GlueGetBlueprintRequest,
    GlueGetBlueprintResponse,
    GlueGetBlueprintRunRequest,
    GlueGetBlueprintRunResponse,
    GlueGetBlueprintRunsRequest,
    GlueGetBlueprintRunsResponse,
    GlueGetCatalogImportStatusRequest,
    GlueGetCatalogImportStatusResponse,
    GlueGetCatalogRequest,
    GlueGetCatalogResponse,
    GlueGetCatalogsRequest,
    GlueGetCatalogsResponse,
    GlueGetClassifierRequest,
    GlueGetClassifierResponse,
    GlueGetClassifiersRequest,
    GlueGetClassifiersResponse,
    GlueGetColumnStatisticsForPartitionRequest,
    GlueGetColumnStatisticsForPartitionResponse,
    GlueGetColumnStatisticsForTableRequest,
    GlueGetColumnStatisticsForTableResponse,
    GlueGetColumnStatisticsTaskRunRequest,
    GlueGetColumnStatisticsTaskRunResponse,
    GlueGetColumnStatisticsTaskRunsRequest,
    GlueGetColumnStatisticsTaskRunsResponse,
    GlueGetColumnStatisticsTaskSettingsRequest,
    GlueGetColumnStatisticsTaskSettingsResponse,
    GlueGetConnectionRequest,
    GlueGetConnectionResponse,
    GlueGetConnectionsRequest,
    GlueGetConnectionsResponse,
    GlueGetCrawlerMetricsRequest,
    GlueGetCrawlerMetricsResponse,
    GlueGetCrawlerRequest,
    GlueGetCrawlerResponse,
    GlueGetCrawlersRequest,
    GlueGetCrawlersResponse,
    GlueGetCustomEntityTypeRequest,
    GlueGetCustomEntityTypeResponse,
    GlueGetDashboardUrlRequest,
    GlueGetDashboardUrlResponse,
    GlueGetDataCatalogEncryptionSettingsRequest,
    GlueGetDataCatalogEncryptionSettingsResponse,
    GlueGetDataCatalogExportConfigurationRequest,
    GlueGetDataCatalogExportConfigurationResponse,
    GlueGetDataQualityEvaluationConfigRequest,
    GlueGetDataQualityEvaluationConfigResponse,
    GlueGetDataQualityModelRequest,
    GlueGetDataQualityModelResponse,
    GlueGetDataQualityModelResultRequest,
    GlueGetDataQualityModelResultResponse,
    GlueGetDataQualityResultRequest,
    GlueGetDataQualityResultResponse,
    GlueGetDataQualityResultV2Request,
    GlueGetDataQualityResultV2Response,
    GlueGetDataQualityRuleRecommendationRunRequest,
    GlueGetDataQualityRuleRecommendationRunResponse,
    GlueGetDataQualityRulesetEvaluationRunRequest,
    GlueGetDataQualityRulesetEvaluationRunResponse,
    GlueGetDataQualityRulesetRequest,
    GlueGetDataQualityRulesetResponse,
    GlueGetDatabaseRequest,
    GlueGetDatabaseResponse,
    GlueGetDatabasesRequest,
    GlueGetDatabasesResponse,
    GlueGetDataflowGraphRequest,
    GlueGetDataflowGraphResponse,
    GlueGetDevEndpointRequest,
    GlueGetDevEndpointResponse,
    GlueGetDevEndpointsRequest,
    GlueGetDevEndpointsResponse,
    GlueGetEntityRecordsRequest,
    GlueGetEntityRecordsResponse,
    GlueGetFormTypeRequest,
    GlueGetFormTypeResponse,
    GlueGetGlossaryRequest,
    GlueGetGlossaryResponse,
    GlueGetGlossaryTermRequest,
    GlueGetGlossaryTermResponse,
    GlueGetGlueIdentityCenterConfigurationRequest,
    GlueGetGlueIdentityCenterConfigurationResponse,
    GlueGetIntegrationResourcePropertyRequest,
    GlueGetIntegrationResourcePropertyResponse,
    GlueGetIntegrationTablePropertiesRequest,
    GlueGetIntegrationTablePropertiesResponse,
    GlueGetJobBookmarkRequest,
    GlueGetJobBookmarkResponse,
    GlueGetJobRequest,
    GlueGetJobResponse,
    GlueGetJobRunRequest,
    GlueGetJobRunResponse,
    GlueGetJobRunsRequest,
    GlueGetJobRunsResponse,
    GlueGetJobUpgradeAnalysisRequest,
    GlueGetJobUpgradeAnalysisResponse,
    GlueGetJobsRequest,
    GlueGetJobsResponse,
    GlueGetMLTaskRunRequest,
    GlueGetMLTaskRunResponse,
    GlueGetMLTaskRunsRequest,
    GlueGetMLTaskRunsResponse,
    GlueGetMLTransformRequest,
    GlueGetMLTransformResponse,
    GlueGetMLTransformsRequest,
    GlueGetMLTransformsResponse,
    GlueGetMappingRequest,
    GlueGetMappingResponse,
    GlueGetMaterializedViewRefreshTaskRunRequest,
    GlueGetMaterializedViewRefreshTaskRunResponse,
    GlueGetPartitionIndexesRequest,
    GlueGetPartitionIndexesResponse,
    GlueGetPartitionRequest,
    GlueGetPartitionResponse,
    GlueGetPartitionsRequest,
    GlueGetPartitionsResponse,
    GlueGetPlanRequest,
    GlueGetPlanResponse,
    GlueGetRegistryRequest,
    GlueGetRegistryResponse,
    GlueGetResourcePoliciesRequest,
    GlueGetResourcePoliciesResponse,
    GlueGetResourcePolicyRequest,
    GlueGetResourcePolicyResponse,
    GlueGetSchemaByDefinitionRequest,
    GlueGetSchemaByDefinitionResponse,
    GlueGetSchemaRequest,
    GlueGetSchemaResponse,
    GlueGetSchemaVersionRequest,
    GlueGetSchemaVersionResponse,
    GlueGetSchemaVersionsDiffRequest,
    GlueGetSchemaVersionsDiffResponse,
    GlueGetSecurityConfigurationRequest,
    GlueGetSecurityConfigurationResponse,
    GlueGetSecurityConfigurationsRequest,
    GlueGetSecurityConfigurationsResponse,
    GlueGetSessionEndpointRequest,
    GlueGetSessionEndpointResponse,
    GlueGetSessionRequest,
    GlueGetSessionResponse,
    GlueGetStatementRequest,
    GlueGetStatementResponse,
    GlueGetSystemLogsForJobRunRequest,
    GlueGetSystemLogsForJobRunResponse,
    GlueGetSystemLogsForSessionRequest,
    GlueGetSystemLogsForSessionResponse,
    GlueGetTableOptimizerRequest,
    GlueGetTableOptimizerResponse,
    GlueGetTableRequest,
    GlueGetTableResponse,
    GlueGetTableVersionRequest,
    GlueGetTableVersionResponse,
    GlueGetTableVersionsRequest,
    GlueGetTableVersionsResponse,
    GlueGetTablesRequest,
    GlueGetTablesResponse,
    GlueGetTagsRequest,
    GlueGetTagsResponse,
    GlueGetTriggerRequest,
    GlueGetTriggerResponse,
    GlueGetTriggersRequest,
    GlueGetTriggersResponse,
    GlueGetUnfilteredPartitionMetadataRequest,
    GlueGetUnfilteredPartitionMetadataResponse,
    GlueGetUnfilteredPartitionsMetadataRequest,
    GlueGetUnfilteredPartitionsMetadataResponse,
    GlueGetUnfilteredTableMetadataRequest,
    GlueGetUnfilteredTableMetadataResponse,
    GlueGetUsageProfileRequest,
    GlueGetUsageProfileResponse,
    GlueGetUserDefinedFunctionRequest,
    GlueGetUserDefinedFunctionResponse,
    GlueGetUserDefinedFunctionsRequest,
    GlueGetUserDefinedFunctionsResponse,
    GlueGetWorkflowRequest,
    GlueGetWorkflowResponse,
    GlueGetWorkflowRunPropertiesRequest,
    GlueGetWorkflowRunPropertiesResponse,
    GlueGetWorkflowRunRequest,
    GlueGetWorkflowRunResponse,
    GlueGetWorkflowRunsRequest,
    GlueGetWorkflowRunsResponse,
    GlueImportCatalogToGlueRequest,
    GlueImportCatalogToGlueResponse,
    GlueListAssetTypesRequest,
    GlueListAssetTypesResponse,
    GlueListBlueprintsRequest,
    GlueListBlueprintsResponse,
    GlueListColumnStatisticsTaskRunsRequest,
    GlueListColumnStatisticsTaskRunsResponse,
    GlueListConnectionTypesRequest,
    GlueListConnectionTypesResponse,
    GlueListCrawlersRequest,
    GlueListCrawlersResponse,
    GlueListCrawlsRequest,
    GlueListCrawlsResponse,
    GlueListCustomEntityTypesRequest,
    GlueListCustomEntityTypesResponse,
    GlueListDataQualityEvaluationConfigsRequest,
    GlueListDataQualityEvaluationConfigsResponse,
    GlueListDataQualityResultsRequest,
    GlueListDataQualityResultsResponse,
    GlueListDataQualityResultsV2Request,
    GlueListDataQualityResultsV2Response,
    GlueListDataQualityRuleRecommendationRunsRequest,
    GlueListDataQualityRuleRecommendationRunsResponse,
    GlueListDataQualityRulesetEvaluationRunsRequest,
    GlueListDataQualityRulesetEvaluationRunsResponse,
    GlueListDataQualityRulesetsRequest,
    GlueListDataQualityRulesetsResponse,
    GlueListDataQualityStatisticAnnotationsRequest,
    GlueListDataQualityStatisticAnnotationsResponse,
    GlueListDataQualityStatisticsRequest,
    GlueListDataQualityStatisticsResponse,
    GlueListDevEndpointsRequest,
    GlueListDevEndpointsResponse,
    GlueListEntitiesRequest,
    GlueListEntitiesResponse,
    GlueListFormTypesRequest,
    GlueListFormTypesResponse,
    GlueListGlossariesRequest,
    GlueListGlossariesResponse,
    GlueListGlossaryTermsRequest,
    GlueListGlossaryTermsResponse,
    GlueListIntegrationResourcePropertiesRequest,
    GlueListIntegrationResourcePropertiesResponse,
    GlueListIntegrationTablePropertiesRequest,
    GlueListIntegrationTablePropertiesResponse,
    GlueListIterableFormsRequest,
    GlueListIterableFormsResponse,
    GlueListJobsRequest,
    GlueListJobsResponse,
    GlueListMLTransformsRequest,
    GlueListMLTransformsResponse,
    GlueListMaterializedViewRefreshTaskRunsRequest,
    GlueListMaterializedViewRefreshTaskRunsResponse,
    GlueListRegistriesRequest,
    GlueListRegistriesResponse,
    GlueListSchemaVersionsRequest,
    GlueListSchemaVersionsResponse,
    GlueListSchemasRequest,
    GlueListSchemasResponse,
    GlueListSessionsRequest,
    GlueListSessionsResponse,
    GlueListStatementsRequest,
    GlueListStatementsResponse,
    GlueListTableOptimizerRunsRequest,
    GlueListTableOptimizerRunsResponse,
    GlueListTriggersRequest,
    GlueListTriggersResponse,
    GlueListUsageProfilesRequest,
    GlueListUsageProfilesResponse,
    GlueListWorkflowsRequest,
    GlueListWorkflowsResponse,
    GlueModifyIntegrationRequest,
    GlueModifyIntegrationResponse,
    GluePublishDataQualityResultV2Request,
    GluePublishDataQualityResultV2Response,
    GluePutAssetRequest,
    GluePutAssetResponse,
    GluePutAttachmentRequest,
    GluePutAttachmentResponse,
    GluePutDataCatalogEncryptionSettingsRequest,
    GluePutDataCatalogEncryptionSettingsResponse,
    GluePutDataCatalogExportConfigurationRequest,
    GluePutDataCatalogExportConfigurationResponse,
    GluePutDataQualityProfileAnnotationRequest,
    GluePutDataQualityProfileAnnotationResponse,
    GluePutFormTypeRequest,
    GluePutFormTypeResponse,
    GluePutResourcePolicyRequest,
    GluePutResourcePolicyResponse,
    GluePutSchemaVersionMetadataRequest,
    GluePutSchemaVersionMetadataResponse,
    GluePutWorkflowRunPropertiesRequest,
    GluePutWorkflowRunPropertiesResponse,
    GlueQuerySchemaVersionMetadataRequest,
    GlueQuerySchemaVersionMetadataResponse,
    GlueRegisterConnectionTypeRequest,
    GlueRegisterConnectionTypeResponse,
    GlueRegisterSchemaVersionRequest,
    GlueRegisterSchemaVersionResponse,
    GlueRemoveSchemaVersionMetadataRequest,
    GlueRemoveSchemaVersionMetadataResponse,
    GlueResetJobBookmarkRequest,
    GlueResetJobBookmarkResponse,
    GlueResumeWorkflowRunRequest,
    GlueResumeWorkflowRunResponse,
    GlueRunStatementRequest,
    GlueRunStatementResponse,
    GlueSearchAssetsRequest,
    GlueSearchAssetsResponse,
    GlueSearchTablesRequest,
    GlueSearchTablesResponse,
    GlueStartBlueprintRunRequest,
    GlueStartBlueprintRunResponse,
    GlueStartColumnStatisticsTaskRunRequest,
    GlueStartColumnStatisticsTaskRunResponse,
    GlueStartColumnStatisticsTaskRunScheduleRequest,
    GlueStartColumnStatisticsTaskRunScheduleResponse,
    GlueStartCrawlerRequest,
    GlueStartCrawlerResponse,
    GlueStartCrawlerScheduleRequest,
    GlueStartCrawlerScheduleResponse,
    GlueStartDataQualityRuleRecommendationRunRequest,
    GlueStartDataQualityRuleRecommendationRunResponse,
    GlueStartDataQualityRulesetEvaluationRunRequest,
    GlueStartDataQualityRulesetEvaluationRunResponse,
    GlueStartExportLabelsTaskRunRequest,
    GlueStartExportLabelsTaskRunResponse,
    GlueStartImportLabelsTaskRunRequest,
    GlueStartImportLabelsTaskRunResponse,
    GlueStartJobRunRequest,
    GlueStartJobRunResponse,
    GlueStartJobUpgradeAnalysisRequest,
    GlueStartJobUpgradeAnalysisResponse,
    GlueStartMLEvaluationTaskRunRequest,
    GlueStartMLEvaluationTaskRunResponse,
    GlueStartMLLabelingSetGenerationTaskRunRequest,
    GlueStartMLLabelingSetGenerationTaskRunResponse,
    GlueStartMaterializedViewRefreshTaskRunRequest,
    GlueStartMaterializedViewRefreshTaskRunResponse,
    GlueStartTriggerRequest,
    GlueStartTriggerResponse,
    GlueStartWorkflowRunRequest,
    GlueStartWorkflowRunResponse,
    GlueStopColumnStatisticsTaskRunRequest,
    GlueStopColumnStatisticsTaskRunResponse,
    GlueStopColumnStatisticsTaskRunScheduleRequest,
    GlueStopColumnStatisticsTaskRunScheduleResponse,
    GlueStopCrawlerRequest,
    GlueStopCrawlerResponse,
    GlueStopCrawlerScheduleRequest,
    GlueStopCrawlerScheduleResponse,
    GlueStopJobUpgradeAnalysisRequest,
    GlueStopJobUpgradeAnalysisResponse,
    GlueStopMaterializedViewRefreshTaskRunRequest,
    GlueStopMaterializedViewRefreshTaskRunResponse,
    GlueStopSessionRequest,
    GlueStopSessionResponse,
    GlueStopTriggerRequest,
    GlueStopTriggerResponse,
    GlueStopWorkflowRunRequest,
    GlueStopWorkflowRunResponse,
    GlueTagResourceRequest,
    GlueTagResourceResponse,
    GlueTestConnectionRequest,
    GlueTestConnectionResponse,
    GlueUntagResourceRequest,
    GlueUntagResourceResponse,
    GlueUpdateAssetRequest,
    GlueUpdateAssetResponse,
    GlueUpdateBlueprintRequest,
    GlueUpdateBlueprintResponse,
    GlueUpdateCatalogRequest,
    GlueUpdateCatalogResponse,
    GlueUpdateClassifierRequest,
    GlueUpdateClassifierResponse,
    GlueUpdateColumnStatisticsForPartitionRequest,
    GlueUpdateColumnStatisticsForPartitionResponse,
    GlueUpdateColumnStatisticsForTableRequest,
    GlueUpdateColumnStatisticsForTableResponse,
    GlueUpdateColumnStatisticsTaskSettingsRequest,
    GlueUpdateColumnStatisticsTaskSettingsResponse,
    GlueUpdateConnectionRequest,
    GlueUpdateConnectionResponse,
    GlueUpdateCrawlerRequest,
    GlueUpdateCrawlerResponse,
    GlueUpdateCrawlerScheduleRequest,
    GlueUpdateCrawlerScheduleResponse,
    GlueUpdateDataQualityEvaluationConfigRequest,
    GlueUpdateDataQualityEvaluationConfigResponse,
    GlueUpdateDataQualityRulesetRequest,
    GlueUpdateDataQualityRulesetResponse,
    GlueUpdateDatabaseRequest,
    GlueUpdateDatabaseResponse,
    GlueUpdateDevEndpointRequest,
    GlueUpdateDevEndpointResponse,
    GlueUpdateGlossaryRequest,
    GlueUpdateGlossaryResponse,
    GlueUpdateGlossaryTermRequest,
    GlueUpdateGlossaryTermResponse,
    GlueUpdateGlueIdentityCenterConfigurationRequest,
    GlueUpdateGlueIdentityCenterConfigurationResponse,
    GlueUpdateIntegrationResourcePropertyRequest,
    GlueUpdateIntegrationResourcePropertyResponse,
    GlueUpdateIntegrationTablePropertiesRequest,
    GlueUpdateIntegrationTablePropertiesResponse,
    GlueUpdateJobFromSourceControlRequest,
    GlueUpdateJobFromSourceControlResponse,
    GlueUpdateJobRequest,
    GlueUpdateJobResponse,
    GlueUpdateMLTransformRequest,
    GlueUpdateMLTransformResponse,
    GlueUpdatePartitionRequest,
    GlueUpdatePartitionResponse,
    GlueUpdateRegistryRequest,
    GlueUpdateRegistryResponse,
    GlueUpdateSchemaRequest,
    GlueUpdateSchemaResponse,
    GlueUpdateSourceControlFromJobRequest,
    GlueUpdateSourceControlFromJobResponse,
    GlueUpdateTableOptimizerRequest,
    GlueUpdateTableOptimizerResponse,
    GlueUpdateTableRequest,
    GlueUpdateTableResponse,
    GlueUpdateTriggerRequest,
    GlueUpdateTriggerResponse,
    GlueUpdateUsageProfileRequest,
    GlueUpdateUsageProfileResponse,
    GlueUpdateUserDefinedFunctionRequest,
    GlueUpdateUserDefinedFunctionResponse,
    GlueUpdateWorkflowRequest,
    GlueUpdateWorkflowResponse,
)
from werkflow_aws.types.glue_client import GlueClient
from .base import AWSBaseService


class AWSGlue(AWSBaseService[GlueClient]):
    service_name = 'glue'
    boto3_service_name = 'glue'

    def __init__(self) -> None:
        super().__init__(service_name='glue', boto3_service_name='glue')

    async def associate_glossary_terms(
        self,
        request: GlueAssociateGlossaryTermsRequest,
    ) -> GlueAssociateGlossaryTermsResponse:
        client = self._require_client()
        return await self._execute(client.associate_glossary_terms, request, GlueAssociateGlossaryTermsResponse)

    async def batch_create_partition(
        self,
        request: GlueBatchCreatePartitionRequest,
    ) -> GlueBatchCreatePartitionResponse:
        client = self._require_client()
        return await self._execute(client.batch_create_partition, request, GlueBatchCreatePartitionResponse)

    async def batch_delete_connection(
        self,
        request: GlueBatchDeleteConnectionRequest,
    ) -> GlueBatchDeleteConnectionResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_connection, request, GlueBatchDeleteConnectionResponse)

    async def batch_delete_partition(
        self,
        request: GlueBatchDeletePartitionRequest,
    ) -> GlueBatchDeletePartitionResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_partition, request, GlueBatchDeletePartitionResponse)

    async def batch_delete_table(
        self,
        request: GlueBatchDeleteTableRequest,
    ) -> GlueBatchDeleteTableResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_table, request, GlueBatchDeleteTableResponse)

    async def batch_delete_table_version(
        self,
        request: GlueBatchDeleteTableVersionRequest,
    ) -> GlueBatchDeleteTableVersionResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_table_version, request, GlueBatchDeleteTableVersionResponse)

    async def batch_get_blueprints(
        self,
        request: GlueBatchGetBlueprintsRequest,
    ) -> GlueBatchGetBlueprintsResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_blueprints, request, GlueBatchGetBlueprintsResponse)

    async def batch_get_crawlers(
        self,
        request: GlueBatchGetCrawlersRequest,
    ) -> GlueBatchGetCrawlersResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_crawlers, request, GlueBatchGetCrawlersResponse)

    async def batch_get_custom_entity_types(
        self,
        request: GlueBatchGetCustomEntityTypesRequest,
    ) -> GlueBatchGetCustomEntityTypesResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_custom_entity_types, request, GlueBatchGetCustomEntityTypesResponse)

    async def batch_get_data_quality_result(
        self,
        request: GlueBatchGetDataQualityResultRequest,
    ) -> GlueBatchGetDataQualityResultResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_data_quality_result, request, GlueBatchGetDataQualityResultResponse)

    async def batch_get_data_quality_result_v2(
        self,
        request: GlueBatchGetDataQualityResultV2Request,
    ) -> GlueBatchGetDataQualityResultV2Response:
        client = self._require_client()
        return await self._execute(client.batch_get_data_quality_result_v2, request, GlueBatchGetDataQualityResultV2Response)

    async def batch_get_data_quality_ruleset_evaluation_run(
        self,
        request: GlueBatchGetDataQualityRulesetEvaluationRunRequest,
    ) -> GlueBatchGetDataQualityRulesetEvaluationRunResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_data_quality_ruleset_evaluation_run, request, GlueBatchGetDataQualityRulesetEvaluationRunResponse)

    async def batch_get_dev_endpoints(
        self,
        request: GlueBatchGetDevEndpointsRequest,
    ) -> GlueBatchGetDevEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_dev_endpoints, request, GlueBatchGetDevEndpointsResponse)

    async def batch_get_iterable_forms(
        self,
        request: GlueBatchGetIterableFormsRequest,
    ) -> GlueBatchGetIterableFormsResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_iterable_forms, request, GlueBatchGetIterableFormsResponse)

    async def batch_get_jobs(
        self,
        request: GlueBatchGetJobsRequest,
    ) -> GlueBatchGetJobsResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_jobs, request, GlueBatchGetJobsResponse)

    async def batch_get_partition(
        self,
        request: GlueBatchGetPartitionRequest,
    ) -> GlueBatchGetPartitionResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_partition, request, GlueBatchGetPartitionResponse)

    async def batch_get_table_optimizer(
        self,
        request: GlueBatchGetTableOptimizerRequest,
    ) -> GlueBatchGetTableOptimizerResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_table_optimizer, request, GlueBatchGetTableOptimizerResponse)

    async def batch_get_triggers(
        self,
        request: GlueBatchGetTriggersRequest,
    ) -> GlueBatchGetTriggersResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_triggers, request, GlueBatchGetTriggersResponse)

    async def batch_get_workflows(
        self,
        request: GlueBatchGetWorkflowsRequest,
    ) -> GlueBatchGetWorkflowsResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_workflows, request, GlueBatchGetWorkflowsResponse)

    async def batch_put_data_quality_statistic_annotation(
        self,
        request: GlueBatchPutDataQualityStatisticAnnotationRequest,
    ) -> GlueBatchPutDataQualityStatisticAnnotationResponse:
        client = self._require_client()
        return await self._execute(client.batch_put_data_quality_statistic_annotation, request, GlueBatchPutDataQualityStatisticAnnotationResponse)

    async def batch_stop_job_run(
        self,
        request: GlueBatchStopJobRunRequest,
    ) -> GlueBatchStopJobRunResponse:
        client = self._require_client()
        return await self._execute(client.batch_stop_job_run, request, GlueBatchStopJobRunResponse)

    async def batch_update_partition(
        self,
        request: GlueBatchUpdatePartitionRequest,
    ) -> GlueBatchUpdatePartitionResponse:
        client = self._require_client()
        return await self._execute(client.batch_update_partition, request, GlueBatchUpdatePartitionResponse)

    async def cancel_data_quality_rule_recommendation_run(
        self,
        request: GlueCancelDataQualityRuleRecommendationRunRequest,
    ) -> GlueCancelDataQualityRuleRecommendationRunResponse:
        client = self._require_client()
        return await self._execute(client.cancel_data_quality_rule_recommendation_run, request, GlueCancelDataQualityRuleRecommendationRunResponse)

    async def cancel_data_quality_ruleset_evaluation_run(
        self,
        request: GlueCancelDataQualityRulesetEvaluationRunRequest,
    ) -> GlueCancelDataQualityRulesetEvaluationRunResponse:
        client = self._require_client()
        return await self._execute(client.cancel_data_quality_ruleset_evaluation_run, request, GlueCancelDataQualityRulesetEvaluationRunResponse)

    async def cancel_ml_task_run(
        self,
        request: GlueCancelMLTaskRunRequest,
    ) -> GlueCancelMLTaskRunResponse:
        client = self._require_client()
        return await self._execute(client.cancel_ml_task_run, request, GlueCancelMLTaskRunResponse)

    async def cancel_statement(
        self,
        request: GlueCancelStatementRequest,
    ) -> GlueCancelStatementResponse:
        client = self._require_client()
        return await self._execute(client.cancel_statement, request, GlueCancelStatementResponse)

    async def check_schema_version_validity(
        self,
        request: GlueCheckSchemaVersionValidityRequest,
    ) -> GlueCheckSchemaVersionValidityResponse:
        client = self._require_client()
        return await self._execute(client.check_schema_version_validity, request, GlueCheckSchemaVersionValidityResponse)

    async def create_blueprint(
        self,
        request: GlueCreateBlueprintRequest,
    ) -> GlueCreateBlueprintResponse:
        client = self._require_client()
        return await self._execute(client.create_blueprint, request, GlueCreateBlueprintResponse)

    async def create_catalog(
        self,
        request: GlueCreateCatalogRequest,
    ) -> GlueCreateCatalogResponse:
        client = self._require_client()
        return await self._execute(client.create_catalog, request, GlueCreateCatalogResponse)

    async def create_classifier(
        self,
        request: GlueCreateClassifierRequest | None = None,
    ) -> GlueCreateClassifierResponse:
        client = self._require_client()
        return await self._execute(client.create_classifier, request, GlueCreateClassifierResponse)

    async def create_column_statistics_task_settings(
        self,
        request: GlueCreateColumnStatisticsTaskSettingsRequest,
    ) -> GlueCreateColumnStatisticsTaskSettingsResponse:
        client = self._require_client()
        return await self._execute(client.create_column_statistics_task_settings, request, GlueCreateColumnStatisticsTaskSettingsResponse)

    async def create_connection(
        self,
        request: GlueCreateConnectionRequest,
    ) -> GlueCreateConnectionResponse:
        client = self._require_client()
        return await self._execute(client.create_connection, request, GlueCreateConnectionResponse)

    async def create_crawler(
        self,
        request: GlueCreateCrawlerRequest,
    ) -> GlueCreateCrawlerResponse:
        client = self._require_client()
        return await self._execute(client.create_crawler, request, GlueCreateCrawlerResponse)

    async def create_custom_entity_type(
        self,
        request: GlueCreateCustomEntityTypeRequest,
    ) -> GlueCreateCustomEntityTypeResponse:
        client = self._require_client()
        return await self._execute(client.create_custom_entity_type, request, GlueCreateCustomEntityTypeResponse)

    async def create_data_quality_evaluation_config(
        self,
        request: GlueCreateDataQualityEvaluationConfigRequest,
    ) -> GlueCreateDataQualityEvaluationConfigResponse:
        client = self._require_client()
        return await self._execute(client.create_data_quality_evaluation_config, request, GlueCreateDataQualityEvaluationConfigResponse)

    async def create_data_quality_ruleset(
        self,
        request: GlueCreateDataQualityRulesetRequest,
    ) -> GlueCreateDataQualityRulesetResponse:
        client = self._require_client()
        return await self._execute(client.create_data_quality_ruleset, request, GlueCreateDataQualityRulesetResponse)

    async def create_database(
        self,
        request: GlueCreateDatabaseRequest,
    ) -> GlueCreateDatabaseResponse:
        client = self._require_client()
        return await self._execute(client.create_database, request, GlueCreateDatabaseResponse)

    async def create_dev_endpoint(
        self,
        request: GlueCreateDevEndpointRequest,
    ) -> GlueCreateDevEndpointResponse:
        client = self._require_client()
        return await self._execute(client.create_dev_endpoint, request, GlueCreateDevEndpointResponse)

    async def create_glossary(
        self,
        request: GlueCreateGlossaryRequest,
    ) -> GlueCreateGlossaryResponse:
        client = self._require_client()
        return await self._execute(client.create_glossary, request, GlueCreateGlossaryResponse)

    async def create_glossary_term(
        self,
        request: GlueCreateGlossaryTermRequest,
    ) -> GlueCreateGlossaryTermResponse:
        client = self._require_client()
        return await self._execute(client.create_glossary_term, request, GlueCreateGlossaryTermResponse)

    async def create_glue_identity_center_configuration(
        self,
        request: GlueCreateGlueIdentityCenterConfigurationRequest,
    ) -> GlueCreateGlueIdentityCenterConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_glue_identity_center_configuration, request, GlueCreateGlueIdentityCenterConfigurationResponse)

    async def create_integration(
        self,
        request: GlueCreateIntegrationRequest,
    ) -> GlueCreateIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.create_integration, request, GlueCreateIntegrationResponse)

    async def create_integration_resource_property(
        self,
        request: GlueCreateIntegrationResourcePropertyRequest,
    ) -> GlueCreateIntegrationResourcePropertyResponse:
        client = self._require_client()
        return await self._execute(client.create_integration_resource_property, request, GlueCreateIntegrationResourcePropertyResponse)

    async def create_integration_table_properties(
        self,
        request: GlueCreateIntegrationTablePropertiesRequest,
    ) -> GlueCreateIntegrationTablePropertiesResponse:
        client = self._require_client()
        return await self._execute(client.create_integration_table_properties, request, GlueCreateIntegrationTablePropertiesResponse)

    async def create_job(
        self,
        request: GlueCreateJobRequest,
    ) -> GlueCreateJobResponse:
        client = self._require_client()
        return await self._execute(client.create_job, request, GlueCreateJobResponse)

    async def create_ml_transform(
        self,
        request: GlueCreateMLTransformRequest,
    ) -> GlueCreateMLTransformResponse:
        client = self._require_client()
        return await self._execute(client.create_ml_transform, request, GlueCreateMLTransformResponse)

    async def create_partition(
        self,
        request: GlueCreatePartitionRequest,
    ) -> GlueCreatePartitionResponse:
        client = self._require_client()
        return await self._execute(client.create_partition, request, GlueCreatePartitionResponse)

    async def create_partition_index(
        self,
        request: GlueCreatePartitionIndexRequest,
    ) -> GlueCreatePartitionIndexResponse:
        client = self._require_client()
        return await self._execute(client.create_partition_index, request, GlueCreatePartitionIndexResponse)

    async def create_registry(
        self,
        request: GlueCreateRegistryRequest,
    ) -> GlueCreateRegistryResponse:
        client = self._require_client()
        return await self._execute(client.create_registry, request, GlueCreateRegistryResponse)

    async def create_schema(
        self,
        request: GlueCreateSchemaRequest,
    ) -> GlueCreateSchemaResponse:
        client = self._require_client()
        return await self._execute(client.create_schema, request, GlueCreateSchemaResponse)

    async def create_script(
        self,
        request: GlueCreateScriptRequest | None = None,
    ) -> GlueCreateScriptResponse:
        client = self._require_client()
        return await self._execute(client.create_script, request, GlueCreateScriptResponse)

    async def create_security_configuration(
        self,
        request: GlueCreateSecurityConfigurationRequest,
    ) -> GlueCreateSecurityConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_security_configuration, request, GlueCreateSecurityConfigurationResponse)

    async def create_session(
        self,
        request: GlueCreateSessionRequest,
    ) -> GlueCreateSessionResponse:
        client = self._require_client()
        return await self._execute(client.create_session, request, GlueCreateSessionResponse)

    async def create_table(
        self,
        request: GlueCreateTableRequest,
    ) -> GlueCreateTableResponse:
        client = self._require_client()
        return await self._execute(client.create_table, request, GlueCreateTableResponse)

    async def create_table_optimizer(
        self,
        request: GlueCreateTableOptimizerRequest,
    ) -> GlueCreateTableOptimizerResponse:
        client = self._require_client()
        return await self._execute(client.create_table_optimizer, request, GlueCreateTableOptimizerResponse)

    async def create_trigger(
        self,
        request: GlueCreateTriggerRequest,
    ) -> GlueCreateTriggerResponse:
        client = self._require_client()
        return await self._execute(client.create_trigger, request, GlueCreateTriggerResponse)

    async def create_usage_profile(
        self,
        request: GlueCreateUsageProfileRequest,
    ) -> GlueCreateUsageProfileResponse:
        client = self._require_client()
        return await self._execute(client.create_usage_profile, request, GlueCreateUsageProfileResponse)

    async def create_user_defined_function(
        self,
        request: GlueCreateUserDefinedFunctionRequest,
    ) -> GlueCreateUserDefinedFunctionResponse:
        client = self._require_client()
        return await self._execute(client.create_user_defined_function, request, GlueCreateUserDefinedFunctionResponse)

    async def create_workflow(
        self,
        request: GlueCreateWorkflowRequest,
    ) -> GlueCreateWorkflowResponse:
        client = self._require_client()
        return await self._execute(client.create_workflow, request, GlueCreateWorkflowResponse)

    async def delete_asset(
        self,
        request: GlueDeleteAssetRequest,
    ) -> GlueDeleteAssetResponse:
        client = self._require_client()
        return await self._execute(client.delete_asset, request, GlueDeleteAssetResponse)

    async def delete_attachment(
        self,
        request: GlueDeleteAttachmentRequest,
    ) -> GlueDeleteAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_attachment, request, GlueDeleteAttachmentResponse)

    async def delete_blueprint(
        self,
        request: GlueDeleteBlueprintRequest,
    ) -> GlueDeleteBlueprintResponse:
        client = self._require_client()
        return await self._execute(client.delete_blueprint, request, GlueDeleteBlueprintResponse)

    async def delete_catalog(
        self,
        request: GlueDeleteCatalogRequest,
    ) -> GlueDeleteCatalogResponse:
        client = self._require_client()
        return await self._execute(client.delete_catalog, request, GlueDeleteCatalogResponse)

    async def delete_classifier(
        self,
        request: GlueDeleteClassifierRequest,
    ) -> GlueDeleteClassifierResponse:
        client = self._require_client()
        return await self._execute(client.delete_classifier, request, GlueDeleteClassifierResponse)

    async def delete_column_statistics_for_partition(
        self,
        request: GlueDeleteColumnStatisticsForPartitionRequest,
    ) -> GlueDeleteColumnStatisticsForPartitionResponse:
        client = self._require_client()
        return await self._execute(client.delete_column_statistics_for_partition, request, GlueDeleteColumnStatisticsForPartitionResponse)

    async def delete_column_statistics_for_table(
        self,
        request: GlueDeleteColumnStatisticsForTableRequest,
    ) -> GlueDeleteColumnStatisticsForTableResponse:
        client = self._require_client()
        return await self._execute(client.delete_column_statistics_for_table, request, GlueDeleteColumnStatisticsForTableResponse)

    async def delete_column_statistics_task_settings(
        self,
        request: GlueDeleteColumnStatisticsTaskSettingsRequest,
    ) -> GlueDeleteColumnStatisticsTaskSettingsResponse:
        client = self._require_client()
        return await self._execute(client.delete_column_statistics_task_settings, request, GlueDeleteColumnStatisticsTaskSettingsResponse)

    async def delete_connection(
        self,
        request: GlueDeleteConnectionRequest,
    ) -> GlueDeleteConnectionResponse:
        client = self._require_client()
        return await self._execute(client.delete_connection, request, GlueDeleteConnectionResponse)

    async def delete_connection_type(
        self,
        request: GlueDeleteConnectionTypeRequest,
    ) -> GlueDeleteConnectionTypeResponse:
        client = self._require_client()
        return await self._execute(client.delete_connection_type, request, GlueDeleteConnectionTypeResponse)

    async def delete_crawler(
        self,
        request: GlueDeleteCrawlerRequest,
    ) -> GlueDeleteCrawlerResponse:
        client = self._require_client()
        return await self._execute(client.delete_crawler, request, GlueDeleteCrawlerResponse)

    async def delete_custom_entity_type(
        self,
        request: GlueDeleteCustomEntityTypeRequest,
    ) -> GlueDeleteCustomEntityTypeResponse:
        client = self._require_client()
        return await self._execute(client.delete_custom_entity_type, request, GlueDeleteCustomEntityTypeResponse)

    async def delete_data_quality_evaluation_config(
        self,
        request: GlueDeleteDataQualityEvaluationConfigRequest,
    ) -> GlueDeleteDataQualityEvaluationConfigResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_quality_evaluation_config, request, GlueDeleteDataQualityEvaluationConfigResponse)

    async def delete_data_quality_ruleset(
        self,
        request: GlueDeleteDataQualityRulesetRequest,
    ) -> GlueDeleteDataQualityRulesetResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_quality_ruleset, request, GlueDeleteDataQualityRulesetResponse)

    async def delete_database(
        self,
        request: GlueDeleteDatabaseRequest,
    ) -> GlueDeleteDatabaseResponse:
        client = self._require_client()
        return await self._execute(client.delete_database, request, GlueDeleteDatabaseResponse)

    async def delete_dev_endpoint(
        self,
        request: GlueDeleteDevEndpointRequest,
    ) -> GlueDeleteDevEndpointResponse:
        client = self._require_client()
        return await self._execute(client.delete_dev_endpoint, request, GlueDeleteDevEndpointResponse)

    async def delete_form_type(
        self,
        request: GlueDeleteFormTypeRequest,
    ) -> GlueDeleteFormTypeResponse:
        client = self._require_client()
        return await self._execute(client.delete_form_type, request, GlueDeleteFormTypeResponse)

    async def delete_glossary(
        self,
        request: GlueDeleteGlossaryRequest,
    ) -> GlueDeleteGlossaryResponse:
        client = self._require_client()
        return await self._execute(client.delete_glossary, request, GlueDeleteGlossaryResponse)

    async def delete_glossary_term(
        self,
        request: GlueDeleteGlossaryTermRequest,
    ) -> GlueDeleteGlossaryTermResponse:
        client = self._require_client()
        return await self._execute(client.delete_glossary_term, request, GlueDeleteGlossaryTermResponse)

    async def delete_glue_identity_center_configuration(
        self,
        request: GlueDeleteGlueIdentityCenterConfigurationRequest | None = None,
    ) -> GlueDeleteGlueIdentityCenterConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_glue_identity_center_configuration, request, GlueDeleteGlueIdentityCenterConfigurationResponse)

    async def delete_integration(
        self,
        request: GlueDeleteIntegrationRequest,
    ) -> GlueDeleteIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.delete_integration, request, GlueDeleteIntegrationResponse)

    async def delete_integration_resource_property(
        self,
        request: GlueDeleteIntegrationResourcePropertyRequest,
    ) -> GlueDeleteIntegrationResourcePropertyResponse:
        client = self._require_client()
        return await self._execute(client.delete_integration_resource_property, request, GlueDeleteIntegrationResourcePropertyResponse)

    async def delete_integration_table_properties(
        self,
        request: GlueDeleteIntegrationTablePropertiesRequest,
    ) -> GlueDeleteIntegrationTablePropertiesResponse:
        client = self._require_client()
        return await self._execute(client.delete_integration_table_properties, request, GlueDeleteIntegrationTablePropertiesResponse)

    async def delete_job(
        self,
        request: GlueDeleteJobRequest,
    ) -> GlueDeleteJobResponse:
        client = self._require_client()
        return await self._execute(client.delete_job, request, GlueDeleteJobResponse)

    async def delete_ml_transform(
        self,
        request: GlueDeleteMLTransformRequest,
    ) -> GlueDeleteMLTransformResponse:
        client = self._require_client()
        return await self._execute(client.delete_ml_transform, request, GlueDeleteMLTransformResponse)

    async def delete_partition(
        self,
        request: GlueDeletePartitionRequest,
    ) -> GlueDeletePartitionResponse:
        client = self._require_client()
        return await self._execute(client.delete_partition, request, GlueDeletePartitionResponse)

    async def delete_partition_index(
        self,
        request: GlueDeletePartitionIndexRequest,
    ) -> GlueDeletePartitionIndexResponse:
        client = self._require_client()
        return await self._execute(client.delete_partition_index, request, GlueDeletePartitionIndexResponse)

    async def delete_registry(
        self,
        request: GlueDeleteRegistryRequest,
    ) -> GlueDeleteRegistryResponse:
        client = self._require_client()
        return await self._execute(client.delete_registry, request, GlueDeleteRegistryResponse)

    async def delete_resource_policy(
        self,
        request: GlueDeleteResourcePolicyRequest | None = None,
    ) -> GlueDeleteResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_policy, request, GlueDeleteResourcePolicyResponse)

    async def delete_schema(
        self,
        request: GlueDeleteSchemaRequest,
    ) -> GlueDeleteSchemaResponse:
        client = self._require_client()
        return await self._execute(client.delete_schema, request, GlueDeleteSchemaResponse)

    async def delete_schema_versions(
        self,
        request: GlueDeleteSchemaVersionsRequest,
    ) -> GlueDeleteSchemaVersionsResponse:
        client = self._require_client()
        return await self._execute(client.delete_schema_versions, request, GlueDeleteSchemaVersionsResponse)

    async def delete_security_configuration(
        self,
        request: GlueDeleteSecurityConfigurationRequest,
    ) -> GlueDeleteSecurityConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_security_configuration, request, GlueDeleteSecurityConfigurationResponse)

    async def delete_session(
        self,
        request: GlueDeleteSessionRequest,
    ) -> GlueDeleteSessionResponse:
        client = self._require_client()
        return await self._execute(client.delete_session, request, GlueDeleteSessionResponse)

    async def delete_table(
        self,
        request: GlueDeleteTableRequest,
    ) -> GlueDeleteTableResponse:
        client = self._require_client()
        return await self._execute(client.delete_table, request, GlueDeleteTableResponse)

    async def delete_table_optimizer(
        self,
        request: GlueDeleteTableOptimizerRequest,
    ) -> GlueDeleteTableOptimizerResponse:
        client = self._require_client()
        return await self._execute(client.delete_table_optimizer, request, GlueDeleteTableOptimizerResponse)

    async def delete_table_version(
        self,
        request: GlueDeleteTableVersionRequest,
    ) -> GlueDeleteTableVersionResponse:
        client = self._require_client()
        return await self._execute(client.delete_table_version, request, GlueDeleteTableVersionResponse)

    async def delete_trigger(
        self,
        request: GlueDeleteTriggerRequest,
    ) -> GlueDeleteTriggerResponse:
        client = self._require_client()
        return await self._execute(client.delete_trigger, request, GlueDeleteTriggerResponse)

    async def delete_usage_profile(
        self,
        request: GlueDeleteUsageProfileRequest,
    ) -> GlueDeleteUsageProfileResponse:
        client = self._require_client()
        return await self._execute(client.delete_usage_profile, request, GlueDeleteUsageProfileResponse)

    async def delete_user_defined_function(
        self,
        request: GlueDeleteUserDefinedFunctionRequest,
    ) -> GlueDeleteUserDefinedFunctionResponse:
        client = self._require_client()
        return await self._execute(client.delete_user_defined_function, request, GlueDeleteUserDefinedFunctionResponse)

    async def delete_workflow(
        self,
        request: GlueDeleteWorkflowRequest,
    ) -> GlueDeleteWorkflowResponse:
        client = self._require_client()
        return await self._execute(client.delete_workflow, request, GlueDeleteWorkflowResponse)

    async def describe_connection_type(
        self,
        request: GlueDescribeConnectionTypeRequest,
    ) -> GlueDescribeConnectionTypeResponse:
        client = self._require_client()
        return await self._execute(client.describe_connection_type, request, GlueDescribeConnectionTypeResponse)

    async def describe_entity(
        self,
        request: GlueDescribeEntityRequest,
    ) -> GlueDescribeEntityResponse:
        client = self._require_client()
        return await self._execute(client.describe_entity, request, GlueDescribeEntityResponse)

    async def describe_entity_paginated(
        self,
        request: GlueDescribeEntityRequest,
    ) -> list[GlueDescribeEntityResponse]:
        return await self._paginate('describe_entity', request, GlueDescribeEntityResponse)

    async def describe_inbound_integrations(
        self,
        request: GlueDescribeInboundIntegrationsRequest | None = None,
    ) -> GlueDescribeInboundIntegrationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_inbound_integrations, request, GlueDescribeInboundIntegrationsResponse)

    async def describe_integrations(
        self,
        request: GlueDescribeIntegrationsRequest | None = None,
    ) -> GlueDescribeIntegrationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_integrations, request, GlueDescribeIntegrationsResponse)

    async def disassociate_glossary_terms(
        self,
        request: GlueDisassociateGlossaryTermsRequest,
    ) -> GlueDisassociateGlossaryTermsResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_glossary_terms, request, GlueDisassociateGlossaryTermsResponse)

    async def get_asset(
        self,
        request: GlueGetAssetRequest,
    ) -> GlueGetAssetResponse:
        client = self._require_client()
        return await self._execute(client.get_asset, request, GlueGetAssetResponse)

    async def get_asset_type(
        self,
        request: GlueGetAssetTypeRequest,
    ) -> GlueGetAssetTypeResponse:
        client = self._require_client()
        return await self._execute(client.get_asset_type, request, GlueGetAssetTypeResponse)

    async def get_blueprint(
        self,
        request: GlueGetBlueprintRequest,
    ) -> GlueGetBlueprintResponse:
        client = self._require_client()
        return await self._execute(client.get_blueprint, request, GlueGetBlueprintResponse)

    async def get_blueprint_run(
        self,
        request: GlueGetBlueprintRunRequest,
    ) -> GlueGetBlueprintRunResponse:
        client = self._require_client()
        return await self._execute(client.get_blueprint_run, request, GlueGetBlueprintRunResponse)

    async def get_blueprint_runs(
        self,
        request: GlueGetBlueprintRunsRequest,
    ) -> GlueGetBlueprintRunsResponse:
        client = self._require_client()
        return await self._execute(client.get_blueprint_runs, request, GlueGetBlueprintRunsResponse)

    async def get_catalog(
        self,
        request: GlueGetCatalogRequest,
    ) -> GlueGetCatalogResponse:
        client = self._require_client()
        return await self._execute(client.get_catalog, request, GlueGetCatalogResponse)

    async def get_catalog_import_status(
        self,
        request: GlueGetCatalogImportStatusRequest | None = None,
    ) -> GlueGetCatalogImportStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_catalog_import_status, request, GlueGetCatalogImportStatusResponse)

    async def get_catalogs(
        self,
        request: GlueGetCatalogsRequest | None = None,
    ) -> GlueGetCatalogsResponse:
        client = self._require_client()
        return await self._execute(client.get_catalogs, request, GlueGetCatalogsResponse)

    async def get_classifier(
        self,
        request: GlueGetClassifierRequest,
    ) -> GlueGetClassifierResponse:
        client = self._require_client()
        return await self._execute(client.get_classifier, request, GlueGetClassifierResponse)

    async def get_classifiers(
        self,
        request: GlueGetClassifiersRequest | None = None,
    ) -> GlueGetClassifiersResponse:
        client = self._require_client()
        return await self._execute(client.get_classifiers, request, GlueGetClassifiersResponse)

    async def get_classifiers_paginated(
        self,
        request: GlueGetClassifiersRequest | None = None,
    ) -> list[GlueGetClassifiersResponse]:
        return await self._paginate('get_classifiers', request, GlueGetClassifiersResponse)

    async def get_column_statistics_for_partition(
        self,
        request: GlueGetColumnStatisticsForPartitionRequest,
    ) -> GlueGetColumnStatisticsForPartitionResponse:
        client = self._require_client()
        return await self._execute(client.get_column_statistics_for_partition, request, GlueGetColumnStatisticsForPartitionResponse)

    async def get_column_statistics_for_table(
        self,
        request: GlueGetColumnStatisticsForTableRequest,
    ) -> GlueGetColumnStatisticsForTableResponse:
        client = self._require_client()
        return await self._execute(client.get_column_statistics_for_table, request, GlueGetColumnStatisticsForTableResponse)

    async def get_column_statistics_task_run(
        self,
        request: GlueGetColumnStatisticsTaskRunRequest,
    ) -> GlueGetColumnStatisticsTaskRunResponse:
        client = self._require_client()
        return await self._execute(client.get_column_statistics_task_run, request, GlueGetColumnStatisticsTaskRunResponse)

    async def get_column_statistics_task_runs(
        self,
        request: GlueGetColumnStatisticsTaskRunsRequest,
    ) -> GlueGetColumnStatisticsTaskRunsResponse:
        client = self._require_client()
        return await self._execute(client.get_column_statistics_task_runs, request, GlueGetColumnStatisticsTaskRunsResponse)

    async def get_column_statistics_task_settings(
        self,
        request: GlueGetColumnStatisticsTaskSettingsRequest,
    ) -> GlueGetColumnStatisticsTaskSettingsResponse:
        client = self._require_client()
        return await self._execute(client.get_column_statistics_task_settings, request, GlueGetColumnStatisticsTaskSettingsResponse)

    async def get_connection(
        self,
        request: GlueGetConnectionRequest,
    ) -> GlueGetConnectionResponse:
        client = self._require_client()
        return await self._execute(client.get_connection, request, GlueGetConnectionResponse)

    async def get_connections(
        self,
        request: GlueGetConnectionsRequest | None = None,
    ) -> GlueGetConnectionsResponse:
        client = self._require_client()
        return await self._execute(client.get_connections, request, GlueGetConnectionsResponse)

    async def get_connections_paginated(
        self,
        request: GlueGetConnectionsRequest | None = None,
    ) -> list[GlueGetConnectionsResponse]:
        return await self._paginate('get_connections', request, GlueGetConnectionsResponse)

    async def get_crawler(
        self,
        request: GlueGetCrawlerRequest,
    ) -> GlueGetCrawlerResponse:
        client = self._require_client()
        return await self._execute(client.get_crawler, request, GlueGetCrawlerResponse)

    async def get_crawler_metrics(
        self,
        request: GlueGetCrawlerMetricsRequest | None = None,
    ) -> GlueGetCrawlerMetricsResponse:
        client = self._require_client()
        return await self._execute(client.get_crawler_metrics, request, GlueGetCrawlerMetricsResponse)

    async def get_crawler_metrics_paginated(
        self,
        request: GlueGetCrawlerMetricsRequest | None = None,
    ) -> list[GlueGetCrawlerMetricsResponse]:
        return await self._paginate('get_crawler_metrics', request, GlueGetCrawlerMetricsResponse)

    async def get_crawlers(
        self,
        request: GlueGetCrawlersRequest | None = None,
    ) -> GlueGetCrawlersResponse:
        client = self._require_client()
        return await self._execute(client.get_crawlers, request, GlueGetCrawlersResponse)

    async def get_crawlers_paginated(
        self,
        request: GlueGetCrawlersRequest | None = None,
    ) -> list[GlueGetCrawlersResponse]:
        return await self._paginate('get_crawlers', request, GlueGetCrawlersResponse)

    async def get_custom_entity_type(
        self,
        request: GlueGetCustomEntityTypeRequest,
    ) -> GlueGetCustomEntityTypeResponse:
        client = self._require_client()
        return await self._execute(client.get_custom_entity_type, request, GlueGetCustomEntityTypeResponse)

    async def get_dashboard_url(
        self,
        request: GlueGetDashboardUrlRequest,
    ) -> GlueGetDashboardUrlResponse:
        client = self._require_client()
        return await self._execute(client.get_dashboard_url, request, GlueGetDashboardUrlResponse)

    async def get_data_catalog_encryption_settings(
        self,
        request: GlueGetDataCatalogEncryptionSettingsRequest | None = None,
    ) -> GlueGetDataCatalogEncryptionSettingsResponse:
        client = self._require_client()
        return await self._execute(client.get_data_catalog_encryption_settings, request, GlueGetDataCatalogEncryptionSettingsResponse)

    async def get_data_catalog_export_configuration(
        self,
        request: GlueGetDataCatalogExportConfigurationRequest | None = None,
    ) -> GlueGetDataCatalogExportConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_data_catalog_export_configuration, request, GlueGetDataCatalogExportConfigurationResponse)

    async def get_data_quality_evaluation_config(
        self,
        request: GlueGetDataQualityEvaluationConfigRequest,
    ) -> GlueGetDataQualityEvaluationConfigResponse:
        client = self._require_client()
        return await self._execute(client.get_data_quality_evaluation_config, request, GlueGetDataQualityEvaluationConfigResponse)

    async def get_data_quality_model(
        self,
        request: GlueGetDataQualityModelRequest,
    ) -> GlueGetDataQualityModelResponse:
        client = self._require_client()
        return await self._execute(client.get_data_quality_model, request, GlueGetDataQualityModelResponse)

    async def get_data_quality_model_result(
        self,
        request: GlueGetDataQualityModelResultRequest,
    ) -> GlueGetDataQualityModelResultResponse:
        client = self._require_client()
        return await self._execute(client.get_data_quality_model_result, request, GlueGetDataQualityModelResultResponse)

    async def get_data_quality_result(
        self,
        request: GlueGetDataQualityResultRequest,
    ) -> GlueGetDataQualityResultResponse:
        client = self._require_client()
        return await self._execute(client.get_data_quality_result, request, GlueGetDataQualityResultResponse)

    async def get_data_quality_result_v2(
        self,
        request: GlueGetDataQualityResultV2Request,
    ) -> GlueGetDataQualityResultV2Response:
        client = self._require_client()
        return await self._execute(client.get_data_quality_result_v2, request, GlueGetDataQualityResultV2Response)

    async def get_data_quality_rule_recommendation_run(
        self,
        request: GlueGetDataQualityRuleRecommendationRunRequest,
    ) -> GlueGetDataQualityRuleRecommendationRunResponse:
        client = self._require_client()
        return await self._execute(client.get_data_quality_rule_recommendation_run, request, GlueGetDataQualityRuleRecommendationRunResponse)

    async def get_data_quality_ruleset(
        self,
        request: GlueGetDataQualityRulesetRequest,
    ) -> GlueGetDataQualityRulesetResponse:
        client = self._require_client()
        return await self._execute(client.get_data_quality_ruleset, request, GlueGetDataQualityRulesetResponse)

    async def get_data_quality_ruleset_evaluation_run(
        self,
        request: GlueGetDataQualityRulesetEvaluationRunRequest,
    ) -> GlueGetDataQualityRulesetEvaluationRunResponse:
        client = self._require_client()
        return await self._execute(client.get_data_quality_ruleset_evaluation_run, request, GlueGetDataQualityRulesetEvaluationRunResponse)

    async def get_database(
        self,
        request: GlueGetDatabaseRequest,
    ) -> GlueGetDatabaseResponse:
        client = self._require_client()
        return await self._execute(client.get_database, request, GlueGetDatabaseResponse)

    async def get_databases(
        self,
        request: GlueGetDatabasesRequest | None = None,
    ) -> GlueGetDatabasesResponse:
        client = self._require_client()
        return await self._execute(client.get_databases, request, GlueGetDatabasesResponse)

    async def get_databases_paginated(
        self,
        request: GlueGetDatabasesRequest | None = None,
    ) -> list[GlueGetDatabasesResponse]:
        return await self._paginate('get_databases', request, GlueGetDatabasesResponse)

    async def get_dataflow_graph(
        self,
        request: GlueGetDataflowGraphRequest | None = None,
    ) -> GlueGetDataflowGraphResponse:
        client = self._require_client()
        return await self._execute(client.get_dataflow_graph, request, GlueGetDataflowGraphResponse)

    async def get_dev_endpoint(
        self,
        request: GlueGetDevEndpointRequest,
    ) -> GlueGetDevEndpointResponse:
        client = self._require_client()
        return await self._execute(client.get_dev_endpoint, request, GlueGetDevEndpointResponse)

    async def get_dev_endpoints(
        self,
        request: GlueGetDevEndpointsRequest | None = None,
    ) -> GlueGetDevEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.get_dev_endpoints, request, GlueGetDevEndpointsResponse)

    async def get_dev_endpoints_paginated(
        self,
        request: GlueGetDevEndpointsRequest | None = None,
    ) -> list[GlueGetDevEndpointsResponse]:
        return await self._paginate('get_dev_endpoints', request, GlueGetDevEndpointsResponse)

    async def get_entity_records(
        self,
        request: GlueGetEntityRecordsRequest,
    ) -> GlueGetEntityRecordsResponse:
        client = self._require_client()
        return await self._execute(client.get_entity_records, request, GlueGetEntityRecordsResponse)

    async def get_form_type(
        self,
        request: GlueGetFormTypeRequest,
    ) -> GlueGetFormTypeResponse:
        client = self._require_client()
        return await self._execute(client.get_form_type, request, GlueGetFormTypeResponse)

    async def get_glossary(
        self,
        request: GlueGetGlossaryRequest,
    ) -> GlueGetGlossaryResponse:
        client = self._require_client()
        return await self._execute(client.get_glossary, request, GlueGetGlossaryResponse)

    async def get_glossary_term(
        self,
        request: GlueGetGlossaryTermRequest,
    ) -> GlueGetGlossaryTermResponse:
        client = self._require_client()
        return await self._execute(client.get_glossary_term, request, GlueGetGlossaryTermResponse)

    async def get_glue_identity_center_configuration(
        self,
        request: GlueGetGlueIdentityCenterConfigurationRequest | None = None,
    ) -> GlueGetGlueIdentityCenterConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_glue_identity_center_configuration, request, GlueGetGlueIdentityCenterConfigurationResponse)

    async def get_integration_resource_property(
        self,
        request: GlueGetIntegrationResourcePropertyRequest,
    ) -> GlueGetIntegrationResourcePropertyResponse:
        client = self._require_client()
        return await self._execute(client.get_integration_resource_property, request, GlueGetIntegrationResourcePropertyResponse)

    async def get_integration_table_properties(
        self,
        request: GlueGetIntegrationTablePropertiesRequest,
    ) -> GlueGetIntegrationTablePropertiesResponse:
        client = self._require_client()
        return await self._execute(client.get_integration_table_properties, request, GlueGetIntegrationTablePropertiesResponse)

    async def get_job(
        self,
        request: GlueGetJobRequest,
    ) -> GlueGetJobResponse:
        client = self._require_client()
        return await self._execute(client.get_job, request, GlueGetJobResponse)

    async def get_job_bookmark(
        self,
        request: GlueGetJobBookmarkRequest,
    ) -> GlueGetJobBookmarkResponse:
        client = self._require_client()
        return await self._execute(client.get_job_bookmark, request, GlueGetJobBookmarkResponse)

    async def get_job_run(
        self,
        request: GlueGetJobRunRequest,
    ) -> GlueGetJobRunResponse:
        client = self._require_client()
        return await self._execute(client.get_job_run, request, GlueGetJobRunResponse)

    async def get_job_runs(
        self,
        request: GlueGetJobRunsRequest,
    ) -> GlueGetJobRunsResponse:
        client = self._require_client()
        return await self._execute(client.get_job_runs, request, GlueGetJobRunsResponse)

    async def get_job_runs_paginated(
        self,
        request: GlueGetJobRunsRequest,
    ) -> list[GlueGetJobRunsResponse]:
        return await self._paginate('get_job_runs', request, GlueGetJobRunsResponse)

    async def get_job_upgrade_analysis(
        self,
        request: GlueGetJobUpgradeAnalysisRequest,
    ) -> GlueGetJobUpgradeAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.get_job_upgrade_analysis, request, GlueGetJobUpgradeAnalysisResponse)

    async def get_jobs(
        self,
        request: GlueGetJobsRequest | None = None,
    ) -> GlueGetJobsResponse:
        client = self._require_client()
        return await self._execute(client.get_jobs, request, GlueGetJobsResponse)

    async def get_jobs_paginated(
        self,
        request: GlueGetJobsRequest | None = None,
    ) -> list[GlueGetJobsResponse]:
        return await self._paginate('get_jobs', request, GlueGetJobsResponse)

    async def get_ml_task_run(
        self,
        request: GlueGetMLTaskRunRequest,
    ) -> GlueGetMLTaskRunResponse:
        client = self._require_client()
        return await self._execute(client.get_ml_task_run, request, GlueGetMLTaskRunResponse)

    async def get_ml_task_runs(
        self,
        request: GlueGetMLTaskRunsRequest,
    ) -> GlueGetMLTaskRunsResponse:
        client = self._require_client()
        return await self._execute(client.get_ml_task_runs, request, GlueGetMLTaskRunsResponse)

    async def get_ml_transform(
        self,
        request: GlueGetMLTransformRequest,
    ) -> GlueGetMLTransformResponse:
        client = self._require_client()
        return await self._execute(client.get_ml_transform, request, GlueGetMLTransformResponse)

    async def get_ml_transforms(
        self,
        request: GlueGetMLTransformsRequest | None = None,
    ) -> GlueGetMLTransformsResponse:
        client = self._require_client()
        return await self._execute(client.get_ml_transforms, request, GlueGetMLTransformsResponse)

    async def get_mapping(
        self,
        request: GlueGetMappingRequest,
    ) -> GlueGetMappingResponse:
        client = self._require_client()
        return await self._execute(client.get_mapping, request, GlueGetMappingResponse)

    async def get_materialized_view_refresh_task_run(
        self,
        request: GlueGetMaterializedViewRefreshTaskRunRequest,
    ) -> GlueGetMaterializedViewRefreshTaskRunResponse:
        client = self._require_client()
        return await self._execute(client.get_materialized_view_refresh_task_run, request, GlueGetMaterializedViewRefreshTaskRunResponse)

    async def get_partition(
        self,
        request: GlueGetPartitionRequest,
    ) -> GlueGetPartitionResponse:
        client = self._require_client()
        return await self._execute(client.get_partition, request, GlueGetPartitionResponse)

    async def get_partition_indexes(
        self,
        request: GlueGetPartitionIndexesRequest,
    ) -> GlueGetPartitionIndexesResponse:
        client = self._require_client()
        return await self._execute(client.get_partition_indexes, request, GlueGetPartitionIndexesResponse)

    async def get_partition_indexes_paginated(
        self,
        request: GlueGetPartitionIndexesRequest,
    ) -> list[GlueGetPartitionIndexesResponse]:
        return await self._paginate('get_partition_indexes', request, GlueGetPartitionIndexesResponse)

    async def get_partitions(
        self,
        request: GlueGetPartitionsRequest,
    ) -> GlueGetPartitionsResponse:
        client = self._require_client()
        return await self._execute(client.get_partitions, request, GlueGetPartitionsResponse)

    async def get_partitions_paginated(
        self,
        request: GlueGetPartitionsRequest,
    ) -> list[GlueGetPartitionsResponse]:
        return await self._paginate('get_partitions', request, GlueGetPartitionsResponse)

    async def get_plan(
        self,
        request: GlueGetPlanRequest,
    ) -> GlueGetPlanResponse:
        client = self._require_client()
        return await self._execute(client.get_plan, request, GlueGetPlanResponse)

    async def get_registry(
        self,
        request: GlueGetRegistryRequest,
    ) -> GlueGetRegistryResponse:
        client = self._require_client()
        return await self._execute(client.get_registry, request, GlueGetRegistryResponse)

    async def get_resource_policies(
        self,
        request: GlueGetResourcePoliciesRequest | None = None,
    ) -> GlueGetResourcePoliciesResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_policies, request, GlueGetResourcePoliciesResponse)

    async def get_resource_policies_paginated(
        self,
        request: GlueGetResourcePoliciesRequest | None = None,
    ) -> list[GlueGetResourcePoliciesResponse]:
        return await self._paginate('get_resource_policies', request, GlueGetResourcePoliciesResponse)

    async def get_resource_policy(
        self,
        request: GlueGetResourcePolicyRequest | None = None,
    ) -> GlueGetResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_policy, request, GlueGetResourcePolicyResponse)

    async def get_schema(
        self,
        request: GlueGetSchemaRequest,
    ) -> GlueGetSchemaResponse:
        client = self._require_client()
        return await self._execute(client.get_schema, request, GlueGetSchemaResponse)

    async def get_schema_by_definition(
        self,
        request: GlueGetSchemaByDefinitionRequest,
    ) -> GlueGetSchemaByDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.get_schema_by_definition, request, GlueGetSchemaByDefinitionResponse)

    async def get_schema_version(
        self,
        request: GlueGetSchemaVersionRequest | None = None,
    ) -> GlueGetSchemaVersionResponse:
        client = self._require_client()
        return await self._execute(client.get_schema_version, request, GlueGetSchemaVersionResponse)

    async def get_schema_versions_diff(
        self,
        request: GlueGetSchemaVersionsDiffRequest,
    ) -> GlueGetSchemaVersionsDiffResponse:
        client = self._require_client()
        return await self._execute(client.get_schema_versions_diff, request, GlueGetSchemaVersionsDiffResponse)

    async def get_security_configuration(
        self,
        request: GlueGetSecurityConfigurationRequest,
    ) -> GlueGetSecurityConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_security_configuration, request, GlueGetSecurityConfigurationResponse)

    async def get_security_configurations(
        self,
        request: GlueGetSecurityConfigurationsRequest | None = None,
    ) -> GlueGetSecurityConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.get_security_configurations, request, GlueGetSecurityConfigurationsResponse)

    async def get_security_configurations_paginated(
        self,
        request: GlueGetSecurityConfigurationsRequest | None = None,
    ) -> list[GlueGetSecurityConfigurationsResponse]:
        return await self._paginate('get_security_configurations', request, GlueGetSecurityConfigurationsResponse)

    async def get_session(
        self,
        request: GlueGetSessionRequest,
    ) -> GlueGetSessionResponse:
        client = self._require_client()
        return await self._execute(client.get_session, request, GlueGetSessionResponse)

    async def get_session_endpoint(
        self,
        request: GlueGetSessionEndpointRequest,
    ) -> GlueGetSessionEndpointResponse:
        client = self._require_client()
        return await self._execute(client.get_session_endpoint, request, GlueGetSessionEndpointResponse)

    async def get_statement(
        self,
        request: GlueGetStatementRequest,
    ) -> GlueGetStatementResponse:
        client = self._require_client()
        return await self._execute(client.get_statement, request, GlueGetStatementResponse)

    async def get_system_logs_for_job_run(
        self,
        request: GlueGetSystemLogsForJobRunRequest,
    ) -> GlueGetSystemLogsForJobRunResponse:
        client = self._require_client()
        return await self._execute(client.get_system_logs_for_job_run, request, GlueGetSystemLogsForJobRunResponse)

    async def get_system_logs_for_session(
        self,
        request: GlueGetSystemLogsForSessionRequest,
    ) -> GlueGetSystemLogsForSessionResponse:
        client = self._require_client()
        return await self._execute(client.get_system_logs_for_session, request, GlueGetSystemLogsForSessionResponse)

    async def get_table(
        self,
        request: GlueGetTableRequest,
    ) -> GlueGetTableResponse:
        client = self._require_client()
        return await self._execute(client.get_table, request, GlueGetTableResponse)

    async def get_table_optimizer(
        self,
        request: GlueGetTableOptimizerRequest,
    ) -> GlueGetTableOptimizerResponse:
        client = self._require_client()
        return await self._execute(client.get_table_optimizer, request, GlueGetTableOptimizerResponse)

    async def get_table_version(
        self,
        request: GlueGetTableVersionRequest,
    ) -> GlueGetTableVersionResponse:
        client = self._require_client()
        return await self._execute(client.get_table_version, request, GlueGetTableVersionResponse)

    async def get_table_versions(
        self,
        request: GlueGetTableVersionsRequest,
    ) -> GlueGetTableVersionsResponse:
        client = self._require_client()
        return await self._execute(client.get_table_versions, request, GlueGetTableVersionsResponse)

    async def get_table_versions_paginated(
        self,
        request: GlueGetTableVersionsRequest,
    ) -> list[GlueGetTableVersionsResponse]:
        return await self._paginate('get_table_versions', request, GlueGetTableVersionsResponse)

    async def get_tables(
        self,
        request: GlueGetTablesRequest,
    ) -> GlueGetTablesResponse:
        client = self._require_client()
        return await self._execute(client.get_tables, request, GlueGetTablesResponse)

    async def get_tables_paginated(
        self,
        request: GlueGetTablesRequest,
    ) -> list[GlueGetTablesResponse]:
        return await self._paginate('get_tables', request, GlueGetTablesResponse)

    async def get_tags(
        self,
        request: GlueGetTagsRequest,
    ) -> GlueGetTagsResponse:
        client = self._require_client()
        return await self._execute(client.get_tags, request, GlueGetTagsResponse)

    async def get_trigger(
        self,
        request: GlueGetTriggerRequest,
    ) -> GlueGetTriggerResponse:
        client = self._require_client()
        return await self._execute(client.get_trigger, request, GlueGetTriggerResponse)

    async def get_triggers(
        self,
        request: GlueGetTriggersRequest | None = None,
    ) -> GlueGetTriggersResponse:
        client = self._require_client()
        return await self._execute(client.get_triggers, request, GlueGetTriggersResponse)

    async def get_triggers_paginated(
        self,
        request: GlueGetTriggersRequest | None = None,
    ) -> list[GlueGetTriggersResponse]:
        return await self._paginate('get_triggers', request, GlueGetTriggersResponse)

    async def get_unfiltered_partition_metadata(
        self,
        request: GlueGetUnfilteredPartitionMetadataRequest,
    ) -> GlueGetUnfilteredPartitionMetadataResponse:
        client = self._require_client()
        return await self._execute(client.get_unfiltered_partition_metadata, request, GlueGetUnfilteredPartitionMetadataResponse)

    async def get_unfiltered_partitions_metadata(
        self,
        request: GlueGetUnfilteredPartitionsMetadataRequest,
    ) -> GlueGetUnfilteredPartitionsMetadataResponse:
        client = self._require_client()
        return await self._execute(client.get_unfiltered_partitions_metadata, request, GlueGetUnfilteredPartitionsMetadataResponse)

    async def get_unfiltered_table_metadata(
        self,
        request: GlueGetUnfilteredTableMetadataRequest,
    ) -> GlueGetUnfilteredTableMetadataResponse:
        client = self._require_client()
        return await self._execute(client.get_unfiltered_table_metadata, request, GlueGetUnfilteredTableMetadataResponse)

    async def get_usage_profile(
        self,
        request: GlueGetUsageProfileRequest,
    ) -> GlueGetUsageProfileResponse:
        client = self._require_client()
        return await self._execute(client.get_usage_profile, request, GlueGetUsageProfileResponse)

    async def get_user_defined_function(
        self,
        request: GlueGetUserDefinedFunctionRequest,
    ) -> GlueGetUserDefinedFunctionResponse:
        client = self._require_client()
        return await self._execute(client.get_user_defined_function, request, GlueGetUserDefinedFunctionResponse)

    async def get_user_defined_functions(
        self,
        request: GlueGetUserDefinedFunctionsRequest,
    ) -> GlueGetUserDefinedFunctionsResponse:
        client = self._require_client()
        return await self._execute(client.get_user_defined_functions, request, GlueGetUserDefinedFunctionsResponse)

    async def get_user_defined_functions_paginated(
        self,
        request: GlueGetUserDefinedFunctionsRequest,
    ) -> list[GlueGetUserDefinedFunctionsResponse]:
        return await self._paginate('get_user_defined_functions', request, GlueGetUserDefinedFunctionsResponse)

    async def get_workflow(
        self,
        request: GlueGetWorkflowRequest,
    ) -> GlueGetWorkflowResponse:
        client = self._require_client()
        return await self._execute(client.get_workflow, request, GlueGetWorkflowResponse)

    async def get_workflow_run(
        self,
        request: GlueGetWorkflowRunRequest,
    ) -> GlueGetWorkflowRunResponse:
        client = self._require_client()
        return await self._execute(client.get_workflow_run, request, GlueGetWorkflowRunResponse)

    async def get_workflow_run_properties(
        self,
        request: GlueGetWorkflowRunPropertiesRequest,
    ) -> GlueGetWorkflowRunPropertiesResponse:
        client = self._require_client()
        return await self._execute(client.get_workflow_run_properties, request, GlueGetWorkflowRunPropertiesResponse)

    async def get_workflow_runs(
        self,
        request: GlueGetWorkflowRunsRequest,
    ) -> GlueGetWorkflowRunsResponse:
        client = self._require_client()
        return await self._execute(client.get_workflow_runs, request, GlueGetWorkflowRunsResponse)

    async def get_workflow_runs_paginated(
        self,
        request: GlueGetWorkflowRunsRequest,
    ) -> list[GlueGetWorkflowRunsResponse]:
        return await self._paginate('get_workflow_runs', request, GlueGetWorkflowRunsResponse)

    async def import_catalog_to_glue(
        self,
        request: GlueImportCatalogToGlueRequest | None = None,
    ) -> GlueImportCatalogToGlueResponse:
        client = self._require_client()
        return await self._execute(client.import_catalog_to_glue, request, GlueImportCatalogToGlueResponse)

    async def list_asset_types(
        self,
        request: GlueListAssetTypesRequest | None = None,
    ) -> GlueListAssetTypesResponse:
        client = self._require_client()
        return await self._execute(client.list_asset_types, request, GlueListAssetTypesResponse)

    async def list_asset_types_paginated(
        self,
        request: GlueListAssetTypesRequest | None = None,
    ) -> list[GlueListAssetTypesResponse]:
        return await self._paginate('list_asset_types', request, GlueListAssetTypesResponse)

    async def list_blueprints(
        self,
        request: GlueListBlueprintsRequest | None = None,
    ) -> GlueListBlueprintsResponse:
        client = self._require_client()
        return await self._execute(client.list_blueprints, request, GlueListBlueprintsResponse)

    async def list_blueprints_paginated(
        self,
        request: GlueListBlueprintsRequest | None = None,
    ) -> list[GlueListBlueprintsResponse]:
        return await self._paginate('list_blueprints', request, GlueListBlueprintsResponse)

    async def list_column_statistics_task_runs(
        self,
        request: GlueListColumnStatisticsTaskRunsRequest | None = None,
    ) -> GlueListColumnStatisticsTaskRunsResponse:
        client = self._require_client()
        return await self._execute(client.list_column_statistics_task_runs, request, GlueListColumnStatisticsTaskRunsResponse)

    async def list_connection_types(
        self,
        request: GlueListConnectionTypesRequest | None = None,
    ) -> GlueListConnectionTypesResponse:
        client = self._require_client()
        return await self._execute(client.list_connection_types, request, GlueListConnectionTypesResponse)

    async def list_connection_types_paginated(
        self,
        request: GlueListConnectionTypesRequest | None = None,
    ) -> list[GlueListConnectionTypesResponse]:
        return await self._paginate('list_connection_types', request, GlueListConnectionTypesResponse)

    async def list_crawlers(
        self,
        request: GlueListCrawlersRequest | None = None,
    ) -> GlueListCrawlersResponse:
        client = self._require_client()
        return await self._execute(client.list_crawlers, request, GlueListCrawlersResponse)

    async def list_crawls(
        self,
        request: GlueListCrawlsRequest,
    ) -> GlueListCrawlsResponse:
        client = self._require_client()
        return await self._execute(client.list_crawls, request, GlueListCrawlsResponse)

    async def list_custom_entity_types(
        self,
        request: GlueListCustomEntityTypesRequest | None = None,
    ) -> GlueListCustomEntityTypesResponse:
        client = self._require_client()
        return await self._execute(client.list_custom_entity_types, request, GlueListCustomEntityTypesResponse)

    async def list_data_quality_evaluation_configs(
        self,
        request: GlueListDataQualityEvaluationConfigsRequest | None = None,
    ) -> GlueListDataQualityEvaluationConfigsResponse:
        client = self._require_client()
        return await self._execute(client.list_data_quality_evaluation_configs, request, GlueListDataQualityEvaluationConfigsResponse)

    async def list_data_quality_evaluation_configs_paginated(
        self,
        request: GlueListDataQualityEvaluationConfigsRequest | None = None,
    ) -> list[GlueListDataQualityEvaluationConfigsResponse]:
        return await self._paginate('list_data_quality_evaluation_configs', request, GlueListDataQualityEvaluationConfigsResponse)

    async def list_data_quality_results(
        self,
        request: GlueListDataQualityResultsRequest | None = None,
    ) -> GlueListDataQualityResultsResponse:
        client = self._require_client()
        return await self._execute(client.list_data_quality_results, request, GlueListDataQualityResultsResponse)

    async def list_data_quality_results_v2(
        self,
        request: GlueListDataQualityResultsV2Request | None = None,
    ) -> GlueListDataQualityResultsV2Response:
        client = self._require_client()
        return await self._execute(client.list_data_quality_results_v2, request, GlueListDataQualityResultsV2Response)

    async def list_data_quality_results_v2_paginated(
        self,
        request: GlueListDataQualityResultsV2Request | None = None,
    ) -> list[GlueListDataQualityResultsV2Response]:
        return await self._paginate('list_data_quality_results_v2', request, GlueListDataQualityResultsV2Response)

    async def list_data_quality_rule_recommendation_runs(
        self,
        request: GlueListDataQualityRuleRecommendationRunsRequest | None = None,
    ) -> GlueListDataQualityRuleRecommendationRunsResponse:
        client = self._require_client()
        return await self._execute(client.list_data_quality_rule_recommendation_runs, request, GlueListDataQualityRuleRecommendationRunsResponse)

    async def list_data_quality_ruleset_evaluation_runs(
        self,
        request: GlueListDataQualityRulesetEvaluationRunsRequest | None = None,
    ) -> GlueListDataQualityRulesetEvaluationRunsResponse:
        client = self._require_client()
        return await self._execute(client.list_data_quality_ruleset_evaluation_runs, request, GlueListDataQualityRulesetEvaluationRunsResponse)

    async def list_data_quality_rulesets(
        self,
        request: GlueListDataQualityRulesetsRequest | None = None,
    ) -> GlueListDataQualityRulesetsResponse:
        client = self._require_client()
        return await self._execute(client.list_data_quality_rulesets, request, GlueListDataQualityRulesetsResponse)

    async def list_data_quality_statistic_annotations(
        self,
        request: GlueListDataQualityStatisticAnnotationsRequest | None = None,
    ) -> GlueListDataQualityStatisticAnnotationsResponse:
        client = self._require_client()
        return await self._execute(client.list_data_quality_statistic_annotations, request, GlueListDataQualityStatisticAnnotationsResponse)

    async def list_data_quality_statistics(
        self,
        request: GlueListDataQualityStatisticsRequest | None = None,
    ) -> GlueListDataQualityStatisticsResponse:
        client = self._require_client()
        return await self._execute(client.list_data_quality_statistics, request, GlueListDataQualityStatisticsResponse)

    async def list_dev_endpoints(
        self,
        request: GlueListDevEndpointsRequest | None = None,
    ) -> GlueListDevEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.list_dev_endpoints, request, GlueListDevEndpointsResponse)

    async def list_entities(
        self,
        request: GlueListEntitiesRequest | None = None,
    ) -> GlueListEntitiesResponse:
        client = self._require_client()
        return await self._execute(client.list_entities, request, GlueListEntitiesResponse)

    async def list_entities_paginated(
        self,
        request: GlueListEntitiesRequest | None = None,
    ) -> list[GlueListEntitiesResponse]:
        return await self._paginate('list_entities', request, GlueListEntitiesResponse)

    async def list_form_types(
        self,
        request: GlueListFormTypesRequest | None = None,
    ) -> GlueListFormTypesResponse:
        client = self._require_client()
        return await self._execute(client.list_form_types, request, GlueListFormTypesResponse)

    async def list_form_types_paginated(
        self,
        request: GlueListFormTypesRequest | None = None,
    ) -> list[GlueListFormTypesResponse]:
        return await self._paginate('list_form_types', request, GlueListFormTypesResponse)

    async def list_glossaries(
        self,
        request: GlueListGlossariesRequest | None = None,
    ) -> GlueListGlossariesResponse:
        client = self._require_client()
        return await self._execute(client.list_glossaries, request, GlueListGlossariesResponse)

    async def list_glossaries_paginated(
        self,
        request: GlueListGlossariesRequest | None = None,
    ) -> list[GlueListGlossariesResponse]:
        return await self._paginate('list_glossaries', request, GlueListGlossariesResponse)

    async def list_glossary_terms(
        self,
        request: GlueListGlossaryTermsRequest,
    ) -> GlueListGlossaryTermsResponse:
        client = self._require_client()
        return await self._execute(client.list_glossary_terms, request, GlueListGlossaryTermsResponse)

    async def list_glossary_terms_paginated(
        self,
        request: GlueListGlossaryTermsRequest,
    ) -> list[GlueListGlossaryTermsResponse]:
        return await self._paginate('list_glossary_terms', request, GlueListGlossaryTermsResponse)

    async def list_integration_resource_properties(
        self,
        request: GlueListIntegrationResourcePropertiesRequest | None = None,
    ) -> GlueListIntegrationResourcePropertiesResponse:
        client = self._require_client()
        return await self._execute(client.list_integration_resource_properties, request, GlueListIntegrationResourcePropertiesResponse)

    async def list_integration_table_properties(
        self,
        request: GlueListIntegrationTablePropertiesRequest | None = None,
    ) -> GlueListIntegrationTablePropertiesResponse:
        client = self._require_client()
        return await self._execute(client.list_integration_table_properties, request, GlueListIntegrationTablePropertiesResponse)

    async def list_iterable_forms(
        self,
        request: GlueListIterableFormsRequest,
    ) -> GlueListIterableFormsResponse:
        client = self._require_client()
        return await self._execute(client.list_iterable_forms, request, GlueListIterableFormsResponse)

    async def list_iterable_forms_paginated(
        self,
        request: GlueListIterableFormsRequest,
    ) -> list[GlueListIterableFormsResponse]:
        return await self._paginate('list_iterable_forms', request, GlueListIterableFormsResponse)

    async def list_jobs(
        self,
        request: GlueListJobsRequest | None = None,
    ) -> GlueListJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_jobs, request, GlueListJobsResponse)

    async def list_jobs_paginated(
        self,
        request: GlueListJobsRequest | None = None,
    ) -> list[GlueListJobsResponse]:
        return await self._paginate('list_jobs', request, GlueListJobsResponse)

    async def list_ml_transforms(
        self,
        request: GlueListMLTransformsRequest | None = None,
    ) -> GlueListMLTransformsResponse:
        client = self._require_client()
        return await self._execute(client.list_ml_transforms, request, GlueListMLTransformsResponse)

    async def list_materialized_view_refresh_task_runs(
        self,
        request: GlueListMaterializedViewRefreshTaskRunsRequest,
    ) -> GlueListMaterializedViewRefreshTaskRunsResponse:
        client = self._require_client()
        return await self._execute(client.list_materialized_view_refresh_task_runs, request, GlueListMaterializedViewRefreshTaskRunsResponse)

    async def list_materialized_view_refresh_task_runs_paginated(
        self,
        request: GlueListMaterializedViewRefreshTaskRunsRequest,
    ) -> list[GlueListMaterializedViewRefreshTaskRunsResponse]:
        return await self._paginate('list_materialized_view_refresh_task_runs', request, GlueListMaterializedViewRefreshTaskRunsResponse)

    async def list_registries(
        self,
        request: GlueListRegistriesRequest | None = None,
    ) -> GlueListRegistriesResponse:
        client = self._require_client()
        return await self._execute(client.list_registries, request, GlueListRegistriesResponse)

    async def list_registries_paginated(
        self,
        request: GlueListRegistriesRequest | None = None,
    ) -> list[GlueListRegistriesResponse]:
        return await self._paginate('list_registries', request, GlueListRegistriesResponse)

    async def list_schema_versions(
        self,
        request: GlueListSchemaVersionsRequest,
    ) -> GlueListSchemaVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_schema_versions, request, GlueListSchemaVersionsResponse)

    async def list_schema_versions_paginated(
        self,
        request: GlueListSchemaVersionsRequest,
    ) -> list[GlueListSchemaVersionsResponse]:
        return await self._paginate('list_schema_versions', request, GlueListSchemaVersionsResponse)

    async def list_schemas(
        self,
        request: GlueListSchemasRequest | None = None,
    ) -> GlueListSchemasResponse:
        client = self._require_client()
        return await self._execute(client.list_schemas, request, GlueListSchemasResponse)

    async def list_schemas_paginated(
        self,
        request: GlueListSchemasRequest | None = None,
    ) -> list[GlueListSchemasResponse]:
        return await self._paginate('list_schemas', request, GlueListSchemasResponse)

    async def list_sessions(
        self,
        request: GlueListSessionsRequest | None = None,
    ) -> GlueListSessionsResponse:
        client = self._require_client()
        return await self._execute(client.list_sessions, request, GlueListSessionsResponse)

    async def list_statements(
        self,
        request: GlueListStatementsRequest,
    ) -> GlueListStatementsResponse:
        client = self._require_client()
        return await self._execute(client.list_statements, request, GlueListStatementsResponse)

    async def list_table_optimizer_runs(
        self,
        request: GlueListTableOptimizerRunsRequest,
    ) -> GlueListTableOptimizerRunsResponse:
        client = self._require_client()
        return await self._execute(client.list_table_optimizer_runs, request, GlueListTableOptimizerRunsResponse)

    async def list_table_optimizer_runs_paginated(
        self,
        request: GlueListTableOptimizerRunsRequest,
    ) -> list[GlueListTableOptimizerRunsResponse]:
        return await self._paginate('list_table_optimizer_runs', request, GlueListTableOptimizerRunsResponse)

    async def list_triggers(
        self,
        request: GlueListTriggersRequest | None = None,
    ) -> GlueListTriggersResponse:
        client = self._require_client()
        return await self._execute(client.list_triggers, request, GlueListTriggersResponse)

    async def list_triggers_paginated(
        self,
        request: GlueListTriggersRequest | None = None,
    ) -> list[GlueListTriggersResponse]:
        return await self._paginate('list_triggers', request, GlueListTriggersResponse)

    async def list_usage_profiles(
        self,
        request: GlueListUsageProfilesRequest | None = None,
    ) -> GlueListUsageProfilesResponse:
        client = self._require_client()
        return await self._execute(client.list_usage_profiles, request, GlueListUsageProfilesResponse)

    async def list_usage_profiles_paginated(
        self,
        request: GlueListUsageProfilesRequest | None = None,
    ) -> list[GlueListUsageProfilesResponse]:
        return await self._paginate('list_usage_profiles', request, GlueListUsageProfilesResponse)

    async def list_workflows(
        self,
        request: GlueListWorkflowsRequest | None = None,
    ) -> GlueListWorkflowsResponse:
        client = self._require_client()
        return await self._execute(client.list_workflows, request, GlueListWorkflowsResponse)

    async def list_workflows_paginated(
        self,
        request: GlueListWorkflowsRequest | None = None,
    ) -> list[GlueListWorkflowsResponse]:
        return await self._paginate('list_workflows', request, GlueListWorkflowsResponse)

    async def modify_integration(
        self,
        request: GlueModifyIntegrationRequest,
    ) -> GlueModifyIntegrationResponse:
        client = self._require_client()
        return await self._execute(client.modify_integration, request, GlueModifyIntegrationResponse)

    async def publish_data_quality_result_v2(
        self,
        request: GluePublishDataQualityResultV2Request,
    ) -> GluePublishDataQualityResultV2Response:
        client = self._require_client()
        return await self._execute(client.publish_data_quality_result_v2, request, GluePublishDataQualityResultV2Response)

    async def put_asset(
        self,
        request: GluePutAssetRequest,
    ) -> GluePutAssetResponse:
        client = self._require_client()
        return await self._execute(client.put_asset, request, GluePutAssetResponse)

    async def put_attachment(
        self,
        request: GluePutAttachmentRequest,
    ) -> GluePutAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.put_attachment, request, GluePutAttachmentResponse)

    async def put_data_catalog_encryption_settings(
        self,
        request: GluePutDataCatalogEncryptionSettingsRequest,
    ) -> GluePutDataCatalogEncryptionSettingsResponse:
        client = self._require_client()
        return await self._execute(client.put_data_catalog_encryption_settings, request, GluePutDataCatalogEncryptionSettingsResponse)

    async def put_data_catalog_export_configuration(
        self,
        request: GluePutDataCatalogExportConfigurationRequest | None = None,
    ) -> GluePutDataCatalogExportConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_data_catalog_export_configuration, request, GluePutDataCatalogExportConfigurationResponse)

    async def put_data_quality_profile_annotation(
        self,
        request: GluePutDataQualityProfileAnnotationRequest,
    ) -> GluePutDataQualityProfileAnnotationResponse:
        client = self._require_client()
        return await self._execute(client.put_data_quality_profile_annotation, request, GluePutDataQualityProfileAnnotationResponse)

    async def put_form_type(
        self,
        request: GluePutFormTypeRequest,
    ) -> GluePutFormTypeResponse:
        client = self._require_client()
        return await self._execute(client.put_form_type, request, GluePutFormTypeResponse)

    async def put_resource_policy(
        self,
        request: GluePutResourcePolicyRequest,
    ) -> GluePutResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_resource_policy, request, GluePutResourcePolicyResponse)

    async def put_schema_version_metadata(
        self,
        request: GluePutSchemaVersionMetadataRequest,
    ) -> GluePutSchemaVersionMetadataResponse:
        client = self._require_client()
        return await self._execute(client.put_schema_version_metadata, request, GluePutSchemaVersionMetadataResponse)

    async def put_workflow_run_properties(
        self,
        request: GluePutWorkflowRunPropertiesRequest,
    ) -> GluePutWorkflowRunPropertiesResponse:
        client = self._require_client()
        return await self._execute(client.put_workflow_run_properties, request, GluePutWorkflowRunPropertiesResponse)

    async def query_schema_version_metadata(
        self,
        request: GlueQuerySchemaVersionMetadataRequest | None = None,
    ) -> GlueQuerySchemaVersionMetadataResponse:
        client = self._require_client()
        return await self._execute(client.query_schema_version_metadata, request, GlueQuerySchemaVersionMetadataResponse)

    async def register_connection_type(
        self,
        request: GlueRegisterConnectionTypeRequest,
    ) -> GlueRegisterConnectionTypeResponse:
        client = self._require_client()
        return await self._execute(client.register_connection_type, request, GlueRegisterConnectionTypeResponse)

    async def register_schema_version(
        self,
        request: GlueRegisterSchemaVersionRequest,
    ) -> GlueRegisterSchemaVersionResponse:
        client = self._require_client()
        return await self._execute(client.register_schema_version, request, GlueRegisterSchemaVersionResponse)

    async def remove_schema_version_metadata(
        self,
        request: GlueRemoveSchemaVersionMetadataRequest,
    ) -> GlueRemoveSchemaVersionMetadataResponse:
        client = self._require_client()
        return await self._execute(client.remove_schema_version_metadata, request, GlueRemoveSchemaVersionMetadataResponse)

    async def reset_job_bookmark(
        self,
        request: GlueResetJobBookmarkRequest,
    ) -> GlueResetJobBookmarkResponse:
        client = self._require_client()
        return await self._execute(client.reset_job_bookmark, request, GlueResetJobBookmarkResponse)

    async def resume_workflow_run(
        self,
        request: GlueResumeWorkflowRunRequest,
    ) -> GlueResumeWorkflowRunResponse:
        client = self._require_client()
        return await self._execute(client.resume_workflow_run, request, GlueResumeWorkflowRunResponse)

    async def run_statement(
        self,
        request: GlueRunStatementRequest,
    ) -> GlueRunStatementResponse:
        client = self._require_client()
        return await self._execute(client.run_statement, request, GlueRunStatementResponse)

    async def search_assets(
        self,
        request: GlueSearchAssetsRequest | None = None,
    ) -> GlueSearchAssetsResponse:
        client = self._require_client()
        return await self._execute(client.search_assets, request, GlueSearchAssetsResponse)

    async def search_assets_paginated(
        self,
        request: GlueSearchAssetsRequest | None = None,
    ) -> list[GlueSearchAssetsResponse]:
        return await self._paginate('search_assets', request, GlueSearchAssetsResponse)

    async def search_tables(
        self,
        request: GlueSearchTablesRequest | None = None,
    ) -> GlueSearchTablesResponse:
        client = self._require_client()
        return await self._execute(client.search_tables, request, GlueSearchTablesResponse)

    async def start_blueprint_run(
        self,
        request: GlueStartBlueprintRunRequest,
    ) -> GlueStartBlueprintRunResponse:
        client = self._require_client()
        return await self._execute(client.start_blueprint_run, request, GlueStartBlueprintRunResponse)

    async def start_column_statistics_task_run(
        self,
        request: GlueStartColumnStatisticsTaskRunRequest,
    ) -> GlueStartColumnStatisticsTaskRunResponse:
        client = self._require_client()
        return await self._execute(client.start_column_statistics_task_run, request, GlueStartColumnStatisticsTaskRunResponse)

    async def start_column_statistics_task_run_schedule(
        self,
        request: GlueStartColumnStatisticsTaskRunScheduleRequest,
    ) -> GlueStartColumnStatisticsTaskRunScheduleResponse:
        client = self._require_client()
        return await self._execute(client.start_column_statistics_task_run_schedule, request, GlueStartColumnStatisticsTaskRunScheduleResponse)

    async def start_crawler(
        self,
        request: GlueStartCrawlerRequest,
    ) -> GlueStartCrawlerResponse:
        client = self._require_client()
        return await self._execute(client.start_crawler, request, GlueStartCrawlerResponse)

    async def start_crawler_schedule(
        self,
        request: GlueStartCrawlerScheduleRequest,
    ) -> GlueStartCrawlerScheduleResponse:
        client = self._require_client()
        return await self._execute(client.start_crawler_schedule, request, GlueStartCrawlerScheduleResponse)

    async def start_data_quality_rule_recommendation_run(
        self,
        request: GlueStartDataQualityRuleRecommendationRunRequest,
    ) -> GlueStartDataQualityRuleRecommendationRunResponse:
        client = self._require_client()
        return await self._execute(client.start_data_quality_rule_recommendation_run, request, GlueStartDataQualityRuleRecommendationRunResponse)

    async def start_data_quality_ruleset_evaluation_run(
        self,
        request: GlueStartDataQualityRulesetEvaluationRunRequest,
    ) -> GlueStartDataQualityRulesetEvaluationRunResponse:
        client = self._require_client()
        return await self._execute(client.start_data_quality_ruleset_evaluation_run, request, GlueStartDataQualityRulesetEvaluationRunResponse)

    async def start_export_labels_task_run(
        self,
        request: GlueStartExportLabelsTaskRunRequest,
    ) -> GlueStartExportLabelsTaskRunResponse:
        client = self._require_client()
        return await self._execute(client.start_export_labels_task_run, request, GlueStartExportLabelsTaskRunResponse)

    async def start_import_labels_task_run(
        self,
        request: GlueStartImportLabelsTaskRunRequest,
    ) -> GlueStartImportLabelsTaskRunResponse:
        client = self._require_client()
        return await self._execute(client.start_import_labels_task_run, request, GlueStartImportLabelsTaskRunResponse)

    async def start_job_run(
        self,
        request: GlueStartJobRunRequest,
    ) -> GlueStartJobRunResponse:
        client = self._require_client()
        return await self._execute(client.start_job_run, request, GlueStartJobRunResponse)

    async def start_job_upgrade_analysis(
        self,
        request: GlueStartJobUpgradeAnalysisRequest,
    ) -> GlueStartJobUpgradeAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.start_job_upgrade_analysis, request, GlueStartJobUpgradeAnalysisResponse)

    async def start_ml_evaluation_task_run(
        self,
        request: GlueStartMLEvaluationTaskRunRequest,
    ) -> GlueStartMLEvaluationTaskRunResponse:
        client = self._require_client()
        return await self._execute(client.start_ml_evaluation_task_run, request, GlueStartMLEvaluationTaskRunResponse)

    async def start_ml_labeling_set_generation_task_run(
        self,
        request: GlueStartMLLabelingSetGenerationTaskRunRequest,
    ) -> GlueStartMLLabelingSetGenerationTaskRunResponse:
        client = self._require_client()
        return await self._execute(client.start_ml_labeling_set_generation_task_run, request, GlueStartMLLabelingSetGenerationTaskRunResponse)

    async def start_materialized_view_refresh_task_run(
        self,
        request: GlueStartMaterializedViewRefreshTaskRunRequest,
    ) -> GlueStartMaterializedViewRefreshTaskRunResponse:
        client = self._require_client()
        return await self._execute(client.start_materialized_view_refresh_task_run, request, GlueStartMaterializedViewRefreshTaskRunResponse)

    async def start_trigger(
        self,
        request: GlueStartTriggerRequest,
    ) -> GlueStartTriggerResponse:
        client = self._require_client()
        return await self._execute(client.start_trigger, request, GlueStartTriggerResponse)

    async def start_workflow_run(
        self,
        request: GlueStartWorkflowRunRequest,
    ) -> GlueStartWorkflowRunResponse:
        client = self._require_client()
        return await self._execute(client.start_workflow_run, request, GlueStartWorkflowRunResponse)

    async def stop_column_statistics_task_run(
        self,
        request: GlueStopColumnStatisticsTaskRunRequest,
    ) -> GlueStopColumnStatisticsTaskRunResponse:
        client = self._require_client()
        return await self._execute(client.stop_column_statistics_task_run, request, GlueStopColumnStatisticsTaskRunResponse)

    async def stop_column_statistics_task_run_schedule(
        self,
        request: GlueStopColumnStatisticsTaskRunScheduleRequest,
    ) -> GlueStopColumnStatisticsTaskRunScheduleResponse:
        client = self._require_client()
        return await self._execute(client.stop_column_statistics_task_run_schedule, request, GlueStopColumnStatisticsTaskRunScheduleResponse)

    async def stop_crawler(
        self,
        request: GlueStopCrawlerRequest,
    ) -> GlueStopCrawlerResponse:
        client = self._require_client()
        return await self._execute(client.stop_crawler, request, GlueStopCrawlerResponse)

    async def stop_crawler_schedule(
        self,
        request: GlueStopCrawlerScheduleRequest,
    ) -> GlueStopCrawlerScheduleResponse:
        client = self._require_client()
        return await self._execute(client.stop_crawler_schedule, request, GlueStopCrawlerScheduleResponse)

    async def stop_job_upgrade_analysis(
        self,
        request: GlueStopJobUpgradeAnalysisRequest,
    ) -> GlueStopJobUpgradeAnalysisResponse:
        client = self._require_client()
        return await self._execute(client.stop_job_upgrade_analysis, request, GlueStopJobUpgradeAnalysisResponse)

    async def stop_materialized_view_refresh_task_run(
        self,
        request: GlueStopMaterializedViewRefreshTaskRunRequest,
    ) -> GlueStopMaterializedViewRefreshTaskRunResponse:
        client = self._require_client()
        return await self._execute(client.stop_materialized_view_refresh_task_run, request, GlueStopMaterializedViewRefreshTaskRunResponse)

    async def stop_session(
        self,
        request: GlueStopSessionRequest,
    ) -> GlueStopSessionResponse:
        client = self._require_client()
        return await self._execute(client.stop_session, request, GlueStopSessionResponse)

    async def stop_trigger(
        self,
        request: GlueStopTriggerRequest,
    ) -> GlueStopTriggerResponse:
        client = self._require_client()
        return await self._execute(client.stop_trigger, request, GlueStopTriggerResponse)

    async def stop_workflow_run(
        self,
        request: GlueStopWorkflowRunRequest,
    ) -> GlueStopWorkflowRunResponse:
        client = self._require_client()
        return await self._execute(client.stop_workflow_run, request, GlueStopWorkflowRunResponse)

    async def tag_resource(
        self,
        request: GlueTagResourceRequest,
    ) -> GlueTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, GlueTagResourceResponse)

    async def test_connection(
        self,
        request: GlueTestConnectionRequest | None = None,
    ) -> GlueTestConnectionResponse:
        client = self._require_client()
        return await self._execute(client.test_connection, request, GlueTestConnectionResponse)

    async def untag_resource(
        self,
        request: GlueUntagResourceRequest,
    ) -> GlueUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, GlueUntagResourceResponse)

    async def update_asset(
        self,
        request: GlueUpdateAssetRequest,
    ) -> GlueUpdateAssetResponse:
        client = self._require_client()
        return await self._execute(client.update_asset, request, GlueUpdateAssetResponse)

    async def update_blueprint(
        self,
        request: GlueUpdateBlueprintRequest,
    ) -> GlueUpdateBlueprintResponse:
        client = self._require_client()
        return await self._execute(client.update_blueprint, request, GlueUpdateBlueprintResponse)

    async def update_catalog(
        self,
        request: GlueUpdateCatalogRequest,
    ) -> GlueUpdateCatalogResponse:
        client = self._require_client()
        return await self._execute(client.update_catalog, request, GlueUpdateCatalogResponse)

    async def update_classifier(
        self,
        request: GlueUpdateClassifierRequest | None = None,
    ) -> GlueUpdateClassifierResponse:
        client = self._require_client()
        return await self._execute(client.update_classifier, request, GlueUpdateClassifierResponse)

    async def update_column_statistics_for_partition(
        self,
        request: GlueUpdateColumnStatisticsForPartitionRequest,
    ) -> GlueUpdateColumnStatisticsForPartitionResponse:
        client = self._require_client()
        return await self._execute(client.update_column_statistics_for_partition, request, GlueUpdateColumnStatisticsForPartitionResponse)

    async def update_column_statistics_for_table(
        self,
        request: GlueUpdateColumnStatisticsForTableRequest,
    ) -> GlueUpdateColumnStatisticsForTableResponse:
        client = self._require_client()
        return await self._execute(client.update_column_statistics_for_table, request, GlueUpdateColumnStatisticsForTableResponse)

    async def update_column_statistics_task_settings(
        self,
        request: GlueUpdateColumnStatisticsTaskSettingsRequest,
    ) -> GlueUpdateColumnStatisticsTaskSettingsResponse:
        client = self._require_client()
        return await self._execute(client.update_column_statistics_task_settings, request, GlueUpdateColumnStatisticsTaskSettingsResponse)

    async def update_connection(
        self,
        request: GlueUpdateConnectionRequest,
    ) -> GlueUpdateConnectionResponse:
        client = self._require_client()
        return await self._execute(client.update_connection, request, GlueUpdateConnectionResponse)

    async def update_crawler(
        self,
        request: GlueUpdateCrawlerRequest,
    ) -> GlueUpdateCrawlerResponse:
        client = self._require_client()
        return await self._execute(client.update_crawler, request, GlueUpdateCrawlerResponse)

    async def update_crawler_schedule(
        self,
        request: GlueUpdateCrawlerScheduleRequest,
    ) -> GlueUpdateCrawlerScheduleResponse:
        client = self._require_client()
        return await self._execute(client.update_crawler_schedule, request, GlueUpdateCrawlerScheduleResponse)

    async def update_data_quality_evaluation_config(
        self,
        request: GlueUpdateDataQualityEvaluationConfigRequest,
    ) -> GlueUpdateDataQualityEvaluationConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_data_quality_evaluation_config, request, GlueUpdateDataQualityEvaluationConfigResponse)

    async def update_data_quality_ruleset(
        self,
        request: GlueUpdateDataQualityRulesetRequest,
    ) -> GlueUpdateDataQualityRulesetResponse:
        client = self._require_client()
        return await self._execute(client.update_data_quality_ruleset, request, GlueUpdateDataQualityRulesetResponse)

    async def update_database(
        self,
        request: GlueUpdateDatabaseRequest,
    ) -> GlueUpdateDatabaseResponse:
        client = self._require_client()
        return await self._execute(client.update_database, request, GlueUpdateDatabaseResponse)

    async def update_dev_endpoint(
        self,
        request: GlueUpdateDevEndpointRequest,
    ) -> GlueUpdateDevEndpointResponse:
        client = self._require_client()
        return await self._execute(client.update_dev_endpoint, request, GlueUpdateDevEndpointResponse)

    async def update_glossary(
        self,
        request: GlueUpdateGlossaryRequest,
    ) -> GlueUpdateGlossaryResponse:
        client = self._require_client()
        return await self._execute(client.update_glossary, request, GlueUpdateGlossaryResponse)

    async def update_glossary_term(
        self,
        request: GlueUpdateGlossaryTermRequest,
    ) -> GlueUpdateGlossaryTermResponse:
        client = self._require_client()
        return await self._execute(client.update_glossary_term, request, GlueUpdateGlossaryTermResponse)

    async def update_glue_identity_center_configuration(
        self,
        request: GlueUpdateGlueIdentityCenterConfigurationRequest | None = None,
    ) -> GlueUpdateGlueIdentityCenterConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_glue_identity_center_configuration, request, GlueUpdateGlueIdentityCenterConfigurationResponse)

    async def update_integration_resource_property(
        self,
        request: GlueUpdateIntegrationResourcePropertyRequest,
    ) -> GlueUpdateIntegrationResourcePropertyResponse:
        client = self._require_client()
        return await self._execute(client.update_integration_resource_property, request, GlueUpdateIntegrationResourcePropertyResponse)

    async def update_integration_table_properties(
        self,
        request: GlueUpdateIntegrationTablePropertiesRequest,
    ) -> GlueUpdateIntegrationTablePropertiesResponse:
        client = self._require_client()
        return await self._execute(client.update_integration_table_properties, request, GlueUpdateIntegrationTablePropertiesResponse)

    async def update_job(
        self,
        request: GlueUpdateJobRequest,
    ) -> GlueUpdateJobResponse:
        client = self._require_client()
        return await self._execute(client.update_job, request, GlueUpdateJobResponse)

    async def update_job_from_source_control(
        self,
        request: GlueUpdateJobFromSourceControlRequest | None = None,
    ) -> GlueUpdateJobFromSourceControlResponse:
        client = self._require_client()
        return await self._execute(client.update_job_from_source_control, request, GlueUpdateJobFromSourceControlResponse)

    async def update_ml_transform(
        self,
        request: GlueUpdateMLTransformRequest,
    ) -> GlueUpdateMLTransformResponse:
        client = self._require_client()
        return await self._execute(client.update_ml_transform, request, GlueUpdateMLTransformResponse)

    async def update_partition(
        self,
        request: GlueUpdatePartitionRequest,
    ) -> GlueUpdatePartitionResponse:
        client = self._require_client()
        return await self._execute(client.update_partition, request, GlueUpdatePartitionResponse)

    async def update_registry(
        self,
        request: GlueUpdateRegistryRequest,
    ) -> GlueUpdateRegistryResponse:
        client = self._require_client()
        return await self._execute(client.update_registry, request, GlueUpdateRegistryResponse)

    async def update_schema(
        self,
        request: GlueUpdateSchemaRequest,
    ) -> GlueUpdateSchemaResponse:
        client = self._require_client()
        return await self._execute(client.update_schema, request, GlueUpdateSchemaResponse)

    async def update_source_control_from_job(
        self,
        request: GlueUpdateSourceControlFromJobRequest | None = None,
    ) -> GlueUpdateSourceControlFromJobResponse:
        client = self._require_client()
        return await self._execute(client.update_source_control_from_job, request, GlueUpdateSourceControlFromJobResponse)

    async def update_table(
        self,
        request: GlueUpdateTableRequest,
    ) -> GlueUpdateTableResponse:
        client = self._require_client()
        return await self._execute(client.update_table, request, GlueUpdateTableResponse)

    async def update_table_optimizer(
        self,
        request: GlueUpdateTableOptimizerRequest,
    ) -> GlueUpdateTableOptimizerResponse:
        client = self._require_client()
        return await self._execute(client.update_table_optimizer, request, GlueUpdateTableOptimizerResponse)

    async def update_trigger(
        self,
        request: GlueUpdateTriggerRequest,
    ) -> GlueUpdateTriggerResponse:
        client = self._require_client()
        return await self._execute(client.update_trigger, request, GlueUpdateTriggerResponse)

    async def update_usage_profile(
        self,
        request: GlueUpdateUsageProfileRequest,
    ) -> GlueUpdateUsageProfileResponse:
        client = self._require_client()
        return await self._execute(client.update_usage_profile, request, GlueUpdateUsageProfileResponse)

    async def update_user_defined_function(
        self,
        request: GlueUpdateUserDefinedFunctionRequest,
    ) -> GlueUpdateUserDefinedFunctionResponse:
        client = self._require_client()
        return await self._execute(client.update_user_defined_function, request, GlueUpdateUserDefinedFunctionResponse)

    async def update_workflow(
        self,
        request: GlueUpdateWorkflowRequest,
    ) -> GlueUpdateWorkflowResponse:
        client = self._require_client()
        return await self._execute(client.update_workflow, request, GlueUpdateWorkflowResponse)
