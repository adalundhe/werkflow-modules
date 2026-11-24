from werkflow_aws.models.bedrock import (
    BedrockArchiveProjectRequest,
    BedrockArchiveProjectResponse,
    BedrockBatchDeleteAdvancedPromptOptimizationJobRequest,
    BedrockBatchDeleteAdvancedPromptOptimizationJobResponse,
    BedrockBatchDeleteEvaluationJobRequest,
    BedrockBatchDeleteEvaluationJobResponse,
    BedrockCancelAutomatedReasoningPolicyBuildWorkflowRequest,
    BedrockCancelAutomatedReasoningPolicyBuildWorkflowResponse,
    BedrockCreateAdvancedPromptOptimizationJobRequest,
    BedrockCreateAdvancedPromptOptimizationJobResponse,
    BedrockCreateAutomatedReasoningPolicyRequest,
    BedrockCreateAutomatedReasoningPolicyResponse,
    BedrockCreateAutomatedReasoningPolicyTestCaseRequest,
    BedrockCreateAutomatedReasoningPolicyTestCaseResponse,
    BedrockCreateAutomatedReasoningPolicyVersionRequest,
    BedrockCreateAutomatedReasoningPolicyVersionResponse,
    BedrockCreateCustomModelDeploymentRequest,
    BedrockCreateCustomModelDeploymentResponse,
    BedrockCreateCustomModelRequest,
    BedrockCreateCustomModelResponse,
    BedrockCreateEvaluationJobRequest,
    BedrockCreateEvaluationJobResponse,
    BedrockCreateFoundationModelAgreementRequest,
    BedrockCreateFoundationModelAgreementResponse,
    BedrockCreateGuardrailRequest,
    BedrockCreateGuardrailResponse,
    BedrockCreateGuardrailVersionRequest,
    BedrockCreateGuardrailVersionResponse,
    BedrockCreateInferenceProfileRequest,
    BedrockCreateInferenceProfileResponse,
    BedrockCreateMarketplaceModelEndpointRequest,
    BedrockCreateMarketplaceModelEndpointResponse,
    BedrockCreateModelCopyJobRequest,
    BedrockCreateModelCopyJobResponse,
    BedrockCreateModelCustomizationJobRequest,
    BedrockCreateModelCustomizationJobResponse,
    BedrockCreateModelImportJobRequest,
    BedrockCreateModelImportJobResponse,
    BedrockCreateModelInvocationJobRequest,
    BedrockCreateModelInvocationJobResponse,
    BedrockCreateProjectRequest,
    BedrockCreateProjectResponse,
    BedrockCreatePromptRouterRequest,
    BedrockCreatePromptRouterResponse,
    BedrockCreateProvisionedModelThroughputRequest,
    BedrockCreateProvisionedModelThroughputResponse,
    BedrockDeleteAccountDataRetentionStorageRequest,
    BedrockDeleteAccountDataRetentionStorageResponse,
    BedrockDeleteAutomatedReasoningPolicyBuildWorkflowRequest,
    BedrockDeleteAutomatedReasoningPolicyBuildWorkflowResponse,
    BedrockDeleteAutomatedReasoningPolicyRequest,
    BedrockDeleteAutomatedReasoningPolicyResponse,
    BedrockDeleteAutomatedReasoningPolicyTestCaseRequest,
    BedrockDeleteAutomatedReasoningPolicyTestCaseResponse,
    BedrockDeleteCustomModelDeploymentRequest,
    BedrockDeleteCustomModelDeploymentResponse,
    BedrockDeleteCustomModelRequest,
    BedrockDeleteCustomModelResponse,
    BedrockDeleteEnforcedGuardrailConfigurationRequest,
    BedrockDeleteEnforcedGuardrailConfigurationResponse,
    BedrockDeleteFoundationModelAgreementRequest,
    BedrockDeleteFoundationModelAgreementResponse,
    BedrockDeleteGuardrailRequest,
    BedrockDeleteGuardrailResponse,
    BedrockDeleteImportedModelRequest,
    BedrockDeleteImportedModelResponse,
    BedrockDeleteInferenceProfileRequest,
    BedrockDeleteInferenceProfileResponse,
    BedrockDeleteMarketplaceModelEndpointRequest,
    BedrockDeleteMarketplaceModelEndpointResponse,
    BedrockDeleteModelInvocationLoggingConfigurationRequest,
    BedrockDeleteModelInvocationLoggingConfigurationResponse,
    BedrockDeleteOrganizationDataRetentionStorageRequest,
    BedrockDeleteOrganizationDataRetentionStorageResponse,
    BedrockDeleteProjectDataRetentionStorageRequest,
    BedrockDeleteProjectDataRetentionStorageResponse,
    BedrockDeletePromptRouterRequest,
    BedrockDeletePromptRouterResponse,
    BedrockDeleteProvisionedModelThroughputRequest,
    BedrockDeleteProvisionedModelThroughputResponse,
    BedrockDeleteResourcePolicyRequest,
    BedrockDeleteResourcePolicyResponse,
    BedrockDeregisterMarketplaceModelEndpointRequest,
    BedrockDeregisterMarketplaceModelEndpointResponse,
    BedrockExportAutomatedReasoningPolicyVersionRequest,
    BedrockExportAutomatedReasoningPolicyVersionResponse,
    BedrockGetAccountDataRetentionRequest,
    BedrockGetAccountDataRetentionResponse,
    BedrockGetAccountDataRetentionStorageRequest,
    BedrockGetAccountDataRetentionStorageResponse,
    BedrockGetAdvancedPromptOptimizationJobRequest,
    BedrockGetAdvancedPromptOptimizationJobResponse,
    BedrockGetAutomatedReasoningPolicyAnnotationsRequest,
    BedrockGetAutomatedReasoningPolicyAnnotationsResponse,
    BedrockGetAutomatedReasoningPolicyBuildWorkflowRequest,
    BedrockGetAutomatedReasoningPolicyBuildWorkflowResponse,
    BedrockGetAutomatedReasoningPolicyBuildWorkflowResultAssetsRequest,
    BedrockGetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse,
    BedrockGetAutomatedReasoningPolicyNextScenarioRequest,
    BedrockGetAutomatedReasoningPolicyNextScenarioResponse,
    BedrockGetAutomatedReasoningPolicyRequest,
    BedrockGetAutomatedReasoningPolicyResponse,
    BedrockGetAutomatedReasoningPolicyTestCaseRequest,
    BedrockGetAutomatedReasoningPolicyTestCaseResponse,
    BedrockGetAutomatedReasoningPolicyTestResultRequest,
    BedrockGetAutomatedReasoningPolicyTestResultResponse,
    BedrockGetCustomModelDeploymentRequest,
    BedrockGetCustomModelDeploymentResponse,
    BedrockGetCustomModelRequest,
    BedrockGetCustomModelResponse,
    BedrockGetEvaluationJobRequest,
    BedrockGetEvaluationJobResponse,
    BedrockGetFoundationModelAvailabilityRequest,
    BedrockGetFoundationModelAvailabilityResponse,
    BedrockGetFoundationModelRequest,
    BedrockGetFoundationModelResponse,
    BedrockGetGuardrailRequest,
    BedrockGetGuardrailResponse,
    BedrockGetImportedModelRequest,
    BedrockGetImportedModelResponse,
    BedrockGetInferenceProfileRequest,
    BedrockGetInferenceProfileResponse,
    BedrockGetMarketplaceModelEndpointRequest,
    BedrockGetMarketplaceModelEndpointResponse,
    BedrockGetModelCopyJobRequest,
    BedrockGetModelCopyJobResponse,
    BedrockGetModelCustomizationJobRequest,
    BedrockGetModelCustomizationJobResponse,
    BedrockGetModelImportJobRequest,
    BedrockGetModelImportJobResponse,
    BedrockGetModelInvocationJobRequest,
    BedrockGetModelInvocationJobResponse,
    BedrockGetModelInvocationLoggingConfigurationRequest,
    BedrockGetModelInvocationLoggingConfigurationResponse,
    BedrockGetOrganizationDataRetentionStorageRequest,
    BedrockGetOrganizationDataRetentionStorageResponse,
    BedrockGetProjectDataRetentionStorageRequest,
    BedrockGetProjectDataRetentionStorageResponse,
    BedrockGetProjectRequest,
    BedrockGetProjectResponse,
    BedrockGetPromptRouterRequest,
    BedrockGetPromptRouterResponse,
    BedrockGetProvisionedModelThroughputRequest,
    BedrockGetProvisionedModelThroughputResponse,
    BedrockGetResourcePolicyRequest,
    BedrockGetResourcePolicyResponse,
    BedrockGetTrustedAccessProgramAccountEnrollmentRequest,
    BedrockGetTrustedAccessProgramAccountEnrollmentResponse,
    BedrockGetTrustedAccessProgramOrganizationEnrollmentRequest,
    BedrockGetTrustedAccessProgramOrganizationEnrollmentResponse,
    BedrockGetTrustedAccessProgramProjectEnrollmentRequest,
    BedrockGetTrustedAccessProgramProjectEnrollmentResponse,
    BedrockGetTrustedAccessProgramRequest,
    BedrockGetTrustedAccessProgramResponse,
    BedrockGetUseCaseForModelAccessRequest,
    BedrockGetUseCaseForModelAccessResponse,
    BedrockListAdvancedPromptOptimizationJobsRequest,
    BedrockListAdvancedPromptOptimizationJobsResponse,
    BedrockListAutomatedReasoningPoliciesRequest,
    BedrockListAutomatedReasoningPoliciesResponse,
    BedrockListAutomatedReasoningPolicyBuildWorkflowsRequest,
    BedrockListAutomatedReasoningPolicyBuildWorkflowsResponse,
    BedrockListAutomatedReasoningPolicyTestCasesRequest,
    BedrockListAutomatedReasoningPolicyTestCasesResponse,
    BedrockListAutomatedReasoningPolicyTestResultsRequest,
    BedrockListAutomatedReasoningPolicyTestResultsResponse,
    BedrockListCustomModelDeploymentsRequest,
    BedrockListCustomModelDeploymentsResponse,
    BedrockListCustomModelsRequest,
    BedrockListCustomModelsResponse,
    BedrockListEnforcedGuardrailsConfigurationRequest,
    BedrockListEnforcedGuardrailsConfigurationResponse,
    BedrockListEvaluationJobsRequest,
    BedrockListEvaluationJobsResponse,
    BedrockListFoundationModelAgreementOffersRequest,
    BedrockListFoundationModelAgreementOffersResponse,
    BedrockListFoundationModelsRequest,
    BedrockListFoundationModelsResponse,
    BedrockListGuardrailsRequest,
    BedrockListGuardrailsResponse,
    BedrockListImportedModelsRequest,
    BedrockListImportedModelsResponse,
    BedrockListInferenceProfilesRequest,
    BedrockListInferenceProfilesResponse,
    BedrockListMarketplaceModelEndpointsRequest,
    BedrockListMarketplaceModelEndpointsResponse,
    BedrockListModelCopyJobsRequest,
    BedrockListModelCopyJobsResponse,
    BedrockListModelCustomizationJobsRequest,
    BedrockListModelCustomizationJobsResponse,
    BedrockListModelImportJobsRequest,
    BedrockListModelImportJobsResponse,
    BedrockListModelInvocationJobsRequest,
    BedrockListModelInvocationJobsResponse,
    BedrockListProjectsRequest,
    BedrockListProjectsResponse,
    BedrockListPromptRoutersRequest,
    BedrockListPromptRoutersResponse,
    BedrockListProvisionedModelThroughputsRequest,
    BedrockListProvisionedModelThroughputsResponse,
    BedrockListTagsForResourceRequest,
    BedrockListTagsForResourceResponse,
    BedrockListTrustedAccessProgramsRequest,
    BedrockListTrustedAccessProgramsResponse,
    BedrockPutAccountDataRetentionRequest,
    BedrockPutAccountDataRetentionResponse,
    BedrockPutAccountDataRetentionStorageRequest,
    BedrockPutAccountDataRetentionStorageResponse,
    BedrockPutEnforcedGuardrailConfigurationRequest,
    BedrockPutEnforcedGuardrailConfigurationResponse,
    BedrockPutModelInvocationLoggingConfigurationRequest,
    BedrockPutModelInvocationLoggingConfigurationResponse,
    BedrockPutOrganizationDataRetentionStorageRequest,
    BedrockPutOrganizationDataRetentionStorageResponse,
    BedrockPutProjectDataRetentionStorageRequest,
    BedrockPutProjectDataRetentionStorageResponse,
    BedrockPutResourcePolicyRequest,
    BedrockPutResourcePolicyResponse,
    BedrockPutTrustedAccessProgramAccountEnrollmentRequest,
    BedrockPutTrustedAccessProgramAccountEnrollmentResponse,
    BedrockPutTrustedAccessProgramOrganizationEnrollmentRequest,
    BedrockPutTrustedAccessProgramOrganizationEnrollmentResponse,
    BedrockPutTrustedAccessProgramProjectEnrollmentRequest,
    BedrockPutTrustedAccessProgramProjectEnrollmentResponse,
    BedrockPutUseCaseForModelAccessRequest,
    BedrockPutUseCaseForModelAccessResponse,
    BedrockRegisterMarketplaceModelEndpointRequest,
    BedrockRegisterMarketplaceModelEndpointResponse,
    BedrockStartAutomatedReasoningPolicyBuildWorkflowRequest,
    BedrockStartAutomatedReasoningPolicyBuildWorkflowResponse,
    BedrockStartAutomatedReasoningPolicyTestWorkflowRequest,
    BedrockStartAutomatedReasoningPolicyTestWorkflowResponse,
    BedrockStartTrustedAccessProgramAccountApplicationRequest,
    BedrockStartTrustedAccessProgramAccountApplicationResponse,
    BedrockStartTrustedAccessProgramOrganizationApplicationRequest,
    BedrockStartTrustedAccessProgramOrganizationApplicationResponse,
    BedrockStartTrustedAccessProgramProjectApplicationRequest,
    BedrockStartTrustedAccessProgramProjectApplicationResponse,
    BedrockStopAdvancedPromptOptimizationJobRequest,
    BedrockStopAdvancedPromptOptimizationJobResponse,
    BedrockStopEvaluationJobRequest,
    BedrockStopEvaluationJobResponse,
    BedrockStopModelCustomizationJobRequest,
    BedrockStopModelCustomizationJobResponse,
    BedrockStopModelInvocationJobRequest,
    BedrockStopModelInvocationJobResponse,
    BedrockTagResourceRequest,
    BedrockTagResourceResponse,
    BedrockUntagResourceRequest,
    BedrockUntagResourceResponse,
    BedrockUpdateAutomatedReasoningPolicyAnnotationsRequest,
    BedrockUpdateAutomatedReasoningPolicyAnnotationsResponse,
    BedrockUpdateAutomatedReasoningPolicyRequest,
    BedrockUpdateAutomatedReasoningPolicyResponse,
    BedrockUpdateAutomatedReasoningPolicyTestCaseRequest,
    BedrockUpdateAutomatedReasoningPolicyTestCaseResponse,
    BedrockUpdateCustomModelDeploymentRequest,
    BedrockUpdateCustomModelDeploymentResponse,
    BedrockUpdateGuardrailRequest,
    BedrockUpdateGuardrailResponse,
    BedrockUpdateMarketplaceModelEndpointRequest,
    BedrockUpdateMarketplaceModelEndpointResponse,
    BedrockUpdateProjectRequest,
    BedrockUpdateProjectResponse,
    BedrockUpdateProvisionedModelThroughputRequest,
    BedrockUpdateProvisionedModelThroughputResponse,
)
from werkflow_aws.types.bedrock_client import BedrockClient
from .base import AWSBaseService


