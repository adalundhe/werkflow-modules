from werkflow_aws.models.sagemaker import (
    SageMakerAddTagsRequest,
    SageMakerAddTagsResponse,
    SageMakerCreateEndpointConfigRequest,
    SageMakerCreateEndpointConfigResponse,
    SageMakerCreateEndpointRequest,
    SageMakerCreateEndpointResponse,
    SageMakerCreateModelRequest,
    SageMakerCreateModelResponse,
    SageMakerCreateTrainingJobRequest,
    SageMakerCreateTrainingJobResponse,
    SageMakerDeleteEndpointConfigRequest,
    SageMakerDeleteEndpointConfigResponse,
    SageMakerDeleteEndpointRequest,
    SageMakerDeleteEndpointResponse,
    SageMakerDeleteModelRequest,
    SageMakerDeleteModelResponse,
    SageMakerDeleteTagsRequest,
    SageMakerDeleteTagsResponse,
    SageMakerDescribeEndpointConfigRequest,
    SageMakerDescribeEndpointConfigResponse,
    SageMakerDescribeEndpointRequest,
    SageMakerDescribeEndpointResponse,
    SageMakerDescribeModelRequest,
    SageMakerDescribeModelResponse,
    SageMakerDescribeNotebookInstanceRequest,
    SageMakerDescribeNotebookInstanceResponse,
    SageMakerDescribePipelineRequest,
    SageMakerDescribePipelineResponse,
    SageMakerDescribeProcessingJobRequest,
    SageMakerDescribeProcessingJobResponse,
    SageMakerDescribeTrainingJobRequest,
    SageMakerDescribeTrainingJobResponse,
    SageMakerListEndpointConfigsRequest,
    SageMakerListEndpointConfigsResponse,
    SageMakerListEndpointsRequest,
    SageMakerListEndpointsResponse,
    SageMakerListModelsRequest,
    SageMakerListModelsResponse,
    SageMakerListNotebookInstancesRequest,
    SageMakerListNotebookInstancesResponse,
    SageMakerListPipelinesRequest,
    SageMakerListPipelinesResponse,
    SageMakerListProcessingJobsRequest,
    SageMakerListProcessingJobsResponse,
    SageMakerListTagsRequest,
    SageMakerListTagsResponse,
    SageMakerListTrainingJobsRequest,
    SageMakerListTrainingJobsResponse,
    SageMakerStartNotebookInstanceRequest,
    SageMakerStartNotebookInstanceResponse,
    SageMakerStartPipelineExecutionRequest,
    SageMakerStartPipelineExecutionResponse,
    SageMakerStopNotebookInstanceRequest,
    SageMakerStopNotebookInstanceResponse,
    SageMakerStopProcessingJobRequest,
    SageMakerStopProcessingJobResponse,
    SageMakerStopTrainingJobRequest,
    SageMakerStopTrainingJobResponse,
    SageMakerUpdateEndpointRequest,
    SageMakerUpdateEndpointResponse,
)
from werkflow_aws.services.base import AWSBaseService
from werkflow_aws.types.sagemaker_client import SageMakerClient
from werkflow_aws.models.sagemaker import (
    SageMakerAddAssociationRequest,
    SageMakerAddAssociationResponse,
    SageMakerAddInferenceGatewayRequest,
    SageMakerAddInferenceGatewayResponse,
    SageMakerAssociateTrialComponentRequest,
    SageMakerAssociateTrialComponentResponse,
    SageMakerAttachClusterNodeNetworkInterfaceRequest,
    SageMakerAttachClusterNodeNetworkInterfaceResponse,
    SageMakerAttachClusterNodeVolumeRequest,
    SageMakerAttachClusterNodeVolumeResponse,
    SageMakerBatchAddClusterNodesRequest,
    SageMakerBatchAddClusterNodesResponse,
    SageMakerBatchDeleteClusterNodesRequest,
    SageMakerBatchDeleteClusterNodesResponse,
    SageMakerBatchDescribeModelPackageRequest,
    SageMakerBatchDescribeModelPackageResponse,
    SageMakerBatchRebootClusterNodesRequest,
    SageMakerBatchRebootClusterNodesResponse,
    SageMakerBatchReplaceClusterNodesRequest,
    SageMakerBatchReplaceClusterNodesResponse,
    SageMakerCreateAIBenchmarkJobRequest,
    SageMakerCreateAIBenchmarkJobResponse,
    SageMakerCreateAIRecommendationJobRequest,
    SageMakerCreateAIRecommendationJobResponse,
    SageMakerCreateAIWorkloadConfigRequest,
    SageMakerCreateAIWorkloadConfigResponse,
    SageMakerCreateActionRequest,
    SageMakerCreateActionResponse,
    SageMakerCreateAlgorithmRequest,
    SageMakerCreateAlgorithmResponse,
    SageMakerCreateAppImageConfigRequest,
    SageMakerCreateAppImageConfigResponse,
    SageMakerCreateAppRequest,
    SageMakerCreateAppResponse,
    SageMakerCreateArtifactRequest,
    SageMakerCreateArtifactResponse,
    SageMakerCreateAutoMLJobRequest,
    SageMakerCreateAutoMLJobResponse,
    SageMakerCreateAutoMLJobV2Request,
    SageMakerCreateAutoMLJobV2Response,
    SageMakerCreateClusterExtensionRequest,
    SageMakerCreateClusterExtensionResponse,
    SageMakerCreateClusterRequest,
    SageMakerCreateClusterResponse,
    SageMakerCreateClusterSchedulerConfigRequest,
    SageMakerCreateClusterSchedulerConfigResponse,
    SageMakerCreateCodeRepositoryRequest,
    SageMakerCreateCodeRepositoryResponse,
    SageMakerCreateCompilationJobRequest,
    SageMakerCreateCompilationJobResponse,
    SageMakerCreateComputeQuotaRequest,
    SageMakerCreateComputeQuotaResponse,
    SageMakerCreateContextRequest,
    SageMakerCreateContextResponse,
    SageMakerCreateDataQualityJobDefinitionRequest,
    SageMakerCreateDataQualityJobDefinitionResponse,
    SageMakerCreateDeviceFleetRequest,
    SageMakerCreateDeviceFleetResponse,
    SageMakerCreateDomainRequest,
    SageMakerCreateDomainResponse,
    SageMakerCreateEdgeDeploymentPlanRequest,
    SageMakerCreateEdgeDeploymentPlanResponse,
    SageMakerCreateEdgeDeploymentStageRequest,
    SageMakerCreateEdgeDeploymentStageResponse,
    SageMakerCreateEdgePackagingJobRequest,
    SageMakerCreateEdgePackagingJobResponse,
    SageMakerCreateExperimentRequest,
    SageMakerCreateExperimentResponse,
    SageMakerCreateFeatureGroupRequest,
    SageMakerCreateFeatureGroupResponse,
    SageMakerCreateFlowDefinitionRequest,
    SageMakerCreateFlowDefinitionResponse,
    SageMakerCreateGlobalInferenceGatewayRequest,
    SageMakerCreateGlobalInferenceGatewayResponse,
    SageMakerCreateHubContentPresignedUrlsRequest,
    SageMakerCreateHubContentPresignedUrlsResponse,
    SageMakerCreateHubContentReferenceRequest,
    SageMakerCreateHubContentReferenceResponse,
    SageMakerCreateHubRequest,
    SageMakerCreateHubResponse,
    SageMakerCreateHumanTaskUiRequest,
    SageMakerCreateHumanTaskUiResponse,
    SageMakerCreateHyperParameterTuningJobRequest,
    SageMakerCreateHyperParameterTuningJobResponse,
    SageMakerCreateImageRequest,
    SageMakerCreateImageResponse,
    SageMakerCreateImageVersionRequest,
    SageMakerCreateImageVersionResponse,
    SageMakerCreateInferenceComponentRequest,
    SageMakerCreateInferenceComponentResponse,
    SageMakerCreateInferenceExperimentRequest,
    SageMakerCreateInferenceExperimentResponse,
    SageMakerCreateInferenceRecommendationsJobRequest,
    SageMakerCreateInferenceRecommendationsJobResponse,
    SageMakerCreateInferenceRouterRequest,
    SageMakerCreateInferenceRouterResponse,
    SageMakerCreateJobRequest,
    SageMakerCreateJobResponse,
    SageMakerCreateLabelingJobRequest,
    SageMakerCreateLabelingJobResponse,
    SageMakerCreateMlflowAppRequest,
    SageMakerCreateMlflowAppResponse,
    SageMakerCreateMlflowTrackingServerRequest,
    SageMakerCreateMlflowTrackingServerResponse,
    SageMakerCreateModelBiasJobDefinitionRequest,
    SageMakerCreateModelBiasJobDefinitionResponse,
    SageMakerCreateModelCardExportJobRequest,
    SageMakerCreateModelCardExportJobResponse,
    SageMakerCreateModelCardRequest,
    SageMakerCreateModelCardResponse,
    SageMakerCreateModelExplainabilityJobDefinitionRequest,
    SageMakerCreateModelExplainabilityJobDefinitionResponse,
    SageMakerCreateModelPackageGroupRequest,
    SageMakerCreateModelPackageGroupResponse,
    SageMakerCreateModelPackageRequest,
    SageMakerCreateModelPackageResponse,
    SageMakerCreateModelQualityJobDefinitionRequest,
    SageMakerCreateModelQualityJobDefinitionResponse,
    SageMakerCreateMonitoringScheduleRequest,
    SageMakerCreateMonitoringScheduleResponse,
    SageMakerCreateNotebookInstanceLifecycleConfigRequest,
    SageMakerCreateNotebookInstanceLifecycleConfigResponse,
    SageMakerCreateNotebookInstanceRequest,
    SageMakerCreateNotebookInstanceResponse,
    SageMakerCreateOptimizationJobRequest,
    SageMakerCreateOptimizationJobResponse,
    SageMakerCreatePartnerAppPresignedUrlRequest,
    SageMakerCreatePartnerAppPresignedUrlResponse,
    SageMakerCreatePartnerAppRequest,
    SageMakerCreatePartnerAppResponse,
    SageMakerCreatePipelineRequest,
    SageMakerCreatePipelineResponse,
    SageMakerCreatePresignedDomainUrlRequest,
    SageMakerCreatePresignedDomainUrlResponse,
    SageMakerCreatePresignedMlflowAppUrlRequest,
    SageMakerCreatePresignedMlflowAppUrlResponse,
    SageMakerCreatePresignedMlflowTrackingServerUrlRequest,
    SageMakerCreatePresignedMlflowTrackingServerUrlResponse,
    SageMakerCreatePresignedNotebookInstanceUrlRequest,
    SageMakerCreatePresignedNotebookInstanceUrlResponse,
    SageMakerCreateProcessingJobRequest,
    SageMakerCreateProcessingJobResponse,
    SageMakerCreateProjectRequest,
    SageMakerCreateProjectResponse,
    SageMakerCreateSpaceRequest,
    SageMakerCreateSpaceResponse,
    SageMakerCreateStudioLifecycleConfigRequest,
    SageMakerCreateStudioLifecycleConfigResponse,
    SageMakerCreateTrainingPlanRequest,
    SageMakerCreateTrainingPlanResponse,
    SageMakerCreateTrainingSessionRequest,
    SageMakerCreateTrainingSessionResponse,
    SageMakerCreateTransformJobRequest,
    SageMakerCreateTransformJobResponse,
    SageMakerCreateTrialComponentRequest,
    SageMakerCreateTrialComponentResponse,
    SageMakerCreateTrialRequest,
    SageMakerCreateTrialResponse,
    SageMakerCreateUserProfileRequest,
    SageMakerCreateUserProfileResponse,
    SageMakerCreateWorkforceRequest,
    SageMakerCreateWorkforceResponse,
    SageMakerCreateWorkteamRequest,
    SageMakerCreateWorkteamResponse,
    SageMakerDeleteAIBenchmarkJobRequest,
    SageMakerDeleteAIBenchmarkJobResponse,
    SageMakerDeleteAIRecommendationJobRequest,
    SageMakerDeleteAIRecommendationJobResponse,
    SageMakerDeleteAIWorkloadConfigRequest,
    SageMakerDeleteAIWorkloadConfigResponse,
    SageMakerDeleteActionRequest,
    SageMakerDeleteActionResponse,
    SageMakerDeleteAlgorithmRequest,
    SageMakerDeleteAlgorithmResponse,
    SageMakerDeleteAppImageConfigRequest,
    SageMakerDeleteAppImageConfigResponse,
    SageMakerDeleteAppRequest,
    SageMakerDeleteAppResponse,
    SageMakerDeleteArtifactRequest,
    SageMakerDeleteArtifactResponse,
    SageMakerDeleteAssociationRequest,
    SageMakerDeleteAssociationResponse,
    SageMakerDeleteClusterExtensionRequest,
    SageMakerDeleteClusterExtensionResponse,
    SageMakerDeleteClusterRequest,
    SageMakerDeleteClusterResponse,
    SageMakerDeleteClusterSchedulerConfigRequest,
    SageMakerDeleteClusterSchedulerConfigResponse,
    SageMakerDeleteCodeRepositoryRequest,
    SageMakerDeleteCodeRepositoryResponse,
    SageMakerDeleteCompilationJobRequest,
    SageMakerDeleteCompilationJobResponse,
    SageMakerDeleteComputeQuotaRequest,
    SageMakerDeleteComputeQuotaResponse,
    SageMakerDeleteContextRequest,
    SageMakerDeleteContextResponse,
    SageMakerDeleteDataQualityJobDefinitionRequest,
    SageMakerDeleteDataQualityJobDefinitionResponse,
    SageMakerDeleteDeviceFleetRequest,
    SageMakerDeleteDeviceFleetResponse,
    SageMakerDeleteDomainRequest,
    SageMakerDeleteDomainResponse,
    SageMakerDeleteEdgeDeploymentPlanRequest,
    SageMakerDeleteEdgeDeploymentPlanResponse,
    SageMakerDeleteEdgeDeploymentStageRequest,
    SageMakerDeleteEdgeDeploymentStageResponse,
    SageMakerDeleteEndpointPolicyRequest,
    SageMakerDeleteEndpointPolicyResponse,
    SageMakerDeleteExperimentRequest,
    SageMakerDeleteExperimentResponse,
    SageMakerDeleteFeatureGroupRequest,
    SageMakerDeleteFeatureGroupResponse,
    SageMakerDeleteFlowDefinitionRequest,
    SageMakerDeleteFlowDefinitionResponse,
    SageMakerDeleteGlobalInferenceGatewayRequest,
    SageMakerDeleteGlobalInferenceGatewayResponse,
    SageMakerDeleteHubContentReferenceRequest,
    SageMakerDeleteHubContentReferenceResponse,
    SageMakerDeleteHubContentRequest,
    SageMakerDeleteHubContentResponse,
    SageMakerDeleteHubRequest,
    SageMakerDeleteHubResponse,
    SageMakerDeleteHumanTaskUiRequest,
    SageMakerDeleteHumanTaskUiResponse,
    SageMakerDeleteHyperParameterTuningJobRequest,
    SageMakerDeleteHyperParameterTuningJobResponse,
    SageMakerDeleteImageRequest,
    SageMakerDeleteImageResponse,
    SageMakerDeleteImageVersionRequest,
    SageMakerDeleteImageVersionResponse,
    SageMakerDeleteInferenceComponentRequest,
    SageMakerDeleteInferenceComponentResponse,
    SageMakerDeleteInferenceExperimentRequest,
    SageMakerDeleteInferenceExperimentResponse,
    SageMakerDeleteInferenceRouterRequest,
    SageMakerDeleteInferenceRouterResponse,
    SageMakerDeleteJobRequest,
    SageMakerDeleteJobResponse,
    SageMakerDeleteMlflowAppRequest,
    SageMakerDeleteMlflowAppResponse,
    SageMakerDeleteMlflowTrackingServerRequest,
    SageMakerDeleteMlflowTrackingServerResponse,
    SageMakerDeleteModelBiasJobDefinitionRequest,
    SageMakerDeleteModelBiasJobDefinitionResponse,
    SageMakerDeleteModelCardRequest,
    SageMakerDeleteModelCardResponse,
    SageMakerDeleteModelExplainabilityJobDefinitionRequest,
    SageMakerDeleteModelExplainabilityJobDefinitionResponse,
    SageMakerDeleteModelPackageGroupPolicyRequest,
    SageMakerDeleteModelPackageGroupPolicyResponse,
    SageMakerDeleteModelPackageGroupRequest,
    SageMakerDeleteModelPackageGroupResponse,
    SageMakerDeleteModelPackageRequest,
    SageMakerDeleteModelPackageResponse,
    SageMakerDeleteModelQualityJobDefinitionRequest,
    SageMakerDeleteModelQualityJobDefinitionResponse,
    SageMakerDeleteMonitoringScheduleRequest,
    SageMakerDeleteMonitoringScheduleResponse,
    SageMakerDeleteNotebookInstanceLifecycleConfigRequest,
    SageMakerDeleteNotebookInstanceLifecycleConfigResponse,
    SageMakerDeleteNotebookInstanceRequest,
    SageMakerDeleteNotebookInstanceResponse,
    SageMakerDeleteOptimizationJobRequest,
    SageMakerDeleteOptimizationJobResponse,
    SageMakerDeletePartnerAppRequest,
    SageMakerDeletePartnerAppResponse,
    SageMakerDeletePipelineRequest,
    SageMakerDeletePipelineResponse,
    SageMakerDeleteProcessingJobRequest,
    SageMakerDeleteProcessingJobResponse,
    SageMakerDeleteProjectRequest,
    SageMakerDeleteProjectResponse,
    SageMakerDeleteSpaceRequest,
    SageMakerDeleteSpaceResponse,
    SageMakerDeleteStudioLifecycleConfigRequest,
    SageMakerDeleteStudioLifecycleConfigResponse,
    SageMakerDeleteTrainingJobRequest,
    SageMakerDeleteTrainingJobResponse,
    SageMakerDeleteTrainingSessionRequest,
    SageMakerDeleteTrainingSessionResponse,
    SageMakerDeleteTrialComponentRequest,
    SageMakerDeleteTrialComponentResponse,
    SageMakerDeleteTrialRequest,
    SageMakerDeleteTrialResponse,
    SageMakerDeleteUserProfileRequest,
    SageMakerDeleteUserProfileResponse,
    SageMakerDeleteWorkforceRequest,
    SageMakerDeleteWorkforceResponse,
    SageMakerDeleteWorkteamRequest,
    SageMakerDeleteWorkteamResponse,
    SageMakerDeregisterDevicesRequest,
    SageMakerDeregisterDevicesResponse,
    SageMakerDescribeAIBenchmarkJobRequest,
    SageMakerDescribeAIBenchmarkJobResponse,
    SageMakerDescribeAIRecommendationJobRequest,
    SageMakerDescribeAIRecommendationJobResponse,
    SageMakerDescribeAIWorkloadConfigRequest,
    SageMakerDescribeAIWorkloadConfigResponse,
    SageMakerDescribeActionRequest,
    SageMakerDescribeActionResponse,
    SageMakerDescribeAlgorithmRequest,
    SageMakerDescribeAlgorithmResponse,
    SageMakerDescribeAppImageConfigRequest,
    SageMakerDescribeAppImageConfigResponse,
    SageMakerDescribeAppRequest,
    SageMakerDescribeAppResponse,
    SageMakerDescribeArtifactRequest,
    SageMakerDescribeArtifactResponse,
    SageMakerDescribeAutoMLJobRequest,
    SageMakerDescribeAutoMLJobResponse,
    SageMakerDescribeAutoMLJobV2Request,
    SageMakerDescribeAutoMLJobV2Response,
    SageMakerDescribeCapacityReservationRequest,
    SageMakerDescribeCapacityReservationResponse,
    SageMakerDescribeClusterEventRequest,
    SageMakerDescribeClusterEventResponse,
    SageMakerDescribeClusterExtensionRequest,
    SageMakerDescribeClusterExtensionResponse,
    SageMakerDescribeClusterNodeRequest,
    SageMakerDescribeClusterNodeResponse,
    SageMakerDescribeClusterOperationRequest,
    SageMakerDescribeClusterOperationResponse,
    SageMakerDescribeClusterRequest,
    SageMakerDescribeClusterResponse,
    SageMakerDescribeClusterSchedulerConfigRequest,
    SageMakerDescribeClusterSchedulerConfigResponse,
    SageMakerDescribeCodeRepositoryRequest,
    SageMakerDescribeCodeRepositoryResponse,
    SageMakerDescribeCompilationJobRequest,
    SageMakerDescribeCompilationJobResponse,
    SageMakerDescribeComputeQuotaRequest,
    SageMakerDescribeComputeQuotaResponse,
    SageMakerDescribeContextRequest,
    SageMakerDescribeContextResponse,
    SageMakerDescribeDataQualityJobDefinitionRequest,
    SageMakerDescribeDataQualityJobDefinitionResponse,
    SageMakerDescribeDeviceFleetRequest,
    SageMakerDescribeDeviceFleetResponse,
    SageMakerDescribeDeviceRequest,
    SageMakerDescribeDeviceResponse,
    SageMakerDescribeDomainRequest,
    SageMakerDescribeDomainResponse,
    SageMakerDescribeEdgeDeploymentPlanRequest,
    SageMakerDescribeEdgeDeploymentPlanResponse,
    SageMakerDescribeEdgePackagingJobRequest,
    SageMakerDescribeEdgePackagingJobResponse,
    SageMakerDescribeExperimentRequest,
    SageMakerDescribeExperimentResponse,
    SageMakerDescribeFeatureGroupRequest,
    SageMakerDescribeFeatureGroupResponse,
    SageMakerDescribeFeatureMetadataRequest,
    SageMakerDescribeFeatureMetadataResponse,
    SageMakerDescribeFlowDefinitionRequest,
    SageMakerDescribeFlowDefinitionResponse,
    SageMakerDescribeGlobalInferenceGatewayRequest,
    SageMakerDescribeGlobalInferenceGatewayResponse,
    SageMakerDescribeHubContentRequest,
    SageMakerDescribeHubContentResponse,
    SageMakerDescribeHubRequest,
    SageMakerDescribeHubResponse,
    SageMakerDescribeHumanTaskUiRequest,
    SageMakerDescribeHumanTaskUiResponse,
    SageMakerDescribeHyperParameterTuningJobRequest,
    SageMakerDescribeHyperParameterTuningJobResponse,
    SageMakerDescribeImageRequest,
    SageMakerDescribeImageResponse,
    SageMakerDescribeImageVersionRequest,
    SageMakerDescribeImageVersionResponse,
    SageMakerDescribeInferenceComponentRequest,
    SageMakerDescribeInferenceComponentResponse,
    SageMakerDescribeInferenceExperimentRequest,
    SageMakerDescribeInferenceExperimentResponse,
    SageMakerDescribeInferenceRecommendationsJobRequest,
    SageMakerDescribeInferenceRecommendationsJobResponse,
    SageMakerDescribeInferenceRouterRequest,
    SageMakerDescribeInferenceRouterResponse,
    SageMakerDescribeJobRequest,
    SageMakerDescribeJobResponse,
    SageMakerDescribeJobSchemaVersionRequest,
    SageMakerDescribeJobSchemaVersionResponse,
    SageMakerDescribeLabelingJobRequest,
    SageMakerDescribeLabelingJobResponse,
    SageMakerDescribeLineageGroupRequest,
    SageMakerDescribeLineageGroupResponse,
    SageMakerDescribeMlflowAppRequest,
    SageMakerDescribeMlflowAppResponse,
    SageMakerDescribeMlflowTrackingServerRequest,
    SageMakerDescribeMlflowTrackingServerResponse,
    SageMakerDescribeModelBiasJobDefinitionRequest,
    SageMakerDescribeModelBiasJobDefinitionResponse,
    SageMakerDescribeModelCardExportJobRequest,
    SageMakerDescribeModelCardExportJobResponse,
    SageMakerDescribeModelCardRequest,
    SageMakerDescribeModelCardResponse,
    SageMakerDescribeModelExplainabilityJobDefinitionRequest,
    SageMakerDescribeModelExplainabilityJobDefinitionResponse,
    SageMakerDescribeModelPackageGroupRequest,
    SageMakerDescribeModelPackageGroupResponse,
    SageMakerDescribeModelPackageRequest,
    SageMakerDescribeModelPackageResponse,
    SageMakerDescribeModelQualityJobDefinitionRequest,
    SageMakerDescribeModelQualityJobDefinitionResponse,
    SageMakerDescribeMonitoringScheduleRequest,
    SageMakerDescribeMonitoringScheduleResponse,
    SageMakerDescribeNotebookInstanceLifecycleConfigRequest,
    SageMakerDescribeNotebookInstanceLifecycleConfigResponse,
    SageMakerDescribeOptimizationJobRequest,
    SageMakerDescribeOptimizationJobResponse,
    SageMakerDescribePartnerAppRequest,
    SageMakerDescribePartnerAppResponse,
    SageMakerDescribePipelineDefinitionForExecutionRequest,
    SageMakerDescribePipelineDefinitionForExecutionResponse,
    SageMakerDescribePipelineExecutionRequest,
    SageMakerDescribePipelineExecutionResponse,
    SageMakerDescribeProjectRequest,
    SageMakerDescribeProjectResponse,
    SageMakerDescribeReservedCapacityRequest,
    SageMakerDescribeReservedCapacityResponse,
    SageMakerDescribeResourceAssociationsRequest,
    SageMakerDescribeResourceAssociationsResponse,
    SageMakerDescribeSpaceRequest,
    SageMakerDescribeSpaceResponse,
    SageMakerDescribeStudioLifecycleConfigRequest,
    SageMakerDescribeStudioLifecycleConfigResponse,
    SageMakerDescribeSubscribedWorkteamRequest,
    SageMakerDescribeSubscribedWorkteamResponse,
    SageMakerDescribeTrainingPlanExtensionHistoryRequest,
    SageMakerDescribeTrainingPlanExtensionHistoryResponse,
    SageMakerDescribeTrainingPlanRequest,
    SageMakerDescribeTrainingPlanResponse,
    SageMakerDescribeTrainingSessionRequest,
    SageMakerDescribeTrainingSessionResponse,
    SageMakerDescribeTransformJobRequest,
    SageMakerDescribeTransformJobResponse,
    SageMakerDescribeTrialComponentRequest,
    SageMakerDescribeTrialComponentResponse,
    SageMakerDescribeTrialRequest,
    SageMakerDescribeTrialResponse,
    SageMakerDescribeUserProfileRequest,
    SageMakerDescribeUserProfileResponse,
    SageMakerDescribeWorkforceRequest,
    SageMakerDescribeWorkforceResponse,
    SageMakerDescribeWorkteamRequest,
    SageMakerDescribeWorkteamResponse,
    SageMakerDetachClusterNodeVolumeRequest,
    SageMakerDetachClusterNodeVolumeResponse,
    SageMakerDisableSagemakerServicecatalogPortfolioRequest,
    SageMakerDisableSagemakerServicecatalogPortfolioResponse,
    SageMakerDisassociateTrialComponentRequest,
    SageMakerDisassociateTrialComponentResponse,
    SageMakerEnableSagemakerServicecatalogPortfolioRequest,
    SageMakerEnableSagemakerServicecatalogPortfolioResponse,
    SageMakerExtendTrainingPlanRequest,
    SageMakerExtendTrainingPlanResponse,
    SageMakerGetCapacityReservationUsageRequest,
    SageMakerGetCapacityReservationUsageResponse,
    SageMakerGetDeviceFleetReportRequest,
    SageMakerGetDeviceFleetReportResponse,
    SageMakerGetEndpointPolicyRequest,
    SageMakerGetEndpointPolicyResponse,
    SageMakerGetLineageGroupPolicyRequest,
    SageMakerGetLineageGroupPolicyResponse,
    SageMakerGetModelPackageGroupPolicyRequest,
    SageMakerGetModelPackageGroupPolicyResponse,
    SageMakerGetSagemakerServicecatalogPortfolioStatusRequest,
    SageMakerGetSagemakerServicecatalogPortfolioStatusResponse,
    SageMakerGetScalingConfigurationRecommendationRequest,
    SageMakerGetScalingConfigurationRecommendationResponse,
    SageMakerGetSearchSuggestionsRequest,
    SageMakerGetSearchSuggestionsResponse,
    SageMakerImportHubContentRequest,
    SageMakerImportHubContentResponse,
    SageMakerListAIBenchmarkJobsRequest,
    SageMakerListAIBenchmarkJobsResponse,
    SageMakerListAIRecommendationJobsRequest,
    SageMakerListAIRecommendationJobsResponse,
    SageMakerListAIWorkloadConfigsRequest,
    SageMakerListAIWorkloadConfigsResponse,
    SageMakerListActionsRequest,
    SageMakerListActionsResponse,
    SageMakerListAlgorithmsRequest,
    SageMakerListAlgorithmsResponse,
    SageMakerListAliasesRequest,
    SageMakerListAliasesResponse,
    SageMakerListAppImageConfigsRequest,
    SageMakerListAppImageConfigsResponse,
    SageMakerListAppsRequest,
    SageMakerListAppsResponse,
    SageMakerListArtifactsRequest,
    SageMakerListArtifactsResponse,
    SageMakerListAssociationsRequest,
    SageMakerListAssociationsResponse,
    SageMakerListAutoMLJobsRequest,
    SageMakerListAutoMLJobsResponse,
    SageMakerListCandidatesForAutoMLJobRequest,
    SageMakerListCandidatesForAutoMLJobResponse,
    SageMakerListCapacityReservationsRequest,
    SageMakerListCapacityReservationsResponse,
    SageMakerListClusterEventsRequest,
    SageMakerListClusterEventsResponse,
    SageMakerListClusterExtensionVersionsRequest,
    SageMakerListClusterExtensionVersionsResponse,
    SageMakerListClusterExtensionsRequest,
    SageMakerListClusterExtensionsResponse,
    SageMakerListClusterNodesRequest,
    SageMakerListClusterNodesResponse,
    SageMakerListClusterOperationsRequest,
    SageMakerListClusterOperationsResponse,
    SageMakerListClusterSchedulerConfigsRequest,
    SageMakerListClusterSchedulerConfigsResponse,
    SageMakerListClustersRequest,
    SageMakerListClustersResponse,
    SageMakerListCodeRepositoriesRequest,
    SageMakerListCodeRepositoriesResponse,
    SageMakerListCompilationJobsRequest,
    SageMakerListCompilationJobsResponse,
    SageMakerListComputeQuotasRequest,
    SageMakerListComputeQuotasResponse,
    SageMakerListContextsRequest,
    SageMakerListContextsResponse,
    SageMakerListDataQualityJobDefinitionsRequest,
    SageMakerListDataQualityJobDefinitionsResponse,
    SageMakerListDeviceFleetsRequest,
    SageMakerListDeviceFleetsResponse,
    SageMakerListDevicesRequest,
    SageMakerListDevicesResponse,
    SageMakerListDomainsRequest,
    SageMakerListDomainsResponse,
    SageMakerListEdgeDeploymentPlansRequest,
    SageMakerListEdgeDeploymentPlansResponse,
    SageMakerListEdgePackagingJobsRequest,
    SageMakerListEdgePackagingJobsResponse,
    SageMakerListExperimentsRequest,
    SageMakerListExperimentsResponse,
    SageMakerListFeatureGroupsRequest,
    SageMakerListFeatureGroupsResponse,
    SageMakerListFlowDefinitionsRequest,
    SageMakerListFlowDefinitionsResponse,
    SageMakerListGlobalInferenceGatewaysRequest,
    SageMakerListGlobalInferenceGatewaysResponse,
    SageMakerListHubContentVersionsRequest,
    SageMakerListHubContentVersionsResponse,
    SageMakerListHubContentsRequest,
    SageMakerListHubContentsResponse,
    SageMakerListHubsRequest,
    SageMakerListHubsResponse,
    SageMakerListHumanTaskUisRequest,
    SageMakerListHumanTaskUisResponse,
    SageMakerListHyperParameterTuningJobsRequest,
    SageMakerListHyperParameterTuningJobsResponse,
    SageMakerListImageVersionsRequest,
    SageMakerListImageVersionsResponse,
    SageMakerListImagesRequest,
    SageMakerListImagesResponse,
    SageMakerListInferenceComponentsRequest,
    SageMakerListInferenceComponentsResponse,
    SageMakerListInferenceExperimentsRequest,
    SageMakerListInferenceExperimentsResponse,
    SageMakerListInferenceGatewaysRequest,
    SageMakerListInferenceGatewaysResponse,
    SageMakerListInferenceRecommendationsJobStepsRequest,
    SageMakerListInferenceRecommendationsJobStepsResponse,
    SageMakerListInferenceRecommendationsJobsRequest,
    SageMakerListInferenceRecommendationsJobsResponse,
    SageMakerListInferenceRoutersRequest,
    SageMakerListInferenceRoutersResponse,
    SageMakerListJobSchemaVersionsRequest,
    SageMakerListJobSchemaVersionsResponse,
    SageMakerListJobsRequest,
    SageMakerListJobsResponse,
    SageMakerListLabelingJobsForWorkteamRequest,
    SageMakerListLabelingJobsForWorkteamResponse,
    SageMakerListLabelingJobsRequest,
    SageMakerListLabelingJobsResponse,
    SageMakerListLineageGroupsRequest,
    SageMakerListLineageGroupsResponse,
    SageMakerListMlflowAppsRequest,
    SageMakerListMlflowAppsResponse,
    SageMakerListMlflowTrackingServersRequest,
    SageMakerListMlflowTrackingServersResponse,
    SageMakerListModelBiasJobDefinitionsRequest,
    SageMakerListModelBiasJobDefinitionsResponse,
    SageMakerListModelCardExportJobsRequest,
    SageMakerListModelCardExportJobsResponse,
    SageMakerListModelCardVersionsRequest,
    SageMakerListModelCardVersionsResponse,
    SageMakerListModelCardsRequest,
    SageMakerListModelCardsResponse,
    SageMakerListModelExplainabilityJobDefinitionsRequest,
    SageMakerListModelExplainabilityJobDefinitionsResponse,
    SageMakerListModelMetadataRequest,
    SageMakerListModelMetadataResponse,
    SageMakerListModelPackageGroupsRequest,
    SageMakerListModelPackageGroupsResponse,
    SageMakerListModelPackagesRequest,
    SageMakerListModelPackagesResponse,
    SageMakerListModelQualityJobDefinitionsRequest,
    SageMakerListModelQualityJobDefinitionsResponse,
    SageMakerListMonitoringAlertHistoryRequest,
    SageMakerListMonitoringAlertHistoryResponse,
    SageMakerListMonitoringAlertsRequest,
    SageMakerListMonitoringAlertsResponse,
    SageMakerListMonitoringExecutionsRequest,
    SageMakerListMonitoringExecutionsResponse,
    SageMakerListMonitoringSchedulesRequest,
    SageMakerListMonitoringSchedulesResponse,
    SageMakerListNotebookInstanceLifecycleConfigsRequest,
    SageMakerListNotebookInstanceLifecycleConfigsResponse,
    SageMakerListOptimizationJobsRequest,
    SageMakerListOptimizationJobsResponse,
    SageMakerListPartnerAppsRequest,
    SageMakerListPartnerAppsResponse,
    SageMakerListPipelineExecutionStepsRequest,
    SageMakerListPipelineExecutionStepsResponse,
    SageMakerListPipelineExecutionsRequest,
    SageMakerListPipelineExecutionsResponse,
    SageMakerListPipelineParametersForExecutionRequest,
    SageMakerListPipelineParametersForExecutionResponse,
    SageMakerListPipelineVersionsRequest,
    SageMakerListPipelineVersionsResponse,
    SageMakerListProjectsRequest,
    SageMakerListProjectsResponse,
    SageMakerListResourceCatalogsRequest,
    SageMakerListResourceCatalogsResponse,
    SageMakerListSpacesRequest,
    SageMakerListSpacesResponse,
    SageMakerListStageDevicesRequest,
    SageMakerListStageDevicesResponse,
    SageMakerListStudioLifecycleConfigsRequest,
    SageMakerListStudioLifecycleConfigsResponse,
    SageMakerListSubscribedWorkteamsRequest,
    SageMakerListSubscribedWorkteamsResponse,
    SageMakerListTrainingJobsForHyperParameterTuningJobRequest,
    SageMakerListTrainingJobsForHyperParameterTuningJobResponse,
    SageMakerListTrainingPlansRequest,
    SageMakerListTrainingPlansResponse,
    SageMakerListTrainingSessionsRequest,
    SageMakerListTrainingSessionsResponse,
    SageMakerListTransformJobsRequest,
    SageMakerListTransformJobsResponse,
    SageMakerListTrialComponentsRequest,
    SageMakerListTrialComponentsResponse,
    SageMakerListTrialsRequest,
    SageMakerListTrialsResponse,
    SageMakerListUltraServersByReservedCapacityRequest,
    SageMakerListUltraServersByReservedCapacityResponse,
    SageMakerListUserProfilesRequest,
    SageMakerListUserProfilesResponse,
    SageMakerListWorkforcesRequest,
    SageMakerListWorkforcesResponse,
    SageMakerListWorkteamsRequest,
    SageMakerListWorkteamsResponse,
    SageMakerMoveClusterNodesRequest,
    SageMakerMoveClusterNodesResponse,
    SageMakerPutEndpointPolicyRequest,
    SageMakerPutEndpointPolicyResponse,
    SageMakerPutModelPackageGroupPolicyRequest,
    SageMakerPutModelPackageGroupPolicyResponse,
    SageMakerQueryLineageRequest,
    SageMakerQueryLineageResponse,
    SageMakerRegisterDevicesRequest,
    SageMakerRegisterDevicesResponse,
    SageMakerRemoveInferenceGatewayRequest,
    SageMakerRemoveInferenceGatewayResponse,
    SageMakerRenderUiTemplateRequest,
    SageMakerRenderUiTemplateResponse,
    SageMakerRetryPipelineExecutionRequest,
    SageMakerRetryPipelineExecutionResponse,
    SageMakerSearchRequest,
    SageMakerSearchResponse,
    SageMakerSearchTrainingPlanOfferingsRequest,
    SageMakerSearchTrainingPlanOfferingsResponse,
    SageMakerSendPipelineExecutionStepFailureRequest,
    SageMakerSendPipelineExecutionStepFailureResponse,
    SageMakerSendPipelineExecutionStepSuccessRequest,
    SageMakerSendPipelineExecutionStepSuccessResponse,
    SageMakerStartClusterHealthCheckRequest,
    SageMakerStartClusterHealthCheckResponse,
    SageMakerStartEdgeDeploymentStageRequest,
    SageMakerStartEdgeDeploymentStageResponse,
    SageMakerStartInferenceExperimentRequest,
    SageMakerStartInferenceExperimentResponse,
    SageMakerStartMlflowTrackingServerRequest,
    SageMakerStartMlflowTrackingServerResponse,
    SageMakerStartMonitoringScheduleRequest,
    SageMakerStartMonitoringScheduleResponse,
    SageMakerStartSessionRequest,
    SageMakerStartSessionResponse,
    SageMakerStopAIBenchmarkJobRequest,
    SageMakerStopAIBenchmarkJobResponse,
    SageMakerStopAIRecommendationJobRequest,
    SageMakerStopAIRecommendationJobResponse,
    SageMakerStopAutoMLJobRequest,
    SageMakerStopAutoMLJobResponse,
    SageMakerStopCompilationJobRequest,
    SageMakerStopCompilationJobResponse,
    SageMakerStopEdgeDeploymentStageRequest,
    SageMakerStopEdgeDeploymentStageResponse,
    SageMakerStopEdgePackagingJobRequest,
    SageMakerStopEdgePackagingJobResponse,
    SageMakerStopHyperParameterTuningJobRequest,
    SageMakerStopHyperParameterTuningJobResponse,
    SageMakerStopInferenceExperimentRequest,
    SageMakerStopInferenceExperimentResponse,
    SageMakerStopInferenceRecommendationsJobRequest,
    SageMakerStopInferenceRecommendationsJobResponse,
    SageMakerStopJobRequest,
    SageMakerStopJobResponse,
    SageMakerStopLabelingJobRequest,
    SageMakerStopLabelingJobResponse,
    SageMakerStopMlflowTrackingServerRequest,
    SageMakerStopMlflowTrackingServerResponse,
    SageMakerStopMonitoringScheduleRequest,
    SageMakerStopMonitoringScheduleResponse,
    SageMakerStopOptimizationJobRequest,
    SageMakerStopOptimizationJobResponse,
    SageMakerStopPipelineExecutionRequest,
    SageMakerStopPipelineExecutionResponse,
    SageMakerStopTrainingSessionRequest,
    SageMakerStopTrainingSessionResponse,
    SageMakerStopTransformJobRequest,
    SageMakerStopTransformJobResponse,
    SageMakerUpdateActionRequest,
    SageMakerUpdateActionResponse,
    SageMakerUpdateAppImageConfigRequest,
    SageMakerUpdateAppImageConfigResponse,
    SageMakerUpdateArtifactRequest,
    SageMakerUpdateArtifactResponse,
    SageMakerUpdateClusterExtensionRequest,
    SageMakerUpdateClusterExtensionResponse,
    SageMakerUpdateClusterRequest,
    SageMakerUpdateClusterResponse,
    SageMakerUpdateClusterSchedulerConfigRequest,
    SageMakerUpdateClusterSchedulerConfigResponse,
    SageMakerUpdateClusterSoftwareRequest,
    SageMakerUpdateClusterSoftwareResponse,
    SageMakerUpdateCodeRepositoryRequest,
    SageMakerUpdateCodeRepositoryResponse,
    SageMakerUpdateComputeQuotaRequest,
    SageMakerUpdateComputeQuotaResponse,
    SageMakerUpdateContextRequest,
    SageMakerUpdateContextResponse,
    SageMakerUpdateDeviceFleetRequest,
    SageMakerUpdateDeviceFleetResponse,
    SageMakerUpdateDevicesRequest,
    SageMakerUpdateDevicesResponse,
    SageMakerUpdateDomainRequest,
    SageMakerUpdateDomainResponse,
    SageMakerUpdateEndpointWeightsAndCapacitiesRequest,
    SageMakerUpdateEndpointWeightsAndCapacitiesResponse,
    SageMakerUpdateExperimentRequest,
    SageMakerUpdateExperimentResponse,
    SageMakerUpdateFeatureGroupRequest,
    SageMakerUpdateFeatureGroupResponse,
    SageMakerUpdateFeatureMetadataRequest,
    SageMakerUpdateFeatureMetadataResponse,
    SageMakerUpdateGlobalInferenceGatewayRequest,
    SageMakerUpdateGlobalInferenceGatewayResponse,
    SageMakerUpdateHubContentReferenceRequest,
    SageMakerUpdateHubContentReferenceResponse,
    SageMakerUpdateHubContentRequest,
    SageMakerUpdateHubContentResponse,
    SageMakerUpdateHubRequest,
    SageMakerUpdateHubResponse,
    SageMakerUpdateImageRequest,
    SageMakerUpdateImageResponse,
    SageMakerUpdateImageVersionRequest,
    SageMakerUpdateImageVersionResponse,
    SageMakerUpdateInferenceComponentRequest,
    SageMakerUpdateInferenceComponentResponse,
    SageMakerUpdateInferenceComponentRuntimeConfigRequest,
    SageMakerUpdateInferenceComponentRuntimeConfigResponse,
    SageMakerUpdateInferenceExperimentRequest,
    SageMakerUpdateInferenceExperimentResponse,
    SageMakerUpdateInferenceRouterRequest,
    SageMakerUpdateInferenceRouterResponse,
    SageMakerUpdateMlflowAppRequest,
    SageMakerUpdateMlflowAppResponse,
    SageMakerUpdateMlflowTrackingServerRequest,
    SageMakerUpdateMlflowTrackingServerResponse,
    SageMakerUpdateModelCardRequest,
    SageMakerUpdateModelCardResponse,
    SageMakerUpdateModelPackageRequest,
    SageMakerUpdateModelPackageResponse,
    SageMakerUpdateMonitoringAlertRequest,
    SageMakerUpdateMonitoringAlertResponse,
    SageMakerUpdateMonitoringScheduleRequest,
    SageMakerUpdateMonitoringScheduleResponse,
    SageMakerUpdateNotebookInstanceLifecycleConfigRequest,
    SageMakerUpdateNotebookInstanceLifecycleConfigResponse,
    SageMakerUpdateNotebookInstanceRequest,
    SageMakerUpdateNotebookInstanceResponse,
    SageMakerUpdatePartnerAppRequest,
    SageMakerUpdatePartnerAppResponse,
    SageMakerUpdatePipelineExecutionRequest,
    SageMakerUpdatePipelineExecutionResponse,
    SageMakerUpdatePipelineRequest,
    SageMakerUpdatePipelineResponse,
    SageMakerUpdatePipelineVersionRequest,
    SageMakerUpdatePipelineVersionResponse,
    SageMakerUpdateProjectRequest,
    SageMakerUpdateProjectResponse,
    SageMakerUpdateSpaceRequest,
    SageMakerUpdateSpaceResponse,
    SageMakerUpdateTrainingJobRequest,
    SageMakerUpdateTrainingJobResponse,
    SageMakerUpdateTrialComponentRequest,
    SageMakerUpdateTrialComponentResponse,
    SageMakerUpdateTrialRequest,
    SageMakerUpdateTrialResponse,
    SageMakerUpdateUserProfileRequest,
    SageMakerUpdateUserProfileResponse,
    SageMakerUpdateWorkforceRequest,
    SageMakerUpdateWorkforceResponse,
    SageMakerUpdateWorkteamRequest,
    SageMakerUpdateWorkteamResponse,
)


