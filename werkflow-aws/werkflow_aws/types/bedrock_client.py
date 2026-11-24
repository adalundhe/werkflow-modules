from abc import ABC, abstractmethod
import datetime
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class BedrockClient(ABC):

    @abstractmethod
    def archive_project(
        self,
        *,
        projectIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_advanced_prompt_optimization_job(
        self,
        *,
        jobIdentifiers: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_evaluation_job(
        self,
        *,
        jobIdentifiers: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_automated_reasoning_policy_build_workflow(
        self,
        *,
        policyArn: str,
        buildWorkflowId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_advanced_prompt_optimization_job(
        self,
        *,
        jobName: str,
        inputConfig: dict[str, Any],
        outputConfig: dict[str, Any],
        modelConfigurations: list[dict[str, Any]],
        jobDescription: str | None = None,
        clientToken: str | None = None,
        encryptionKeyArn: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_automated_reasoning_policy(
        self,
        *,
        name: str,
        description: str | None = None,
        clientRequestToken: str | None = None,
        policyDefinition: dict[str, Any] | None = None,
        kmsKeyId: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_automated_reasoning_policy_test_case(
        self,
        *,
        policyArn: str,
        guardContent: str,
        expectedAggregatedFindingsResult: str,
        queryContent: str | None = None,
        clientRequestToken: str | None = None,
        confidenceThreshold: float | int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_automated_reasoning_policy_version(
        self,
        *,
        policyArn: str,
        lastUpdatedDefinitionHash: str,
        clientRequestToken: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_custom_model(
        self,
        *,
        modelName: str,
        modelSourceConfig: dict[str, Any] | None = None,
        customModelDataSource: dict[str, Any] | None = None,
        modelKmsKeyArn: str | None = None,
        roleArn: str | None = None,
        modelTags: list[dict[str, Any]] | None = None,
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_custom_model_deployment(
        self,
        *,
        modelDeploymentName: str,
        modelArn: str,
        description: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_evaluation_job(
        self,
        *,
        jobName: str,
        roleArn: str,
        evaluationConfig: dict[str, Any],
        inferenceConfig: dict[str, Any],
        outputDataConfig: dict[str, Any],
        jobDescription: str | None = None,
        clientRequestToken: str | None = None,
        customerEncryptionKeyId: str | None = None,
        jobTags: list[dict[str, Any]] | None = None,
        applicationType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_foundation_model_agreement(
        self,
        *,
        offerToken: str,
        modelId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_guardrail(
        self,
        *,
        name: str,
        blockedInputMessaging: str,
        blockedOutputsMessaging: str,
        description: str | None = None,
        topicPolicyConfig: dict[str, Any] | None = None,
        contentPolicyConfig: dict[str, Any] | None = None,
        wordPolicyConfig: dict[str, Any] | None = None,
        sensitiveInformationPolicyConfig: dict[str, Any] | None = None,
        contextualGroundingPolicyConfig: dict[str, Any] | None = None,
        automatedReasoningPolicyConfig: dict[str, Any] | None = None,
        crossRegionConfig: dict[str, Any] | None = None,
        kmsKeyId: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_guardrail_version(
        self,
        *,
        guardrailIdentifier: str,
        description: str | None = None,
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_inference_profile(
        self,
        *,
        inferenceProfileName: str,
        modelSource: dict[str, Any],
        description: str | None = None,
        clientRequestToken: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_marketplace_model_endpoint(
        self,
        *,
        modelSourceIdentifier: str,
        endpointConfig: dict[str, Any],
        endpointName: str,
        acceptEula: bool | None = None,
        clientRequestToken: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_model_copy_job(
        self,
        *,
        sourceModelArn: str,
        targetModelName: str,
        modelKmsKeyId: str | None = None,
        targetModelTags: list[dict[str, Any]] | None = None,
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_model_customization_job(
        self,
        *,
        jobName: str,
        customModelName: str,
        roleArn: str,
        baseModelIdentifier: str,
        trainingDataConfig: dict[str, Any],
        outputDataConfig: dict[str, Any],
        clientRequestToken: str | None = None,
        customizationType: str | None = None,
        customModelKmsKeyId: str | None = None,
        jobTags: list[dict[str, Any]] | None = None,
        customModelTags: list[dict[str, Any]] | None = None,
        validationDataConfig: dict[str, Any] | None = None,
        hyperParameters: dict[str, str] | None = None,
        vpcConfig: dict[str, Any] | None = None,
        customizationConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_model_import_job(
        self,
        *,
        jobName: str,
        importedModelName: str,
        roleArn: str,
        modelDataSource: dict[str, Any],
        jobTags: list[dict[str, Any]] | None = None,
        importedModelTags: list[dict[str, Any]] | None = None,
        clientRequestToken: str | None = None,
        vpcConfig: dict[str, Any] | None = None,
        importedModelKmsKeyId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_model_invocation_job(
        self,
        *,
        jobName: str,
        roleArn: str,
        modelId: str,
        inputDataConfig: dict[str, Any],
        outputDataConfig: dict[str, Any],
        clientRequestToken: str | None = None,
        vpcConfig: dict[str, Any] | None = None,
        timeoutDurationInHours: int | None = None,
        tags: list[dict[str, Any]] | None = None,
        modelInvocationType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_project(
        self,
        *,
        name: str,
        tags: list[dict[str, Any]] | None = None,
        dataRetention: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_prompt_router(
        self,
        *,
        promptRouterName: str,
        models: list[dict[str, Any]],
        routingCriteria: dict[str, Any],
        fallbackModel: dict[str, Any],
        clientRequestToken: str | None = None,
        description: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_provisioned_model_throughput(
        self,
        *,
        modelUnits: int,
        provisionedModelName: str,
        modelId: str,
        clientRequestToken: str | None = None,
        commitmentDuration: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_account_data_retention_storage(
        self,
        *,
        modelProvider: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_automated_reasoning_policy(
        self,
        *,
        policyArn: str,
        force: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_automated_reasoning_policy_build_workflow(
        self,
        *,
        policyArn: str,
        buildWorkflowId: str,
        lastUpdatedAt: datetime.datetime | str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_automated_reasoning_policy_test_case(
        self,
        *,
        policyArn: str,
        testCaseId: str,
        lastUpdatedAt: datetime.datetime | str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_custom_model(
        self,
        *,
        modelIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_custom_model_deployment(
        self,
        *,
        customModelDeploymentIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_enforced_guardrail_configuration(
        self,
        *,
        configId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_foundation_model_agreement(
        self,
        *,
        modelId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_guardrail(
        self,
        *,
        guardrailIdentifier: str,
        guardrailVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_imported_model(
        self,
        *,
        modelIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_inference_profile(
        self,
        *,
        inferenceProfileIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_marketplace_model_endpoint(
        self,
        *,
        endpointArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_model_invocation_logging_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_organization_data_retention_storage(
        self,
        *,
        modelProvider: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_project_data_retention_storage(
        self,
        *,
        projectIdentifier: str,
        modelProvider: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_prompt_router(
        self,
        *,
        promptRouterArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_provisioned_model_throughput(
        self,
        *,
        provisionedModelId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_policy(
        self,
        *,
        resourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_marketplace_model_endpoint(
        self,
        *,
        endpointArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_automated_reasoning_policy_version(
        self,
        *,
        policyArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_account_data_retention(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_account_data_retention_storage(
        self,
        *,
        modelProvider: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_advanced_prompt_optimization_job(
        self,
        *,
        jobIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_automated_reasoning_policy(
        self,
        *,
        policyArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_automated_reasoning_policy_annotations(
        self,
        *,
        policyArn: str,
        buildWorkflowId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_automated_reasoning_policy_build_workflow(
        self,
        *,
        policyArn: str,
        buildWorkflowId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_automated_reasoning_policy_build_workflow_result_assets(
        self,
        *,
        policyArn: str,
        buildWorkflowId: str,
        assetType: str,
        assetId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_automated_reasoning_policy_next_scenario(
        self,
        *,
        policyArn: str,
        buildWorkflowId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_automated_reasoning_policy_test_case(
        self,
        *,
        policyArn: str,
        testCaseId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_automated_reasoning_policy_test_result(
        self,
        *,
        policyArn: str,
        buildWorkflowId: str,
        testCaseId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_custom_model(
        self,
        *,
        modelIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_custom_model_deployment(
        self,
        *,
        customModelDeploymentIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_evaluation_job(
        self,
        *,
        jobIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_foundation_model(
        self,
        *,
        modelIdentifier: str,
        projectIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_foundation_model_availability(
        self,
        *,
        modelId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_guardrail(
        self,
        *,
        guardrailIdentifier: str,
        guardrailVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_imported_model(
        self,
        *,
        modelIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_inference_profile(
        self,
        *,
        inferenceProfileIdentifier: str,
        projectIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_marketplace_model_endpoint(
        self,
        *,
        endpointArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_model_copy_job(
        self,
        *,
        jobArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_model_customization_job(
        self,
        *,
        jobIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_model_import_job(
        self,
        *,
        jobIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_model_invocation_job(
        self,
        *,
        jobIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_model_invocation_logging_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_organization_data_retention_storage(
        self,
        *,
        modelProvider: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_project(
        self,
        *,
        projectIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_project_data_retention_storage(
        self,
        *,
        projectIdentifier: str,
        modelProvider: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_prompt_router(
        self,
        *,
        promptRouterArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_provisioned_model_throughput(
        self,
        *,
        provisionedModelId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_policy(
        self,
        *,
        resourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_trusted_access_program(
        self,
        *,
        programIdentifier: str,
        projectIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_trusted_access_program_account_enrollment(
        self,
        *,
        programIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_trusted_access_program_organization_enrollment(
        self,
        *,
        programIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_trusted_access_program_project_enrollment(
        self,
        *,
        programIdentifier: str,
        projectIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_use_case_for_model_access(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_advanced_prompt_optimization_jobs(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_automated_reasoning_policies(
        self,
        *,
        policyArn: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_automated_reasoning_policy_build_workflows(
        self,
        *,
        policyArn: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_automated_reasoning_policy_test_cases(
        self,
        *,
        policyArn: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_automated_reasoning_policy_test_results(
        self,
        *,
        policyArn: str,
        buildWorkflowId: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_custom_model_deployments(
        self,
        *,
        createdBefore: datetime.datetime | str | None = None,
        createdAfter: datetime.datetime | str | None = None,
        nameContains: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        statusEquals: str | None = None,
        modelArnEquals: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_custom_models(
        self,
        *,
        creationTimeBefore: datetime.datetime | str | None = None,
        creationTimeAfter: datetime.datetime | str | None = None,
        nameContains: str | None = None,
        baseModelArnEquals: str | None = None,
        foundationModelArnEquals: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        isOwned: bool | None = None,
        modelStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_enforced_guardrails_configuration(
        self,
        *,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_evaluation_jobs(
        self,
        *,
        creationTimeAfter: datetime.datetime | str | None = None,
        creationTimeBefore: datetime.datetime | str | None = None,
        statusEquals: str | None = None,
        applicationTypeEquals: str | None = None,
        nameContains: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_foundation_model_agreement_offers(
        self,
        *,
        modelId: str,
        offerType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_foundation_models(
        self,
        *,
        byProvider: str | None = None,
        byCustomizationType: str | None = None,
        byOutputModality: str | None = None,
        byInferenceType: str | None = None,
        projectIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_guardrails(
        self,
        *,
        guardrailIdentifier: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_imported_models(
        self,
        *,
        creationTimeBefore: datetime.datetime | str | None = None,
        creationTimeAfter: datetime.datetime | str | None = None,
        nameContains: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_inference_profiles(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
        typeEquals: str | None = None,
        projectIdentifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_marketplace_model_endpoints(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
        modelSourceEquals: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_model_copy_jobs(
        self,
        *,
        creationTimeAfter: datetime.datetime | str | None = None,
        creationTimeBefore: datetime.datetime | str | None = None,
        statusEquals: str | None = None,
        sourceAccountEquals: str | None = None,
        sourceModelArnEquals: str | None = None,
        targetModelNameContains: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_model_customization_jobs(
        self,
        *,
        creationTimeAfter: datetime.datetime | str | None = None,
        creationTimeBefore: datetime.datetime | str | None = None,
        statusEquals: str | None = None,
        nameContains: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_model_import_jobs(
        self,
        *,
        creationTimeAfter: datetime.datetime | str | None = None,
        creationTimeBefore: datetime.datetime | str | None = None,
        statusEquals: str | None = None,
        nameContains: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_model_invocation_jobs(
        self,
        *,
        submitTimeAfter: datetime.datetime | str | None = None,
        submitTimeBefore: datetime.datetime | str | None = None,
        statusEquals: str | None = None,
        nameContains: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_projects(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
        statusFilter: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_prompt_routers(
        self,
        *,
        maxResults: int | None = None,
        nextToken: str | None = None,
        type: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_provisioned_model_throughputs(
        self,
        *,
        creationTimeAfter: datetime.datetime | str | None = None,
        creationTimeBefore: datetime.datetime | str | None = None,
        statusEquals: str | None = None,
        modelArnEquals: str | None = None,
        nameContains: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        resourceARN: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_trusted_access_programs(
        self,
        *,
        projectIdentifier: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_account_data_retention(
        self,
        *,
        mode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_account_data_retention_storage(
        self,
        *,
        modelProvider: str,
        storageDestination: str,
        storageConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_enforced_guardrail_configuration(
        self,
        *,
        guardrailInferenceConfig: dict[str, Any],
        configId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_model_invocation_logging_configuration(
        self,
        *,
        loggingConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_organization_data_retention_storage(
        self,
        *,
        modelProvider: str,
        storageDestination: str,
        storageConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_project_data_retention_storage(
        self,
        *,
        projectIdentifier: str,
        modelProvider: str,
        storageDestination: str,
        storageConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_resource_policy(
        self,
        *,
        resourceArn: str,
        resourcePolicy: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_trusted_access_program_account_enrollment(
        self,
        *,
        programIdentifier: str,
        optIn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_trusted_access_program_organization_enrollment(
        self,
        *,
        programIdentifier: str,
        optIn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_trusted_access_program_project_enrollment(
        self,
        *,
        programIdentifier: str,
        projectIdentifier: str,
        optIn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_use_case_for_model_access(
        self,
        *,
        formData: bytes | BinaryIO | str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_marketplace_model_endpoint(
        self,
        *,
        endpointIdentifier: str,
        modelSourceIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_automated_reasoning_policy_build_workflow(
        self,
        *,
        policyArn: str,
        buildWorkflowType: str,
        sourceContent: dict[str, Any],
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_automated_reasoning_policy_test_workflow(
        self,
        *,
        policyArn: str,
        buildWorkflowId: str,
        testCaseIds: list[str] | None = None,
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_trusted_access_program_account_application(
        self,
        *,
        programIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_trusted_access_program_organization_application(
        self,
        *,
        programIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_trusted_access_program_project_application(
        self,
        *,
        programIdentifier: str,
        projectIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_advanced_prompt_optimization_job(
        self,
        *,
        jobIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_evaluation_job(
        self,
        *,
        jobIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_model_customization_job(
        self,
        *,
        jobIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_model_invocation_job(
        self,
        *,
        jobIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        resourceARN: str,
        tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        resourceARN: str,
        tagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_automated_reasoning_policy(
        self,
        *,
        policyArn: str,
        policyDefinition: dict[str, Any],
        name: str | None = None,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_automated_reasoning_policy_annotations(
        self,
        *,
        policyArn: str,
        buildWorkflowId: str,
        annotations: list[dict[str, Any]],
        lastUpdatedAnnotationSetHash: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_automated_reasoning_policy_test_case(
        self,
        *,
        policyArn: str,
        testCaseId: str,
        guardContent: str,
        lastUpdatedAt: datetime.datetime | str,
        expectedAggregatedFindingsResult: str,
        queryContent: str | None = None,
        confidenceThreshold: float | int | None = None,
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_custom_model_deployment(
        self,
        *,
        modelArn: str,
        customModelDeploymentIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_guardrail(
        self,
        *,
        guardrailIdentifier: str,
        name: str,
        blockedInputMessaging: str,
        blockedOutputsMessaging: str,
        description: str | None = None,
        topicPolicyConfig: dict[str, Any] | None = None,
        contentPolicyConfig: dict[str, Any] | None = None,
        wordPolicyConfig: dict[str, Any] | None = None,
        sensitiveInformationPolicyConfig: dict[str, Any] | None = None,
        contextualGroundingPolicyConfig: dict[str, Any] | None = None,
        automatedReasoningPolicyConfig: dict[str, Any] | None = None,
        crossRegionConfig: dict[str, Any] | None = None,
        kmsKeyId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_marketplace_model_endpoint(
        self,
        *,
        endpointArn: str,
        endpointConfig: dict[str, Any],
        clientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_project(
        self,
        *,
        projectIdentifier: str,
        name: str | None = None,
        dataRetention: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_provisioned_model_throughput(
        self,
        *,
        provisionedModelId: str,
        desiredProvisionedModelName: str | None = None,
        desiredModelId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