class AWSBedrock(AWSBaseService[BedrockClient]):
    service_name = 'bedrock'
    boto3_service_name = 'bedrock'

    def __init__(self) -> None:
        super().__init__(service_name='bedrock', boto3_service_name='bedrock')

    async def archive_project(
        self,
        request: BedrockArchiveProjectRequest,
    ) -> BedrockArchiveProjectResponse:
        client = self._require_client()
        return await self._execute(client.archive_project, request, BedrockArchiveProjectResponse)

    async def batch_delete_advanced_prompt_optimization_job(
        self,
        request: BedrockBatchDeleteAdvancedPromptOptimizationJobRequest,
    ) -> BedrockBatchDeleteAdvancedPromptOptimizationJobResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_advanced_prompt_optimization_job, request, BedrockBatchDeleteAdvancedPromptOptimizationJobResponse)

    async def batch_delete_evaluation_job(
        self,
        request: BedrockBatchDeleteEvaluationJobRequest,
    ) -> BedrockBatchDeleteEvaluationJobResponse:
        client = self._require_client()
        return await self._execute(client.batch_delete_evaluation_job, request, BedrockBatchDeleteEvaluationJobResponse)

    async def cancel_automated_reasoning_policy_build_workflow(
        self,
        request: BedrockCancelAutomatedReasoningPolicyBuildWorkflowRequest,
    ) -> BedrockCancelAutomatedReasoningPolicyBuildWorkflowResponse:
        client = self._require_client()
        return await self._execute(client.cancel_automated_reasoning_policy_build_workflow, request, BedrockCancelAutomatedReasoningPolicyBuildWorkflowResponse)

    async def create_advanced_prompt_optimization_job(
        self,
        request: BedrockCreateAdvancedPromptOptimizationJobRequest,
    ) -> BedrockCreateAdvancedPromptOptimizationJobResponse:
        client = self._require_client()
        return await self._execute(client.create_advanced_prompt_optimization_job, request, BedrockCreateAdvancedPromptOptimizationJobResponse)

    async def create_automated_reasoning_policy(
        self,
        request: BedrockCreateAutomatedReasoningPolicyRequest,
    ) -> BedrockCreateAutomatedReasoningPolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_automated_reasoning_policy, request, BedrockCreateAutomatedReasoningPolicyResponse)

    async def create_automated_reasoning_policy_test_case(
        self,
        request: BedrockCreateAutomatedReasoningPolicyTestCaseRequest,
    ) -> BedrockCreateAutomatedReasoningPolicyTestCaseResponse:
        client = self._require_client()
        return await self._execute(client.create_automated_reasoning_policy_test_case, request, BedrockCreateAutomatedReasoningPolicyTestCaseResponse)

    async def create_automated_reasoning_policy_version(
        self,
        request: BedrockCreateAutomatedReasoningPolicyVersionRequest,
    ) -> BedrockCreateAutomatedReasoningPolicyVersionResponse:
        client = self._require_client()
        return await self._execute(client.create_automated_reasoning_policy_version, request, BedrockCreateAutomatedReasoningPolicyVersionResponse)

    async def create_custom_model(
        self,
        request: BedrockCreateCustomModelRequest,
    ) -> BedrockCreateCustomModelResponse:
        client = self._require_client()
        return await self._execute(client.create_custom_model, request, BedrockCreateCustomModelResponse)

    async def create_custom_model_deployment(
        self,
        request: BedrockCreateCustomModelDeploymentRequest,
    ) -> BedrockCreateCustomModelDeploymentResponse:
        client = self._require_client()
        return await self._execute(client.create_custom_model_deployment, request, BedrockCreateCustomModelDeploymentResponse)

    async def create_evaluation_job(
        self,
        request: BedrockCreateEvaluationJobRequest,
    ) -> BedrockCreateEvaluationJobResponse:
        client = self._require_client()
        return await self._execute(client.create_evaluation_job, request, BedrockCreateEvaluationJobResponse)

    async def create_foundation_model_agreement(
        self,
        request: BedrockCreateFoundationModelAgreementRequest,
    ) -> BedrockCreateFoundationModelAgreementResponse:
        client = self._require_client()
        return await self._execute(client.create_foundation_model_agreement, request, BedrockCreateFoundationModelAgreementResponse)

    async def create_guardrail(
        self,
        request: BedrockCreateGuardrailRequest,
    ) -> BedrockCreateGuardrailResponse:
        client = self._require_client()
        return await self._execute(client.create_guardrail, request, BedrockCreateGuardrailResponse)

    async def create_guardrail_version(
        self,
        request: BedrockCreateGuardrailVersionRequest,
    ) -> BedrockCreateGuardrailVersionResponse:
        client = self._require_client()
        return await self._execute(client.create_guardrail_version, request, BedrockCreateGuardrailVersionResponse)

    async def create_inference_profile(
        self,
        request: BedrockCreateInferenceProfileRequest,
    ) -> BedrockCreateInferenceProfileResponse:
        client = self._require_client()
        return await self._execute(client.create_inference_profile, request, BedrockCreateInferenceProfileResponse)

    async def create_marketplace_model_endpoint(
        self,
        request: BedrockCreateMarketplaceModelEndpointRequest,
    ) -> BedrockCreateMarketplaceModelEndpointResponse:
        client = self._require_client()
        return await self._execute(client.create_marketplace_model_endpoint, request, BedrockCreateMarketplaceModelEndpointResponse)

    async def create_model_copy_job(
        self,
        request: BedrockCreateModelCopyJobRequest,
    ) -> BedrockCreateModelCopyJobResponse:
        client = self._require_client()
        return await self._execute(client.create_model_copy_job, request, BedrockCreateModelCopyJobResponse)

    async def create_model_customization_job(
        self,
        request: BedrockCreateModelCustomizationJobRequest,
    ) -> BedrockCreateModelCustomizationJobResponse:
        client = self._require_client()
        return await self._execute(client.create_model_customization_job, request, BedrockCreateModelCustomizationJobResponse)

    async def create_model_import_job(
        self,
        request: BedrockCreateModelImportJobRequest,
    ) -> BedrockCreateModelImportJobResponse:
        client = self._require_client()
        return await self._execute(client.create_model_import_job, request, BedrockCreateModelImportJobResponse)

    async def create_model_invocation_job(
        self,
        request: BedrockCreateModelInvocationJobRequest,
    ) -> BedrockCreateModelInvocationJobResponse:
        client = self._require_client()
        return await self._execute(client.create_model_invocation_job, request, BedrockCreateModelInvocationJobResponse)

    async def create_project(
        self,
        request: BedrockCreateProjectRequest,
    ) -> BedrockCreateProjectResponse:
        client = self._require_client()
        return await self._execute(client.create_project, request, BedrockCreateProjectResponse)

    async def create_prompt_router(
        self,
        request: BedrockCreatePromptRouterRequest,
    ) -> BedrockCreatePromptRouterResponse:
        client = self._require_client()
        return await self._execute(client.create_prompt_router, request, BedrockCreatePromptRouterResponse)

    async def create_provisioned_model_throughput(
        self,
        request: BedrockCreateProvisionedModelThroughputRequest,
    ) -> BedrockCreateProvisionedModelThroughputResponse:
        client = self._require_client()
        return await self._execute(client.create_provisioned_model_throughput, request, BedrockCreateProvisionedModelThroughputResponse)

    async def delete_account_data_retention_storage(
        self,
        request: BedrockDeleteAccountDataRetentionStorageRequest,
    ) -> BedrockDeleteAccountDataRetentionStorageResponse:
        client = self._require_client()
        return await self._execute(client.delete_account_data_retention_storage, request, BedrockDeleteAccountDataRetentionStorageResponse)

    async def delete_automated_reasoning_policy(
        self,
        request: BedrockDeleteAutomatedReasoningPolicyRequest,
    ) -> BedrockDeleteAutomatedReasoningPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_automated_reasoning_policy, request, BedrockDeleteAutomatedReasoningPolicyResponse)

    async def delete_automated_reasoning_policy_build_workflow(
        self,
        request: BedrockDeleteAutomatedReasoningPolicyBuildWorkflowRequest,
    ) -> BedrockDeleteAutomatedReasoningPolicyBuildWorkflowResponse:
        client = self._require_client()
        return await self._execute(client.delete_automated_reasoning_policy_build_workflow, request, BedrockDeleteAutomatedReasoningPolicyBuildWorkflowResponse)

    async def delete_automated_reasoning_policy_test_case(
        self,
        request: BedrockDeleteAutomatedReasoningPolicyTestCaseRequest,
    ) -> BedrockDeleteAutomatedReasoningPolicyTestCaseResponse:
        client = self._require_client()
        return await self._execute(client.delete_automated_reasoning_policy_test_case, request, BedrockDeleteAutomatedReasoningPolicyTestCaseResponse)

    async def delete_custom_model(
        self,
        request: BedrockDeleteCustomModelRequest,
    ) -> BedrockDeleteCustomModelResponse:
        client = self._require_client()
        return await self._execute(client.delete_custom_model, request, BedrockDeleteCustomModelResponse)

    async def delete_custom_model_deployment(
        self,
        request: BedrockDeleteCustomModelDeploymentRequest,
    ) -> BedrockDeleteCustomModelDeploymentResponse:
        client = self._require_client()
        return await self._execute(client.delete_custom_model_deployment, request, BedrockDeleteCustomModelDeploymentResponse)

    async def delete_enforced_guardrail_configuration(
        self,
        request: BedrockDeleteEnforcedGuardrailConfigurationRequest,
    ) -> BedrockDeleteEnforcedGuardrailConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_enforced_guardrail_configuration, request, BedrockDeleteEnforcedGuardrailConfigurationResponse)

    async def delete_foundation_model_agreement(
        self,
        request: BedrockDeleteFoundationModelAgreementRequest,
    ) -> BedrockDeleteFoundationModelAgreementResponse:
        client = self._require_client()
        return await self._execute(client.delete_foundation_model_agreement, request, BedrockDeleteFoundationModelAgreementResponse)

    async def delete_guardrail(
        self,
        request: BedrockDeleteGuardrailRequest,
    ) -> BedrockDeleteGuardrailResponse:
        client = self._require_client()
        return await self._execute(client.delete_guardrail, request, BedrockDeleteGuardrailResponse)

    async def delete_imported_model(
        self,
        request: BedrockDeleteImportedModelRequest,
    ) -> BedrockDeleteImportedModelResponse:
        client = self._require_client()
        return await self._execute(client.delete_imported_model, request, BedrockDeleteImportedModelResponse)

    async def delete_inference_profile(
        self,
        request: BedrockDeleteInferenceProfileRequest,
    ) -> BedrockDeleteInferenceProfileResponse:
        client = self._require_client()
        return await self._execute(client.delete_inference_profile, request, BedrockDeleteInferenceProfileResponse)

    async def delete_marketplace_model_endpoint(
        self,
        request: BedrockDeleteMarketplaceModelEndpointRequest,
    ) -> BedrockDeleteMarketplaceModelEndpointResponse:
        client = self._require_client()
        return await self._execute(client.delete_marketplace_model_endpoint, request, BedrockDeleteMarketplaceModelEndpointResponse)

    async def delete_model_invocation_logging_configuration(
        self,
        request: BedrockDeleteModelInvocationLoggingConfigurationRequest | None = None,
    ) -> BedrockDeleteModelInvocationLoggingConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_model_invocation_logging_configuration, request, BedrockDeleteModelInvocationLoggingConfigurationResponse)

    async def delete_organization_data_retention_storage(
        self,
        request: BedrockDeleteOrganizationDataRetentionStorageRequest,
    ) -> BedrockDeleteOrganizationDataRetentionStorageResponse:
        client = self._require_client()
        return await self._execute(client.delete_organization_data_retention_storage, request, BedrockDeleteOrganizationDataRetentionStorageResponse)

    async def delete_project_data_retention_storage(
        self,
        request: BedrockDeleteProjectDataRetentionStorageRequest,
    ) -> BedrockDeleteProjectDataRetentionStorageResponse:
        client = self._require_client()
        return await self._execute(client.delete_project_data_retention_storage, request, BedrockDeleteProjectDataRetentionStorageResponse)

    async def delete_prompt_router(
        self,
        request: BedrockDeletePromptRouterRequest,
    ) -> BedrockDeletePromptRouterResponse:
        client = self._require_client()
        return await self._execute(client.delete_prompt_router, request, BedrockDeletePromptRouterResponse)

    async def delete_provisioned_model_throughput(
        self,
        request: BedrockDeleteProvisionedModelThroughputRequest,
    ) -> BedrockDeleteProvisionedModelThroughputResponse:
        client = self._require_client()
        return await self._execute(client.delete_provisioned_model_throughput, request, BedrockDeleteProvisionedModelThroughputResponse)

    async def delete_resource_policy(
        self,
        request: BedrockDeleteResourcePolicyRequest,
    ) -> BedrockDeleteResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_policy, request, BedrockDeleteResourcePolicyResponse)

    async def deregister_marketplace_model_endpoint(
        self,
        request: BedrockDeregisterMarketplaceModelEndpointRequest,
    ) -> BedrockDeregisterMarketplaceModelEndpointResponse:
        client = self._require_client()
        return await self._execute(client.deregister_marketplace_model_endpoint, request, BedrockDeregisterMarketplaceModelEndpointResponse)

    async def export_automated_reasoning_policy_version(
        self,
        request: BedrockExportAutomatedReasoningPolicyVersionRequest,
    ) -> BedrockExportAutomatedReasoningPolicyVersionResponse:
        client = self._require_client()
        return await self._execute(client.export_automated_reasoning_policy_version, request, BedrockExportAutomatedReasoningPolicyVersionResponse)

    async def get_account_data_retention(
        self,
        request: BedrockGetAccountDataRetentionRequest | None = None,
    ) -> BedrockGetAccountDataRetentionResponse:
        client = self._require_client()
        return await self._execute(client.get_account_data_retention, request, BedrockGetAccountDataRetentionResponse)

    async def get_account_data_retention_storage(
        self,
        request: BedrockGetAccountDataRetentionStorageRequest,
    ) -> BedrockGetAccountDataRetentionStorageResponse:
        client = self._require_client()
        return await self._execute(client.get_account_data_retention_storage, request, BedrockGetAccountDataRetentionStorageResponse)

    async def get_advanced_prompt_optimization_job(
        self,
        request: BedrockGetAdvancedPromptOptimizationJobRequest,
    ) -> BedrockGetAdvancedPromptOptimizationJobResponse:
        client = self._require_client()
        return await self._execute(client.get_advanced_prompt_optimization_job, request, BedrockGetAdvancedPromptOptimizationJobResponse)

    async def get_automated_reasoning_policy(
        self,
        request: BedrockGetAutomatedReasoningPolicyRequest,
    ) -> BedrockGetAutomatedReasoningPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_automated_reasoning_policy, request, BedrockGetAutomatedReasoningPolicyResponse)

    async def get_automated_reasoning_policy_annotations(
        self,
        request: BedrockGetAutomatedReasoningPolicyAnnotationsRequest,
    ) -> BedrockGetAutomatedReasoningPolicyAnnotationsResponse:
        client = self._require_client()
        return await self._execute(client.get_automated_reasoning_policy_annotations, request, BedrockGetAutomatedReasoningPolicyAnnotationsResponse)

    async def get_automated_reasoning_policy_build_workflow(
        self,
        request: BedrockGetAutomatedReasoningPolicyBuildWorkflowRequest,
    ) -> BedrockGetAutomatedReasoningPolicyBuildWorkflowResponse:
        client = self._require_client()
        return await self._execute(client.get_automated_reasoning_policy_build_workflow, request, BedrockGetAutomatedReasoningPolicyBuildWorkflowResponse)

    async def get_automated_reasoning_policy_build_workflow_result_assets(
        self,
        request: BedrockGetAutomatedReasoningPolicyBuildWorkflowResultAssetsRequest,
    ) -> BedrockGetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse:
        client = self._require_client()
        return await self._execute(client.get_automated_reasoning_policy_build_workflow_result_assets, request, BedrockGetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse)

    async def get_automated_reasoning_policy_next_scenario(
        self,
        request: BedrockGetAutomatedReasoningPolicyNextScenarioRequest,
    ) -> BedrockGetAutomatedReasoningPolicyNextScenarioResponse:
        client = self._require_client()
        return await self._execute(client.get_automated_reasoning_policy_next_scenario, request, BedrockGetAutomatedReasoningPolicyNextScenarioResponse)

    async def get_automated_reasoning_policy_test_case(
        self,
        request: BedrockGetAutomatedReasoningPolicyTestCaseRequest,
    ) -> BedrockGetAutomatedReasoningPolicyTestCaseResponse:
        client = self._require_client()
        return await self._execute(client.get_automated_reasoning_policy_test_case, request, BedrockGetAutomatedReasoningPolicyTestCaseResponse)

    async def get_automated_reasoning_policy_test_result(
        self,
        request: BedrockGetAutomatedReasoningPolicyTestResultRequest,
    ) -> BedrockGetAutomatedReasoningPolicyTestResultResponse:
        client = self._require_client()
        return await self._execute(client.get_automated_reasoning_policy_test_result, request, BedrockGetAutomatedReasoningPolicyTestResultResponse)

    async def get_custom_model(
        self,
        request: BedrockGetCustomModelRequest,
    ) -> BedrockGetCustomModelResponse:
        client = self._require_client()
        return await self._execute(client.get_custom_model, request, BedrockGetCustomModelResponse)

    async def get_custom_model_deployment(
        self,
        request: BedrockGetCustomModelDeploymentRequest,
    ) -> BedrockGetCustomModelDeploymentResponse:
        client = self._require_client()
        return await self._execute(client.get_custom_model_deployment, request, BedrockGetCustomModelDeploymentResponse)

    async def get_evaluation_job(
        self,
        request: BedrockGetEvaluationJobRequest,
    ) -> BedrockGetEvaluationJobResponse:
        client = self._require_client()
        return await self._execute(client.get_evaluation_job, request, BedrockGetEvaluationJobResponse)

    async def get_foundation_model(
        self,
        request: BedrockGetFoundationModelRequest,
    ) -> BedrockGetFoundationModelResponse:
        client = self._require_client()
        return await self._execute(client.get_foundation_model, request, BedrockGetFoundationModelResponse)

    async def get_foundation_model_availability(
        self,
        request: BedrockGetFoundationModelAvailabilityRequest,
    ) -> BedrockGetFoundationModelAvailabilityResponse:
        client = self._require_client()
        return await self._execute(client.get_foundation_model_availability, request, BedrockGetFoundationModelAvailabilityResponse)

    async def get_guardrail(
        self,
        request: BedrockGetGuardrailRequest,
    ) -> BedrockGetGuardrailResponse:
        client = self._require_client()
        return await self._execute(client.get_guardrail, request, BedrockGetGuardrailResponse)

    async def get_imported_model(
        self,
        request: BedrockGetImportedModelRequest,
    ) -> BedrockGetImportedModelResponse:
        client = self._require_client()
        return await self._execute(client.get_imported_model, request, BedrockGetImportedModelResponse)

    async def get_inference_profile(
        self,
        request: BedrockGetInferenceProfileRequest,
    ) -> BedrockGetInferenceProfileResponse:
        client = self._require_client()
        return await self._execute(client.get_inference_profile, request, BedrockGetInferenceProfileResponse)

    async def get_marketplace_model_endpoint(
        self,
        request: BedrockGetMarketplaceModelEndpointRequest,
    ) -> BedrockGetMarketplaceModelEndpointResponse:
        client = self._require_client()
        return await self._execute(client.get_marketplace_model_endpoint, request, BedrockGetMarketplaceModelEndpointResponse)

    async def get_model_copy_job(
        self,
        request: BedrockGetModelCopyJobRequest,
    ) -> BedrockGetModelCopyJobResponse:
        client = self._require_client()
        return await self._execute(client.get_model_copy_job, request, BedrockGetModelCopyJobResponse)

    async def get_model_customization_job(
        self,
        request: BedrockGetModelCustomizationJobRequest,
    ) -> BedrockGetModelCustomizationJobResponse:
        client = self._require_client()
        return await self._execute(client.get_model_customization_job, request, BedrockGetModelCustomizationJobResponse)

    async def get_model_import_job(
        self,
        request: BedrockGetModelImportJobRequest,
    ) -> BedrockGetModelImportJobResponse:
        client = self._require_client()
        return await self._execute(client.get_model_import_job, request, BedrockGetModelImportJobResponse)

    async def get_model_invocation_job(
        self,
        request: BedrockGetModelInvocationJobRequest,
    ) -> BedrockGetModelInvocationJobResponse:
        client = self._require_client()
        return await self._execute(client.get_model_invocation_job, request, BedrockGetModelInvocationJobResponse)

    async def get_model_invocation_logging_configuration(
        self,
        request: BedrockGetModelInvocationLoggingConfigurationRequest | None = None,
    ) -> BedrockGetModelInvocationLoggingConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.get_model_invocation_logging_configuration, request, BedrockGetModelInvocationLoggingConfigurationResponse)

    async def get_organization_data_retention_storage(
        self,
        request: BedrockGetOrganizationDataRetentionStorageRequest,
    ) -> BedrockGetOrganizationDataRetentionStorageResponse:
        client = self._require_client()
        return await self._execute(client.get_organization_data_retention_storage, request, BedrockGetOrganizationDataRetentionStorageResponse)

    async def get_project(
        self,
        request: BedrockGetProjectRequest,
    ) -> BedrockGetProjectResponse:
        client = self._require_client()
        return await self._execute(client.get_project, request, BedrockGetProjectResponse)

    async def get_project_data_retention_storage(
        self,
        request: BedrockGetProjectDataRetentionStorageRequest,
    ) -> BedrockGetProjectDataRetentionStorageResponse:
        client = self._require_client()
        return await self._execute(client.get_project_data_retention_storage, request, BedrockGetProjectDataRetentionStorageResponse)

    async def get_prompt_router(
        self,
        request: BedrockGetPromptRouterRequest,
    ) -> BedrockGetPromptRouterResponse:
        client = self._require_client()
        return await self._execute(client.get_prompt_router, request, BedrockGetPromptRouterResponse)

    async def get_provisioned_model_throughput(
        self,
        request: BedrockGetProvisionedModelThroughputRequest,
    ) -> BedrockGetProvisionedModelThroughputResponse:
        client = self._require_client()
        return await self._execute(client.get_provisioned_model_throughput, request, BedrockGetProvisionedModelThroughputResponse)

    async def get_resource_policy(
        self,
        request: BedrockGetResourcePolicyRequest,
    ) -> BedrockGetResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_policy, request, BedrockGetResourcePolicyResponse)

    async def get_trusted_access_program(
        self,
        request: BedrockGetTrustedAccessProgramRequest,
    ) -> BedrockGetTrustedAccessProgramResponse:
        client = self._require_client()
        return await self._execute(client.get_trusted_access_program, request, BedrockGetTrustedAccessProgramResponse)

    async def get_trusted_access_program_account_enrollment(
        self,
        request: BedrockGetTrustedAccessProgramAccountEnrollmentRequest,
    ) -> BedrockGetTrustedAccessProgramAccountEnrollmentResponse:
        client = self._require_client()
        return await self._execute(client.get_trusted_access_program_account_enrollment, request, BedrockGetTrustedAccessProgramAccountEnrollmentResponse)

    async def get_trusted_access_program_organization_enrollment(
        self,
        request: BedrockGetTrustedAccessProgramOrganizationEnrollmentRequest,
    ) -> BedrockGetTrustedAccessProgramOrganizationEnrollmentResponse:
        client = self._require_client()
        return await self._execute(client.get_trusted_access_program_organization_enrollment, request, BedrockGetTrustedAccessProgramOrganizationEnrollmentResponse)

    async def get_trusted_access_program_project_enrollment(
        self,
        request: BedrockGetTrustedAccessProgramProjectEnrollmentRequest,
    ) -> BedrockGetTrustedAccessProgramProjectEnrollmentResponse:
        client = self._require_client()
        return await self._execute(client.get_trusted_access_program_project_enrollment, request, BedrockGetTrustedAccessProgramProjectEnrollmentResponse)

    async def get_use_case_for_model_access(
        self,
        request: BedrockGetUseCaseForModelAccessRequest | None = None,
    ) -> BedrockGetUseCaseForModelAccessResponse:
        client = self._require_client()
        return await self._execute(client.get_use_case_for_model_access, request, BedrockGetUseCaseForModelAccessResponse)

    async def list_advanced_prompt_optimization_jobs(
        self,
        request: BedrockListAdvancedPromptOptimizationJobsRequest | None = None,
    ) -> BedrockListAdvancedPromptOptimizationJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_advanced_prompt_optimization_jobs, request, BedrockListAdvancedPromptOptimizationJobsResponse)

    async def list_advanced_prompt_optimization_jobs_paginated(
        self,
        request: BedrockListAdvancedPromptOptimizationJobsRequest | None = None,
    ) -> list[BedrockListAdvancedPromptOptimizationJobsResponse]:
        return await self._paginate('list_advanced_prompt_optimization_jobs', request, BedrockListAdvancedPromptOptimizationJobsResponse)

    async def list_automated_reasoning_policies(
        self,
        request: BedrockListAutomatedReasoningPoliciesRequest | None = None,
    ) -> BedrockListAutomatedReasoningPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.list_automated_reasoning_policies, request, BedrockListAutomatedReasoningPoliciesResponse)

    async def list_automated_reasoning_policies_paginated(
        self,
        request: BedrockListAutomatedReasoningPoliciesRequest | None = None,
    ) -> list[BedrockListAutomatedReasoningPoliciesResponse]:
        return await self._paginate('list_automated_reasoning_policies', request, BedrockListAutomatedReasoningPoliciesResponse)

    async def list_automated_reasoning_policy_build_workflows(
        self,
        request: BedrockListAutomatedReasoningPolicyBuildWorkflowsRequest,
    ) -> BedrockListAutomatedReasoningPolicyBuildWorkflowsResponse:
        client = self._require_client()
        return await self._execute(client.list_automated_reasoning_policy_build_workflows, request, BedrockListAutomatedReasoningPolicyBuildWorkflowsResponse)

    async def list_automated_reasoning_policy_build_workflows_paginated(
        self,
        request: BedrockListAutomatedReasoningPolicyBuildWorkflowsRequest,
    ) -> list[BedrockListAutomatedReasoningPolicyBuildWorkflowsResponse]:
        return await self._paginate('list_automated_reasoning_policy_build_workflows', request, BedrockListAutomatedReasoningPolicyBuildWorkflowsResponse)

    async def list_automated_reasoning_policy_test_cases(
        self,
        request: BedrockListAutomatedReasoningPolicyTestCasesRequest,
    ) -> BedrockListAutomatedReasoningPolicyTestCasesResponse:
        client = self._require_client()
        return await self._execute(client.list_automated_reasoning_policy_test_cases, request, BedrockListAutomatedReasoningPolicyTestCasesResponse)

    async def list_automated_reasoning_policy_test_cases_paginated(
        self,
        request: BedrockListAutomatedReasoningPolicyTestCasesRequest,
    ) -> list[BedrockListAutomatedReasoningPolicyTestCasesResponse]:
        return await self._paginate('list_automated_reasoning_policy_test_cases', request, BedrockListAutomatedReasoningPolicyTestCasesResponse)

    async def list_automated_reasoning_policy_test_results(
        self,
        request: BedrockListAutomatedReasoningPolicyTestResultsRequest,
    ) -> BedrockListAutomatedReasoningPolicyTestResultsResponse:
        client = self._require_client()
        return await self._execute(client.list_automated_reasoning_policy_test_results, request, BedrockListAutomatedReasoningPolicyTestResultsResponse)

    async def list_automated_reasoning_policy_test_results_paginated(
        self,
        request: BedrockListAutomatedReasoningPolicyTestResultsRequest,
    ) -> list[BedrockListAutomatedReasoningPolicyTestResultsResponse]:
        return await self._paginate('list_automated_reasoning_policy_test_results', request, BedrockListAutomatedReasoningPolicyTestResultsResponse)

    async def list_custom_model_deployments(
        self,
        request: BedrockListCustomModelDeploymentsRequest | None = None,
    ) -> BedrockListCustomModelDeploymentsResponse:
        client = self._require_client()
        return await self._execute(client.list_custom_model_deployments, request, BedrockListCustomModelDeploymentsResponse)

    async def list_custom_model_deployments_paginated(
        self,
        request: BedrockListCustomModelDeploymentsRequest | None = None,
    ) -> list[BedrockListCustomModelDeploymentsResponse]:
        return await self._paginate('list_custom_model_deployments', request, BedrockListCustomModelDeploymentsResponse)

    async def list_custom_models(
        self,
        request: BedrockListCustomModelsRequest | None = None,
    ) -> BedrockListCustomModelsResponse:
        client = self._require_client()
        return await self._execute(client.list_custom_models, request, BedrockListCustomModelsResponse)

    async def list_custom_models_paginated(
        self,
        request: BedrockListCustomModelsRequest | None = None,
    ) -> list[BedrockListCustomModelsResponse]:
        return await self._paginate('list_custom_models', request, BedrockListCustomModelsResponse)

    async def list_enforced_guardrails_configuration(
        self,
        request: BedrockListEnforcedGuardrailsConfigurationRequest | None = None,
    ) -> BedrockListEnforcedGuardrailsConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.list_enforced_guardrails_configuration, request, BedrockListEnforcedGuardrailsConfigurationResponse)

    async def list_enforced_guardrails_configuration_paginated(
        self,
        request: BedrockListEnforcedGuardrailsConfigurationRequest | None = None,
    ) -> list[BedrockListEnforcedGuardrailsConfigurationResponse]:
        return await self._paginate('list_enforced_guardrails_configuration', request, BedrockListEnforcedGuardrailsConfigurationResponse)

    async def list_evaluation_jobs(
        self,
        request: BedrockListEvaluationJobsRequest | None = None,
    ) -> BedrockListEvaluationJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_evaluation_jobs, request, BedrockListEvaluationJobsResponse)

    async def list_evaluation_jobs_paginated(
        self,
        request: BedrockListEvaluationJobsRequest | None = None,
    ) -> list[BedrockListEvaluationJobsResponse]:
        return await self._paginate('list_evaluation_jobs', request, BedrockListEvaluationJobsResponse)

    async def list_foundation_model_agreement_offers(
        self,
        request: BedrockListFoundationModelAgreementOffersRequest,
    ) -> BedrockListFoundationModelAgreementOffersResponse:
        client = self._require_client()
        return await self._execute(client.list_foundation_model_agreement_offers, request, BedrockListFoundationModelAgreementOffersResponse)

    async def list_foundation_models(
        self,
        request: BedrockListFoundationModelsRequest | None = None,
    ) -> BedrockListFoundationModelsResponse:
        client = self._require_client()
        return await self._execute(client.list_foundation_models, request, BedrockListFoundationModelsResponse)

    async def list_guardrails(
        self,
        request: BedrockListGuardrailsRequest | None = None,
    ) -> BedrockListGuardrailsResponse:
        client = self._require_client()
        return await self._execute(client.list_guardrails, request, BedrockListGuardrailsResponse)

    async def list_guardrails_paginated(
        self,
        request: BedrockListGuardrailsRequest | None = None,
    ) -> list[BedrockListGuardrailsResponse]:
        return await self._paginate('list_guardrails', request, BedrockListGuardrailsResponse)

    async def list_imported_models(
        self,
        request: BedrockListImportedModelsRequest | None = None,
    ) -> BedrockListImportedModelsResponse:
        client = self._require_client()
        return await self._execute(client.list_imported_models, request, BedrockListImportedModelsResponse)

    async def list_imported_models_paginated(
        self,
        request: BedrockListImportedModelsRequest | None = None,
    ) -> list[BedrockListImportedModelsResponse]:
        return await self._paginate('list_imported_models', request, BedrockListImportedModelsResponse)

    async def list_inference_profiles(
        self,
        request: BedrockListInferenceProfilesRequest | None = None,
    ) -> BedrockListInferenceProfilesResponse:
        client = self._require_client()
        return await self._execute(client.list_inference_profiles, request, BedrockListInferenceProfilesResponse)

    async def list_inference_profiles_paginated(
        self,
        request: BedrockListInferenceProfilesRequest | None = None,
    ) -> list[BedrockListInferenceProfilesResponse]:
        return await self._paginate('list_inference_profiles', request, BedrockListInferenceProfilesResponse)

    async def list_marketplace_model_endpoints(
        self,
        request: BedrockListMarketplaceModelEndpointsRequest | None = None,
    ) -> BedrockListMarketplaceModelEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.list_marketplace_model_endpoints, request, BedrockListMarketplaceModelEndpointsResponse)

    async def list_marketplace_model_endpoints_paginated(
        self,
        request: BedrockListMarketplaceModelEndpointsRequest | None = None,
    ) -> list[BedrockListMarketplaceModelEndpointsResponse]:
        return await self._paginate('list_marketplace_model_endpoints', request, BedrockListMarketplaceModelEndpointsResponse)

    async def list_model_copy_jobs(
        self,
        request: BedrockListModelCopyJobsRequest | None = None,
    ) -> BedrockListModelCopyJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_model_copy_jobs, request, BedrockListModelCopyJobsResponse)

    async def list_model_copy_jobs_paginated(
        self,
        request: BedrockListModelCopyJobsRequest | None = None,
    ) -> list[BedrockListModelCopyJobsResponse]:
        return await self._paginate('list_model_copy_jobs', request, BedrockListModelCopyJobsResponse)

    async def list_model_customization_jobs(
        self,
        request: BedrockListModelCustomizationJobsRequest | None = None,
    ) -> BedrockListModelCustomizationJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_model_customization_jobs, request, BedrockListModelCustomizationJobsResponse)

    async def list_model_customization_jobs_paginated(
        self,
        request: BedrockListModelCustomizationJobsRequest | None = None,
    ) -> list[BedrockListModelCustomizationJobsResponse]:
        return await self._paginate('list_model_customization_jobs', request, BedrockListModelCustomizationJobsResponse)

    async def list_model_import_jobs(
        self,
        request: BedrockListModelImportJobsRequest | None = None,
    ) -> BedrockListModelImportJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_model_import_jobs, request, BedrockListModelImportJobsResponse)

    async def list_model_import_jobs_paginated(
        self,
        request: BedrockListModelImportJobsRequest | None = None,
    ) -> list[BedrockListModelImportJobsResponse]:
        return await self._paginate('list_model_import_jobs', request, BedrockListModelImportJobsResponse)

    async def list_model_invocation_jobs(
        self,
        request: BedrockListModelInvocationJobsRequest | None = None,
    ) -> BedrockListModelInvocationJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_model_invocation_jobs, request, BedrockListModelInvocationJobsResponse)

    async def list_model_invocation_jobs_paginated(
        self,
        request: BedrockListModelInvocationJobsRequest | None = None,
    ) -> list[BedrockListModelInvocationJobsResponse]:
        return await self._paginate('list_model_invocation_jobs', request, BedrockListModelInvocationJobsResponse)

    async def list_projects(
        self,
        request: BedrockListProjectsRequest | None = None,
    ) -> BedrockListProjectsResponse:
        client = self._require_client()
        return await self._execute(client.list_projects, request, BedrockListProjectsResponse)

    async def list_projects_paginated(
        self,
        request: BedrockListProjectsRequest | None = None,
    ) -> list[BedrockListProjectsResponse]:
        return await self._paginate('list_projects', request, BedrockListProjectsResponse)

    async def list_prompt_routers(
        self,
        request: BedrockListPromptRoutersRequest | None = None,
    ) -> BedrockListPromptRoutersResponse:
        client = self._require_client()
        return await self._execute(client.list_prompt_routers, request, BedrockListPromptRoutersResponse)

    async def list_prompt_routers_paginated(
        self,
        request: BedrockListPromptRoutersRequest | None = None,
    ) -> list[BedrockListPromptRoutersResponse]:
        return await self._paginate('list_prompt_routers', request, BedrockListPromptRoutersResponse)

    async def list_provisioned_model_throughputs(
        self,
        request: BedrockListProvisionedModelThroughputsRequest | None = None,
    ) -> BedrockListProvisionedModelThroughputsResponse:
        client = self._require_client()
        return await self._execute(client.list_provisioned_model_throughputs, request, BedrockListProvisionedModelThroughputsResponse)

    async def list_provisioned_model_throughputs_paginated(
        self,
        request: BedrockListProvisionedModelThroughputsRequest | None = None,
    ) -> list[BedrockListProvisionedModelThroughputsResponse]:
        return await self._paginate('list_provisioned_model_throughputs', request, BedrockListProvisionedModelThroughputsResponse)

    async def list_tags_for_resource(
        self,
        request: BedrockListTagsForResourceRequest,
    ) -> BedrockListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, BedrockListTagsForResourceResponse)

    async def list_trusted_access_programs(
        self,
        request: BedrockListTrustedAccessProgramsRequest | None = None,
    ) -> BedrockListTrustedAccessProgramsResponse:
        client = self._require_client()
        return await self._execute(client.list_trusted_access_programs, request, BedrockListTrustedAccessProgramsResponse)

    async def list_trusted_access_programs_paginated(
        self,
        request: BedrockListTrustedAccessProgramsRequest | None = None,
    ) -> list[BedrockListTrustedAccessProgramsResponse]:
        return await self._paginate('list_trusted_access_programs', request, BedrockListTrustedAccessProgramsResponse)

    async def put_account_data_retention(
        self,
        request: BedrockPutAccountDataRetentionRequest,
    ) -> BedrockPutAccountDataRetentionResponse:
        client = self._require_client()
        return await self._execute(client.put_account_data_retention, request, BedrockPutAccountDataRetentionResponse)

    async def put_account_data_retention_storage(
        self,
        request: BedrockPutAccountDataRetentionStorageRequest,
    ) -> BedrockPutAccountDataRetentionStorageResponse:
        client = self._require_client()
        return await self._execute(client.put_account_data_retention_storage, request, BedrockPutAccountDataRetentionStorageResponse)

    async def put_enforced_guardrail_configuration(
        self,
        request: BedrockPutEnforcedGuardrailConfigurationRequest,
    ) -> BedrockPutEnforcedGuardrailConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_enforced_guardrail_configuration, request, BedrockPutEnforcedGuardrailConfigurationResponse)

    async def put_model_invocation_logging_configuration(
        self,
        request: BedrockPutModelInvocationLoggingConfigurationRequest,
    ) -> BedrockPutModelInvocationLoggingConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.put_model_invocation_logging_configuration, request, BedrockPutModelInvocationLoggingConfigurationResponse)

    async def put_organization_data_retention_storage(
        self,
        request: BedrockPutOrganizationDataRetentionStorageRequest,
    ) -> BedrockPutOrganizationDataRetentionStorageResponse:
        client = self._require_client()
        return await self._execute(client.put_organization_data_retention_storage, request, BedrockPutOrganizationDataRetentionStorageResponse)

    async def put_project_data_retention_storage(
        self,
        request: BedrockPutProjectDataRetentionStorageRequest,
    ) -> BedrockPutProjectDataRetentionStorageResponse:
        client = self._require_client()
        return await self._execute(client.put_project_data_retention_storage, request, BedrockPutProjectDataRetentionStorageResponse)

    async def put_resource_policy(
        self,
        request: BedrockPutResourcePolicyRequest,
    ) -> BedrockPutResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_resource_policy, request, BedrockPutResourcePolicyResponse)

    async def put_trusted_access_program_account_enrollment(
        self,
        request: BedrockPutTrustedAccessProgramAccountEnrollmentRequest,
    ) -> BedrockPutTrustedAccessProgramAccountEnrollmentResponse:
        client = self._require_client()
        return await self._execute(client.put_trusted_access_program_account_enrollment, request, BedrockPutTrustedAccessProgramAccountEnrollmentResponse)

    async def put_trusted_access_program_organization_enrollment(
        self,
        request: BedrockPutTrustedAccessProgramOrganizationEnrollmentRequest,
    ) -> BedrockPutTrustedAccessProgramOrganizationEnrollmentResponse:
        client = self._require_client()
        return await self._execute(client.put_trusted_access_program_organization_enrollment, request, BedrockPutTrustedAccessProgramOrganizationEnrollmentResponse)

    async def put_trusted_access_program_project_enrollment(
        self,
        request: BedrockPutTrustedAccessProgramProjectEnrollmentRequest,
    ) -> BedrockPutTrustedAccessProgramProjectEnrollmentResponse:
        client = self._require_client()
        return await self._execute(client.put_trusted_access_program_project_enrollment, request, BedrockPutTrustedAccessProgramProjectEnrollmentResponse)

    async def put_use_case_for_model_access(
        self,
        request: BedrockPutUseCaseForModelAccessRequest,
    ) -> BedrockPutUseCaseForModelAccessResponse:
        client = self._require_client()
        return await self._execute(client.put_use_case_for_model_access, request, BedrockPutUseCaseForModelAccessResponse)

    async def register_marketplace_model_endpoint(
        self,
        request: BedrockRegisterMarketplaceModelEndpointRequest,
    ) -> BedrockRegisterMarketplaceModelEndpointResponse:
        client = self._require_client()
        return await self._execute(client.register_marketplace_model_endpoint, request, BedrockRegisterMarketplaceModelEndpointResponse)

    async def start_automated_reasoning_policy_build_workflow(
        self,
        request: BedrockStartAutomatedReasoningPolicyBuildWorkflowRequest,
    ) -> BedrockStartAutomatedReasoningPolicyBuildWorkflowResponse:
        client = self._require_client()
        return await self._execute(client.start_automated_reasoning_policy_build_workflow, request, BedrockStartAutomatedReasoningPolicyBuildWorkflowResponse)

    async def start_automated_reasoning_policy_test_workflow(
        self,
        request: BedrockStartAutomatedReasoningPolicyTestWorkflowRequest,
    ) -> BedrockStartAutomatedReasoningPolicyTestWorkflowResponse:
        client = self._require_client()
        return await self._execute(client.start_automated_reasoning_policy_test_workflow, request, BedrockStartAutomatedReasoningPolicyTestWorkflowResponse)

    async def start_trusted_access_program_account_application(
        self,
        request: BedrockStartTrustedAccessProgramAccountApplicationRequest,
    ) -> BedrockStartTrustedAccessProgramAccountApplicationResponse:
        client = self._require_client()
        return await self._execute(client.start_trusted_access_program_account_application, request, BedrockStartTrustedAccessProgramAccountApplicationResponse)

    async def start_trusted_access_program_organization_application(
        self,
        request: BedrockStartTrustedAccessProgramOrganizationApplicationRequest,
    ) -> BedrockStartTrustedAccessProgramOrganizationApplicationResponse:
        client = self._require_client()
        return await self._execute(client.start_trusted_access_program_organization_application, request, BedrockStartTrustedAccessProgramOrganizationApplicationResponse)

    async def start_trusted_access_program_project_application(
        self,
        request: BedrockStartTrustedAccessProgramProjectApplicationRequest,
    ) -> BedrockStartTrustedAccessProgramProjectApplicationResponse:
        client = self._require_client()
        return await self._execute(client.start_trusted_access_program_project_application, request, BedrockStartTrustedAccessProgramProjectApplicationResponse)

    async def stop_advanced_prompt_optimization_job(
        self,
        request: BedrockStopAdvancedPromptOptimizationJobRequest,
    ) -> BedrockStopAdvancedPromptOptimizationJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_advanced_prompt_optimization_job, request, BedrockStopAdvancedPromptOptimizationJobResponse)

    async def stop_evaluation_job(
        self,
        request: BedrockStopEvaluationJobRequest,
    ) -> BedrockStopEvaluationJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_evaluation_job, request, BedrockStopEvaluationJobResponse)

    async def stop_model_customization_job(
        self,
        request: BedrockStopModelCustomizationJobRequest,
    ) -> BedrockStopModelCustomizationJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_model_customization_job, request, BedrockStopModelCustomizationJobResponse)

    async def stop_model_invocation_job(
        self,
        request: BedrockStopModelInvocationJobRequest,
    ) -> BedrockStopModelInvocationJobResponse:
        client = self._require_client()
        return await self._execute(client.stop_model_invocation_job, request, BedrockStopModelInvocationJobResponse)

    async def tag_resource(
        self,
        request: BedrockTagResourceRequest,
    ) -> BedrockTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, BedrockTagResourceResponse)

    async def untag_resource(
        self,
        request: BedrockUntagResourceRequest,
    ) -> BedrockUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, BedrockUntagResourceResponse)

    async def update_automated_reasoning_policy(
        self,
        request: BedrockUpdateAutomatedReasoningPolicyRequest,
    ) -> BedrockUpdateAutomatedReasoningPolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_automated_reasoning_policy, request, BedrockUpdateAutomatedReasoningPolicyResponse)

    async def update_automated_reasoning_policy_annotations(
        self,
        request: BedrockUpdateAutomatedReasoningPolicyAnnotationsRequest,
    ) -> BedrockUpdateAutomatedReasoningPolicyAnnotationsResponse:
        client = self._require_client()
        return await self._execute(client.update_automated_reasoning_policy_annotations, request, BedrockUpdateAutomatedReasoningPolicyAnnotationsResponse)

    async def update_automated_reasoning_policy_test_case(
        self,
        request: BedrockUpdateAutomatedReasoningPolicyTestCaseRequest,
    ) -> BedrockUpdateAutomatedReasoningPolicyTestCaseResponse:
        client = self._require_client()
        return await self._execute(client.update_automated_reasoning_policy_test_case, request, BedrockUpdateAutomatedReasoningPolicyTestCaseResponse)

    async def update_custom_model_deployment(
        self,
        request: BedrockUpdateCustomModelDeploymentRequest,
    ) -> BedrockUpdateCustomModelDeploymentResponse:
        client = self._require_client()
        return await self._execute(client.update_custom_model_deployment, request, BedrockUpdateCustomModelDeploymentResponse)

    async def update_guardrail(
        self,
        request: BedrockUpdateGuardrailRequest,
    ) -> BedrockUpdateGuardrailResponse:
        client = self._require_client()
        return await self._execute(client.update_guardrail, request, BedrockUpdateGuardrailResponse)

    async def update_marketplace_model_endpoint(
        self,
        request: BedrockUpdateMarketplaceModelEndpointRequest,
    ) -> BedrockUpdateMarketplaceModelEndpointResponse:
        client = self._require_client()
        return await self._execute(client.update_marketplace_model_endpoint, request, BedrockUpdateMarketplaceModelEndpointResponse)

    async def update_project(
        self,
        request: BedrockUpdateProjectRequest,
    ) -> BedrockUpdateProjectResponse:
        client = self._require_client()
        return await self._execute(client.update_project, request, BedrockUpdateProjectResponse)

    async def update_provisioned_model_throughput(
        self,
        request: BedrockUpdateProvisionedModelThroughputRequest,
    ) -> BedrockUpdateProvisionedModelThroughputResponse:
        client = self._require_client()
        return await self._execute(client.update_provisioned_model_throughput, request, BedrockUpdateProvisionedModelThroughputResponse)