class AWSSageMaker(AWSBaseService[SageMakerClient]):
    service_name = 'SageMaker'
    boto3_service_name = 'sagemaker'

    async def list_training_jobs(
        self,
        request: SageMakerListTrainingJobsRequest | None = None,
    ) -> SageMakerListTrainingJobsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_training_jobs,
            request,
            SageMakerListTrainingJobsResponse,
        )

    async def list_training_jobs_paginated(
        self,
        request: SageMakerListTrainingJobsRequest | None = None,
    ) -> list[SageMakerListTrainingJobsResponse]:
        self._require_client()
        return await self._paginate(
            'list_training_jobs',
            request,
            SageMakerListTrainingJobsResponse,
        )

    async def describe_training_job(
        self,
        request: SageMakerDescribeTrainingJobRequest,
    ) -> SageMakerDescribeTrainingJobResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_training_job,
            request,
            SageMakerDescribeTrainingJobResponse,
        )

    async def create_training_job(
        self,
        request: SageMakerCreateTrainingJobRequest,
    ) -> SageMakerCreateTrainingJobResponse:
        client = self._require_client()
        return await self._execute(
            client.create_training_job,
            request,
            SageMakerCreateTrainingJobResponse,
        )

    async def stop_training_job(
        self,
        request: SageMakerStopTrainingJobRequest,
    ) -> SageMakerStopTrainingJobResponse:
        client = self._require_client()
        return await self._execute(
            client.stop_training_job,
            request,
            SageMakerStopTrainingJobResponse,
        )

    async def list_processing_jobs(
        self,
        request: SageMakerListProcessingJobsRequest | None = None,
    ) -> SageMakerListProcessingJobsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_processing_jobs,
            request,
            SageMakerListProcessingJobsResponse,
        )

    async def list_processing_jobs_paginated(
        self,
        request: SageMakerListProcessingJobsRequest | None = None,
    ) -> list[SageMakerListProcessingJobsResponse]:
        self._require_client()
        return await self._paginate(
            'list_processing_jobs',
            request,
            SageMakerListProcessingJobsResponse,
        )

    async def describe_processing_job(
        self,
        request: SageMakerDescribeProcessingJobRequest,
    ) -> SageMakerDescribeProcessingJobResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_processing_job,
            request,
            SageMakerDescribeProcessingJobResponse,
        )

    async def stop_processing_job(
        self,
        request: SageMakerStopProcessingJobRequest,
    ) -> SageMakerStopProcessingJobResponse:
        client = self._require_client()
        return await self._execute(
            client.stop_processing_job,
            request,
            SageMakerStopProcessingJobResponse,
        )

    async def list_models(
        self,
        request: SageMakerListModelsRequest | None = None,
    ) -> SageMakerListModelsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_models,
            request,
            SageMakerListModelsResponse,
        )

    async def list_models_paginated(
        self,
        request: SageMakerListModelsRequest | None = None,
    ) -> list[SageMakerListModelsResponse]:
        self._require_client()
        return await self._paginate(
            'list_models',
            request,
            SageMakerListModelsResponse,
        )

    async def describe_model(
        self,
        request: SageMakerDescribeModelRequest,
    ) -> SageMakerDescribeModelResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_model,
            request,
            SageMakerDescribeModelResponse,
        )

    async def create_model(
        self,
        request: SageMakerCreateModelRequest,
    ) -> SageMakerCreateModelResponse:
        client = self._require_client()
        return await self._execute(
            client.create_model,
            request,
            SageMakerCreateModelResponse,
        )

    async def delete_model(
        self,
        request: SageMakerDeleteModelRequest,
    ) -> SageMakerDeleteModelResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_model,
            request,
            SageMakerDeleteModelResponse,
        )

    async def list_endpoint_configs(
        self,
        request: SageMakerListEndpointConfigsRequest | None = None,
    ) -> SageMakerListEndpointConfigsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_endpoint_configs,
            request,
            SageMakerListEndpointConfigsResponse,
        )

    async def list_endpoint_configs_paginated(
        self,
        request: SageMakerListEndpointConfigsRequest | None = None,
    ) -> list[SageMakerListEndpointConfigsResponse]:
        self._require_client()
        return await self._paginate(
            'list_endpoint_configs',
            request,
            SageMakerListEndpointConfigsResponse,
        )

    async def describe_endpoint_config(
        self,
        request: SageMakerDescribeEndpointConfigRequest,
    ) -> SageMakerDescribeEndpointConfigResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_endpoint_config,
            request,
            SageMakerDescribeEndpointConfigResponse,
        )

    async def create_endpoint_config(
        self,
        request: SageMakerCreateEndpointConfigRequest,
    ) -> SageMakerCreateEndpointConfigResponse:
        client = self._require_client()
        return await self._execute(
            client.create_endpoint_config,
            request,
            SageMakerCreateEndpointConfigResponse,
        )

    async def delete_endpoint_config(
        self,
        request: SageMakerDeleteEndpointConfigRequest,
    ) -> SageMakerDeleteEndpointConfigResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_endpoint_config,
            request,
            SageMakerDeleteEndpointConfigResponse,
        )

    async def list_endpoints(
        self,
        request: SageMakerListEndpointsRequest | None = None,
    ) -> SageMakerListEndpointsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_endpoints,
            request,
            SageMakerListEndpointsResponse,
        )

    async def list_endpoints_paginated(
        self,
        request: SageMakerListEndpointsRequest | None = None,
    ) -> list[SageMakerListEndpointsResponse]:
        self._require_client()
        return await self._paginate(
            'list_endpoints',
            request,
            SageMakerListEndpointsResponse,
        )

    async def describe_endpoint(
        self,
        request: SageMakerDescribeEndpointRequest,
    ) -> SageMakerDescribeEndpointResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_endpoint,
            request,
            SageMakerDescribeEndpointResponse,
        )

    async def create_endpoint(
        self,
        request: SageMakerCreateEndpointRequest,
    ) -> SageMakerCreateEndpointResponse:
        client = self._require_client()
        return await self._execute(
            client.create_endpoint,
            request,
            SageMakerCreateEndpointResponse,
        )

    async def update_endpoint(
        self,
        request: SageMakerUpdateEndpointRequest,
    ) -> SageMakerUpdateEndpointResponse:
        client = self._require_client()
        return await self._execute(
            client.update_endpoint,
            request,
            SageMakerUpdateEndpointResponse,
        )

    async def delete_endpoint(
        self,
        request: SageMakerDeleteEndpointRequest,
    ) -> SageMakerDeleteEndpointResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_endpoint,
            request,
            SageMakerDeleteEndpointResponse,
        )

    async def list_notebook_instances(
        self,
        request: SageMakerListNotebookInstancesRequest | None = None,
    ) -> SageMakerListNotebookInstancesResponse:
        client = self._require_client()
        return await self._execute(
            client.list_notebook_instances,
            request,
            SageMakerListNotebookInstancesResponse,
        )

    async def list_notebook_instances_paginated(
        self,
        request: SageMakerListNotebookInstancesRequest | None = None,
    ) -> list[SageMakerListNotebookInstancesResponse]:
        self._require_client()
        return await self._paginate(
            'list_notebook_instances',
            request,
            SageMakerListNotebookInstancesResponse,
        )

    async def describe_notebook_instance(
        self,
        request: SageMakerDescribeNotebookInstanceRequest,
    ) -> SageMakerDescribeNotebookInstanceResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_notebook_instance,
            request,
            SageMakerDescribeNotebookInstanceResponse,
        )

    async def start_notebook_instance(
        self,
        request: SageMakerStartNotebookInstanceRequest,
    ) -> SageMakerStartNotebookInstanceResponse:
        client = self._require_client()
        return await self._execute(
            client.start_notebook_instance,
            request,
            SageMakerStartNotebookInstanceResponse,
        )

    async def stop_notebook_instance(
        self,
        request: SageMakerStopNotebookInstanceRequest,
    ) -> SageMakerStopNotebookInstanceResponse:
        client = self._require_client()
        return await self._execute(
            client.stop_notebook_instance,
            request,
            SageMakerStopNotebookInstanceResponse,
        )

    async def list_pipelines(
        self,
        request: SageMakerListPipelinesRequest | None = None,
    ) -> SageMakerListPipelinesResponse:
        client = self._require_client()
        return await self._execute(
            client.list_pipelines,
            request,
            SageMakerListPipelinesResponse,
        )

    async def list_pipelines_paginated(
        self,
        request: SageMakerListPipelinesRequest | None = None,
    ) -> list[SageMakerListPipelinesResponse]:
        self._require_client()
        return await self._paginate(
            'list_pipelines',
            request,
            SageMakerListPipelinesResponse,
        )

    async def describe_pipeline(
        self,
        request: SageMakerDescribePipelineRequest,
    ) -> SageMakerDescribePipelineResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_pipeline,
            request,
            SageMakerDescribePipelineResponse,
        )

    async def start_pipeline_execution(
        self,
        request: SageMakerStartPipelineExecutionRequest,
    ) -> SageMakerStartPipelineExecutionResponse:
        client = self._require_client()
        return await self._execute(
            client.start_pipeline_execution,
            request,
            SageMakerStartPipelineExecutionResponse,
        )

    async def list_tags(
        self,
        request: SageMakerListTagsRequest,
    ) -> SageMakerListTagsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_tags,
            request,
            SageMakerListTagsResponse,
        )

    async def list_tags_paginated(
        self,
        request: SageMakerListTagsRequest,
    ) -> list[SageMakerListTagsResponse]:
        self._require_client()
        return await self._paginate(
            'list_tags',
            request,
            SageMakerListTagsResponse,
        )

    async def add_tags(
        self,
        request: SageMakerAddTagsRequest,
    ) -> SageMakerAddTagsResponse:
        client = self._require_client()
        return await self._execute(
            client.add_tags,
            request,
            SageMakerAddTagsResponse,
        )

    async def delete_tags(
        self,
        request: SageMakerDeleteTagsRequest,
    ) -> SageMakerDeleteTagsResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_tags,
            request,
            SageMakerDeleteTagsResponse,
        )

    async def add_association(
        self,
        request: SageMakerAddAssociationRequest,
    ) -> SageMakerAddAssociationResponse:
        client = self._require_client()
        return await self._execute(client.add_association, request, SageMakerAddAssociationResponse)

    async def add_inference_gateway(
        self,
        request: SageMakerAddInferenceGatewayRequest,
    ) -> SageMakerAddInferenceGatewayResponse:
        client = self._require_client()
        return await self._execute(client.add_inference_gateway, request, SageMakerAddInferenceGatewayResponse)

    async def associate_trial_component(
        self,
        request: SageMakerAssociateTrialComponentRequest,
    ) -> SageMakerAssociateTrialComponentResponse:
        client = self._require_client()
        return await self._execute(client.associate_trial_component, request, SageMakerAssociateTrialComponentResponse)

    async def attach_cluster_node_network_interface(
        self,
        request: SageMakerAttachClusterNodeNetworkInterfaceRequest,
    ) -> SageMakerAttachClusterNodeNetworkInterfaceResponse:
        client = self._require_client()
        return await self._execute(client.attach_cluster_node_network_interface, request, SageMakerAttachClusterNodeNetworkInterfaceResponse)

    async def attach_cluster_node_volume(
        self,
        request: SageMakerAttachClusterNodeVolumeRequest,
    ) -> SageMakerAttachClusterNodeVolumeResponse:
        client = self._require_client()
        return await self._execute(client.attach_cluster_node_volume, request, SageMakerAttachClusterNodeVolumeResponse)

    async def batch_add_cluster_nodes(
        self,
        request: SageMakerBatchAddClusterNodesRequest,
    ) -> SageMakerBatchAddClusterNodesResponse:
        client = self._require_client()
        return await self._execute(client.batch_add_cluster_nodes, request, SageMakerBatchAddClusterNodesResponse)

    async def batch_delete_cluster_nodes(
        self,
        request: SageMakerBatchDeleteClusterNodesRequest,
    ) -> SageMakerBatchDeleteClusterNodesResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_cluster_nodes, request, SageMakerBatchDeleteClusterNodesResponse)

    async def batch_describe_model_package(
        self,
        request: SageMakerBatchDescribeModelPackageRequest,
    ) -> SageMakerBatchDescribeModelPackageResponse:
        client = self._require_client()
        return await self._execute(client.batch_describe_model_package, request, SageMakerBatchDescribeModelPackageResponse)

    async def batch_reboot_cluster_nodes(
        self,
        request: SageMakerBatchRebootClusterNodesRequest,
    ) -> SageMakerBatchRebootClusterNodesResponse:
        client = self._require_client()
        return await self._execute(client.batch_reboot_cluster_nodes, request, SageMakerBatchRebootClusterNodesResponse)

    async def batch_replace_cluster_nodes(
        self,
        request: SageMakerBatchReplaceClusterNodesRequest,
    ) -> SageMakerBatchReplaceClusterNodesResponse:
        client = self._require_client()
        return await self._execute(client.batch_replace_cluster_nodes, request, SageMakerBatchReplaceClusterNodesResponse)

    async def create_ai_benchmark_job(
        self,
        request: SageMakerCreateAIBenchmarkJobRequest,
    ) -> SageMakerCreateAIBenchmarkJobResponse:
        client = self._require_client()
        return await self._execute(client.create_ai_benchmark_job, request, SageMakerCreateAIBenchmarkJobResponse)

    async def create_ai_recommendation_job(
        self,
        request: SageMakerCreateAIRecommendationJobRequest,
    ) -> SageMakerCreateAIRecommendationJobResponse:
        client = self._require_client()
        return await self._execute(client.create_ai_recommendation_job, request, SageMakerCreateAIRecommendationJobResponse)

    async def create_ai_workload_config(
        self,
        request: SageMakerCreateAIWorkloadConfigRequest,
    ) -> SageMakerCreateAIWorkloadConfigResponse:
        client = self._require_client()
        return await self._execute(client.create_ai_workload_config, request, SageMakerCreateAIWorkloadConfigResponse)

    async def create_action(
        self,
        request: SageMakerCreateActionRequest,
    ) -> SageMakerCreateActionResponse:
        client = self._require_client()
        return await self._execute(client.create_action, request, SageMakerCreateActionResponse)

    async def create_algorithm(
        self,
        request: SageMakerCreateAlgorithmRequest,
    ) -> SageMakerCreateAlgorithmResponse:
        client = self._require_client()
        return await self._execute(client.create_algorithm, request, SageMakerCreateAlgorithmResponse)

    async def create_app(
        self,
        request: SageMakerCreateAppRequest,
    ) -> SageMakerCreateAppResponse:
        client = self._require_client()
        return await self._execute(client.create_app, request, SageMakerCreateAppResponse)

    async def create_app_image_config(
        self,
        request: SageMakerCreateAppImageConfigRequest,
    ) -> SageMakerCreateAppImageConfigResponse:
        client = self._require_client()
        return await self._execute(client.create_app_image_config, request, SageMakerCreateAppImageConfigResponse)

    async def create_artifact(
        self,
        request: SageMakerCreateArtifactRequest,
    ) -> SageMakerCreateArtifactResponse:
        client = self._require_client()
        return await self._execute(client.create_artifact, request, SageMakerCreateArtifactResponse)

    async def create_auto_ml_job(
        self,
        request: SageMakerCreateAutoMLJobRequest,
    ) -> SageMakerCreateAutoMLJobResponse:
        client = self._require_client()
        return await self._execute(client.create_auto_ml_job, request, SageMakerCreateAutoMLJobResponse)

    async def create_auto_ml_job_v2(
        self,
        request: SageMakerCreateAutoMLJobV2Request,
    ) -> SageMakerCreateAutoMLJobV2Response:
        client = self._require_client()
        return await self._execute(client.create_auto_ml_job_v2, request, SageMakerCreateAutoMLJobV2Response)

    async def create_cluster(
        self,
        request: SageMakerCreateClusterRequest,
    ) -> SageMakerCreateClusterResponse:
        client = self._require_client()
        return await self._execute(client.create_cluster, request, SageMakerCreateClusterResponse)

    async def create_cluster_extension(
        self,
        request: SageMakerCreateClusterExtensionRequest,
    ) -> SageMakerCreateClusterExtensionResponse:
        client = self._require_client()
        return await self._execute(client.create_cluster_extension, request, SageMakerCreateClusterExtensionResponse)

    async def create_cluster_scheduler_config(
        self,
        request: SageMakerCreateClusterSchedulerConfigRequest,
    ) -> SageMakerCreateClusterSchedulerConfigResponse:
        client = self._require_client()
        return await self._execute(client.create_cluster_scheduler_config, request, SageMakerCreateClusterSchedulerConfigResponse)

    async def create_code_repository(
        self,
        request: SageMakerCreateCodeRepositoryRequest,
    ) -> SageMakerCreateCodeRepositoryResponse:
        client = self._require_client()
        return await self._execute(client.create_code_repository, request, SageMakerCreateCodeRepositoryResponse)

    async def create_compilation_job(
        self,
        request: SageMakerCreateCompilationJobRequest,
    ) -> SageMakerCreateCompilationJobResponse:
        client = self._require_client()
        return await self._execute(client.create_compilation_job, request, SageMakerCreateCompilationJobResponse)

    async def create_compute_quota(
        self,
        request: SageMakerCreateComputeQuotaRequest,
    ) -> SageMakerCreateComputeQuotaResponse:
        client = self._require_client()
        return await self._execute(client.create_compute_quota, request, SageMakerCreateComputeQuotaResponse)

    async def create_context(
        self,
        request: SageMakerCreateContextRequest,
    ) -> SageMakerCreateContextResponse:
        client = self._require_client()
        return await self._execute(client.create_context, request, SageMakerCreateContextResponse)

    async def create_data_quality_job_definition(
        self,
        request: SageMakerCreateDataQualityJobDefinitionRequest,
    ) -> SageMakerCreateDataQualityJobDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.create_data_quality_job_definition, request, SageMakerCreateDataQualityJobDefinitionResponse)

    async def create_device_fleet(
        self,
        request: SageMakerCreateDeviceFleetRequest,
    ) -> SageMakerCreateDeviceFleetResponse:
        client = self._require_client()
        return await self._execute(client.create_device_fleet, request, SageMakerCreateDeviceFleetResponse)

    async def create_domain(
        self,
        request: SageMakerCreateDomainRequest,
    ) -> SageMakerCreateDomainResponse:
        client = self._require_client()
        return await self._execute(client.create_domain, request, SageMakerCreateDomainResponse)

    async def create_edge_deployment_plan(
        self,
        request: SageMakerCreateEdgeDeploymentPlanRequest,
    ) -> SageMakerCreateEdgeDeploymentPlanResponse:
        client = self._require_client()
        return await self._execute(client.create_edge_deployment_plan, request, SageMakerCreateEdgeDeploymentPlanResponse)

    async def create_edge_deployment_stage(
        self,
        request: SageMakerCreateEdgeDeploymentStageRequest,
    ) -> SageMakerCreateEdgeDeploymentStageResponse:
        client = self._require_client()
        return await self._execute(client.create_edge_deployment_stage, request, SageMakerCreateEdgeDeploymentStageResponse)

    async def create_edge_packaging_job(
        self,
        request: SageMakerCreateEdgePackagingJobRequest,
    ) -> SageMakerCreateEdgePackagingJobResponse:
        client = self._require_client()
        return await self._execute(client.create_edge_packaging_job, request, SageMakerCreateEdgePackagingJobResponse)

    async def create_experiment(
        self,
        request: SageMakerCreateExperimentRequest,
    ) -> SageMakerCreateExperimentResponse:
        client = self._require_client()
        return await self._execute(client.create_experiment, request, SageMakerCreateExperimentResponse)

    async def create_feature_group(
        self,
        request: SageMakerCreateFeatureGroupRequest,
    ) -> SageMakerCreateFeatureGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_feature_group, request, SageMakerCreateFeatureGroupResponse)

    async def create_flow_definition(
        self,
        request: SageMakerCreateFlowDefinitionRequest,
    ) -> SageMakerCreateFlowDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.create_flow_definition, request, SageMakerCreateFlowDefinitionResponse)

    async def create_global_inference_gateway(
        self,
        request: SageMakerCreateGlobalInferenceGatewayRequest,
    ) -> SageMakerCreateGlobalInferenceGatewayResponse:
        client = self._require_client()
        return await self._execute(client.create_global_inference_gateway, request, SageMakerCreateGlobalInferenceGatewayResponse)

    async def create_hub(
        self,
        request: SageMakerCreateHubRequest,
    ) -> SageMakerCreateHubResponse:
        client = self._require_client()
        return await self._execute(client.create_hub, request, SageMakerCreateHubResponse)

    async def create_hub_content_presigned_urls(
        self,
        request: SageMakerCreateHubContentPresignedUrlsRequest,
    ) -> SageMakerCreateHubContentPresignedUrlsResponse:
        client = self._require_client()
        return await self._execute(client.create_hub_content_presigned_urls, request, SageMakerCreateHubContentPresignedUrlsResponse)

    async def create_hub_content_presigned_urls_paginated(
        self,
        request: SageMakerCreateHubContentPresignedUrlsRequest,
    ) -> list[SageMakerCreateHubContentPresignedUrlsResponse]:
        return await self._paginate('create_hub_content_presigned_urls', request, SageMakerCreateHubContentPresignedUrlsResponse)

    async def create_hub_content_reference(
        self,
        request: SageMakerCreateHubContentReferenceRequest,
    ) -> SageMakerCreateHubContentReferenceResponse:
        client = self._require_client()
        return await self._execute(client.create_hub_content_reference, request, SageMakerCreateHubContentReferenceResponse)

    async def create_human_task_ui(
        self,
        request: SageMakerCreateHumanTaskUiRequest,
    ) -> SageMakerCreateHumanTaskUiResponse:
        client = self._require_client()
        return await self._execute(client.create_human_task_ui, request, SageMakerCreateHumanTaskUiResponse)

    async def create_hyper_parameter_tuning_job(
        self,
        request: SageMakerCreateHyperParameterTuningJobRequest,
    ) -> SageMakerCreateHyperParameterTuningJobResponse:
        client = self._require_client()
        return await self._execute(client.create_hyper_parameter_tuning_job, request, SageMakerCreateHyperParameterTuningJobResponse)

    async def create_image(
        self,
        request: SageMakerCreateImageRequest,
    ) -> SageMakerCreateImageResponse:
        client = self._require_client()
        return await self._execute(client.create_image, request, SageMakerCreateImageResponse)

    async def create_image_version(
        self,
        request: SageMakerCreateImageVersionRequest,
    ) -> SageMakerCreateImageVersionResponse:
        client = self._require_client()
        return await self._execute(client.create_image_version, request, SageMakerCreateImageVersionResponse)

    async def create_inference_component(
        self,
        request: SageMakerCreateInferenceComponentRequest,
    ) -> SageMakerCreateInferenceComponentResponse:
        client = self._require_client()
        return await self._execute(client.create_inference_component, request, SageMakerCreateInferenceComponentResponse)

    async def create_inference_experiment(
        self,
        request: SageMakerCreateInferenceExperimentRequest,
    ) -> SageMakerCreateInferenceExperimentResponse:
        client = self._require_client()
        return await self._execute(client.create_inference_experiment, request, SageMakerCreateInferenceExperimentResponse)

    async def create_inference_recommendations_job(
        self,
        request: SageMakerCreateInferenceRecommendationsJobRequest,
    ) -> SageMakerCreateInferenceRecommendationsJobResponse:
        client = self._require_client()
        return await self._execute(client.create_inference_recommendations_job, request, SageMakerCreateInferenceRecommendationsJobResponse)

    async def create_inference_router(
        self,
        request: SageMakerCreateInferenceRouterRequest,
    ) -> SageMakerCreateInferenceRouterResponse:
        client = self._require_client()
        return await self._execute(client.create_inference_router, request, SageMakerCreateInferenceRouterResponse)

    async def create_job(
        self,
        request: SageMakerCreateJobRequest,
    ) -> SageMakerCreateJobResponse:
        client = self._require_client()
        return await self._execute(client.create_job, request, SageMakerCreateJobResponse)

    async def create_labeling_job(
        self,
        request: SageMakerCreateLabelingJobRequest,
    ) -> SageMakerCreateLabelingJobResponse:
        client = self._require_client()
        return await self._execute(client.create_labeling_job, request, SageMakerCreateLabelingJobResponse)

    async def create_mlflow_app(
        self,
        request: SageMakerCreateMlflowAppRequest,
    ) -> SageMakerCreateMlflowAppResponse:
        client = self._require_client()
        return await self._execute(client.create_mlflow_app, request, SageMakerCreateMlflowAppResponse)

    async def create_mlflow_tracking_server(
        self,
        request: SageMakerCreateMlflowTrackingServerRequest,
    ) -> SageMakerCreateMlflowTrackingServerResponse:
        client = self._require_client()
        return await self._execute(client.create_mlflow_tracking_server, request, SageMakerCreateMlflowTrackingServerResponse)

    async def create_model_bias_job_definition(
        self,
        request: SageMakerCreateModelBiasJobDefinitionRequest,
    ) -> SageMakerCreateModelBiasJobDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.create_model_bias_job_definition, request, SageMakerCreateModelBiasJobDefinitionResponse)

    async def create_model_card(
        self,
        request: SageMakerCreateModelCardRequest,
    ) -> SageMakerCreateModelCardResponse:
        client = self._require_client()
        return await self._execute(client.create_model_card, request, SageMakerCreateModelCardResponse)

    async def create_model_card_export_job(
        self,
        request: SageMakerCreateModelCardExportJobRequest,
    ) -> SageMakerCreateModelCardExportJobResponse:
        client = self._require_client()
        return await self._execute(client.create_model_card_export_job, request, SageMakerCreateModelCardExportJobResponse)

    async def create_model_explainability_job_definition(
        self,
        request: SageMakerCreateModelExplainabilityJobDefinitionRequest,
    ) -> SageMakerCreateModelExplainabilityJobDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.create_model_explainability_job_definition, request, SageMakerCreateModelExplainabilityJobDefinitionResponse)

    async def create_model_package(
        self,
        request: SageMakerCreateModelPackageRequest | None = None,
    ) -> SageMakerCreateModelPackageResponse:
        client = self._require_client()
        return await self._execute(client.create_model_package, request, SageMakerCreateModelPackageResponse)

    async def create_model_package_group(
        self,
        request: SageMakerCreateModelPackageGroupRequest,
    ) -> SageMakerCreateModelPackageGroupResponse:
        client = self._require_client()
        return await self._execute(client.create_model_package_group, request, SageMakerCreateModelPackageGroupResponse)

    async def create_model_quality_job_definition(
        self,
        request: SageMakerCreateModelQualityJobDefinitionRequest,
    ) -> SageMakerCreateModelQualityJobDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.create_model_quality_job_definition, request, SageMakerCreateModelQualityJobDefinitionResponse)

    async def create_monitoring_schedule(
        self,
        request: SageMakerCreateMonitoringScheduleRequest,
    ) -> SageMakerCreateMonitoringScheduleResponse:
        client = self._require_client()
        return await self._execute(client.create_monitoring_schedule, request, SageMakerCreateMonitoringScheduleResponse)

    async def create_notebook_instance(
        self,
        request: SageMakerCreateNotebookInstanceRequest,
    ) -> SageMakerCreateNotebookInstanceResponse:
        client = self._require_client()
        return await self._execute(client.create_notebook_instance, request, SageMakerCreateNotebookInstanceResponse)

    async def create_notebook_instance_lifecycle_config(
        self,
        request: SageMakerCreateNotebookInstanceLifecycleConfigRequest,
    ) -> SageMakerCreateNotebookInstanceLifecycleConfigResponse:
        client = self._require_client()
        return await self._execute(client.create_notebook_instance_lifecycle_config, request, SageMakerCreateNotebookInstanceLifecycleConfigResponse)

    async def create_optimization_job(
        self,
        request: SageMakerCreateOptimizationJobRequest,
    ) -> SageMakerCreateOptimizationJobResponse:
        client = self._require_client()
        return await self._execute(client.create_optimization_job, request, SageMakerCreateOptimizationJobResponse)

    async def create_partner_app(
        self,
        request: SageMakerCreatePartnerAppRequest,
    ) -> SageMakerCreatePartnerAppResponse:
        client = self._require_client()
        return await self._execute(client.create_partner_app, request, SageMakerCreatePartnerAppResponse)

    async def create_partner_app_presigned_url(
        self,
        request: SageMakerCreatePartnerAppPresignedUrlRequest,
    ) -> SageMakerCreatePartnerAppPresignedUrlResponse:
        client = self._require_client()
        return await self._execute(client.create_partner_app_presigned_url, request, SageMakerCreatePartnerAppPresignedUrlResponse)

    async def create_pipeline(
        self,
        request: SageMakerCreatePipelineRequest,
    ) -> SageMakerCreatePipelineResponse:
        client = self._require_client()
        return await self._execute(client.create_pipeline, request, SageMakerCreatePipelineResponse)

    async def create_presigned_domain_url(
        self,
        request: SageMakerCreatePresignedDomainUrlRequest,
    ) -> SageMakerCreatePresignedDomainUrlResponse:
        client = self._require_client()
        return await self._execute(client.create_presigned_domain_url, request, SageMakerCreatePresignedDomainUrlResponse)

    async def create_presigned_mlflow_app_url(
        self,
        request: SageMakerCreatePresignedMlflowAppUrlRequest,
    ) -> SageMakerCreatePresignedMlflowAppUrlResponse:
        client = self._require_client()
        return await self._execute(client.create_presigned_mlflow_app_url, request, SageMakerCreatePresignedMlflowAppUrlResponse)

    async def create_presigned_mlflow_tracking_server_url(
        self,
        request: SageMakerCreatePresignedMlflowTrackingServerUrlRequest,
    ) -> SageMakerCreatePresignedMlflowTrackingServerUrlResponse:
        client = self._require_client()
        return await self._execute(client.create_presigned_mlflow_tracking_server_url, request, SageMakerCreatePresignedMlflowTrackingServerUrlResponse)

    async def create_presigned_notebook_instance_url(
        self,
        request: SageMakerCreatePresignedNotebookInstanceUrlRequest,
    ) -> SageMakerCreatePresignedNotebookInstanceUrlResponse:
        client = self._require_client()
        return await self._execute(client.create_presigned_notebook_instance_url, request, SageMakerCreatePresignedNotebookInstanceUrlResponse)

    async def create_processing_job(
        self,
        request: SageMakerCreateProcessingJobRequest,
    ) -> SageMakerCreateProcessingJobResponse:
        client = self._require_client()
        return await self._execute(client.create_processing_job, request, SageMakerCreateProcessingJobResponse)

    async def create_project(
        self,
        request: SageMakerCreateProjectRequest,
    ) -> SageMakerCreateProjectResponse:
        client = self._require_client()
        return await self._execute(client.create_project, request, SageMakerCreateProjectResponse)

    async def create_space(
        self,
        request: SageMakerCreateSpaceRequest,
    ) -> SageMakerCreateSpaceResponse:
        client = self._require_client()
        return await self._execute(client.create_space, request, SageMakerCreateSpaceResponse)

    async def create_studio_lifecycle_config(
        self,
        request: SageMakerCreateStudioLifecycleConfigRequest,
    ) -> SageMakerCreateStudioLifecycleConfigResponse:
        client = self._require_client()
        return await self._execute(client.create_studio_lifecycle_config, request, SageMakerCreateStudioLifecycleConfigResponse)

    async def create_training_plan(
        self,
        request: SageMakerCreateTrainingPlanRequest,
    ) -> SageMakerCreateTrainingPlanResponse:
        client = self._require_client()
        return await self._execute(client.create_training_plan, request, SageMakerCreateTrainingPlanResponse)

    async def create_training_session(
        self,
        request: SageMakerCreateTrainingSessionRequest,
    ) -> SageMakerCreateTrainingSessionResponse:
        client = self._require_client()
        return await self._execute(client.create_training_session, request, SageMakerCreateTrainingSessionResponse)

    async def create_transform_job(
        self,
        request: SageMakerCreateTransformJobRequest,
    ) -> SageMakerCreateTransformJobResponse:
        client = self._require_client()
        return await self._execute(client.create_transform_job, request, SageMakerCreateTransformJobResponse)

    async def create_trial(
        self,
        request: SageMakerCreateTrialRequest,
    ) -> SageMakerCreateTrialResponse:
        client = self._require_client()
        return await self._execute(client.create_trial, request, SageMakerCreateTrialResponse)

    async def create_trial_component(
        self,
        request: SageMakerCreateTrialComponentRequest,
    ) -> SageMakerCreateTrialComponentResponse:
        client = self._require_client()
        return await self._execute(client.create_trial_component, request, SageMakerCreateTrialComponentResponse)

    async def create_user_profile(
        self,
        request: SageMakerCreateUserProfileRequest,
    ) -> SageMakerCreateUserProfileResponse:
        client = self._require_client()
        return await self._execute(client.create_user_profile, request, SageMakerCreateUserProfileResponse)

    async def create_workforce(
        self,
        request: SageMakerCreateWorkforceRequest,
    ) -> SageMakerCreateWorkforceResponse:
        client = self._require_client()
        return await self._execute(client.create_workforce, request, SageMakerCreateWorkforceResponse)

    async def create_workteam(
        self,
        request: SageMakerCreateWorkteamRequest,
    ) -> SageMakerCreateWorkteamResponse:
        client = self._require_client()
        return await self._execute(client.create_workteam, request, SageMakerCreateWorkteamResponse)

    async def delete_ai_benchmark_job(
        self,
        request: SageMakerDeleteAIBenchmarkJobRequest,
    ) -> SageMakerDeleteAIBenchmarkJobResponse:
        client = self._require_client()
        return await self._execute(client.delete_ai_benchmark_job, request, SageMakerDeleteAIBenchmarkJobResponse)

    async def delete_ai_recommendation_job(
        self,
        request: SageMakerDeleteAIRecommendationJobRequest,
    ) -> SageMakerDeleteAIRecommendationJobResponse:
        client = self._require_client()
        return await self._execute(client.delete_ai_recommendation_job, request, SageMakerDeleteAIRecommendationJobResponse)

    async def delete_ai_workload_config(
        self,
        request: SageMakerDeleteAIWorkloadConfigRequest,
    ) -> SageMakerDeleteAIWorkloadConfigResponse:
        client = self._require_client()
        return await self._execute(client.delete_ai_workload_config, request, SageMakerDeleteAIWorkloadConfigResponse)

    async def delete_action(
        self,
        request: SageMakerDeleteActionRequest,
    ) -> SageMakerDeleteActionResponse:
        client = self._require_client()
        return await self._execute(client.delete_action, request, SageMakerDeleteActionResponse)

    async def delete_algorithm(
        self,
        request: SageMakerDeleteAlgorithmRequest,
    ) -> SageMakerDeleteAlgorithmResponse:
        client = self._require_client()
        return await self._execute(client.delete_algorithm, request, SageMakerDeleteAlgorithmResponse)

    async def delete_app(
        self,
        request: SageMakerDeleteAppRequest,
    ) -> SageMakerDeleteAppResponse:
        client = self._require_client()
        return await self._execute(client.delete_app, request, SageMakerDeleteAppResponse)

    async def delete_app_image_config(
        self,
        request: SageMakerDeleteAppImageConfigRequest,
    ) -> SageMakerDeleteAppImageConfigResponse:
        client = self._require_client()
        return await self._execute(client.delete_app_image_config, request, SageMakerDeleteAppImageConfigResponse)

    async def delete_artifact(
        self,
        request: SageMakerDeleteArtifactRequest | None = None,
    ) -> SageMakerDeleteArtifactResponse:
        client = self._require_client()
        return await self._execute(client.delete_artifact, request, SageMakerDeleteArtifactResponse)

    async def delete_association(
        self,
        request: SageMakerDeleteAssociationRequest,
    ) -> SageMakerDeleteAssociationResponse:
        client = self._require_client()
        return await self._execute(client.delete_association, request, SageMakerDeleteAssociationResponse)

    async def delete_cluster(
        self,
        request: SageMakerDeleteClusterRequest,
    ) -> SageMakerDeleteClusterResponse:
        client = self._require_client()
        return await self._execute(client.delete_cluster, request, SageMakerDeleteClusterResponse)

    async def delete_cluster_extension(
        self,
        request: SageMakerDeleteClusterExtensionRequest,
    ) -> SageMakerDeleteClusterExtensionResponse:
        client = self._require_client()
        return await self._execute(client.delete_cluster_extension, request, SageMakerDeleteClusterExtensionResponse)

    async def delete_cluster_scheduler_config(
        self,
        request: SageMakerDeleteClusterSchedulerConfigRequest,
    ) -> SageMakerDeleteClusterSchedulerConfigResponse:
        client = self._require_client()
        return await self._execute(client.delete_cluster_scheduler_config, request, SageMakerDeleteClusterSchedulerConfigResponse)

    async def delete_code_repository(
        self,
        request: SageMakerDeleteCodeRepositoryRequest,
    ) -> SageMakerDeleteCodeRepositoryResponse:
        client = self._require_client()
        return await self._execute(client.delete_code_repository, request, SageMakerDeleteCodeRepositoryResponse)

    async def delete_compilation_job(
        self,
        request: SageMakerDeleteCompilationJobRequest,
    ) -> SageMakerDeleteCompilationJobResponse:
        client = self._require_client()
        return await self._execute(client.delete_compilation_job, request, SageMakerDeleteCompilationJobResponse)

    async def delete_compute_quota(
        self,
        request: SageMakerDeleteComputeQuotaRequest,
    ) -> SageMakerDeleteComputeQuotaResponse:
        client = self._require_client()
        return await self._execute(client.delete_compute_quota, request, SageMakerDeleteComputeQuotaResponse)

    async def delete_context(
        self,
        request: SageMakerDeleteContextRequest,
    ) -> SageMakerDeleteContextResponse:
        client = self._require_client()
        return await self._execute(client.delete_context, request, SageMakerDeleteContextResponse)

    async def delete_data_quality_job_definition(
        self,
        request: SageMakerDeleteDataQualityJobDefinitionRequest,
    ) -> SageMakerDeleteDataQualityJobDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.delete_data_quality_job_definition, request, SageMakerDeleteDataQualityJobDefinitionResponse)

    async def delete_device_fleet(
        self,
        request: SageMakerDeleteDeviceFleetRequest,
    ) -> SageMakerDeleteDeviceFleetResponse:
        client = self._require_client()
        return await self._execute(client.delete_device_fleet, request, SageMakerDeleteDeviceFleetResponse)

    async def delete_domain(
        self,
        request: SageMakerDeleteDomainRequest,
    ) -> SageMakerDeleteDomainResponse:
        client = self._require_client()
        return await self._execute(client.delete_domain, request, SageMakerDeleteDomainResponse)

    async def delete_edge_deployment_plan(
        self,
        request: SageMakerDeleteEdgeDeploymentPlanRequest,
    ) -> SageMakerDeleteEdgeDeploymentPlanResponse:
        client = self._require_client()
        return await self._execute(client.delete_edge_deployment_plan, request, SageMakerDeleteEdgeDeploymentPlanResponse)

    async def delete_edge_deployment_stage(
        self,
        request: SageMakerDeleteEdgeDeploymentStageRequest,
    ) -> SageMakerDeleteEdgeDeploymentStageResponse:
        client = self._require_client()
        return await self._execute(client.delete_edge_deployment_stage, request, SageMakerDeleteEdgeDeploymentStageResponse)

    async def delete_endpoint_policy(
        self,
        request: SageMakerDeleteEndpointPolicyRequest,
    ) -> SageMakerDeleteEndpointPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_endpoint_policy, request, SageMakerDeleteEndpointPolicyResponse)

    async def delete_experiment(
        self,
        request: SageMakerDeleteExperimentRequest,
    ) -> SageMakerDeleteExperimentResponse:
        client = self._require_client()
        return await self._execute(client.delete_experiment, request, SageMakerDeleteExperimentResponse)

    async def delete_feature_group(
        self,
        request: SageMakerDeleteFeatureGroupRequest,
    ) -> SageMakerDeleteFeatureGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_feature_group, request, SageMakerDeleteFeatureGroupResponse)

    async def delete_flow_definition(
        self,
        request: SageMakerDeleteFlowDefinitionRequest,
    ) -> SageMakerDeleteFlowDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.delete_flow_definition, request, SageMakerDeleteFlowDefinitionResponse)

    async def delete_global_inference_gateway(
        self,
        request: SageMakerDeleteGlobalInferenceGatewayRequest,
    ) -> SageMakerDeleteGlobalInferenceGatewayResponse:
        client = self._require_client()
        return await self._execute(client.delete_global_inference_gateway, request, SageMakerDeleteGlobalInferenceGatewayResponse)

    async def delete_hub(
        self,
        request: SageMakerDeleteHubRequest,
    ) -> SageMakerDeleteHubResponse:
        client = self._require_client()
        return await self._execute(client.delete_hub, request, SageMakerDeleteHubResponse)

    async def delete_hub_content(
        self,
        request: SageMakerDeleteHubContentRequest,
    ) -> SageMakerDeleteHubContentResponse:
        client = self._require_client()
        return await self._execute(client.delete_hub_content, request, SageMakerDeleteHubContentResponse)

    async def delete_hub_content_reference(
        self,
        request: SageMakerDeleteHubContentReferenceRequest,
    ) -> SageMakerDeleteHubContentReferenceResponse:
        client = self._require_client()
        return await self._execute(client.delete_hub_content_reference, request, SageMakerDeleteHubContentReferenceResponse)

    async def delete_human_task_ui(
        self,
        request: SageMakerDeleteHumanTaskUiRequest,
    ) -> SageMakerDeleteHumanTaskUiResponse:
        client = self._require_client()
        return await self._execute(client.delete_human_task_ui, request, SageMakerDeleteHumanTaskUiResponse)

    async def delete_hyper_parameter_tuning_job(
        self,
        request: SageMakerDeleteHyperParameterTuningJobRequest,
    ) -> SageMakerDeleteHyperParameterTuningJobResponse:
        client = self._require_client()
        return await self._execute(client.delete_hyper_parameter_tuning_job, request, SageMakerDeleteHyperParameterTuningJobResponse)

    async def delete_image(
        self,
        request: SageMakerDeleteImageRequest,
    ) -> SageMakerDeleteImageResponse:
        client = self._require_client()
        return await self._execute(client.delete_image, request, SageMakerDeleteImageResponse)

    async def delete_image_version(
        self,
        request: SageMakerDeleteImageVersionRequest,
    ) -> SageMakerDeleteImageVersionResponse:
        client = self._require_client()
        return await self._execute(client.delete_image_version, request, SageMakerDeleteImageVersionResponse)

    async def delete_inference_component(
        self,
        request: SageMakerDeleteInferenceComponentRequest,
    ) -> SageMakerDeleteInferenceComponentResponse:
        client = self._require_client()
        return await self._execute(client.delete_inference_component, request, SageMakerDeleteInferenceComponentResponse)

    async def delete_inference_experiment(
        self,
        request: SageMakerDeleteInferenceExperimentRequest,
    ) -> SageMakerDeleteInferenceExperimentResponse:
        client = self._require_client()
        return await self._execute(client.delete_inference_experiment, request, SageMakerDeleteInferenceExperimentResponse)

    async def delete_inference_router(
        self,
        request: SageMakerDeleteInferenceRouterRequest,
    ) -> SageMakerDeleteInferenceRouterResponse:
        client = self._require_client()
        return await self._execute(client.delete_inference_router, request, SageMakerDeleteInferenceRouterResponse)

    async def delete_job(
        self,
        request: SageMakerDeleteJobRequest,
    ) -> SageMakerDeleteJobResponse:
        client = self._require_client()
        return await self._execute(client.delete_job, request, SageMakerDeleteJobResponse)

    async def delete_mlflow_app(
        self,
        request: SageMakerDeleteMlflowAppRequest,
    ) -> SageMakerDeleteMlflowAppResponse:
        client = self._require_client()
        return await self._execute(client.delete_mlflow_app, request, SageMakerDeleteMlflowAppResponse)

    async def delete_mlflow_tracking_server(
        self,
        request: SageMakerDeleteMlflowTrackingServerRequest,
    ) -> SageMakerDeleteMlflowTrackingServerResponse:
        client = self._require_client()
        return await self._execute(client.delete_mlflow_tracking_server, request, SageMakerDeleteMlflowTrackingServerResponse)

    async def delete_model_bias_job_definition(
        self,
        request: SageMakerDeleteModelBiasJobDefinitionRequest,
    ) -> SageMakerDeleteModelBiasJobDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.delete_model_bias_job_definition, request, SageMakerDeleteModelBiasJobDefinitionResponse)

    async def delete_model_card(
        self,
        request: SageMakerDeleteModelCardRequest,
    ) -> SageMakerDeleteModelCardResponse:
        client = self._require_client()
        return await self._execute(client.delete_model_card, request, SageMakerDeleteModelCardResponse)

    async def delete_model_explainability_job_definition(
        self,
        request: SageMakerDeleteModelExplainabilityJobDefinitionRequest,
    ) -> SageMakerDeleteModelExplainabilityJobDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.delete_model_explainability_job_definition, request, SageMakerDeleteModelExplainabilityJobDefinitionResponse)

    async def delete_model_package(
        self,
        request: SageMakerDeleteModelPackageRequest,
    ) -> SageMakerDeleteModelPackageResponse:
        client = self._require_client()
        return await self._execute(client.delete_model_package, request, SageMakerDeleteModelPackageResponse)

    async def delete_model_package_group(
        self,
        request: SageMakerDeleteModelPackageGroupRequest,
    ) -> SageMakerDeleteModelPackageGroupResponse:
        client = self._require_client()
        return await self._execute(client.delete_model_package_group, request, SageMakerDeleteModelPackageGroupResponse)

    async def delete_model_package_group_policy(
        self,
        request: SageMakerDeleteModelPackageGroupPolicyRequest,
    ) -> SageMakerDeleteModelPackageGroupPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_model_package_group_policy, request, SageMakerDeleteModelPackageGroupPolicyResponse)

    async def delete_model_quality_job_definition(
        self,
        request: SageMakerDeleteModelQualityJobDefinitionRequest,
    ) -> SageMakerDeleteModelQualityJobDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.delete_model_quality_job_definition, request, SageMakerDeleteModelQualityJobDefinitionResponse)

    async def delete_monitoring_schedule(
        self,
        request: SageMakerDeleteMonitoringScheduleRequest,
    ) -> SageMakerDeleteMonitoringScheduleResponse:
        client = self._require_client()
        return await self._execute(client.delete_monitoring_schedule, request, SageMakerDeleteMonitoringScheduleResponse)

    async def delete_notebook_instance(
        self,
        request: SageMakerDeleteNotebookInstanceRequest,
    ) -> SageMakerDeleteNotebookInstanceResponse:
        client = self._require_client()
        return await self._execute(client.delete_notebook_instance, request, SageMakerDeleteNotebookInstanceResponse)

    async def delete_notebook_instance_lifecycle_config(
        self,
        request: SageMakerDeleteNotebookInstanceLifecycleConfigRequest,
    ) -> SageMakerDeleteNotebookInstanceLifecycleConfigResponse:
        client = self._require_client()
        return await self._execute(client.delete_notebook_instance_lifecycle_config, request, SageMakerDeleteNotebookInstanceLifecycleConfigResponse)

    async def delete_optimization_job(
        self,
        request: SageMakerDeleteOptimizationJobRequest,
    ) -> SageMakerDeleteOptimizationJobResponse:
        client = self._require_client()
        return await self._execute(client.delete_optimization_job, request, SageMakerDeleteOptimizationJobResponse)

    async def delete_partner_app(
        self,
        request: SageMakerDeletePartnerAppRequest,
    ) -> SageMakerDeletePartnerAppResponse:
        client = self._require_client()
        return await self._execute(client.delete_partner_app, request, SageMakerDeletePartnerAppResponse)

    async def delete_pipeline(
        self,
        request: SageMakerDeletePipelineRequest,
    ) -> SageMakerDeletePipelineResponse:
        client = self._require_client()
        return await self._execute(client.delete_pipeline, request, SageMakerDeletePipelineResponse)

    async def delete_processing_job(
        self,
        request: SageMakerDeleteProcessingJobRequest,
    ) -> SageMakerDeleteProcessingJobResponse:
        client = self._require_client()
        return await self._execute(client.delete_processing_job, request, SageMakerDeleteProcessingJobResponse)

    async def delete_project(
        self,
        request: SageMakerDeleteProjectRequest,
    ) -> SageMakerDeleteProjectResponse:
        client = self._require_client()
        return await self._execute(client.delete_project, request, SageMakerDeleteProjectResponse)

    async def delete_space(
        self,
        request: SageMakerDeleteSpaceRequest,
    ) -> SageMakerDeleteSpaceResponse:
        client = self._require_client()
        return await self._execute(client.delete_space, request, SageMakerDeleteSpaceResponse)

    async def delete_studio_lifecycle_config(
        self,
        request: SageMakerDeleteStudioLifecycleConfigRequest,
    ) -> SageMakerDeleteStudioLifecycleConfigResponse:
        client = self._require_client()
        return await self._execute(client.delete_studio_lifecycle_config, request, SageMakerDeleteStudioLifecycleConfigResponse)

    async def delete_training_job(
        self,
        request: SageMakerDeleteTrainingJobRequest,
    ) -> SageMakerDeleteTrainingJobResponse:
        client = self._require_client()
        return await self._execute(client.delete_training_job, request, SageMakerDeleteTrainingJobResponse)

    async def delete_training_session(
        self,
        request: SageMakerDeleteTrainingSessionRequest,
    ) -> SageMakerDeleteTrainingSessionResponse:
        client = self._require_client()
        return await self._execute(client.delete_training_session, request, SageMakerDeleteTrainingSessionResponse)

    async def delete_trial(
        self,
        request: SageMakerDeleteTrialRequest,
    ) -> SageMakerDeleteTrialResponse:
        client = self._require_client()
        return await self._execute(client.delete_trial, request, SageMakerDeleteTrialResponse)

    async def delete_trial_component(
        self,
        request: SageMakerDeleteTrialComponentRequest,
    ) -> SageMakerDeleteTrialComponentResponse:
        client = self._require_client()
        return await self._execute(client.delete_trial_component, request, SageMakerDeleteTrialComponentResponse)

    async def delete_user_profile(
        self,
        request: SageMakerDeleteUserProfileRequest,
    ) -> SageMakerDeleteUserProfileResponse:
        client = self._require_client()
        return await self._execute(client.delete_user_profile, request, SageMakerDeleteUserProfileResponse)

    async def delete_workforce(
        self,
        request: SageMakerDeleteWorkforceRequest,
    ) -> SageMakerDeleteWorkforceResponse:
        client = self._require_client()
        return await self._execute(client.delete_workforce, request, SageMakerDeleteWorkforceResponse)

    async def delete_workteam(
        self,
        request: SageMakerDeleteWorkteamRequest,
    ) -> SageMakerDeleteWorkteamResponse:
        client = self._require_client()
        return await self._execute(client.delete_workteam, request, SageMakerDeleteWorkteamResponse)

    async def deregister_devices(
        self,
        request: SageMakerDeregisterDevicesRequest,
    ) -> SageMakerDeregisterDevicesResponse:
        client = self._require_client()
        return await self._execute(client.deregister_devices, request, SageMakerDeregisterDevicesResponse)

    async def describe_ai_benchmark_job(
        self,
        request: SageMakerDescribeAIBenchmarkJobRequest,
    ) -> SageMakerDescribeAIBenchmarkJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_ai_benchmark_job, request, SageMakerDescribeAIBenchmarkJobResponse)

    async def describe_ai_recommendation_job(
        self,
        request: SageMakerDescribeAIRecommendationJobRequest,
    ) -> SageMakerDescribeAIRecommendationJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_ai_recommendation_job, request, SageMakerDescribeAIRecommendationJobResponse)

    async def describe_ai_workload_config(
        self,
        request: SageMakerDescribeAIWorkloadConfigRequest,
    ) -> SageMakerDescribeAIWorkloadConfigResponse:
        client = self._require_client()
        return await self._execute(client.describe_ai_workload_config, request, SageMakerDescribeAIWorkloadConfigResponse)

    async def describe_action(
        self,
        request: SageMakerDescribeActionRequest,
    ) -> SageMakerDescribeActionResponse:
        client = self._require_client()
        return await self._execute(client.describe_action, request, SageMakerDescribeActionResponse)

    async def describe_algorithm(
        self,
        request: SageMakerDescribeAlgorithmRequest,
    ) -> SageMakerDescribeAlgorithmResponse:
        client = self._require_client()
        return await self._execute(client.describe_algorithm, request, SageMakerDescribeAlgorithmResponse)

    async def describe_app(
        self,
        request: SageMakerDescribeAppRequest,
    ) -> SageMakerDescribeAppResponse:
        client = self._require_client()
        return await self._execute(client.describe_app, request, SageMakerDescribeAppResponse)

    async def describe_app_image_config(
        self,
        request: SageMakerDescribeAppImageConfigRequest,
    ) -> SageMakerDescribeAppImageConfigResponse:
        client = self._require_client()
        return await self._execute(client.describe_app_image_config, request, SageMakerDescribeAppImageConfigResponse)

    async def describe_artifact(
        self,
        request: SageMakerDescribeArtifactRequest,
    ) -> SageMakerDescribeArtifactResponse:
        client = self._require_client()
        return await self._execute(client.describe_artifact, request, SageMakerDescribeArtifactResponse)

    async def describe_auto_ml_job(
        self,
        request: SageMakerDescribeAutoMLJobRequest,
    ) -> SageMakerDescribeAutoMLJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_auto_ml_job, request, SageMakerDescribeAutoMLJobResponse)

    async def describe_auto_ml_job_v2(
        self,
        request: SageMakerDescribeAutoMLJobV2Request,
    ) -> SageMakerDescribeAutoMLJobV2Response:
        client = self._require_client()
        return await self._execute(client.describe_auto_ml_job_v2, request, SageMakerDescribeAutoMLJobV2Response)

    async def describe_capacity_reservation(
        self,
        request: SageMakerDescribeCapacityReservationRequest,
    ) -> SageMakerDescribeCapacityReservationResponse:
        client = self._require_client()
        return await self._execute(client.describe_capacity_reservation, request, SageMakerDescribeCapacityReservationResponse)

    async def describe_cluster(
        self,
        request: SageMakerDescribeClusterRequest,
    ) -> SageMakerDescribeClusterResponse:
        client = self._require_client()
        return await self._execute(client.describe_cluster, request, SageMakerDescribeClusterResponse)

    async def describe_cluster_event(
        self,
        request: SageMakerDescribeClusterEventRequest,
    ) -> SageMakerDescribeClusterEventResponse:
        client = self._require_client()
        return await self._execute(client.describe_cluster_event, request, SageMakerDescribeClusterEventResponse)

    async def describe_cluster_extension(
        self,
        request: SageMakerDescribeClusterExtensionRequest,
    ) -> SageMakerDescribeClusterExtensionResponse:
        client = self._require_client()
        return await self._execute(client.describe_cluster_extension, request, SageMakerDescribeClusterExtensionResponse)

    async def describe_cluster_node(
        self,
        request: SageMakerDescribeClusterNodeRequest,
    ) -> SageMakerDescribeClusterNodeResponse:
        client = self._require_client()
        return await self._execute(client.describe_cluster_node, request, SageMakerDescribeClusterNodeResponse)

    async def describe_cluster_operation(
        self,
        request: SageMakerDescribeClusterOperationRequest,
    ) -> SageMakerDescribeClusterOperationResponse:
        client = self._require_client()
        return await self._execute(client.describe_cluster_operation, request, SageMakerDescribeClusterOperationResponse)

    async def describe_cluster_scheduler_config(
        self,
        request: SageMakerDescribeClusterSchedulerConfigRequest,
    ) -> SageMakerDescribeClusterSchedulerConfigResponse:
        client = self._require_client()
        return await self._execute(client.describe_cluster_scheduler_config, request, SageMakerDescribeClusterSchedulerConfigResponse)

    async def describe_code_repository(
        self,
        request: SageMakerDescribeCodeRepositoryRequest,
    ) -> SageMakerDescribeCodeRepositoryResponse:
        client = self._require_client()
        return await self._execute(client.describe_code_repository, request, SageMakerDescribeCodeRepositoryResponse)

    async def describe_compilation_job(
        self,
        request: SageMakerDescribeCompilationJobRequest,
    ) -> SageMakerDescribeCompilationJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_compilation_job, request, SageMakerDescribeCompilationJobResponse)

    async def describe_compute_quota(
        self,
        request: SageMakerDescribeComputeQuotaRequest,
    ) -> SageMakerDescribeComputeQuotaResponse:
        client = self._require_client()
        return await self._execute(client.describe_compute_quota, request, SageMakerDescribeComputeQuotaResponse)

    async def describe_context(
        self,
        request: SageMakerDescribeContextRequest,
    ) -> SageMakerDescribeContextResponse:
        client = self._require_client()
        return await self._execute(client.describe_context, request, SageMakerDescribeContextResponse)

    async def describe_data_quality_job_definition(
        self,
        request: SageMakerDescribeDataQualityJobDefinitionRequest,
    ) -> SageMakerDescribeDataQualityJobDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.describe_data_quality_job_definition, request, SageMakerDescribeDataQualityJobDefinitionResponse)

    async def describe_device(
        self,
        request: SageMakerDescribeDeviceRequest,
    ) -> SageMakerDescribeDeviceResponse:
        client = self._require_client()
        return await self._execute(client.describe_device, request, SageMakerDescribeDeviceResponse)

    async def describe_device_fleet(
        self,
        request: SageMakerDescribeDeviceFleetRequest,
    ) -> SageMakerDescribeDeviceFleetResponse:
        client = self._require_client()
        return await self._execute(client.describe_device_fleet, request, SageMakerDescribeDeviceFleetResponse)

    async def describe_domain(
        self,
        request: SageMakerDescribeDomainRequest,
    ) -> SageMakerDescribeDomainResponse:
        client = self._require_client()
        return await self._execute(client.describe_domain, request, SageMakerDescribeDomainResponse)

    async def describe_edge_deployment_plan(
        self,
        request: SageMakerDescribeEdgeDeploymentPlanRequest,
    ) -> SageMakerDescribeEdgeDeploymentPlanResponse:
        client = self._require_client()
        return await self._execute(client.describe_edge_deployment_plan, request, SageMakerDescribeEdgeDeploymentPlanResponse)

    async def describe_edge_packaging_job(
        self,
        request: SageMakerDescribeEdgePackagingJobRequest,
    ) -> SageMakerDescribeEdgePackagingJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_edge_packaging_job, request, SageMakerDescribeEdgePackagingJobResponse)

    async def describe_experiment(
        self,
        request: SageMakerDescribeExperimentRequest,
    ) -> SageMakerDescribeExperimentResponse:
        client = self._require_client()
        return await self._execute(client.describe_experiment, request, SageMakerDescribeExperimentResponse)

    async def describe_feature_group(
        self,
        request: SageMakerDescribeFeatureGroupRequest,
    ) -> SageMakerDescribeFeatureGroupResponse:
        client = self._require_client()
        return await self._execute(client.describe_feature_group, request, SageMakerDescribeFeatureGroupResponse)

    async def describe_feature_metadata(
        self,
        request: SageMakerDescribeFeatureMetadataRequest,
    ) -> SageMakerDescribeFeatureMetadataResponse:
        client = self._require_client()
        return await self._execute(client.describe_feature_metadata, request, SageMakerDescribeFeatureMetadataResponse)

    async def describe_flow_definition(
        self,
        request: SageMakerDescribeFlowDefinitionRequest,
    ) -> SageMakerDescribeFlowDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.describe_flow_definition, request, SageMakerDescribeFlowDefinitionResponse)

    async def describe_global_inference_gateway(
        self,
        request: SageMakerDescribeGlobalInferenceGatewayRequest,
    ) -> SageMakerDescribeGlobalInferenceGatewayResponse:
        client = self._require_client()
        return await self._execute(client.describe_global_inference_gateway, request, SageMakerDescribeGlobalInferenceGatewayResponse)

    async def describe_hub(
        self,
        request: SageMakerDescribeHubRequest,
    ) -> SageMakerDescribeHubResponse:
        client = self._require_client()
        return await self._execute(client.describe_hub, request, SageMakerDescribeHubResponse)

    async def describe_hub_content(
        self,
        request: SageMakerDescribeHubContentRequest,
    ) -> SageMakerDescribeHubContentResponse:
        client = self._require_client()
        return await self._execute(client.describe_hub_content, request, SageMakerDescribeHubContentResponse)

    async def describe_human_task_ui(
        self,
        request: SageMakerDescribeHumanTaskUiRequest,
    ) -> SageMakerDescribeHumanTaskUiResponse:
        client = self._require_client()
        return await self._execute(client.describe_human_task_ui, request, SageMakerDescribeHumanTaskUiResponse)

    async def describe_hyper_parameter_tuning_job(
        self,
        request: SageMakerDescribeHyperParameterTuningJobRequest,
    ) -> SageMakerDescribeHyperParameterTuningJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_hyper_parameter_tuning_job, request, SageMakerDescribeHyperParameterTuningJobResponse)

    async def describe_image(
        self,
        request: SageMakerDescribeImageRequest,
    ) -> SageMakerDescribeImageResponse:
        client = self._require_client()
        return await self._execute(client.describe_image, request, SageMakerDescribeImageResponse)

    async def describe_image_version(
        self,
        request: SageMakerDescribeImageVersionRequest,
    ) -> SageMakerDescribeImageVersionResponse:
        client = self._require_client()
        return await self._execute(client.describe_image_version, request, SageMakerDescribeImageVersionResponse)

    async def describe_inference_component(
        self,
        request: SageMakerDescribeInferenceComponentRequest,
    ) -> SageMakerDescribeInferenceComponentResponse:
        client = self._require_client()
        return await self._execute(client.describe_inference_component, request, SageMakerDescribeInferenceComponentResponse)

    async def describe_inference_experiment(
        self,
        request: SageMakerDescribeInferenceExperimentRequest,
    ) -> SageMakerDescribeInferenceExperimentResponse:
        client = self._require_client()
        return await self._execute(client.describe_inference_experiment, request, SageMakerDescribeInferenceExperimentResponse)

    async def describe_inference_recommendations_job(
        self,
        request: SageMakerDescribeInferenceRecommendationsJobRequest,
    ) -> SageMakerDescribeInferenceRecommendationsJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_inference_recommendations_job, request, SageMakerDescribeInferenceRecommendationsJobResponse)

    async def describe_inference_router(
        self,
        request: SageMakerDescribeInferenceRouterRequest,
    ) -> SageMakerDescribeInferenceRouterResponse:
        client = self._require_client()
        return await self._execute(client.describe_inference_router, request, SageMakerDescribeInferenceRouterResponse)

    async def describe_job(
        self,
        request: SageMakerDescribeJobRequest,
    ) -> SageMakerDescribeJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_job, request, SageMakerDescribeJobResponse)

    async def describe_job_schema_version(
        self,
        request: SageMakerDescribeJobSchemaVersionRequest,
    ) -> SageMakerDescribeJobSchemaVersionResponse:
        client = self._require_client()
        return await self._execute(client.describe_job_schema_version, request, SageMakerDescribeJobSchemaVersionResponse)

    async def describe_labeling_job(
        self,
        request: SageMakerDescribeLabelingJobRequest,
    ) -> SageMakerDescribeLabelingJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_labeling_job, request, SageMakerDescribeLabelingJobResponse)

    async def describe_lineage_group(
        self,
        request: SageMakerDescribeLineageGroupRequest,
    ) -> SageMakerDescribeLineageGroupResponse:
        client = self._require_client()
        return await self._execute(client.describe_lineage_group, request, SageMakerDescribeLineageGroupResponse)

    async def describe_mlflow_app(
        self,
        request: SageMakerDescribeMlflowAppRequest,
    ) -> SageMakerDescribeMlflowAppResponse:
        client = self._require_client()
        return await self._execute(client.describe_mlflow_app, request, SageMakerDescribeMlflowAppResponse)

    async def describe_mlflow_tracking_server(
        self,
        request: SageMakerDescribeMlflowTrackingServerRequest,
    ) -> SageMakerDescribeMlflowTrackingServerResponse:
        client = self._require_client()
        return await self._execute(client.describe_mlflow_tracking_server, request, SageMakerDescribeMlflowTrackingServerResponse)

    async def describe_model_bias_job_definition(
        self,
        request: SageMakerDescribeModelBiasJobDefinitionRequest,
    ) -> SageMakerDescribeModelBiasJobDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.describe_model_bias_job_definition, request, SageMakerDescribeModelBiasJobDefinitionResponse)

    async def describe_model_card(
        self,
        request: SageMakerDescribeModelCardRequest,
    ) -> SageMakerDescribeModelCardResponse:
        client = self._require_client()
        return await self._execute(client.describe_model_card, request, SageMakerDescribeModelCardResponse)

    async def describe_model_card_export_job(
        self,
        request: SageMakerDescribeModelCardExportJobRequest,
    ) -> SageMakerDescribeModelCardExportJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_model_card_export_job, request, SageMakerDescribeModelCardExportJobResponse)

    async def describe_model_explainability_job_definition(
        self,
        request: SageMakerDescribeModelExplainabilityJobDefinitionRequest,
    ) -> SageMakerDescribeModelExplainabilityJobDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.describe_model_explainability_job_definition, request, SageMakerDescribeModelExplainabilityJobDefinitionResponse)

    async def describe_model_package(
        self,
        request: SageMakerDescribeModelPackageRequest,
    ) -> SageMakerDescribeModelPackageResponse:
        client = self._require_client()
        return await self._execute(client.describe_model_package, request, SageMakerDescribeModelPackageResponse)

    async def describe_model_package_group(
        self,
        request: SageMakerDescribeModelPackageGroupRequest,
    ) -> SageMakerDescribeModelPackageGroupResponse:
        client = self._require_client()
        return await self._execute(client.describe_model_package_group, request, SageMakerDescribeModelPackageGroupResponse)

    async def describe_model_quality_job_definition(
        self,
        request: SageMakerDescribeModelQualityJobDefinitionRequest,
    ) -> SageMakerDescribeModelQualityJobDefinitionResponse:
        client = self._require_client()
        return await self._execute(client.describe_model_quality_job_definition, request, SageMakerDescribeModelQualityJobDefinitionResponse)

    async def describe_monitoring_schedule(
        self,
        request: SageMakerDescribeMonitoringScheduleRequest,
    ) -> SageMakerDescribeMonitoringScheduleResponse:
        client = self._require_client()
        return await self._execute(client.describe_monitoring_schedule, request, SageMakerDescribeMonitoringScheduleResponse)

    async def describe_notebook_instance_lifecycle_config(
        self,
        request: SageMakerDescribeNotebookInstanceLifecycleConfigRequest,
    ) -> SageMakerDescribeNotebookInstanceLifecycleConfigResponse:
        client = self._require_client()
        return await self._execute(client.describe_notebook_instance_lifecycle_config, request, SageMakerDescribeNotebookInstanceLifecycleConfigResponse)

    async def describe_optimization_job(
        self,
        request: SageMakerDescribeOptimizationJobRequest,
    ) -> SageMakerDescribeOptimizationJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_optimization_job, request, SageMakerDescribeOptimizationJobResponse)

    async def describe_partner_app(
        self,
        request: SageMakerDescribePartnerAppRequest,
    ) -> SageMakerDescribePartnerAppResponse:
        client = self._require_client()
        return await self._execute(client.describe_partner_app, request, SageMakerDescribePartnerAppResponse)

    async def describe_pipeline_definition_for_execution(
        self,
        request: SageMakerDescribePipelineDefinitionForExecutionRequest,
    ) -> SageMakerDescribePipelineDefinitionForExecutionResponse:
        client = self._require_client()
        return await self._execute(client.describe_pipeline_definition_for_execution, request, SageMakerDescribePipelineDefinitionForExecutionResponse)

    async def describe_pipeline_execution(
        self,
        request: SageMakerDescribePipelineExecutionRequest,
    ) -> SageMakerDescribePipelineExecutionResponse:
        client = self._require_client()
        return await self._execute(client.describe_pipeline_execution, request, SageMakerDescribePipelineExecutionResponse)

    async def describe_project(
        self,
        request: SageMakerDescribeProjectRequest,
    ) -> SageMakerDescribeProjectResponse:
        client = self._require_client()
        return await self._execute(client.describe_project, request, SageMakerDescribeProjectResponse)

    async def describe_reserved_capacity(
        self,
        request: SageMakerDescribeReservedCapacityRequest,
    ) -> SageMakerDescribeReservedCapacityResponse:
        client = self._require_client()
        return await self._execute(client.describe_reserved_capacity, request, SageMakerDescribeReservedCapacityResponse)

    async def describe_resource_associations(
        self,
        request: SageMakerDescribeResourceAssociationsRequest,
    ) -> SageMakerDescribeResourceAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_resource_associations, request, SageMakerDescribeResourceAssociationsResponse)

    async def describe_resource_associations_paginated(
        self,
        request: SageMakerDescribeResourceAssociationsRequest,
    ) -> list[SageMakerDescribeResourceAssociationsResponse]:
        return await self._paginate('describe_resource_associations', request, SageMakerDescribeResourceAssociationsResponse)

    async def describe_space(
        self,
        request: SageMakerDescribeSpaceRequest,
    ) -> SageMakerDescribeSpaceResponse:
        client = self._require_client()
        return await self._execute(client.describe_space, request, SageMakerDescribeSpaceResponse)

    async def describe_studio_lifecycle_config(
        self,
        request: SageMakerDescribeStudioLifecycleConfigRequest,
    ) -> SageMakerDescribeStudioLifecycleConfigResponse:
        client = self._require_client()
        return await self._execute(client.describe_studio_lifecycle_config, request, SageMakerDescribeStudioLifecycleConfigResponse)

    async def describe_subscribed_workteam(
        self,
        request: SageMakerDescribeSubscribedWorkteamRequest,
    ) -> SageMakerDescribeSubscribedWorkteamResponse:
        client = self._require_client()
        return await self._execute(client.describe_subscribed_workteam, request, SageMakerDescribeSubscribedWorkteamResponse)

    async def describe_training_plan(
        self,
        request: SageMakerDescribeTrainingPlanRequest,
    ) -> SageMakerDescribeTrainingPlanResponse:
        client = self._require_client()
        return await self._execute(client.describe_training_plan, request, SageMakerDescribeTrainingPlanResponse)

    async def describe_training_plan_extension_history(
        self,
        request: SageMakerDescribeTrainingPlanExtensionHistoryRequest,
    ) -> SageMakerDescribeTrainingPlanExtensionHistoryResponse:
        client = self._require_client()
        return await self._execute(client.describe_training_plan_extension_history, request, SageMakerDescribeTrainingPlanExtensionHistoryResponse)

    async def describe_training_plan_extension_history_paginated(
        self,
        request: SageMakerDescribeTrainingPlanExtensionHistoryRequest,
    ) -> list[SageMakerDescribeTrainingPlanExtensionHistoryResponse]:
        return await self._paginate('describe_training_plan_extension_history', request, SageMakerDescribeTrainingPlanExtensionHistoryResponse)

    async def describe_training_session(
        self,
        request: SageMakerDescribeTrainingSessionRequest,
    ) -> SageMakerDescribeTrainingSessionResponse:
        client = self._require_client()
        return await self._execute(client.describe_training_session, request, SageMakerDescribeTrainingSessionResponse)

    async def describe_transform_job(
        self,
        request: SageMakerDescribeTransformJobRequest,
    ) -> SageMakerDescribeTransformJobResponse:
        client = self._require_client()
        return await self._execute(client.describe_transform_job, request, SageMakerDescribeTransformJobResponse)

    async def describe_trial(
        self,
        request: SageMakerDescribeTrialRequest,
    ) -> SageMakerDescribeTrialResponse:
        client = self._require_client()
        return await self._execute(client.describe_trial, request, SageMakerDescribeTrialResponse)

    async def describe_trial_component(
        self,
        request: SageMakerDescribeTrialComponentRequest,
    ) -> SageMakerDescribeTrialComponentResponse:
        client = self._require_client()
        return await self._execute(client.describe_trial_component, request, SageMakerDescribeTrialComponentResponse)

    async def describe_user_profile(
        self,
        request: SageMakerDescribeUserProfileRequest,
    ) -> SageMakerDescribeUserProfileResponse:
        client = self._require_client()
        return await self._execute(client.describe_user_profile, request, SageMakerDescribeUserProfileResponse)

    async def describe_workforce(
        self,
        request: SageMakerDescribeWorkforceRequest,
    ) -> SageMakerDescribeWorkforceResponse:
        client = self._require_client()
        return await self._execute(client.describe_workforce, request, SageMakerDescribeWorkforceResponse)

    async def describe_workteam(
        self,
        request: SageMakerDescribeWorkteamRequest,
    ) -> SageMakerDescribeWorkteamResponse:
        client = self._require_client()
        return await self._execute(client.describe_workteam, request, SageMakerDescribeWorkteamResponse)

    async def detach_cluster_node_volume(
        self,
        request: SageMakerDetachClusterNodeVolumeRequest,
    ) -> SageMakerDetachClusterNodeVolumeResponse:
        client = self._require_client()
        return await self._execute(client.detach_cluster_node_volume, request, SageMakerDetachClusterNodeVolumeResponse)

    async def disable_sagemaker_servicecatalog_portfolio(
        self,
        request: SageMakerDisableSagemakerServicecatalogPortfolioRequest | None = None,
    ) -> SageMakerDisableSagemakerServicecatalogPortfolioResponse:
        client = self._require_client()
        return await self._execute(client.disable_sagemaker_servicecatalog_portfolio, request, SageMakerDisableSagemakerServicecatalogPortfolioResponse)

    async def disassociate_trial_component(
        self,
        request: SageMakerDisassociateTrialComponentRequest,
    ) -> SageMakerDisassociateTrialComponentResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_trial_component, request, SageMakerDisassociateTrialComponentResponse)

    async def enable_sagemaker_servicecatalog_portfolio(
        self,
        request: SageMakerEnableSagemakerServicecatalogPortfolioRequest | None = None,
    ) -> SageMakerEnableSagemakerServicecatalogPortfolioResponse:
        client = self._require_client()
        return await self._execute(client.enable_sagemaker_servicecatalog_portfolio, request, SageMakerEnableSagemakerServicecatalogPortfolioResponse)

    async def extend_training_plan(
        self,
        request: SageMakerExtendTrainingPlanRequest,
    ) -> SageMakerExtendTrainingPlanResponse:
        client = self._require_client()
        return await self._execute(client.extend_training_plan, request, SageMakerExtendTrainingPlanResponse)

    async def get_capacity_reservation_usage(
        self,
        request: SageMakerGetCapacityReservationUsageRequest,
    ) -> SageMakerGetCapacityReservationUsageResponse:
        client = self._require_client()
        return await self._execute(client.get_capacity_reservation_usage, request, SageMakerGetCapacityReservationUsageResponse)

    async def get_capacity_reservation_usage_paginated(
        self,
        request: SageMakerGetCapacityReservationUsageRequest,
    ) -> list[SageMakerGetCapacityReservationUsageResponse]:
        return await self._paginate('get_capacity_reservation_usage', request, SageMakerGetCapacityReservationUsageResponse)

    async def get_device_fleet_report(
        self,
        request: SageMakerGetDeviceFleetReportRequest,
    ) -> SageMakerGetDeviceFleetReportResponse:
        client = self._require_client()
        return await self._execute(client.get_device_fleet_report, request, SageMakerGetDeviceFleetReportResponse)

    async def get_endpoint_policy(
        self,
        request: SageMakerGetEndpointPolicyRequest,
    ) -> SageMakerGetEndpointPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_endpoint_policy, request, SageMakerGetEndpointPolicyResponse)

    async def get_lineage_group_policy(
        self,
        request: SageMakerGetLineageGroupPolicyRequest,
    ) -> SageMakerGetLineageGroupPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_lineage_group_policy, request, SageMakerGetLineageGroupPolicyResponse)

    async def get_model_package_group_policy(
        self,
        request: SageMakerGetModelPackageGroupPolicyRequest,
    ) -> SageMakerGetModelPackageGroupPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_model_package_group_policy, request, SageMakerGetModelPackageGroupPolicyResponse)

    async def get_sagemaker_servicecatalog_portfolio_status(
        self,
        request: SageMakerGetSagemakerServicecatalogPortfolioStatusRequest | None = None,
    ) -> SageMakerGetSagemakerServicecatalogPortfolioStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_sagemaker_servicecatalog_portfolio_status, request, SageMakerGetSagemakerServicecatalogPortfolioStatusResponse)

    async def get_scaling_configuration_recommendation(
        self,
        request: SageMakerGetScalingConfigurationRecommendationRequest,
    ) -> SageMakerGetScalingConfigurationRecommendationResponse:
        client = self._require_client()
        return await self._execute(client.get_scaling_configuration_recommendation, request, SageMakerGetScalingConfigurationRecommendationResponse)

    async def get_search_suggestions(
        self,
        request: SageMakerGetSearchSuggestionsRequest,
    ) -> SageMakerGetSearchSuggestionsResponse:
        client = self._require_client()
        return await self._execute(client.get_search_suggestions, request, SageMakerGetSearchSuggestionsResponse)

    async def import_hub_content(
        self,
        request: SageMakerImportHubContentRequest,
    ) -> SageMakerImportHubContentResponse:
        client = self._require_client()
        return await self._execute(client.import_hub_content, request, SageMakerImportHubContentResponse)

    async def list_ai_benchmark_jobs(
        self,
        request: SageMakerListAIBenchmarkJobsRequest | None = None,
    ) -> SageMakerListAIBenchmarkJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_ai_benchmark_jobs, request, SageMakerListAIBenchmarkJobsResponse)

    async def list_ai_benchmark_jobs_paginated(
        self,
        request: SageMakerListAIBenchmarkJobsRequest | None = None,
    ) -> list[SageMakerListAIBenchmarkJobsResponse]:
        return await self._paginate('list_ai_benchmark_jobs', request, SageMakerListAIBenchmarkJobsResponse)

    async def list_ai_recommendation_jobs(
        self,
        request: SageMakerListAIRecommendationJobsRequest | None = None,
    ) -> SageMakerListAIRecommendationJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_ai_recommendation_jobs, request, SageMakerListAIRecommendationJobsResponse)

    async def list_ai_recommendation_jobs_paginated(
        self,
        request: SageMakerListAIRecommendationJobsRequest | None = None,
    ) -> list[SageMakerListAIRecommendationJobsResponse]:
        return await self._paginate('list_ai_recommendation_jobs', request, SageMakerListAIRecommendationJobsResponse)

    async def list_ai_workload_configs(
        self,
        request: SageMakerListAIWorkloadConfigsRequest | None = None,
    ) -> SageMakerListAIWorkloadConfigsResponse:
        client = self._require_client()
        return await self._execute(client.list_ai_workload_configs, request, SageMakerListAIWorkloadConfigsResponse)

    async def list_ai_workload_configs_paginated(
        self,
        request: SageMakerListAIWorkloadConfigsRequest | None = None,
    ) -> list[SageMakerListAIWorkloadConfigsResponse]:
        return await self._paginate('list_ai_workload_configs', request, SageMakerListAIWorkloadConfigsResponse)

    async def list_actions(
        self,
        request: SageMakerListActionsRequest | None = None,
    ) -> SageMakerListActionsResponse:
        client = self._require_client()
        return await self._execute(client.list_actions, request, SageMakerListActionsResponse)

    async def list_actions_paginated(
        self,
        request: SageMakerListActionsRequest | None = None,
    ) -> list[SageMakerListActionsResponse]:
        return await self._paginate('list_actions', request, SageMakerListActionsResponse)

    async def list_algorithms(
        self,
        request: SageMakerListAlgorithmsRequest | None = None,
    ) -> SageMakerListAlgorithmsResponse:
        client = self._require_client()
        return await self._execute(client.list_algorithms, request, SageMakerListAlgorithmsResponse)

    async def list_algorithms_paginated(
        self,
        request: SageMakerListAlgorithmsRequest | None = None,
    ) -> list[SageMakerListAlgorithmsResponse]:
        return await self._paginate('list_algorithms', request, SageMakerListAlgorithmsResponse)

    async def list_aliases(
        self,
        request: SageMakerListAliasesRequest,
    ) -> SageMakerListAliasesResponse:
        client = self._require_client()
        return await self._execute(client.list_aliases, request, SageMakerListAliasesResponse)

    async def list_aliases_paginated(
        self,
        request: SageMakerListAliasesRequest,
    ) -> list[SageMakerListAliasesResponse]:
        return await self._paginate('list_aliases', request, SageMakerListAliasesResponse)

    async def list_app_image_configs(
        self,
        request: SageMakerListAppImageConfigsRequest | None = None,
    ) -> SageMakerListAppImageConfigsResponse:
        client = self._require_client()
        return await self._execute(client.list_app_image_configs, request, SageMakerListAppImageConfigsResponse)

    async def list_app_image_configs_paginated(
        self,
        request: SageMakerListAppImageConfigsRequest | None = None,
    ) -> list[SageMakerListAppImageConfigsResponse]:
        return await self._paginate('list_app_image_configs', request, SageMakerListAppImageConfigsResponse)

    async def list_apps(
        self,
        request: SageMakerListAppsRequest | None = None,
    ) -> SageMakerListAppsResponse:
        client = self._require_client()
        return await self._execute(client.list_apps, request, SageMakerListAppsResponse)

    async def list_apps_paginated(
        self,
        request: SageMakerListAppsRequest | None = None,
    ) -> list[SageMakerListAppsResponse]:
        return await self._paginate('list_apps', request, SageMakerListAppsResponse)

    async def list_artifacts(
        self,
        request: SageMakerListArtifactsRequest | None = None,
    ) -> SageMakerListArtifactsResponse:
        client = self._require_client()
        return await self._execute(client.list_artifacts, request, SageMakerListArtifactsResponse)

    async def list_artifacts_paginated(
        self,
        request: SageMakerListArtifactsRequest | None = None,
    ) -> list[SageMakerListArtifactsResponse]:
        return await self._paginate('list_artifacts', request, SageMakerListArtifactsResponse)

    async def list_associations(
        self,
        request: SageMakerListAssociationsRequest | None = None,
    ) -> SageMakerListAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.list_associations, request, SageMakerListAssociationsResponse)

    async def list_associations_paginated(
        self,
        request: SageMakerListAssociationsRequest | None = None,
    ) -> list[SageMakerListAssociationsResponse]:
        return await self._paginate('list_associations', request, SageMakerListAssociationsResponse)

    async def list_auto_ml_jobs(
        self,
        request: SageMakerListAutoMLJobsRequest | None = None,
    ) -> SageMakerListAutoMLJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_auto_ml_jobs, request, SageMakerListAutoMLJobsResponse)

    async def list_auto_ml_jobs_paginated(
        self,
        request: SageMakerListAutoMLJobsRequest | None = None,
    ) -> list[SageMakerListAutoMLJobsResponse]:
        return await self._paginate('list_auto_ml_jobs', request, SageMakerListAutoMLJobsResponse)

    async def list_candidates_for_auto_ml_job(
        self,
        request: SageMakerListCandidatesForAutoMLJobRequest,
    ) -> SageMakerListCandidatesForAutoMLJobResponse:
        client = self._require_client()
        return await self._execute(client.list_candidates_for_auto_ml_job, request, SageMakerListCandidatesForAutoMLJobResponse)

    async def list_candidates_for_auto_ml_job_paginated(
        self,
        request: SageMakerListCandidatesForAutoMLJobRequest,
    ) -> list[SageMakerListCandidatesForAutoMLJobResponse]:
        return await self._paginate('list_candidates_for_auto_ml_job', request, SageMakerListCandidatesForAutoMLJobResponse)

    async def list_capacity_reservations(
        self,
        request: SageMakerListCapacityReservationsRequest | None = None,
    ) -> SageMakerListCapacityReservationsResponse:
        client = self._require_client()
        return await self._execute(client.list_capacity_reservations, request, SageMakerListCapacityReservationsResponse)

    async def list_capacity_reservations_paginated(
        self,
        request: SageMakerListCapacityReservationsRequest | None = None,
    ) -> list[SageMakerListCapacityReservationsResponse]:
        return await self._paginate('list_capacity_reservations', request, SageMakerListCapacityReservationsResponse)

    async def list_cluster_events(
        self,
        request: SageMakerListClusterEventsRequest,
    ) -> SageMakerListClusterEventsResponse:
        client = self._require_client()
        return await self._execute(client.list_cluster_events, request, SageMakerListClusterEventsResponse)

    async def list_cluster_events_paginated(
        self,
        request: SageMakerListClusterEventsRequest,
    ) -> list[SageMakerListClusterEventsResponse]:
        return await self._paginate('list_cluster_events', request, SageMakerListClusterEventsResponse)

    async def list_cluster_extension_versions(
        self,
        request: SageMakerListClusterExtensionVersionsRequest,
    ) -> SageMakerListClusterExtensionVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_cluster_extension_versions, request, SageMakerListClusterExtensionVersionsResponse)

    async def list_cluster_extension_versions_paginated(
        self,
        request: SageMakerListClusterExtensionVersionsRequest,
    ) -> list[SageMakerListClusterExtensionVersionsResponse]:
        return await self._paginate('list_cluster_extension_versions', request, SageMakerListClusterExtensionVersionsResponse)

    async def list_cluster_extensions(
        self,
        request: SageMakerListClusterExtensionsRequest,
    ) -> SageMakerListClusterExtensionsResponse:
        client = self._require_client()
        return await self._execute(client.list_cluster_extensions, request, SageMakerListClusterExtensionsResponse)

    async def list_cluster_extensions_paginated(
        self,
        request: SageMakerListClusterExtensionsRequest,
    ) -> list[SageMakerListClusterExtensionsResponse]:
        return await self._paginate('list_cluster_extensions', request, SageMakerListClusterExtensionsResponse)

    async def list_cluster_nodes(
        self,
        request: SageMakerListClusterNodesRequest,
    ) -> SageMakerListClusterNodesResponse:
        client = self._require_client()
        return await self._execute(client.list_cluster_nodes, request, SageMakerListClusterNodesResponse)

    async def list_cluster_nodes_paginated(
        self,
        request: SageMakerListClusterNodesRequest,
    ) -> list[SageMakerListClusterNodesResponse]:
        return await self._paginate('list_cluster_nodes', request, SageMakerListClusterNodesResponse)

    async def list_cluster_operations(
        self,
        request: SageMakerListClusterOperationsRequest,
    ) -> SageMakerListClusterOperationsResponse:
        client = self._require_client()
        return await self._execute(client.list_cluster_operations, request, SageMakerListClusterOperationsResponse)

    async def list_cluster_operations_paginated(
        self,
        request: SageMakerListClusterOperationsRequest,
    ) -> list[SageMakerListClusterOperationsResponse]:
        return await self._paginate('list_cluster_operations', request, SageMakerListClusterOperationsResponse)

    async def list_cluster_scheduler_configs(
        self,
        request: SageMakerListClusterSchedulerConfigsRequest | None = None,
    ) -> SageMakerListClusterSchedulerConfigsResponse:
        client = self._require_client()
        return await self._execute(client.list_cluster_scheduler_configs, request, SageMakerListClusterSchedulerConfigsResponse)

    async def list_cluster_scheduler_configs_paginated(
        self,
        request: SageMakerListClusterSchedulerConfigsRequest | None = None,
    ) -> list[SageMakerListClusterSchedulerConfigsResponse]:
        return await self._paginate('list_cluster_scheduler_configs', request, SageMakerListClusterSchedulerConfigsResponse)

    async def list_clusters(
        self,
        request: SageMakerListClustersRequest | None = None,
    ) -> SageMakerListClustersResponse:
        client = self._require_client()
        return await self._execute(client.list_clusters, request, SageMakerListClustersResponse)

    async def list_clusters_paginated(
        self,
        request: SageMakerListClustersRequest | None = None,
    ) -> list[SageMakerListClustersResponse]:
        return await self._paginate('list_clusters', request, SageMakerListClustersResponse)

    async def list_code_repositories(
        self,
        request: SageMakerListCodeRepositoriesRequest | None = None,
    ) -> SageMakerListCodeRepositoriesResponse:
        client = self._require_client()
        return await self._execute(client.list_code_repositories, request, SageMakerListCodeRepositoriesResponse)

    async def list_code_repositories_paginated(
        self,
        request: SageMakerListCodeRepositoriesRequest | None = None,
    ) -> list[SageMakerListCodeRepositoriesResponse]:
        return await self._paginate('list_code_repositories', request, SageMakerListCodeRepositoriesResponse)

    async def list_compilation_jobs(
        self,
        request: SageMakerListCompilationJobsRequest | None = None,
    ) -> SageMakerListCompilationJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_compilation_jobs, request, SageMakerListCompilationJobsResponse)

    async def list_compilation_jobs_paginated(
        self,
        request: SageMakerListCompilationJobsRequest | None = None,
    ) -> list[SageMakerListCompilationJobsResponse]:
        return await self._paginate('list_compilation_jobs', request, SageMakerListCompilationJobsResponse)

    async def list_compute_quotas(
        self,
        request: SageMakerListComputeQuotasRequest | None = None,
    ) -> SageMakerListComputeQuotasResponse:
        client = self._require_client()
        return await self._execute(client.list_compute_quotas, request, SageMakerListComputeQuotasResponse)

    async def list_compute_quotas_paginated(
        self,
        request: SageMakerListComputeQuotasRequest | None = None,
    ) -> list[SageMakerListComputeQuotasResponse]:
        return await self._paginate('list_compute_quotas', request, SageMakerListComputeQuotasResponse)

    async def list_contexts(
        self,
        request: SageMakerListContextsRequest | None = None,
    ) -> SageMakerListContextsResponse:
        client = self._require_client()
        return await self._execute(client.list_contexts, request, SageMakerListContextsResponse)

    async def list_contexts_paginated(
        self,
        request: SageMakerListContextsRequest | None = None,
    ) -> list[SageMakerListContextsResponse]:
        return await self._paginate('list_contexts', request, SageMakerListContextsResponse)

    async def list_data_quality_job_definitions(
        self,
        request: SageMakerListDataQualityJobDefinitionsRequest | None = None,
    ) -> SageMakerListDataQualityJobDefinitionsResponse:
        client = self._require_client()
        return await self._execute(client.list_data_quality_job_definitions, request, SageMakerListDataQualityJobDefinitionsResponse)

    async def list_data_quality_job_definitions_paginated(
        self,
        request: SageMakerListDataQualityJobDefinitionsRequest | None = None,
    ) -> list[SageMakerListDataQualityJobDefinitionsResponse]:
        return await self._paginate('list_data_quality_job_definitions', request, SageMakerListDataQualityJobDefinitionsResponse)

    async def list_device_fleets(
        self,
        request: SageMakerListDeviceFleetsRequest | None = None,
    ) -> SageMakerListDeviceFleetsResponse:
        client = self._require_client()
        return await self._execute(client.list_device_fleets, request, SageMakerListDeviceFleetsResponse)

    async def list_device_fleets_paginated(
        self,
        request: SageMakerListDeviceFleetsRequest | None = None,
    ) -> list[SageMakerListDeviceFleetsResponse]:
        return await self._paginate('list_device_fleets', request, SageMakerListDeviceFleetsResponse)

    async def list_devices(
        self,
        request: SageMakerListDevicesRequest | None = None,
    ) -> SageMakerListDevicesResponse:
        client = self._require_client()
        return await self._execute(client.list_devices, request, SageMakerListDevicesResponse)

    async def list_devices_paginated(
        self,
        request: SageMakerListDevicesRequest | None = None,
    ) -> list[SageMakerListDevicesResponse]:
        return await self._paginate('list_devices', request, SageMakerListDevicesResponse)

    async def list_domains(
        self,
        request: SageMakerListDomainsRequest | None = None,
    ) -> SageMakerListDomainsResponse:
        client = self._require_client()
        return await self._execute(client.list_domains, request, SageMakerListDomainsResponse)

    async def list_domains_paginated(
        self,
        request: SageMakerListDomainsRequest | None = None,
    ) -> list[SageMakerListDomainsResponse]:
        return await self._paginate('list_domains', request, SageMakerListDomainsResponse)

    async def list_edge_deployment_plans(
        self,
        request: SageMakerListEdgeDeploymentPlansRequest | None = None,
    ) -> SageMakerListEdgeDeploymentPlansResponse:
        client = self._require_client()
        return await self._execute(client.list_edge_deployment_plans, request, SageMakerListEdgeDeploymentPlansResponse)

    async def list_edge_deployment_plans_paginated(
        self,
        request: SageMakerListEdgeDeploymentPlansRequest | None = None,
    ) -> list[SageMakerListEdgeDeploymentPlansResponse]:
        return await self._paginate('list_edge_deployment_plans', request, SageMakerListEdgeDeploymentPlansResponse)

    async def list_edge_packaging_jobs(
        self,
        request: SageMakerListEdgePackagingJobsRequest | None = None,
    ) -> SageMakerListEdgePackagingJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_edge_packaging_jobs, request, SageMakerListEdgePackagingJobsResponse)

    async def list_edge_packaging_jobs_paginated(
        self,
        request: SageMakerListEdgePackagingJobsRequest | None = None,
    ) -> list[SageMakerListEdgePackagingJobsResponse]:
        return await self._paginate('list_edge_packaging_jobs', request, SageMakerListEdgePackagingJobsResponse)

    async def list_experiments(
        self,
        request: SageMakerListExperimentsRequest | None = None,
    ) -> SageMakerListExperimentsResponse:
        client = self._require_client()
        return await self._execute(client.list_experiments, request, SageMakerListExperimentsResponse)

    async def list_experiments_paginated(
        self,
        request: SageMakerListExperimentsRequest | None = None,
    ) -> list[SageMakerListExperimentsResponse]:
        return await self._paginate('list_experiments', request, SageMakerListExperimentsResponse)

    async def list_feature_groups(
        self,
        request: SageMakerListFeatureGroupsRequest | None = None,
    ) -> SageMakerListFeatureGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_feature_groups, request, SageMakerListFeatureGroupsResponse)

    async def list_feature_groups_paginated(
        self,
        request: SageMakerListFeatureGroupsRequest | None = None,
    ) -> list[SageMakerListFeatureGroupsResponse]:
        return await self._paginate('list_feature_groups', request, SageMakerListFeatureGroupsResponse)

    async def list_flow_definitions(
        self,
        request: SageMakerListFlowDefinitionsRequest | None = None,
    ) -> SageMakerListFlowDefinitionsResponse:
        client = self._require_client()
        return await self._execute(client.list_flow_definitions, request, SageMakerListFlowDefinitionsResponse)

    async def list_flow_definitions_paginated(
        self,
        request: SageMakerListFlowDefinitionsRequest | None = None,
    ) -> list[SageMakerListFlowDefinitionsResponse]:
        return await self._paginate('list_flow_definitions', request, SageMakerListFlowDefinitionsResponse)

    async def list_global_inference_gateways(
        self,
        request: SageMakerListGlobalInferenceGatewaysRequest | None = None,
    ) -> SageMakerListGlobalInferenceGatewaysResponse:
        client = self._require_client()
        return await self._execute(client.list_global_inference_gateways, request, SageMakerListGlobalInferenceGatewaysResponse)

    async def list_global_inference_gateways_paginated(
        self,
        request: SageMakerListGlobalInferenceGatewaysRequest | None = None,
    ) -> list[SageMakerListGlobalInferenceGatewaysResponse]:
        return await self._paginate('list_global_inference_gateways', request, SageMakerListGlobalInferenceGatewaysResponse)

    async def list_hub_content_versions(
        self,
        request: SageMakerListHubContentVersionsRequest,
    ) -> SageMakerListHubContentVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_hub_content_versions, request, SageMakerListHubContentVersionsResponse)

    async def list_hub_contents(
        self,
        request: SageMakerListHubContentsRequest,
    ) -> SageMakerListHubContentsResponse:
        client = self._require_client()
        return await self._execute(client.list_hub_contents, request, SageMakerListHubContentsResponse)

    async def list_hubs(
        self,
        request: SageMakerListHubsRequest | None = None,
    ) -> SageMakerListHubsResponse:
        client = self._require_client()
        return await self._execute(client.list_hubs, request, SageMakerListHubsResponse)

    async def list_human_task_uis(
        self,
        request: SageMakerListHumanTaskUisRequest | None = None,
    ) -> SageMakerListHumanTaskUisResponse:
        client = self._require_client()
        return await self._execute(client.list_human_task_uis, request, SageMakerListHumanTaskUisResponse)

    async def list_human_task_uis_paginated(
        self,
        request: SageMakerListHumanTaskUisRequest | None = None,
    ) -> list[SageMakerListHumanTaskUisResponse]:
        return await self._paginate('list_human_task_uis', request, SageMakerListHumanTaskUisResponse)

    async def list_hyper_parameter_tuning_jobs(
        self,
        request: SageMakerListHyperParameterTuningJobsRequest | None = None,
    ) -> SageMakerListHyperParameterTuningJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_hyper_parameter_tuning_jobs, request, SageMakerListHyperParameterTuningJobsResponse)

    async def list_hyper_parameter_tuning_jobs_paginated(
        self,
        request: SageMakerListHyperParameterTuningJobsRequest | None = None,
    ) -> list[SageMakerListHyperParameterTuningJobsResponse]:
        return await self._paginate('list_hyper_parameter_tuning_jobs', request, SageMakerListHyperParameterTuningJobsResponse)

    async def list_image_versions(
        self,
        request: SageMakerListImageVersionsRequest,
    ) -> SageMakerListImageVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_image_versions, request, SageMakerListImageVersionsResponse)

    async def list_image_versions_paginated(
        self,
        request: SageMakerListImageVersionsRequest,
    ) -> list[SageMakerListImageVersionsResponse]:
        return await self._paginate('list_image_versions', request, SageMakerListImageVersionsResponse)

    async def list_images(
        self,
        request: SageMakerListImagesRequest | None = None,
    ) -> SageMakerListImagesResponse:
        client = self._require_client()
        return await self._execute(client.list_images, request, SageMakerListImagesResponse)

    async def list_images_paginated(
        self,
        request: SageMakerListImagesRequest | None = None,
    ) -> list[SageMakerListImagesResponse]:
        return await self._paginate('list_images', request, SageMakerListImagesResponse)

    async def list_inference_components(
        self,
        request: SageMakerListInferenceComponentsRequest | None = None,
    ) -> SageMakerListInferenceComponentsResponse:
        client = self._require_client()
        return await self._execute(client.list_inference_components, request, SageMakerListInferenceComponentsResponse)

    async def list_inference_components_paginated(
        self,
        request: SageMakerListInferenceComponentsRequest | None = None,
    ) -> list[SageMakerListInferenceComponentsResponse]:
        return await self._paginate('list_inference_components', request, SageMakerListInferenceComponentsResponse)

    async def list_inference_experiments(
        self,
        request: SageMakerListInferenceExperimentsRequest | None = None,
    ) -> SageMakerListInferenceExperimentsResponse:
        client = self._require_client()
        return await self._execute(client.list_inference_experiments, request, SageMakerListInferenceExperimentsResponse)

    async def list_inference_experiments_paginated(
        self,
        request: SageMakerListInferenceExperimentsRequest | None = None,
    ) -> list[SageMakerListInferenceExperimentsResponse]:
        return await self._paginate('list_inference_experiments', request, SageMakerListInferenceExperimentsResponse)

    async def list_inference_gateways(
        self,
        request: SageMakerListInferenceGatewaysRequest,
    ) -> SageMakerListInferenceGatewaysResponse:
        client = self._require_client()
        return await self._execute(client.list_inference_gateways, request, SageMakerListInferenceGatewaysResponse)

    async def list_inference_gateways_paginated(
        self,
        request: SageMakerListInferenceGatewaysRequest,
    ) -> list[SageMakerListInferenceGatewaysResponse]:
        return await self._paginate('list_inference_gateways', request, SageMakerListInferenceGatewaysResponse)

    async def list_inference_recommendations_job_steps(
        self,
        request: SageMakerListInferenceRecommendationsJobStepsRequest,
    ) -> SageMakerListInferenceRecommendationsJobStepsResponse:
        client = self._require_client()
        return await self._execute(client.list_inference_recommendations_job_steps, request, SageMakerListInferenceRecommendationsJobStepsResponse)

    async def list_inference_recommendations_job_steps_paginated(
        self,
        request: SageMakerListInferenceRecommendationsJobStepsRequest,
    ) -> list[SageMakerListInferenceRecommendationsJobStepsResponse]:
        return await self._paginate('list_inference_recommendations_job_steps', request, SageMakerListInferenceRecommendationsJobStepsResponse)

    async def list_inference_recommendations_jobs(
        self,
        request: SageMakerListInferenceRecommendationsJobsRequest | None = None,
    ) -> SageMakerListInferenceRecommendationsJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_inference_recommendations_jobs, request, SageMakerListInferenceRecommendationsJobsResponse)

    async def list_inference_recommendations_jobs_paginated(
        self,
        request: SageMakerListInferenceRecommendationsJobsRequest | None = None,
    ) -> list[SageMakerListInferenceRecommendationsJobsResponse]:
        return await self._paginate('list_inference_recommendations_jobs', request, SageMakerListInferenceRecommendationsJobsResponse)

    async def list_inference_routers(
        self,
        request: SageMakerListInferenceRoutersRequest | None = None,
    ) -> SageMakerListInferenceRoutersResponse:
        client = self._require_client()
        return await self._execute(client.list_inference_routers, request, SageMakerListInferenceRoutersResponse)

    async def list_inference_routers_paginated(
        self,
        request: SageMakerListInferenceRoutersRequest | None = None,
    ) -> list[SageMakerListInferenceRoutersResponse]:
        return await self._paginate('list_inference_routers', request, SageMakerListInferenceRoutersResponse)

    async def list_job_schema_versions(
        self,
        request: SageMakerListJobSchemaVersionsRequest,
    ) -> SageMakerListJobSchemaVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_job_schema_versions, request, SageMakerListJobSchemaVersionsResponse)

    async def list_job_schema_versions_paginated(
        self,
        request: SageMakerListJobSchemaVersionsRequest,
    ) -> list[SageMakerListJobSchemaVersionsResponse]:
        return await self._paginate('list_job_schema_versions', request, SageMakerListJobSchemaVersionsResponse)

    async def list_jobs(
        self,
        request: SageMakerListJobsRequest,
    ) -> SageMakerListJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_jobs, request, SageMakerListJobsResponse)

    async def list_jobs_paginated(
        self,
        request: SageMakerListJobsRequest,
    ) -> list[SageMakerListJobsResponse]:
        return await self._paginate('list_jobs', request, SageMakerListJobsResponse)

    async def list_labeling_jobs(
        self,
        request: SageMakerListLabelingJobsRequest | None = None,
    ) -> SageMakerListLabelingJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_labeling_jobs, request, SageMakerListLabelingJobsResponse)

    async def list_labeling_jobs_paginated(
        self,
        request: SageMakerListLabelingJobsRequest | None = None,
    ) -> list[SageMakerListLabelingJobsResponse]:
        return await self._paginate('list_labeling_jobs', request, SageMakerListLabelingJobsResponse)

    async def list_labeling_jobs_for_workteam(
        self,
        request: SageMakerListLabelingJobsForWorkteamRequest,
    ) -> SageMakerListLabelingJobsForWorkteamResponse:
        client = self._require_client()
        return await self._execute(client.list_labeling_jobs_for_workteam, request, SageMakerListLabelingJobsForWorkteamResponse)

    async def list_labeling_jobs_for_workteam_paginated(
        self,
        request: SageMakerListLabelingJobsForWorkteamRequest,
    ) -> list[SageMakerListLabelingJobsForWorkteamResponse]:
        return await self._paginate('list_labeling_jobs_for_workteam', request, SageMakerListLabelingJobsForWorkteamResponse)

    async def list_lineage_groups(
        self,
        request: SageMakerListLineageGroupsRequest | None = None,
    ) -> SageMakerListLineageGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_lineage_groups, request, SageMakerListLineageGroupsResponse)

    async def list_lineage_groups_paginated(
        self,
        request: SageMakerListLineageGroupsRequest | None = None,
    ) -> list[SageMakerListLineageGroupsResponse]:
        return await self._paginate('list_lineage_groups', request, SageMakerListLineageGroupsResponse)

    async def list_mlflow_apps(
        self,
        request: SageMakerListMlflowAppsRequest | None = None,
    ) -> SageMakerListMlflowAppsResponse:
        client = self._require_client()
        return await self._execute(client.list_mlflow_apps, request, SageMakerListMlflowAppsResponse)

    async def list_mlflow_apps_paginated(
        self,
        request: SageMakerListMlflowAppsRequest | None = None,
    ) -> list[SageMakerListMlflowAppsResponse]:
        return await self._paginate('list_mlflow_apps', request, SageMakerListMlflowAppsResponse)

    async def list_mlflow_tracking_servers(
        self,
        request: SageMakerListMlflowTrackingServersRequest | None = None,
    ) -> SageMakerListMlflowTrackingServersResponse:
        client = self._require_client()
        return await self._execute(client.list_mlflow_tracking_servers, request, SageMakerListMlflowTrackingServersResponse)

    async def list_mlflow_tracking_servers_paginated(
        self,
        request: SageMakerListMlflowTrackingServersRequest | None = None,
    ) -> list[SageMakerListMlflowTrackingServersResponse]:
        return await self._paginate('list_mlflow_tracking_servers', request, SageMakerListMlflowTrackingServersResponse)

    async def list_model_bias_job_definitions(
        self,
        request: SageMakerListModelBiasJobDefinitionsRequest | None = None,
    ) -> SageMakerListModelBiasJobDefinitionsResponse:
        client = self._require_client()
        return await self._execute(client.list_model_bias_job_definitions, request, SageMakerListModelBiasJobDefinitionsResponse)

    async def list_model_bias_job_definitions_paginated(
        self,
        request: SageMakerListModelBiasJobDefinitionsRequest | None = None,
    ) -> list[SageMakerListModelBiasJobDefinitionsResponse]:
        return await self._paginate('list_model_bias_job_definitions', request, SageMakerListModelBiasJobDefinitionsResponse)

    async def list_model_card_export_jobs(
        self,
        request: SageMakerListModelCardExportJobsRequest,
    ) -> SageMakerListModelCardExportJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_model_card_export_jobs, request, SageMakerListModelCardExportJobsResponse)

    async def list_model_card_export_jobs_paginated(
        self,
        request: SageMakerListModelCardExportJobsRequest,
    ) -> list[SageMakerListModelCardExportJobsResponse]:
        return await self._paginate('list_model_card_export_jobs', request, SageMakerListModelCardExportJobsResponse)

    async def list_model_card_versions(
        self,
        request: SageMakerListModelCardVersionsRequest,
    ) -> SageMakerListModelCardVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_model_card_versions, request, SageMakerListModelCardVersionsResponse)

    async def list_model_card_versions_paginated(
        self,
        request: SageMakerListModelCardVersionsRequest,
    ) -> list[SageMakerListModelCardVersionsResponse]:
        return await self._paginate('list_model_card_versions', request, SageMakerListModelCardVersionsResponse)

    async def list_model_cards(
        self,
        request: SageMakerListModelCardsRequest | None = None,
    ) -> SageMakerListModelCardsResponse:
        client = self._require_client()
        return await self._execute(client.list_model_cards, request, SageMakerListModelCardsResponse)

    async def list_model_cards_paginated(
        self,
        request: SageMakerListModelCardsRequest | None = None,
    ) -> list[SageMakerListModelCardsResponse]:
        return await self._paginate('list_model_cards', request, SageMakerListModelCardsResponse)

    async def list_model_explainability_job_definitions(
        self,
        request: SageMakerListModelExplainabilityJobDefinitionsRequest | None = None,
    ) -> SageMakerListModelExplainabilityJobDefinitionsResponse:
        client = self._require_client()
        return await self._execute(client.list_model_explainability_job_definitions, request, SageMakerListModelExplainabilityJobDefinitionsResponse)

    async def list_model_explainability_job_definitions_paginated(
        self,
        request: SageMakerListModelExplainabilityJobDefinitionsRequest | None = None,
    ) -> list[SageMakerListModelExplainabilityJobDefinitionsResponse]:
        return await self._paginate('list_model_explainability_job_definitions', request, SageMakerListModelExplainabilityJobDefinitionsResponse)

    async def list_model_metadata(
        self,
        request: SageMakerListModelMetadataRequest | None = None,
    ) -> SageMakerListModelMetadataResponse:
        client = self._require_client()
        return await self._execute(client.list_model_metadata, request, SageMakerListModelMetadataResponse)

    async def list_model_metadata_paginated(
        self,
        request: SageMakerListModelMetadataRequest | None = None,
    ) -> list[SageMakerListModelMetadataResponse]:
        return await self._paginate('list_model_metadata', request, SageMakerListModelMetadataResponse)

    async def list_model_package_groups(
        self,
        request: SageMakerListModelPackageGroupsRequest | None = None,
    ) -> SageMakerListModelPackageGroupsResponse:
        client = self._require_client()
        return await self._execute(client.list_model_package_groups, request, SageMakerListModelPackageGroupsResponse)

    async def list_model_package_groups_paginated(
        self,
        request: SageMakerListModelPackageGroupsRequest | None = None,
    ) -> list[SageMakerListModelPackageGroupsResponse]:
        return await self._paginate('list_model_package_groups', request, SageMakerListModelPackageGroupsResponse)

    async def list_model_packages(
        self,
        request: SageMakerListModelPackagesRequest | None = None,
    ) -> SageMakerListModelPackagesResponse:
        client = self._require_client()
        return await self._execute(client.list_model_packages, request, SageMakerListModelPackagesResponse)

    async def list_model_packages_paginated(
        self,
        request: SageMakerListModelPackagesRequest | None = None,
    ) -> list[SageMakerListModelPackagesResponse]:
        return await self._paginate('list_model_packages', request, SageMakerListModelPackagesResponse)

    async def list_model_quality_job_definitions(
        self,
        request: SageMakerListModelQualityJobDefinitionsRequest | None = None,
    ) -> SageMakerListModelQualityJobDefinitionsResponse:
        client = self._require_client()
        return await self._execute(client.list_model_quality_job_definitions, request, SageMakerListModelQualityJobDefinitionsResponse)

    async def list_model_quality_job_definitions_paginated(
        self,
        request: SageMakerListModelQualityJobDefinitionsRequest | None = None,
    ) -> list[SageMakerListModelQualityJobDefinitionsResponse]:
        return await self._paginate('list_model_quality_job_definitions', request, SageMakerListModelQualityJobDefinitionsResponse)

    async def list_monitoring_alert_history(
        self,
        request: SageMakerListMonitoringAlertHistoryRequest | None = None,
    ) -> SageMakerListMonitoringAlertHistoryResponse:
        client = self._require_client()
        return await self._execute(client.list_monitoring_alert_history, request, SageMakerListMonitoringAlertHistoryResponse)

    async def list_monitoring_alert_history_paginated(
        self,
        request: SageMakerListMonitoringAlertHistoryRequest | None = None,
    ) -> list[SageMakerListMonitoringAlertHistoryResponse]:
        return await self._paginate('list_monitoring_alert_history', request, SageMakerListMonitoringAlertHistoryResponse)

    async def list_monitoring_alerts(
        self,
        request: SageMakerListMonitoringAlertsRequest,
    ) -> SageMakerListMonitoringAlertsResponse:
        client = self._require_client()
        return await self._execute(client.list_monitoring_alerts, request, SageMakerListMonitoringAlertsResponse)

    async def list_monitoring_alerts_paginated(
        self,
        request: SageMakerListMonitoringAlertsRequest,
    ) -> list[SageMakerListMonitoringAlertsResponse]:
        return await self._paginate('list_monitoring_alerts', request, SageMakerListMonitoringAlertsResponse)

    async def list_monitoring_executions(
        self,
        request: SageMakerListMonitoringExecutionsRequest | None = None,
    ) -> SageMakerListMonitoringExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.list_monitoring_executions, request, SageMakerListMonitoringExecutionsResponse)

    async def list_monitoring_executions_paginated(
        self,
        request: SageMakerListMonitoringExecutionsRequest | None = None,
    ) -> list[SageMakerListMonitoringExecutionsResponse]:
        return await self._paginate('list_monitoring_executions', request, SageMakerListMonitoringExecutionsResponse)

    async def list_monitoring_schedules(
        self,
        request: SageMakerListMonitoringSchedulesRequest | None = None,
    ) -> SageMakerListMonitoringSchedulesResponse:
        client = self._require_client()
        return await self._execute(client.list_monitoring_schedules, request, SageMakerListMonitoringSchedulesResponse)

    async def list_monitoring_schedules_paginated(
        self,
        request: SageMakerListMonitoringSchedulesRequest | None = None,
    ) -> list[SageMakerListMonitoringSchedulesResponse]:
        return await self._paginate('list_monitoring_schedules', request, SageMakerListMonitoringSchedulesResponse)

    async def list_notebook_instance_lifecycle_configs(
        self,
        request: SageMakerListNotebookInstanceLifecycleConfigsRequest | None = None,
    ) -> SageMakerListNotebookInstanceLifecycleConfigsResponse:
        client = self._require_client()
        return await self._execute(client.list_notebook_instance_lifecycle_configs, request, SageMakerListNotebookInstanceLifecycleConfigsResponse)

    async def list_notebook_instance_lifecycle_configs_paginated(
        self,
        request: SageMakerListNotebookInstanceLifecycleConfigsRequest | None = None,
    ) -> list[SageMakerListNotebookInstanceLifecycleConfigsResponse]:
        return await self._paginate('list_notebook_instance_lifecycle_configs', request, SageMakerListNotebookInstanceLifecycleConfigsResponse)

    async def list_optimization_jobs(
        self,
        request: SageMakerListOptimizationJobsRequest | None = None,
    ) -> SageMakerListOptimizationJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_optimization_jobs, request, SageMakerListOptimizationJobsResponse)

    async def list_optimization_jobs_paginated(
        self,
        request: SageMakerListOptimizationJobsRequest | None = None,
    ) -> list[SageMakerListOptimizationJobsResponse]:
        return await self._paginate('list_optimization_jobs', request, SageMakerListOptimizationJobsResponse)

    async def list_partner_apps(
        self,
        request: SageMakerListPartnerAppsRequest | None = None,
    ) -> SageMakerListPartnerAppsResponse:
        client = self._require_client()
        return await self._execute(client.list_partner_apps, request, SageMakerListPartnerAppsResponse)

    async def list_partner_apps_paginated(
        self,
        request: SageMakerListPartnerAppsRequest | None = None,
    ) -> list[SageMakerListPartnerAppsResponse]:
        return await self._paginate('list_partner_apps', request, SageMakerListPartnerAppsResponse)

    async def list_pipeline_execution_steps(
        self,
        request: SageMakerListPipelineExecutionStepsRequest | None = None,
    ) -> SageMakerListPipelineExecutionStepsResponse:
        client = self._require_client()
        return await self._execute(client.list_pipeline_execution_steps, request, SageMakerListPipelineExecutionStepsResponse)

    async def list_pipeline_execution_steps_paginated(
        self,
        request: SageMakerListPipelineExecutionStepsRequest | None = None,
    ) -> list[SageMakerListPipelineExecutionStepsResponse]:
        return await self._paginate('list_pipeline_execution_steps', request, SageMakerListPipelineExecutionStepsResponse)

    async def list_pipeline_executions(
        self,
        request: SageMakerListPipelineExecutionsRequest,
    ) -> SageMakerListPipelineExecutionsResponse:
        client = self._require_client()
        return await self._execute(client.list_pipeline_executions, request, SageMakerListPipelineExecutionsResponse)

    async def list_pipeline_executions_paginated(
        self,
        request: SageMakerListPipelineExecutionsRequest,
    ) -> list[SageMakerListPipelineExecutionsResponse]:
        return await self._paginate('list_pipeline_executions', request, SageMakerListPipelineExecutionsResponse)

    async def list_pipeline_parameters_for_execution(
        self,
        request: SageMakerListPipelineParametersForExecutionRequest,
    ) -> SageMakerListPipelineParametersForExecutionResponse:
        client = self._require_client()
        return await self._execute(client.list_pipeline_parameters_for_execution, request, SageMakerListPipelineParametersForExecutionResponse)

    async def list_pipeline_parameters_for_execution_paginated(
        self,
        request: SageMakerListPipelineParametersForExecutionRequest,
    ) -> list[SageMakerListPipelineParametersForExecutionResponse]:
        return await self._paginate('list_pipeline_parameters_for_execution', request, SageMakerListPipelineParametersForExecutionResponse)

    async def list_pipeline_versions(
        self,
        request: SageMakerListPipelineVersionsRequest,
    ) -> SageMakerListPipelineVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_pipeline_versions, request, SageMakerListPipelineVersionsResponse)

    async def list_pipeline_versions_paginated(
        self,
        request: SageMakerListPipelineVersionsRequest,
    ) -> list[SageMakerListPipelineVersionsResponse]:
        return await self._paginate('list_pipeline_versions', request, SageMakerListPipelineVersionsResponse)

    async def list_projects(
        self,
        request: SageMakerListProjectsRequest | None = None,
    ) -> SageMakerListProjectsResponse:
        client = self._require_client()
        return await self._execute(client.list_projects, request, SageMakerListProjectsResponse)

    async def list_projects_paginated(
        self,
        request: SageMakerListProjectsRequest | None = None,
    ) -> list[SageMakerListProjectsResponse]:
        return await self._paginate('list_projects', request, SageMakerListProjectsResponse)

    async def list_resource_catalogs(
        self,
        request: SageMakerListResourceCatalogsRequest | None = None,
    ) -> SageMakerListResourceCatalogsResponse:
        client = self._require_client()
        return await self._execute(client.list_resource_catalogs, request, SageMakerListResourceCatalogsResponse)

    async def list_resource_catalogs_paginated(
        self,
        request: SageMakerListResourceCatalogsRequest | None = None,
    ) -> list[SageMakerListResourceCatalogsResponse]:
        return await self._paginate('list_resource_catalogs', request, SageMakerListResourceCatalogsResponse)

    async def list_spaces(
        self,
        request: SageMakerListSpacesRequest | None = None,
    ) -> SageMakerListSpacesResponse:
        client = self._require_client()
        return await self._execute(client.list_spaces, request, SageMakerListSpacesResponse)

    async def list_spaces_paginated(
        self,
        request: SageMakerListSpacesRequest | None = None,
    ) -> list[SageMakerListSpacesResponse]:
        return await self._paginate('list_spaces', request, SageMakerListSpacesResponse)

    async def list_stage_devices(
        self,
        request: SageMakerListStageDevicesRequest,
    ) -> SageMakerListStageDevicesResponse:
        client = self._require_client()
        return await self._execute(client.list_stage_devices, request, SageMakerListStageDevicesResponse)

    async def list_stage_devices_paginated(
        self,
        request: SageMakerListStageDevicesRequest,
    ) -> list[SageMakerListStageDevicesResponse]:
        return await self._paginate('list_stage_devices', request, SageMakerListStageDevicesResponse)

    async def list_studio_lifecycle_configs(
        self,
        request: SageMakerListStudioLifecycleConfigsRequest | None = None,
    ) -> SageMakerListStudioLifecycleConfigsResponse:
        client = self._require_client()
        return await self._execute(client.list_studio_lifecycle_configs, request, SageMakerListStudioLifecycleConfigsResponse)

    async def list_studio_lifecycle_configs_paginated(
        self,
        request: SageMakerListStudioLifecycleConfigsRequest | None = None,
    ) -> list[SageMakerListStudioLifecycleConfigsResponse]:
        return await self._paginate('list_studio_lifecycle_configs', request, SageMakerListStudioLifecycleConfigsResponse)

    async def list_subscribed_workteams(
        self,
        request: SageMakerListSubscribedWorkteamsRequest | None = None,
    ) -> SageMakerListSubscribedWorkteamsResponse:
        client = self._require_client()
        return await self._execute(client.list_subscribed_workteams, request, SageMakerListSubscribedWorkteamsResponse)

    async def list_subscribed_workteams_paginated(
        self,
        request: SageMakerListSubscribedWorkteamsRequest | None = None,
    ) -> list[SageMakerListSubscribedWorkteamsResponse]:
        return await self._paginate('list_subscribed_workteams', request, SageMakerListSubscribedWorkteamsResponse)

    async def list_training_jobs_for_hyper_parameter_tuning_job(
        self,
        request: SageMakerListTrainingJobsForHyperParameterTuningJobRequest,
    ) -> SageMakerListTrainingJobsForHyperParameterTuningJobResponse:
        client = self._require_client()
        return await self._execute(client.list_training_jobs_for_hyper_parameter_tuning_job, request, SageMakerListTrainingJobsForHyperParameterTuningJobResponse)

    async def list_training_jobs_for_hyper_parameter_tuning_job_paginated(
        self,
        request: SageMakerListTrainingJobsForHyperParameterTuningJobRequest,
    ) -> list[SageMakerListTrainingJobsForHyperParameterTuningJobResponse]:
        return await self._paginate('list_training_jobs_for_hyper_parameter_tuning_job', request, SageMakerListTrainingJobsForHyperParameterTuningJobResponse)

    async def list_training_plans(
        self,
        request: SageMakerListTrainingPlansRequest | None = None,
    ) -> SageMakerListTrainingPlansResponse:
        client = self._require_client()
        return await self._execute(client.list_training_plans, request, SageMakerListTrainingPlansResponse)

    async def list_training_plans_paginated(
        self,
        request: SageMakerListTrainingPlansRequest | None = None,
    ) -> list[SageMakerListTrainingPlansResponse]:
        return await self._paginate('list_training_plans', request, SageMakerListTrainingPlansResponse)

    async def list_training_sessions(
        self,
        request: SageMakerListTrainingSessionsRequest | None = None,
    ) -> SageMakerListTrainingSessionsResponse:
        client = self._require_client()
        return await self._execute(client.list_training_sessions, request, SageMakerListTrainingSessionsResponse)

    async def list_training_sessions_paginated(
        self,
        request: SageMakerListTrainingSessionsRequest | None = None,
    ) -> list[SageMakerListTrainingSessionsResponse]:
        return await self._paginate('list_training_sessions', request, SageMakerListTrainingSessionsResponse)

    async def list_transform_jobs(
        self,
        request: SageMakerListTransformJobsRequest | None = None,
    ) -> SageMakerListTransformJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_transform_jobs, request, SageMakerListTransformJobsResponse)

    async def list_transform_jobs_paginated(
        self,
        request: SageMakerListTransformJobsRequest | None = None,
    ) -> list[SageMakerListTransformJobsResponse]:
        return await self._paginate('list_transform_jobs', request, SageMakerListTransformJobsResponse)

    async def list_trial_components(
        self,
        request: SageMakerListTrialComponentsRequest | None = None,
    ) -> SageMakerListTrialComponentsResponse:
        client = self._require_client()
        return await self._execute(client.list_trial_components, request, SageMakerListTrialComponentsResponse)

    async def list_trial_components_paginated(
        self,
        request: SageMakerListTrialComponentsRequest | None = None,
    ) -> list[SageMakerListTrialComponentsResponse]:
        return await self._paginate('list_trial_components', request, SageMakerListTrialComponentsResponse)

    async def list_trials(
        self,
        request: SageMakerListTrialsRequest | None = None,
    ) -> SageMakerListTrialsResponse:
        client = self._require_client()
        return await self._execute(client.list_trials, request, SageMakerListTrialsResponse)

    async def list_trials_paginated(
        self,
        request: SageMakerListTrialsRequest | None = None,
    ) -> list[SageMakerListTrialsResponse]:
        return await self._paginate('list_trials', request, SageMakerListTrialsResponse)

    async def list_ultra_servers_by_reserved_capacity(
        self,
        request: SageMakerListUltraServersByReservedCapacityRequest,
    ) -> SageMakerListUltraServersByReservedCapacityResponse:
        client = self._require_client()
        return await self._execute(client.list_ultra_servers_by_reserved_capacity, request, SageMakerListUltraServersByReservedCapacityResponse)

    async def list_ultra_servers_by_reserved_capacity_paginated(
        self,
        request: SageMakerListUltraServersByReservedCapacityRequest,
    ) -> list[SageMakerListUltraServersByReservedCapacityResponse]:
        return await self._paginate('list_ultra_servers_by_reserved_capacity', request, SageMakerListUltraServersByReservedCapacityResponse)

    async def list_user_profiles(
        self,
        request: SageMakerListUserProfilesRequest | None = None,
    ) -> SageMakerListUserProfilesResponse:
        client = self._require_client()
        return await self._execute(client.list_user_profiles, request, SageMakerListUserProfilesResponse)

    async def list_user_profiles_paginated(
        self,
        request: SageMakerListUserProfilesRequest | None = None,
    ) -> list[SageMakerListUserProfilesResponse]:
        return await self._paginate('list_user_profiles', request, SageMakerListUserProfilesResponse)

    async def list_workforces(
        self,
        request: SageMakerListWorkforcesRequest | None = None,
    ) -> SageMakerListWorkforcesResponse:
        client = self._require_client()
        return await self._execute(client.list_workforces, request, SageMakerListWorkforcesResponse)

    async def list_workforces_paginated(
        self,
        request: SageMakerListWorkforcesRequest | None = None,
    ) -> list[SageMakerListWorkforcesResponse]:
        return await self._paginate('list_workforces', request, SageMakerListWorkforcesResponse)

    async def list_workteams(
        self,
        request: SageMakerListWorkteamsRequest | None = None,
    ) -> SageMakerListWorkteamsResponse:
        client = self._require_client()
        return await self._execute(client.list_workteams, request, SageMakerListWorkteamsResponse)

    async def list_workteams_paginated(
        self,
        request: SageMakerListWorkteamsRequest | None = None,
    ) -> list[SageMakerListWorkteamsResponse]:
        return await self._paginate('list_workteams', request, SageMakerListWorkteamsResponse)

    async def move_cluster_nodes(
        self,
        request: SageMakerMoveClusterNodesRequest,
    ) -> SageMakerMoveClusterNodesResponse:
        client = self._require_client()
        return await self._execute(client.move_cluster_nodes, request, SageMakerMoveClusterNodesResponse)

    async def put_endpoint_policy(
        self,
        request: SageMakerPutEndpointPolicyRequest,
    ) -> SageMakerPutEndpointPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_endpoint_policy, request, SageMakerPutEndpointPolicyResponse)

    async def put_model_package_group_policy(
        self,
        request: SageMakerPutModelPackageGroupPolicyRequest,
    ) -> SageMakerPutModelPackageGroupPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_model_package_group_policy, request, SageMakerPutModelPackageGroupPolicyResponse)

    async def query_lineage(
        self,
        request: SageMakerQueryLineageRequest | None = None,
    ) -> SageMakerQueryLineageResponse:
        client = self._require_client()
        return await self._execute(client.query_lineage, request, SageMakerQueryLineageResponse)

    async def register_devices(
        self,
        request: SageMakerRegisterDevicesRequest,
    ) -> SageMakerRegisterDevicesResponse:
        client = self._require_client()
        return await self._execute(client.register_devices, request, SageMakerRegisterDevicesResponse)

    async def remove_inference_gateway(
        self,
        request: SageMakerRemoveInferenceGatewayRequest,
    ) -> SageMakerRemoveInferenceGatewayResponse:
        client = self._require_client()
        return await self._execute(client.remove_inference_gateway, request, SageMakerRemoveInferenceGatewayResponse)

    async def render_ui_template(
        self,
        request: SageMakerRenderUiTemplateRequest,
    ) -> SageMakerRenderUiTemplateResponse:
        client = self._require_client()
        return await self._execute(client.render_ui_template, request, SageMakerRenderUiTemplateResponse)

    async def retry_pipeline_execution(
        self,
        request: SageMakerRetryPipelineExecutionRequest,
    ) -> SageMakerRetryPipelineExecutionResponse:
        client = self._require_client()
        return await self._execute(client.retry_pipeline_execution, request, SageMakerRetryPipelineExecutionResponse)

    async def search(
        self,
        request: SageMakerSearchRequest,
    ) -> SageMakerSearchResponse:
        client = self._require_client()
        return await self._execute(client.search, request, SageMakerSearchResponse)

    async def search_paginated(
        self,
        request: SageMakerSearchRequest,
    ) -> list[SageMakerSearchResponse]:
        return await self._paginate('search', request, SageMakerSearchResponse)

    async def search_training_plan_offerings(
        self,
        request: SageMakerSearchTrainingPlanOfferingsRequest | None = None,
    ) -> SageMakerSearchTrainingPlanOfferingsResponse:
        client = self._require_client()
        return await self._execute(client.search_training_plan_offerings, request, SageMakerSearchTrainingPlanOfferingsResponse)

    async def send_pipeline_execution_step_failure(
        self,
        request: SageMakerSendPipelineExecutionStepFailureRequest,
    ) -> SageMakerSendPipelineExecutionStepFailureResponse:
        client = self._require_client()
        return await self._execute(client.send_pipeline_execution_step_failure, request, SageMakerSendPipelineExecutionStepFailureResponse)

    async def send_pipeline_execution_step_success(
        self,
        request: SageMakerSendPipelineExecutionStepSuccessRequest,
    ) -> SageMakerSendPipelineExecutionStepSuccessResponse:
        client = self._require_client()
        return await self._execute(client.send_pipeline_execution_step_success, request, SageMakerSendPipelineExecutionStepSuccessResponse)

    async def start_cluster_health_check(
        self,
        request: SageMakerStartClusterHealthCheckRequest,
    ) -> SageMakerStartClusterHealthCheckResponse:
        client = self._require_client()
        return await self._execute(client.start_cluster_health_check, request, SageMakerStartClusterHealthCheckResponse)

    async def start_edge_deployment_stage(
        self,
        request: SageMakerStartEdgeDeploymentStageRequest,
    ) -> SageMakerStartEdgeDeploymentStageResponse:
        client = self._require_client()
        return await self._execute(client.start_edge_deployment_stage, request, SageMakerStartEdgeDeploymentStageResponse)

    async def start_inference_experiment(
        self,
        request: SageMakerStartInferenceExperimentRequest,
    ) -> SageMakerStartInferenceExperimentResponse:
        client = self._require_client()
        return await self._execute(client.start_inference_experiment, request, SageMakerStartInferenceExperimentResponse)

    async def start_mlflow_tracking_server(
        self,
        request: SageMakerStartMlflowTrackingServerRequest,
    ) -> SageMakerStartMlflowTrackingServerResponse:
        client = self._require_client()
        return await self._execute(client.start_mlflow_tracking_server, request, SageMakerStartMlflowTrackingServerResponse)

    async def start_monitoring_schedule(
        self,
        request: SageMakerStartMonitoringScheduleRequest,
    ) -> SageMakerStartMonitoringScheduleResponse:
        client = self._require_client()
        return await self._execute(client.start_monitoring_schedule, request, SageMakerStartMonitoringScheduleResponse)

    async def start_session(
        self,
        request: SageMakerStartSessionRequest,
    ) -> SageMakerStartSessionResponse:
        client = self._require_client()
        return await self._execute(client.start_session, request, SageMakerStartSessionResponse)

    async def stop_ai_benchmark_job(
        self,
        request: SageMakerStopAIBenchmarkJobRequest,
    ) -> SageMakerStopAIBenchmarkJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_ai_benchmark_job, request, SageMakerStopAIBenchmarkJobResponse)

    async def stop_ai_recommendation_job(
        self,
        request: SageMakerStopAIRecommendationJobRequest,
    ) -> SageMakerStopAIRecommendationJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_ai_recommendation_job, request, SageMakerStopAIRecommendationJobResponse)

    async def stop_auto_ml_job(
        self,
        request: SageMakerStopAutoMLJobRequest,
    ) -> SageMakerStopAutoMLJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_auto_ml_job, request, SageMakerStopAutoMLJobResponse)

    async def stop_compilation_job(
        self,
        request: SageMakerStopCompilationJobRequest,
    ) -> SageMakerStopCompilationJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_compilation_job, request, SageMakerStopCompilationJobResponse)

    async def stop_edge_deployment_stage(
        self,
        request: SageMakerStopEdgeDeploymentStageRequest,
    ) -> SageMakerStopEdgeDeploymentStageResponse:
        client = self._require_client()
        return await self._execute(client.stop_edge_deployment_stage, request, SageMakerStopEdgeDeploymentStageResponse)

    async def stop_edge_packaging_job(
        self,
        request: SageMakerStopEdgePackagingJobRequest,
    ) -> SageMakerStopEdgePackagingJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_edge_packaging_job, request, SageMakerStopEdgePackagingJobResponse)

    async def stop_hyper_parameter_tuning_job(
        self,
        request: SageMakerStopHyperParameterTuningJobRequest,
    ) -> SageMakerStopHyperParameterTuningJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_hyper_parameter_tuning_job, request, SageMakerStopHyperParameterTuningJobResponse)

    async def stop_inference_experiment(
        self,
        request: SageMakerStopInferenceExperimentRequest,
    ) -> SageMakerStopInferenceExperimentResponse:
        client = self._require_client()
        return await self._execute(client.stop_inference_experiment, request, SageMakerStopInferenceExperimentResponse)

    async def stop_inference_recommendations_job(
        self,
        request: SageMakerStopInferenceRecommendationsJobRequest,
    ) -> SageMakerStopInferenceRecommendationsJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_inference_recommendations_job, request, SageMakerStopInferenceRecommendationsJobResponse)

    async def stop_job(
        self,
        request: SageMakerStopJobRequest,
    ) -> SageMakerStopJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_job, request, SageMakerStopJobResponse)

    async def stop_labeling_job(
        self,
        request: SageMakerStopLabelingJobRequest,
    ) -> SageMakerStopLabelingJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_labeling_job, request, SageMakerStopLabelingJobResponse)

    async def stop_mlflow_tracking_server(
        self,
        request: SageMakerStopMlflowTrackingServerRequest,
    ) -> SageMakerStopMlflowTrackingServerResponse:
        client = self._require_client()
        return await self._execute(client.stop_mlflow_tracking_server, request, SageMakerStopMlflowTrackingServerResponse)

    async def stop_monitoring_schedule(
        self,
        request: SageMakerStopMonitoringScheduleRequest,
    ) -> SageMakerStopMonitoringScheduleResponse:
        client = self._require_client()
        return await self._execute(client.stop_monitoring_schedule, request, SageMakerStopMonitoringScheduleResponse)

    async def stop_optimization_job(
        self,
        request: SageMakerStopOptimizationJobRequest,
    ) -> SageMakerStopOptimizationJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_optimization_job, request, SageMakerStopOptimizationJobResponse)

    async def stop_pipeline_execution(
        self,
        request: SageMakerStopPipelineExecutionRequest,
    ) -> SageMakerStopPipelineExecutionResponse:
        client = self._require_client()
        return await self._execute(client.stop_pipeline_execution, request, SageMakerStopPipelineExecutionResponse)

    async def stop_training_session(
        self,
        request: SageMakerStopTrainingSessionRequest,
    ) -> SageMakerStopTrainingSessionResponse:
        client = self._require_client()
        return await self._execute(client.stop_training_session, request, SageMakerStopTrainingSessionResponse)

    async def stop_transform_job(
        self,
        request: SageMakerStopTransformJobRequest,
    ) -> SageMakerStopTransformJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_transform_job, request, SageMakerStopTransformJobResponse)

    async def update_action(
        self,
        request: SageMakerUpdateActionRequest,
    ) -> SageMakerUpdateActionResponse:
        client = self._require_client()
        return await self._execute(client.update_action, request, SageMakerUpdateActionResponse)

    async def update_app_image_config(
        self,
        request: SageMakerUpdateAppImageConfigRequest,
    ) -> SageMakerUpdateAppImageConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_app_image_config, request, SageMakerUpdateAppImageConfigResponse)

    async def update_artifact(
        self,
        request: SageMakerUpdateArtifactRequest,
    ) -> SageMakerUpdateArtifactResponse:
        client = self._require_client()
        return await self._execute(client.update_artifact, request, SageMakerUpdateArtifactResponse)

    async def update_cluster(
        self,
        request: SageMakerUpdateClusterRequest,
    ) -> SageMakerUpdateClusterResponse:
        client = self._require_client()
        return await self._execute(client.update_cluster, request, SageMakerUpdateClusterResponse)

    async def update_cluster_extension(
        self,
        request: SageMakerUpdateClusterExtensionRequest,
    ) -> SageMakerUpdateClusterExtensionResponse:
        client = self._require_client()
        return await self._execute(client.update_cluster_extension, request, SageMakerUpdateClusterExtensionResponse)

    async def update_cluster_scheduler_config(
        self,
        request: SageMakerUpdateClusterSchedulerConfigRequest,
    ) -> SageMakerUpdateClusterSchedulerConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_cluster_scheduler_config, request, SageMakerUpdateClusterSchedulerConfigResponse)

    async def update_cluster_software(
        self,
        request: SageMakerUpdateClusterSoftwareRequest,
    ) -> SageMakerUpdateClusterSoftwareResponse:
        client = self._require_client()
        return await self._execute(client.update_cluster_software, request, SageMakerUpdateClusterSoftwareResponse)

    async def update_code_repository(
        self,
        request: SageMakerUpdateCodeRepositoryRequest,
    ) -> SageMakerUpdateCodeRepositoryResponse:
        client = self._require_client()
        return await self._execute(client.update_code_repository, request, SageMakerUpdateCodeRepositoryResponse)

    async def update_compute_quota(
        self,
        request: SageMakerUpdateComputeQuotaRequest,
    ) -> SageMakerUpdateComputeQuotaResponse:
        client = self._require_client()
        return await self._execute(client.update_compute_quota, request, SageMakerUpdateComputeQuotaResponse)

    async def update_context(
        self,
        request: SageMakerUpdateContextRequest,
    ) -> SageMakerUpdateContextResponse:
        client = self._require_client()
        return await self._execute(client.update_context, request, SageMakerUpdateContextResponse)

    async def update_device_fleet(
        self,
        request: SageMakerUpdateDeviceFleetRequest,
    ) -> SageMakerUpdateDeviceFleetResponse:
        client = self._require_client()
        return await self._execute(client.update_device_fleet, request, SageMakerUpdateDeviceFleetResponse)

    async def update_devices(
        self,
        request: SageMakerUpdateDevicesRequest,
    ) -> SageMakerUpdateDevicesResponse:
        client = self._require_client()
        return await self._execute(client.update_devices, request, SageMakerUpdateDevicesResponse)

    async def update_domain(
        self,
        request: SageMakerUpdateDomainRequest,
    ) -> SageMakerUpdateDomainResponse:
        client = self._require_client()
        return await self._execute(client.update_domain, request, SageMakerUpdateDomainResponse)

    async def update_endpoint_weights_and_capacities(
        self,
        request: SageMakerUpdateEndpointWeightsAndCapacitiesRequest,
    ) -> SageMakerUpdateEndpointWeightsAndCapacitiesResponse:
        client = self._require_client()
        return await self._execute(client.update_endpoint_weights_and_capacities, request, SageMakerUpdateEndpointWeightsAndCapacitiesResponse)

    async def update_experiment(
        self,
        request: SageMakerUpdateExperimentRequest,
    ) -> SageMakerUpdateExperimentResponse:
        client = self._require_client()
        return await self._execute(client.update_experiment, request, SageMakerUpdateExperimentResponse)

    async def update_feature_group(
        self,
        request: SageMakerUpdateFeatureGroupRequest,
    ) -> SageMakerUpdateFeatureGroupResponse:
        client = self._require_client()
        return await self._execute(client.update_feature_group, request, SageMakerUpdateFeatureGroupResponse)

    async def update_feature_metadata(
        self,
        request: SageMakerUpdateFeatureMetadataRequest,
    ) -> SageMakerUpdateFeatureMetadataResponse:
        client = self._require_client()
        return await self._execute(client.update_feature_metadata, request, SageMakerUpdateFeatureMetadataResponse)

    async def update_global_inference_gateway(
        self,
        request: SageMakerUpdateGlobalInferenceGatewayRequest,
    ) -> SageMakerUpdateGlobalInferenceGatewayResponse:
        client = self._require_client()
        return await self._execute(client.update_global_inference_gateway, request, SageMakerUpdateGlobalInferenceGatewayResponse)

    async def update_hub(
        self,
        request: SageMakerUpdateHubRequest,
    ) -> SageMakerUpdateHubResponse:
        client = self._require_client()
        return await self._execute(client.update_hub, request, SageMakerUpdateHubResponse)

    async def update_hub_content(
        self,
        request: SageMakerUpdateHubContentRequest,
    ) -> SageMakerUpdateHubContentResponse:
        client = self._require_client()
        return await self._execute(client.update_hub_content, request, SageMakerUpdateHubContentResponse)

    async def update_hub_content_reference(
        self,
        request: SageMakerUpdateHubContentReferenceRequest,
    ) -> SageMakerUpdateHubContentReferenceResponse:
        client = self._require_client()
        return await self._execute(client.update_hub_content_reference, request, SageMakerUpdateHubContentReferenceResponse)

    async def update_image(
        self,
        request: SageMakerUpdateImageRequest,
    ) -> SageMakerUpdateImageResponse:
        client = self._require_client()
        return await self._execute(client.update_image, request, SageMakerUpdateImageResponse)

    async def update_image_version(
        self,
        request: SageMakerUpdateImageVersionRequest,
    ) -> SageMakerUpdateImageVersionResponse:
        client = self._require_client()
        return await self._execute(client.update_image_version, request, SageMakerUpdateImageVersionResponse)

    async def update_inference_component(
        self,
        request: SageMakerUpdateInferenceComponentRequest,
    ) -> SageMakerUpdateInferenceComponentResponse:
        client = self._require_client()
        return await self._execute(client.update_inference_component, request, SageMakerUpdateInferenceComponentResponse)

    async def update_inference_component_runtime_config(
        self,
        request: SageMakerUpdateInferenceComponentRuntimeConfigRequest,
    ) -> SageMakerUpdateInferenceComponentRuntimeConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_inference_component_runtime_config, request, SageMakerUpdateInferenceComponentRuntimeConfigResponse)

    async def update_inference_experiment(
        self,
        request: SageMakerUpdateInferenceExperimentRequest,
    ) -> SageMakerUpdateInferenceExperimentResponse:
        client = self._require_client()
        return await self._execute(client.update_inference_experiment, request, SageMakerUpdateInferenceExperimentResponse)

    async def update_inference_router(
        self,
        request: SageMakerUpdateInferenceRouterRequest,
    ) -> SageMakerUpdateInferenceRouterResponse:
        client = self._require_client()
        return await self._execute(client.update_inference_router, request, SageMakerUpdateInferenceRouterResponse)

    async def update_mlflow_app(
        self,
        request: SageMakerUpdateMlflowAppRequest,
    ) -> SageMakerUpdateMlflowAppResponse:
        client = self._require_client()
        return await self._execute(client.update_mlflow_app, request, SageMakerUpdateMlflowAppResponse)

    async def update_mlflow_tracking_server(
        self,
        request: SageMakerUpdateMlflowTrackingServerRequest,
    ) -> SageMakerUpdateMlflowTrackingServerResponse:
        client = self._require_client()
        return await self._execute(client.update_mlflow_tracking_server, request, SageMakerUpdateMlflowTrackingServerResponse)

    async def update_model_card(
        self,
        request: SageMakerUpdateModelCardRequest,
    ) -> SageMakerUpdateModelCardResponse:
        client = self._require_client()
        return await self._execute(client.update_model_card, request, SageMakerUpdateModelCardResponse)

    async def update_model_package(
        self,
        request: SageMakerUpdateModelPackageRequest,
    ) -> SageMakerUpdateModelPackageResponse:
        client = self._require_client()
        return await self._execute(client.update_model_package, request, SageMakerUpdateModelPackageResponse)

    async def update_monitoring_alert(
        self,
        request: SageMakerUpdateMonitoringAlertRequest,
    ) -> SageMakerUpdateMonitoringAlertResponse:
        client = self._require_client()
        return await self._execute(client.update_monitoring_alert, request, SageMakerUpdateMonitoringAlertResponse)

    async def update_monitoring_schedule(
        self,
        request: SageMakerUpdateMonitoringScheduleRequest,
    ) -> SageMakerUpdateMonitoringScheduleResponse:
        client = self._require_client()
        return await self._execute(client.update_monitoring_schedule, request, SageMakerUpdateMonitoringScheduleResponse)

    async def update_notebook_instance(
        self,
        request: SageMakerUpdateNotebookInstanceRequest,
    ) -> SageMakerUpdateNotebookInstanceResponse:
        client = self._require_client()
        return await self._execute(client.update_notebook_instance, request, SageMakerUpdateNotebookInstanceResponse)

    async def update_notebook_instance_lifecycle_config(
        self,
        request: SageMakerUpdateNotebookInstanceLifecycleConfigRequest,
    ) -> SageMakerUpdateNotebookInstanceLifecycleConfigResponse:
        client = self._require_client()
        return await self._execute(client.update_notebook_instance_lifecycle_config, request, SageMakerUpdateNotebookInstanceLifecycleConfigResponse)

    async def update_partner_app(
        self,
        request: SageMakerUpdatePartnerAppRequest,
    ) -> SageMakerUpdatePartnerAppResponse:
        client = self._require_client()
        return await self._execute(client.update_partner_app, request, SageMakerUpdatePartnerAppResponse)

    async def update_pipeline(
        self,
        request: SageMakerUpdatePipelineRequest,
    ) -> SageMakerUpdatePipelineResponse:
        client = self._require_client()
        return await self._execute(client.update_pipeline, request, SageMakerUpdatePipelineResponse)

    async def update_pipeline_execution(
        self,
        request: SageMakerUpdatePipelineExecutionRequest,
    ) -> SageMakerUpdatePipelineExecutionResponse:
        client = self._require_client()
        return await self._execute(client.update_pipeline_execution, request, SageMakerUpdatePipelineExecutionResponse)

    async def update_pipeline_version(
        self,
        request: SageMakerUpdatePipelineVersionRequest,
    ) -> SageMakerUpdatePipelineVersionResponse:
        client = self._require_client()
        return await self._execute(client.update_pipeline_version, request, SageMakerUpdatePipelineVersionResponse)

    async def update_project(
        self,
        request: SageMakerUpdateProjectRequest,
    ) -> SageMakerUpdateProjectResponse:
        client = self._require_client()
        return await self._execute(client.update_project, request, SageMakerUpdateProjectResponse)

    async def update_space(
        self,
        request: SageMakerUpdateSpaceRequest,
    ) -> SageMakerUpdateSpaceResponse:
        client = self._require_client()
        return await self._execute(client.update_space, request, SageMakerUpdateSpaceResponse)

    async def update_training_job(
        self,
        request: SageMakerUpdateTrainingJobRequest,
    ) -> SageMakerUpdateTrainingJobResponse:
        client = self._require_client()
        return await self._execute(client.update_training_job, request, SageMakerUpdateTrainingJobResponse)

    async def update_trial(
        self,
        request: SageMakerUpdateTrialRequest,
    ) -> SageMakerUpdateTrialResponse:
        client = self._require_client()
        return await self._execute(client.update_trial, request, SageMakerUpdateTrialResponse)

    async def update_trial_component(
        self,
        request: SageMakerUpdateTrialComponentRequest,
    ) -> SageMakerUpdateTrialComponentResponse:
        client = self._require_client()
        return await self._execute(client.update_trial_component, request, SageMakerUpdateTrialComponentResponse)

    async def update_user_profile(
        self,
        request: SageMakerUpdateUserProfileRequest,
    ) -> SageMakerUpdateUserProfileResponse:
        client = self._require_client()
        return await self._execute(client.update_user_profile, request, SageMakerUpdateUserProfileResponse)

    async def update_workforce(
        self,
        request: SageMakerUpdateWorkforceRequest,
    ) -> SageMakerUpdateWorkforceResponse:
        client = self._require_client()
        return await self._execute(client.update_workforce, request, SageMakerUpdateWorkforceResponse)

    async def update_workteam(
        self,
        request: SageMakerUpdateWorkteamRequest,
    ) -> SageMakerUpdateWorkteamResponse:
        client = self._require_client()
        return await self._execute(client.update_workteam, request, SageMakerUpdateWorkteamResponse)

