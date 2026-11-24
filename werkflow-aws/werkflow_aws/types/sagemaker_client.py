from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class SageMakerClient(ABC):

    @abstractmethod
    def list_training_jobs(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        NameContains: str | None = None,
        StatusEquals: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        WarmPoolStatusEquals: str | None = None,
        TrainingPlanArnEquals: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_training_job(
        self,
        *,
        TrainingJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_training_job(
        self,
        *,
        TrainingJobName: str,
        RoleArn: str,
        OutputDataConfig: dict[str, Any],
        HyperParameters: dict[str, str] | None = None,
        AlgorithmSpecification: dict[str, Any] | None = None,
        InputDataConfig: list[dict[str, Any]] | None = None,
        ResourceConfig: dict[str, Any] | None = None,
        VpcConfig: dict[str, Any] | None = None,
        StoppingCondition: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        EnableNetworkIsolation: bool | None = None,
        EnableInterContainerTrafficEncryption: bool | None = None,
        EnableManagedSpotTraining: bool | None = None,
        CheckpointConfig: dict[str, Any] | None = None,
        DebugHookConfig: dict[str, Any] | None = None,
        DebugRuleConfigurations: list[dict[str, Any]] | None = None,
        TensorBoardOutputConfig: dict[str, Any] | None = None,
        ExperimentConfig: dict[str, Any] | None = None,
        ProfilerConfig: dict[str, Any] | None = None,
        ProfilerRuleConfigurations: list[dict[str, Any]] | None = None,
        Environment: dict[str, str] | None = None,
        RetryStrategy: dict[str, Any] | None = None,
        RemoteDebugConfig: dict[str, Any] | None = None,
        InfraCheckConfig: dict[str, Any] | None = None,
        SessionChainingConfig: dict[str, Any] | None = None,
        ServerlessJobConfig: dict[str, Any] | None = None,
        MlflowConfig: dict[str, Any] | None = None,
        ModelPackageConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_training_job(
        self,
        *,
        TrainingJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_processing_jobs(
        self,
        *,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        NameContains: str | None = None,
        StatusEquals: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_processing_job(
        self,
        *,
        ProcessingJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_processing_job(
        self,
        *,
        ProcessingJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_models(
        self,
        *,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        NameContains: str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_model(
        self,
        *,
        ModelName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_model(
        self,
        *,
        ModelName: str,
        PrimaryContainer: dict[str, Any] | None = None,
        Containers: list[dict[str, Any]] | None = None,
        InferenceExecutionConfig: dict[str, Any] | None = None,
        ExecutionRoleArn: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        VpcConfig: dict[str, Any] | None = None,
        EnableNetworkIsolation: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_model(
        self,
        *,
        ModelName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_endpoint_configs(
        self,
        *,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        NameContains: str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_endpoint_config(
        self,
        *,
        EndpointConfigName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_endpoint_config(
        self,
        *,
        EndpointConfigName: str,
        ProductionVariants: list[dict[str, Any]],
        DataCaptureConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        KmsKeyId: str | None = None,
        AsyncInferenceConfig: dict[str, Any] | None = None,
        ExplainerConfig: dict[str, Any] | None = None,
        ShadowProductionVariants: list[dict[str, Any]] | None = None,
        ExecutionRoleArn: str | None = None,
        VpcConfig: dict[str, Any] | None = None,
        EnableNetworkIsolation: bool | None = None,
        MetricsConfig: dict[str, Any] | None = None,
        CrossRegionTrafficConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_endpoint_config(
        self,
        *,
        EndpointConfigName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_endpoints(
        self,
        *,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        NameContains: str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        StatusEquals: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_endpoint(
        self,
        *,
        EndpointName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_endpoint(
        self,
        *,
        EndpointName: str,
        EndpointConfigName: str,
        DeploymentConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_endpoint(
        self,
        *,
        EndpointName: str,
        EndpointConfigName: str,
        RetainAllVariantProperties: bool | None = None,
        ExcludeRetainedVariantProperties: list[dict[str, Any]] | None = None,
        DeploymentConfig: dict[str, Any] | None = None,
        RetainDeploymentConfig: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_endpoint(
        self,
        *,
        EndpointName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_notebook_instances(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NameContains: str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        StatusEquals: str | None = None,
        NotebookInstanceLifecycleConfigNameContains: str | None = None,
        DefaultCodeRepositoryContains: str | None = None,
        AdditionalCodeRepositoryEquals: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_notebook_instance(
        self,
        *,
        NotebookInstanceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_notebook_instance(
        self,
        *,
        NotebookInstanceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_notebook_instance(
        self,
        *,
        NotebookInstanceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_pipelines(
        self,
        *,
        PipelineNamePrefix: str | None = None,
        CreatedAfter: datetime.datetime | str | None = None,
        CreatedBefore: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        ManagedBy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_pipeline(
        self,
        *,
        PipelineName: str,
        PipelineVersionId: int | None = None,
        PipelineVersionAlias: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_pipeline_execution(
        self,
        *,
        PipelineName: str,
        ClientRequestToken: str,
        PipelineExecutionDisplayName: str | None = None,
        PipelineParameters: list[dict[str, Any]] | None = None,
        PipelineExecutionDescription: str | None = None,
        ParallelismConfiguration: dict[str, Any] | None = None,
        SelectiveExecutionConfig: dict[str, Any] | None = None,
        PipelineVersionId: int | None = None,
        MlflowExperimentName: str | None = None,
        PipelineVersionAlias: str | None = None,
        RoleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags(
        self,
        *,
        ResourceArn: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_tags(
        self,
        *,
        ResourceArn: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_tags(
        self,
        *,
        ResourceArn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_association(
        self,
        *,
        SourceArn: str,
        DestinationArn: str,
        AssociationType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_inference_gateway(
        self,
        *,
        Identifier: str,
        ClusterArn: str,
        Namespace: str,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_trial_component(
        self,
        *,
        TrialComponentName: str,
        TrialName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_cluster_node_network_interface(
        self,
        *,
        ClusterName: str,
        NodeId: str,
        NetworkInterfaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_cluster_node_volume(
        self,
        *,
        ClusterArn: str,
        NodeId: str,
        VolumeId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_add_cluster_nodes(
        self,
        *,
        ClusterName: str,
        NodesToAdd: list[dict[str, Any]],
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_cluster_nodes(
        self,
        *,
        ClusterName: str,
        NodeIds: list[str] | None = None,
        NodeLogicalIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_describe_model_package(
        self,
        *,
        ModelPackageArnList: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_reboot_cluster_nodes(
        self,
        *,
        ClusterName: str,
        NodeIds: list[str] | None = None,
        NodeLogicalIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_replace_cluster_nodes(
        self,
        *,
        ClusterName: str,
        NodeIds: list[str] | None = None,
        NodeLogicalIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ai_benchmark_job(
        self,
        *,
        AIBenchmarkJobName: str,
        BenchmarkTarget: dict[str, Any],
        OutputConfig: dict[str, Any],
        AIWorkloadConfigIdentifier: str,
        RoleArn: str,
        NetworkConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ai_recommendation_job(
        self,
        *,
        AIRecommendationJobName: str,
        ModelSource: dict[str, Any],
        OutputConfig: dict[str, Any],
        AIWorkloadConfigIdentifier: str,
        PerformanceTarget: dict[str, Any],
        RoleArn: str,
        InferenceSpecification: dict[str, Any] | None = None,
        OptimizeModel: bool | None = None,
        ComputeSpec: dict[str, Any] | None = None,
        AdapterSource: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ai_workload_config(
        self,
        *,
        AIWorkloadConfigName: str,
        DatasetConfig: dict[str, Any] | None = None,
        AIWorkloadConfigs: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_action(
        self,
        *,
        ActionName: str,
        Source: dict[str, Any],
        ActionType: str,
        Description: str | None = None,
        Status: str | None = None,
        Properties: dict[str, str] | None = None,
        MetadataProperties: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_algorithm(
        self,
        *,
        AlgorithmName: str,
        TrainingSpecification: dict[str, Any],
        AlgorithmDescription: str | None = None,
        InferenceSpecification: dict[str, Any] | None = None,
        ValidationSpecification: dict[str, Any] | None = None,
        CertifyForMarketplace: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_app(
        self,
        *,
        DomainId: str,
        AppType: str,
        AppName: str,
        UserProfileName: str | None = None,
        SpaceName: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ResourceSpec: dict[str, Any] | None = None,
        RecoveryMode: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_app_image_config(
        self,
        *,
        AppImageConfigName: str,
        Tags: list[dict[str, Any]] | None = None,
        KernelGatewayImageConfig: dict[str, Any] | None = None,
        JupyterLabAppImageConfig: dict[str, Any] | None = None,
        CodeEditorAppImageConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_artifact(
        self,
        *,
        Source: dict[str, Any],
        ArtifactType: str,
        ArtifactName: str | None = None,
        Properties: dict[str, str] | None = None,
        MetadataProperties: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_auto_ml_job(
        self,
        *,
        AutoMLJobName: str,
        InputDataConfig: list[dict[str, Any]],
        OutputDataConfig: dict[str, Any],
        RoleArn: str,
        ProblemType: str | None = None,
        AutoMLJobObjective: dict[str, Any] | None = None,
        AutoMLJobConfig: dict[str, Any] | None = None,
        GenerateCandidateDefinitionsOnly: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ModelDeployConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_auto_ml_job_v2(
        self,
        *,
        AutoMLJobName: str,
        AutoMLJobInputDataConfig: list[dict[str, Any]],
        OutputDataConfig: dict[str, Any],
        AutoMLProblemTypeConfig: dict[str, Any],
        RoleArn: str,
        Tags: list[dict[str, Any]] | None = None,
        SecurityConfig: dict[str, Any] | None = None,
        AutoMLJobObjective: dict[str, Any] | None = None,
        ModelDeployConfig: dict[str, Any] | None = None,
        DataSplitConfig: dict[str, Any] | None = None,
        AutoMLComputeConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cluster(
        self,
        *,
        ClusterName: str,
        InstanceGroups: list[dict[str, Any]] | None = None,
        RestrictedInstanceGroups: list[dict[str, Any]] | None = None,
        RestrictedInstanceGroupsConfig: dict[str, Any] | None = None,
        VpcConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        Orchestrator: dict[str, Any] | None = None,
        NodeRecovery: str | None = None,
        TieredStorageConfig: dict[str, Any] | None = None,
        NodeProvisioningMode: str | None = None,
        ClusterRole: str | None = None,
        AutoScaling: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cluster_extension(
        self,
        *,
        ClusterArn: str,
        ExtensionName: str,
        ExtensionVersion: str | None = None,
        ConfigurationValues: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cluster_scheduler_config(
        self,
        *,
        Name: str,
        ClusterArn: str,
        SchedulerConfig: dict[str, Any],
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_code_repository(
        self,
        *,
        CodeRepositoryName: str,
        GitConfig: dict[str, Any],
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_compilation_job(
        self,
        *,
        CompilationJobName: str,
        RoleArn: str,
        OutputConfig: dict[str, Any],
        StoppingCondition: dict[str, Any],
        ModelPackageVersionArn: str | None = None,
        InputConfig: dict[str, Any] | None = None,
        VpcConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_compute_quota(
        self,
        *,
        Name: str,
        ClusterArn: str,
        ComputeQuotaConfig: dict[str, Any],
        ComputeQuotaTarget: dict[str, Any],
        Description: str | None = None,
        ActivationState: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_context(
        self,
        *,
        ContextName: str,
        Source: dict[str, Any],
        ContextType: str,
        Description: str | None = None,
        Properties: dict[str, str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_quality_job_definition(
        self,
        *,
        JobDefinitionName: str,
        DataQualityAppSpecification: dict[str, Any],
        DataQualityJobInput: dict[str, Any],
        DataQualityJobOutputConfig: dict[str, Any],
        JobResources: dict[str, Any],
        RoleArn: str,
        DataQualityBaselineConfig: dict[str, Any] | None = None,
        NetworkConfig: dict[str, Any] | None = None,
        StoppingCondition: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_device_fleet(
        self,
        *,
        DeviceFleetName: str,
        OutputConfig: dict[str, Any],
        RoleArn: str | None = None,
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        EnableIotRoleAlias: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_domain(
        self,
        *,
        DomainName: str,
        AuthMode: str,
        DefaultUserSettings: dict[str, Any],
        DomainSettings: dict[str, Any] | None = None,
        SubnetIds: list[str] | None = None,
        VpcId: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        AppNetworkAccessType: str | None = None,
        HomeEfsFileSystemKmsKeyId: str | None = None,
        KmsKeyId: str | None = None,
        AppSecurityGroupManagement: str | None = None,
        HomeEfsFileSystemCreation: str | None = None,
        TagPropagation: str | None = None,
        DefaultSpaceSettings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_edge_deployment_plan(
        self,
        *,
        EdgeDeploymentPlanName: str,
        ModelConfigs: list[dict[str, Any]],
        DeviceFleetName: str,
        Stages: list[dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_edge_deployment_stage(
        self,
        *,
        EdgeDeploymentPlanName: str,
        Stages: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_edge_packaging_job(
        self,
        *,
        EdgePackagingJobName: str,
        CompilationJobName: str,
        ModelName: str,
        ModelVersion: str,
        RoleArn: str,
        OutputConfig: dict[str, Any],
        ResourceKey: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_experiment(
        self,
        *,
        ExperimentName: str,
        DisplayName: str | None = None,
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_feature_group(
        self,
        *,
        FeatureGroupName: str,
        RecordIdentifierFeatureName: str,
        EventTimeFeatureName: str,
        FeatureDefinitions: list[dict[str, Any]],
        OnlineStoreConfig: dict[str, Any] | None = None,
        OfflineStoreConfig: dict[str, Any] | None = None,
        ThroughputConfig: dict[str, Any] | None = None,
        RoleArn: str | None = None,
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_flow_definition(
        self,
        *,
        FlowDefinitionName: str,
        OutputConfig: dict[str, Any],
        RoleArn: str,
        HumanLoopRequestSource: dict[str, Any] | None = None,
        HumanLoopActivationConfig: dict[str, Any] | None = None,
        HumanLoopConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_global_inference_gateway(
        self,
        *,
        Name: str,
        ExecutionRoleArn: str,
        Gateways: list[dict[str, Any]],
        Routing: dict[str, Any] | None = None,
        ClientToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_hub(
        self,
        *,
        HubName: str,
        HubDescription: str,
        HubDisplayName: str | None = None,
        HubSearchKeywords: list[str] | None = None,
        S3StorageConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_hub_content_presigned_urls(
        self,
        *,
        HubName: str,
        HubContentType: str,
        HubContentName: str,
        HubContentVersion: str | None = None,
        AccessConfig: dict[str, Any] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_hub_content_reference(
        self,
        *,
        HubName: str,
        SageMakerPublicHubContentArn: str,
        HubContentName: str | None = None,
        MinVersion: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_human_task_ui(
        self,
        *,
        HumanTaskUiName: str,
        UiTemplate: dict[str, Any],
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_hyper_parameter_tuning_job(
        self,
        *,
        HyperParameterTuningJobName: str,
        HyperParameterTuningJobConfig: dict[str, Any],
        TrainingJobDefinition: dict[str, Any] | None = None,
        TrainingJobDefinitions: list[dict[str, Any]] | None = None,
        WarmStartConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        Autotune: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_image(
        self,
        *,
        ImageName: str,
        RoleArn: str,
        Description: str | None = None,
        DisplayName: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_image_version(
        self,
        *,
        BaseImage: str,
        ClientToken: str,
        ImageName: str,
        Aliases: list[str] | None = None,
        VendorGuidance: str | None = None,
        JobType: str | None = None,
        MLFramework: str | None = None,
        ProgrammingLang: str | None = None,
        Processor: str | None = None,
        Horovod: bool | None = None,
        ReleaseNotes: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_inference_component(
        self,
        *,
        InferenceComponentName: str,
        EndpointName: str,
        VariantName: str | None = None,
        Specification: dict[str, Any] | None = None,
        Specifications: list[dict[str, Any]] | None = None,
        RuntimeConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_inference_experiment(
        self,
        *,
        Name: str,
        Type: str,
        RoleArn: str,
        EndpointName: str,
        ModelVariants: list[dict[str, Any]],
        ShadowModeConfig: dict[str, Any],
        Schedule: dict[str, Any] | None = None,
        Description: str | None = None,
        DataStorageConfig: dict[str, Any] | None = None,
        KmsKey: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_inference_recommendations_job(
        self,
        *,
        JobName: str,
        JobType: str,
        RoleArn: str,
        InputConfig: dict[str, Any],
        JobDescription: str | None = None,
        StoppingConditions: dict[str, Any] | None = None,
        OutputConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_inference_router(
        self,
        *,
        InferenceRouterName: str,
        RoutingTargets: list[dict[str, Any]],
        ClientToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_job(
        self,
        *,
        JobName: str,
        RoleArn: str,
        JobCategory: str,
        JobConfigSchemaVersion: str,
        JobConfigDocument: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_labeling_job(
        self,
        *,
        LabelingJobName: str,
        LabelAttributeName: str,
        InputConfig: dict[str, Any],
        OutputConfig: dict[str, Any],
        RoleArn: str,
        HumanTaskConfig: dict[str, Any],
        LabelCategoryConfigS3Uri: str | None = None,
        StoppingConditions: dict[str, Any] | None = None,
        LabelingJobAlgorithmsConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_mlflow_app(
        self,
        *,
        Name: str,
        ArtifactStoreUri: str,
        RoleArn: str,
        KmsKeyId: str | None = None,
        ModelRegistrationMode: str | None = None,
        WeeklyMaintenanceWindowStart: str | None = None,
        AccountDefaultStatus: str | None = None,
        DefaultDomainIdList: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_mlflow_tracking_server(
        self,
        *,
        TrackingServerName: str,
        ArtifactStoreUri: str,
        RoleArn: str,
        TrackingServerSize: str | None = None,
        MlflowVersion: str | None = None,
        AutomaticModelRegistration: bool | None = None,
        WeeklyMaintenanceWindowStart: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        S3BucketOwnerAccountId: str | None = None,
        S3BucketOwnerVerification: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_model_bias_job_definition(
        self,
        *,
        JobDefinitionName: str,
        ModelBiasAppSpecification: dict[str, Any],
        ModelBiasJobInput: dict[str, Any],
        ModelBiasJobOutputConfig: dict[str, Any],
        JobResources: dict[str, Any],
        RoleArn: str,
        ModelBiasBaselineConfig: dict[str, Any] | None = None,
        NetworkConfig: dict[str, Any] | None = None,
        StoppingCondition: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_model_card(
        self,
        *,
        ModelCardName: str,
        Content: str,
        ModelCardStatus: str,
        SecurityConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_model_card_export_job(
        self,
        *,
        ModelCardName: str,
        ModelCardExportJobName: str,
        OutputConfig: dict[str, Any],
        ModelCardVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_model_explainability_job_definition(
        self,
        *,
        JobDefinitionName: str,
        ModelExplainabilityAppSpecification: dict[str, Any],
        ModelExplainabilityJobInput: dict[str, Any],
        ModelExplainabilityJobOutputConfig: dict[str, Any],
        JobResources: dict[str, Any],
        RoleArn: str,
        ModelExplainabilityBaselineConfig: dict[str, Any] | None = None,
        NetworkConfig: dict[str, Any] | None = None,
        StoppingCondition: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_model_package(
        self,
        *,
        ModelPackageName: str | None = None,
        ModelPackageGroupName: str | None = None,
        ModelPackageDescription: str | None = None,
        ModelPackageRegistrationType: str | None = None,
        InferenceSpecification: dict[str, Any] | None = None,
        ValidationSpecification: dict[str, Any] | None = None,
        SourceAlgorithmSpecification: dict[str, Any] | None = None,
        CertifyForMarketplace: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ModelApprovalStatus: str | None = None,
        MetadataProperties: dict[str, Any] | None = None,
        ModelMetrics: dict[str, Any] | None = None,
        ClientToken: str | None = None,
        Domain: str | None = None,
        Task: str | None = None,
        SamplePayloadUrl: str | None = None,
        CustomerMetadataProperties: dict[str, str] | None = None,
        DriftCheckBaselines: dict[str, Any] | None = None,
        AdditionalInferenceSpecifications: list[dict[str, Any]] | None = None,
        SkipModelValidation: str | None = None,
        SourceUri: str | None = None,
        SecurityConfig: dict[str, Any] | None = None,
        ModelCard: dict[str, Any] | None = None,
        ModelLifeCycle: dict[str, Any] | None = None,
        ManagedStorageType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_model_package_group(
        self,
        *,
        ModelPackageGroupName: str,
        ModelPackageGroupDescription: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ManagedConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_model_quality_job_definition(
        self,
        *,
        JobDefinitionName: str,
        ModelQualityAppSpecification: dict[str, Any],
        ModelQualityJobInput: dict[str, Any],
        ModelQualityJobOutputConfig: dict[str, Any],
        JobResources: dict[str, Any],
        RoleArn: str,
        ModelQualityBaselineConfig: dict[str, Any] | None = None,
        NetworkConfig: dict[str, Any] | None = None,
        StoppingCondition: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_monitoring_schedule(
        self,
        *,
        MonitoringScheduleName: str,
        MonitoringScheduleConfig: dict[str, Any],
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_notebook_instance(
        self,
        *,
        NotebookInstanceName: str,
        InstanceType: str,
        RoleArn: str,
        SubnetId: str | None = None,
        SecurityGroupIds: list[str] | None = None,
        IpAddressType: str | None = None,
        KmsKeyId: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        LifecycleConfigName: str | None = None,
        DirectInternetAccess: str | None = None,
        VolumeSizeInGB: int | None = None,
        AcceleratorTypes: list[str] | None = None,
        DefaultCodeRepository: str | None = None,
        AdditionalCodeRepositories: list[str] | None = None,
        RootAccess: str | None = None,
        PlatformIdentifier: str | None = None,
        InstanceMetadataServiceConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_notebook_instance_lifecycle_config(
        self,
        *,
        NotebookInstanceLifecycleConfigName: str,
        OnCreate: list[dict[str, Any]] | None = None,
        OnStart: list[dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_optimization_job(
        self,
        *,
        OptimizationJobName: str,
        RoleArn: str,
        ModelSource: dict[str, Any],
        DeploymentInstanceType: str,
        OptimizationConfigs: list[dict[str, Any]],
        OutputConfig: dict[str, Any],
        StoppingCondition: dict[str, Any],
        MaxInstanceCount: int | None = None,
        OptimizationEnvironment: dict[str, str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        VpcConfig: dict[str, Any] | None = None,
        TrainingPlanArns: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_partner_app(
        self,
        *,
        Name: str,
        Type: str,
        ExecutionRoleArn: str,
        Tier: str,
        AuthType: str,
        KmsKeyId: str | None = None,
        MaintenanceConfig: dict[str, Any] | None = None,
        ApplicationConfig: dict[str, Any] | None = None,
        IdcConfig: dict[str, Any] | None = None,
        EnableIamSessionBasedIdentity: bool | None = None,
        EnableAutoMinorVersionUpgrade: bool | None = None,
        ClientToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_partner_app_presigned_url(
        self,
        *,
        Arn: str,
        ExpiresInSeconds: int | None = None,
        SessionExpirationDurationInSeconds: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_pipeline(
        self,
        *,
        PipelineName: str,
        ClientRequestToken: str,
        RoleArn: str,
        PipelineDisplayName: str | None = None,
        PipelineDefinition: str | None = None,
        PipelineDefinitionS3Location: dict[str, Any] | None = None,
        PipelineDescription: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ParallelismConfiguration: dict[str, Any] | None = None,
        PipelineVersionAliases: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_presigned_domain_url(
        self,
        *,
        DomainId: str,
        UserProfileName: str,
        SessionExpirationDurationInSeconds: int | None = None,
        ExpiresInSeconds: int | None = None,
        SpaceName: str | None = None,
        LandingUri: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_presigned_mlflow_app_url(
        self,
        *,
        Arn: str,
        ExpiresInSeconds: int | None = None,
        SessionExpirationDurationInSeconds: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_presigned_mlflow_tracking_server_url(
        self,
        *,
        TrackingServerName: str,
        ExpiresInSeconds: int | None = None,
        SessionExpirationDurationInSeconds: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_presigned_notebook_instance_url(
        self,
        *,
        NotebookInstanceName: str,
        SessionExpirationDurationInSeconds: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_processing_job(
        self,
        *,
        ProcessingJobName: str,
        ProcessingResources: dict[str, Any],
        AppSpecification: dict[str, Any],
        RoleArn: str,
        ProcessingInputs: list[dict[str, Any]] | None = None,
        ProcessingOutputConfig: dict[str, Any] | None = None,
        StoppingCondition: dict[str, Any] | None = None,
        Environment: dict[str, str] | None = None,
        NetworkConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ExperimentConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_project(
        self,
        *,
        ProjectName: str,
        ProjectDescription: str | None = None,
        ServiceCatalogProvisioningDetails: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        TemplateProviders: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_space(
        self,
        *,
        DomainId: str,
        SpaceName: str,
        Tags: list[dict[str, Any]] | None = None,
        SpaceSettings: dict[str, Any] | None = None,
        OwnershipSettings: dict[str, Any] | None = None,
        SpaceSharingSettings: dict[str, Any] | None = None,
        SpaceDisplayName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_studio_lifecycle_config(
        self,
        *,
        StudioLifecycleConfigName: str,
        StudioLifecycleConfigContent: str,
        StudioLifecycleConfigAppType: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_training_plan(
        self,
        *,
        TrainingPlanName: str,
        TrainingPlanOfferingId: str,
        SpareInstanceCountPerUltraServer: int | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_training_session(
        self,
        *,
        TrainingSessionName: str,
        LoraConfig: dict[str, Any],
        RoleArn: str,
        ModelConfig: dict[str, Any],
        OutputConfig: dict[str, Any],
        ModelPackageGroupArn: str | None = None,
        VpcConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_transform_job(
        self,
        *,
        TransformJobName: str,
        ModelName: str,
        TransformInput: dict[str, Any],
        TransformOutput: dict[str, Any],
        TransformResources: dict[str, Any],
        MaxConcurrentTransforms: int | None = None,
        ModelClientConfig: dict[str, Any] | None = None,
        MaxPayloadInMB: int | None = None,
        BatchStrategy: str | None = None,
        Environment: dict[str, str] | None = None,
        DataCaptureConfig: dict[str, Any] | None = None,
        DataProcessing: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ExperimentConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_trial(
        self,
        *,
        TrialName: str,
        ExperimentName: str,
        DisplayName: str | None = None,
        MetadataProperties: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_trial_component(
        self,
        *,
        TrialComponentName: str,
        DisplayName: str | None = None,
        Status: dict[str, Any] | None = None,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        Parameters: dict[str, dict[str, Any]] | None = None,
        InputArtifacts: dict[str, dict[str, Any]] | None = None,
        OutputArtifacts: dict[str, dict[str, Any]] | None = None,
        MetadataProperties: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_user_profile(
        self,
        *,
        DomainId: str,
        UserProfileName: str,
        SingleSignOnUserIdentifier: str | None = None,
        SingleSignOnUserValue: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        UserSettings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_workforce(
        self,
        *,
        WorkforceName: str,
        CognitoConfig: dict[str, Any] | None = None,
        OidcConfig: dict[str, Any] | None = None,
        SourceIpConfig: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        WorkforceVpcConfig: dict[str, Any] | None = None,
        IpAddressType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_workteam(
        self,
        *,
        WorkteamName: str,
        MemberDefinitions: list[dict[str, Any]],
        Description: str,
        WorkforceName: str | None = None,
        NotificationConfiguration: dict[str, Any] | None = None,
        WorkerAccessConfiguration: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ai_benchmark_job(
        self,
        *,
        AIBenchmarkJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ai_recommendation_job(
        self,
        *,
        AIRecommendationJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ai_workload_config(
        self,
        *,
        AIWorkloadConfigName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_action(
        self,
        *,
        ActionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_algorithm(
        self,
        *,
        AlgorithmName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_app(
        self,
        *,
        DomainId: str,
        AppType: str,
        AppName: str,
        UserProfileName: str | None = None,
        SpaceName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_app_image_config(
        self,
        *,
        AppImageConfigName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_artifact(
        self,
        *,
        ArtifactArn: str | None = None,
        Source: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_association(
        self,
        *,
        SourceArn: str,
        DestinationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cluster(
        self,
        *,
        ClusterName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cluster_extension(
        self,
        *,
        ClusterArn: str,
        ExtensionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cluster_scheduler_config(
        self,
        *,
        ClusterSchedulerConfigId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_code_repository(
        self,
        *,
        CodeRepositoryName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_compilation_job(
        self,
        *,
        CompilationJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_compute_quota(
        self,
        *,
        ComputeQuotaId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_context(
        self,
        *,
        ContextName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_quality_job_definition(
        self,
        *,
        JobDefinitionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_device_fleet(
        self,
        *,
        DeviceFleetName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_domain(
        self,
        *,
        DomainId: str,
        RetentionPolicy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_edge_deployment_plan(
        self,
        *,
        EdgeDeploymentPlanName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_edge_deployment_stage(
        self,
        *,
        EdgeDeploymentPlanName: str,
        StageName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_endpoint_policy(
        self,
        *,
        EndpointName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_experiment(
        self,
        *,
        ExperimentName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_feature_group(
        self,
        *,
        FeatureGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_flow_definition(
        self,
        *,
        FlowDefinitionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_global_inference_gateway(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_hub(
        self,
        *,
        HubName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_hub_content(
        self,
        *,
        HubName: str,
        HubContentType: str,
        HubContentName: str,
        HubContentVersion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_hub_content_reference(
        self,
        *,
        HubName: str,
        HubContentType: str,
        HubContentName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_human_task_ui(
        self,
        *,
        HumanTaskUiName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_hyper_parameter_tuning_job(
        self,
        *,
        HyperParameterTuningJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_image(
        self,
        *,
        ImageName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_image_version(
        self,
        *,
        ImageName: str,
        Version: int | None = None,
        Alias: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_inference_component(
        self,
        *,
        InferenceComponentName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_inference_experiment(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_inference_router(
        self,
        *,
        InferenceRouterName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_job(
        self,
        *,
        JobName: str,
        JobCategory: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_mlflow_app(
        self,
        *,
        Arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_mlflow_tracking_server(
        self,
        *,
        TrackingServerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_model_bias_job_definition(
        self,
        *,
        JobDefinitionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_model_card(
        self,
        *,
        ModelCardName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_model_explainability_job_definition(
        self,
        *,
        JobDefinitionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_model_package(
        self,
        *,
        ModelPackageName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_model_package_group(
        self,
        *,
        ModelPackageGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_model_package_group_policy(
        self,
        *,
        ModelPackageGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_model_quality_job_definition(
        self,
        *,
        JobDefinitionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_monitoring_schedule(
        self,
        *,
        MonitoringScheduleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_notebook_instance(
        self,
        *,
        NotebookInstanceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_notebook_instance_lifecycle_config(
        self,
        *,
        NotebookInstanceLifecycleConfigName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_optimization_job(
        self,
        *,
        OptimizationJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_partner_app(
        self,
        *,
        Arn: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_pipeline(
        self,
        *,
        PipelineName: str,
        ClientRequestToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_processing_job(
        self,
        *,
        ProcessingJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_project(
        self,
        *,
        ProjectName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_space(
        self,
        *,
        DomainId: str,
        SpaceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_studio_lifecycle_config(
        self,
        *,
        StudioLifecycleConfigName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_training_job(
        self,
        *,
        TrainingJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_training_session(
        self,
        *,
        TrainingSessionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_trial(
        self,
        *,
        TrialName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_trial_component(
        self,
        *,
        TrialComponentName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user_profile(
        self,
        *,
        DomainId: str,
        UserProfileName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_workforce(
        self,
        *,
        WorkforceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_workteam(
        self,
        *,
        WorkteamName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_devices(
        self,
        *,
        DeviceFleetName: str,
        DeviceNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ai_benchmark_job(
        self,
        *,
        AIBenchmarkJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ai_recommendation_job(
        self,
        *,
        AIRecommendationJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ai_workload_config(
        self,
        *,
        AIWorkloadConfigName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_action(
        self,
        *,
        ActionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_algorithm(
        self,
        *,
        AlgorithmName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_app(
        self,
        *,
        DomainId: str,
        AppType: str,
        AppName: str,
        UserProfileName: str | None = None,
        SpaceName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_app_image_config(
        self,
        *,
        AppImageConfigName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_artifact(
        self,
        *,
        ArtifactArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_auto_ml_job(
        self,
        *,
        AutoMLJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_auto_ml_job_v2(
        self,
        *,
        AutoMLJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_capacity_reservation(
        self,
        *,
        SMCapacityReservationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster(
        self,
        *,
        ClusterName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster_event(
        self,
        *,
        EventId: str,
        ClusterName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster_extension(
        self,
        *,
        ClusterArn: str,
        ExtensionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster_node(
        self,
        *,
        ClusterName: str,
        NodeId: str | None = None,
        NodeLogicalId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster_operation(
        self,
        *,
        ClusterName: str,
        OperationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cluster_scheduler_config(
        self,
        *,
        ClusterSchedulerConfigId: str,
        ClusterSchedulerConfigVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_code_repository(
        self,
        *,
        CodeRepositoryName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_compilation_job(
        self,
        *,
        CompilationJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_compute_quota(
        self,
        *,
        ComputeQuotaId: str,
        ComputeQuotaVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_context(
        self,
        *,
        ContextName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_data_quality_job_definition(
        self,
        *,
        JobDefinitionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_device(
        self,
        *,
        DeviceName: str,
        DeviceFleetName: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_device_fleet(
        self,
        *,
        DeviceFleetName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_domain(
        self,
        *,
        DomainId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_edge_deployment_plan(
        self,
        *,
        EdgeDeploymentPlanName: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_edge_packaging_job(
        self,
        *,
        EdgePackagingJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_experiment(
        self,
        *,
        ExperimentName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_feature_group(
        self,
        *,
        FeatureGroupName: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_feature_metadata(
        self,
        *,
        FeatureGroupName: str,
        FeatureName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_flow_definition(
        self,
        *,
        FlowDefinitionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_global_inference_gateway(
        self,
        *,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_hub(
        self,
        *,
        HubName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_hub_content(
        self,
        *,
        HubName: str,
        HubContentType: str,
        HubContentName: str,
        HubContentVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_human_task_ui(
        self,
        *,
        HumanTaskUiName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_hyper_parameter_tuning_job(
        self,
        *,
        HyperParameterTuningJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_image(
        self,
        *,
        ImageName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_image_version(
        self,
        *,
        ImageName: str,
        Version: int | None = None,
        Alias: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_inference_component(
        self,
        *,
        InferenceComponentName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_inference_experiment(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_inference_recommendations_job(
        self,
        *,
        JobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_inference_router(
        self,
        *,
        InferenceRouterName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_job(
        self,
        *,
        JobName: str,
        JobCategory: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_job_schema_version(
        self,
        *,
        JobCategory: str,
        JobConfigSchemaVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_labeling_job(
        self,
        *,
        LabelingJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_lineage_group(
        self,
        *,
        LineageGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_mlflow_app(
        self,
        *,
        Arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_mlflow_tracking_server(
        self,
        *,
        TrackingServerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_model_bias_job_definition(
        self,
        *,
        JobDefinitionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_model_card(
        self,
        *,
        ModelCardName: str,
        ModelCardVersion: int | None = None,
        IncludedData: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_model_card_export_job(
        self,
        *,
        ModelCardExportJobArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_model_explainability_job_definition(
        self,
        *,
        JobDefinitionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_model_package(
        self,
        *,
        ModelPackageName: str,
        IncludedData: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_model_package_group(
        self,
        *,
        ModelPackageGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_model_quality_job_definition(
        self,
        *,
        JobDefinitionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_monitoring_schedule(
        self,
        *,
        MonitoringScheduleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_notebook_instance_lifecycle_config(
        self,
        *,
        NotebookInstanceLifecycleConfigName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_optimization_job(
        self,
        *,
        OptimizationJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_partner_app(
        self,
        *,
        Arn: str,
        IncludeAvailableUpgrade: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_pipeline_definition_for_execution(
        self,
        *,
        PipelineExecutionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_pipeline_execution(
        self,
        *,
        PipelineExecutionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_project(
        self,
        *,
        ProjectName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_reserved_capacity(
        self,
        *,
        ReservedCapacityArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_resource_associations(
        self,
        *,
        SMCapacityReservationArn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_space(
        self,
        *,
        DomainId: str,
        SpaceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_studio_lifecycle_config(
        self,
        *,
        StudioLifecycleConfigName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_subscribed_workteam(
        self,
        *,
        WorkteamArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_training_plan(
        self,
        *,
        TrainingPlanName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_training_plan_extension_history(
        self,
        *,
        TrainingPlanArn: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_training_session(
        self,
        *,
        TrainingSessionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_transform_job(
        self,
        *,
        TransformJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_trial(
        self,
        *,
        TrialName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_trial_component(
        self,
        *,
        TrialComponentName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_user_profile(
        self,
        *,
        DomainId: str,
        UserProfileName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_workforce(
        self,
        *,
        WorkforceName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_workteam(
        self,
        *,
        WorkteamName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_cluster_node_volume(
        self,
        *,
        ClusterArn: str,
        NodeId: str,
        VolumeId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_sagemaker_servicecatalog_portfolio(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_trial_component(
        self,
        *,
        TrialComponentName: str,
        TrialName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_sagemaker_servicecatalog_portfolio(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def extend_training_plan(
        self,
        *,
        TrainingPlanExtensionOfferingId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_capacity_reservation_usage(
        self,
        *,
        SMCapacityReservationArn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_device_fleet_report(
        self,
        *,
        DeviceFleetName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_endpoint_policy(
        self,
        *,
        EndpointName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_lineage_group_policy(
        self,
        *,
        LineageGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_model_package_group_policy(
        self,
        *,
        ModelPackageGroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_sagemaker_servicecatalog_portfolio_status(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_scaling_configuration_recommendation(
        self,
        *,
        InferenceRecommendationsJobName: str,
        RecommendationId: str | None = None,
        EndpointName: str | None = None,
        TargetCpuUtilizationPerCore: int | None = None,
        ScalingPolicyObjective: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_search_suggestions(
        self,
        *,
        Resource: str,
        SuggestionQuery: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_hub_content(
        self,
        *,
        HubContentName: str,
        HubContentType: str,
        DocumentSchemaVersion: str,
        HubName: str,
        HubContentDocument: str,
        HubContentVersion: str | None = None,
        HubContentDisplayName: str | None = None,
        HubContentDescription: str | None = None,
        HubContentMarkdown: str | None = None,
        SupportStatus: str | None = None,
        HubContentSearchKeywords: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_ai_benchmark_jobs(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        NameContains: str | None = None,
        StatusEquals: str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_ai_recommendation_jobs(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        NameContains: str | None = None,
        StatusEquals: str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_ai_workload_configs(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        NameContains: str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_actions(
        self,
        *,
        SourceUri: str | None = None,
        ActionType: str | None = None,
        CreatedAfter: datetime.datetime | str | None = None,
        CreatedBefore: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_algorithms(
        self,
        *,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        MaxResults: int | None = None,
        NameContains: str | None = None,
        NextToken: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_aliases(
        self,
        *,
        ImageName: str,
        Alias: str | None = None,
        Version: int | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_app_image_configs(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        NameContains: str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        ModifiedTimeBefore: datetime.datetime | str | None = None,
        ModifiedTimeAfter: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_apps(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SortOrder: str | None = None,
        SortBy: str | None = None,
        DomainIdEquals: str | None = None,
        UserProfileNameEquals: str | None = None,
        SpaceNameEquals: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_artifacts(
        self,
        *,
        SourceUri: str | None = None,
        ArtifactType: str | None = None,
        CreatedAfter: datetime.datetime | str | None = None,
        CreatedBefore: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_associations(
        self,
        *,
        SourceArn: str | None = None,
        DestinationArn: str | None = None,
        SourceType: str | None = None,
        DestinationType: str | None = None,
        AssociationType: str | None = None,
        CreatedAfter: datetime.datetime | str | None = None,
        CreatedBefore: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_auto_ml_jobs(
        self,
        *,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        NameContains: str | None = None,
        StatusEquals: str | None = None,
        SortOrder: str | None = None,
        SortBy: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_candidates_for_auto_ml_job(
        self,
        *,
        AutoMLJobName: str,
        StatusEquals: str | None = None,
        CandidateNameEquals: str | None = None,
        SortOrder: str | None = None,
        SortBy: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_capacity_reservations(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_cluster_events(
        self,
        *,
        ClusterName: str,
        InstanceGroupName: str | None = None,
        NodeId: str | None = None,
        EventTimeAfter: datetime.datetime | str | None = None,
        EventTimeBefore: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        ResourceType: str | None = None,
        OperationId: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_cluster_extension_versions(
        self,
        *,
        ExtensionName: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_cluster_extensions(
        self,
        *,
        ClusterArn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_cluster_nodes(
        self,
        *,
        ClusterName: str,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        InstanceGroupNameContains: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        IncludeNodeLogicalIds: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_cluster_operations(
        self,
        *,
        ClusterName: str,
        Status: str | None = None,
        Type: str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_cluster_scheduler_configs(
        self,
        *,
        CreatedAfter: datetime.datetime | str | None = None,
        CreatedBefore: datetime.datetime | str | None = None,
        NameContains: str | None = None,
        ClusterArn: str | None = None,
        Status: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_clusters(
        self,
        *,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        MaxResults: int | None = None,
        NameContains: str | None = None,
        NextToken: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        TrainingPlanArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_code_repositories(
        self,
        *,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        MaxResults: int | None = None,
        NameContains: str | None = None,
        NextToken: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_compilation_jobs(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        NameContains: str | None = None,
        StatusEquals: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_compute_quotas(
        self,
        *,
        CreatedAfter: datetime.datetime | str | None = None,
        CreatedBefore: datetime.datetime | str | None = None,
        NameContains: str | None = None,
        Status: str | None = None,
        ClusterArn: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_contexts(
        self,
        *,
        SourceUri: str | None = None,
        ContextType: str | None = None,
        CreatedAfter: datetime.datetime | str | None = None,
        CreatedBefore: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_quality_job_definitions(
        self,
        *,
        EndpointName: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        NameContains: str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_device_fleets(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        NameContains: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_devices(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        LatestHeartbeatAfter: datetime.datetime | str | None = None,
        ModelName: str | None = None,
        DeviceFleetName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_domains(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_edge_deployment_plans(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        NameContains: str | None = None,
        DeviceFleetNameContains: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_edge_packaging_jobs(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        NameContains: str | None = None,
        ModelNameContains: str | None = None,
        StatusEquals: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_experiments(
        self,
        *,
        CreatedAfter: datetime.datetime | str | None = None,
        CreatedBefore: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_feature_groups(
        self,
        *,
        NameContains: str | None = None,
        FeatureGroupStatusEquals: str | None = None,
        OfflineStoreStatusEquals: str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        SortOrder: str | None = None,
        SortBy: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_flow_definitions(
        self,
        *,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_global_inference_gateways(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_hub_content_versions(
        self,
        *,
        HubName: str,
        HubContentType: str,
        HubContentName: str,
        MinVersion: str | None = None,
        MaxSchemaVersion: str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_hub_contents(
        self,
        *,
        HubName: str,
        HubContentType: str,
        NameContains: str | None = None,
        MaxSchemaVersion: str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_hubs(
        self,
        *,
        NameContains: str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_human_task_uis(
        self,
        *,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_hyper_parameter_tuning_jobs(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NameContains: str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        StatusEquals: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_image_versions(
        self,
        *,
        ImageName: str,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_images(
        self,
        *,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        MaxResults: int | None = None,
        NameContains: str | None = None,
        NextToken: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_inference_components(
        self,
        *,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        NameContains: str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        StatusEquals: str | None = None,
        EndpointNameEquals: str | None = None,
        VariantNameEquals: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_inference_experiments(
        self,
        *,
        NameContains: str | None = None,
        Type: str | None = None,
        StatusEquals: str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_inference_gateways(
        self,
        *,
        Identifier: str,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_inference_recommendations_job_steps(
        self,
        *,
        JobName: str,
        Status: str | None = None,
        StepType: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_inference_recommendations_jobs(
        self,
        *,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        NameContains: str | None = None,
        StatusEquals: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        ModelNameEquals: str | None = None,
        ModelPackageVersionArnEquals: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_inference_routers(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_job_schema_versions(
        self,
        *,
        JobCategory: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_jobs(
        self,
        *,
        JobCategory: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        NameContains: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        StatusEquals: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_labeling_jobs(
        self,
        *,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        NameContains: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        StatusEquals: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_labeling_jobs_for_workteam(
        self,
        *,
        WorkteamArn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        JobReferenceCodeContains: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_lineage_groups(
        self,
        *,
        CreatedAfter: datetime.datetime | str | None = None,
        CreatedBefore: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_mlflow_apps(
        self,
        *,
        CreatedAfter: datetime.datetime | str | None = None,
        CreatedBefore: datetime.datetime | str | None = None,
        Status: str | None = None,
        MlflowVersion: str | None = None,
        DefaultForDomainId: str | None = None,
        AccountDefaultStatus: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_mlflow_tracking_servers(
        self,
        *,
        CreatedAfter: datetime.datetime | str | None = None,
        CreatedBefore: datetime.datetime | str | None = None,
        TrackingServerStatus: str | None = None,
        MlflowVersion: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_model_bias_job_definitions(
        self,
        *,
        EndpointName: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        NameContains: str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_model_card_export_jobs(
        self,
        *,
        ModelCardName: str,
        ModelCardVersion: int | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        ModelCardExportJobNameContains: str | None = None,
        StatusEquals: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_model_card_versions(
        self,
        *,
        ModelCardName: str,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        MaxResults: int | None = None,
        ModelCardStatus: str | None = None,
        NextToken: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_model_cards(
        self,
        *,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        MaxResults: int | None = None,
        NameContains: str | None = None,
        ModelCardStatus: str | None = None,
        NextToken: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_model_explainability_job_definitions(
        self,
        *,
        EndpointName: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        NameContains: str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_model_metadata(
        self,
        *,
        SearchExpression: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_model_package_groups(
        self,
        *,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        MaxResults: int | None = None,
        NameContains: str | None = None,
        NextToken: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        CrossAccountFilterOption: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_model_packages(
        self,
        *,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        MaxResults: int | None = None,
        NameContains: str | None = None,
        ModelApprovalStatus: str | None = None,
        ModelPackageGroupName: str | None = None,
        ModelPackageType: str | None = None,
        NextToken: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_model_quality_job_definitions(
        self,
        *,
        EndpointName: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        NameContains: str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_monitoring_alert_history(
        self,
        *,
        MonitoringScheduleName: str | None = None,
        MonitoringAlertName: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        StatusEquals: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_monitoring_alerts(
        self,
        *,
        MonitoringScheduleName: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_monitoring_executions(
        self,
        *,
        MonitoringScheduleName: str | None = None,
        EndpointName: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        ScheduledTimeBefore: datetime.datetime | str | None = None,
        ScheduledTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        StatusEquals: str | None = None,
        MonitoringJobDefinitionName: str | None = None,
        MonitoringTypeEquals: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_monitoring_schedules(
        self,
        *,
        EndpointName: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        NameContains: str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        StatusEquals: str | None = None,
        MonitoringJobDefinitionName: str | None = None,
        MonitoringTypeEquals: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_notebook_instance_lifecycle_configs(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NameContains: str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_optimization_jobs(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        OptimizationContains: str | None = None,
        NameContains: str | None = None,
        StatusEquals: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_partner_apps(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_pipeline_execution_steps(
        self,
        *,
        PipelineExecutionArn: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_pipeline_executions(
        self,
        *,
        PipelineName: str,
        CreatedAfter: datetime.datetime | str | None = None,
        CreatedBefore: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        PipelineVersionAlias: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_pipeline_parameters_for_execution(
        self,
        *,
        PipelineExecutionArn: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_pipeline_versions(
        self,
        *,
        PipelineName: str,
        CreatedAfter: datetime.datetime | str | None = None,
        CreatedBefore: datetime.datetime | str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_projects(
        self,
        *,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        MaxResults: int | None = None,
        NameContains: str | None = None,
        NextToken: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resource_catalogs(
        self,
        *,
        NameContains: str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        SortOrder: str | None = None,
        SortBy: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_spaces(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SortOrder: str | None = None,
        SortBy: str | None = None,
        DomainIdEquals: str | None = None,
        SpaceNameContains: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_stage_devices(
        self,
        *,
        EdgeDeploymentPlanName: str,
        StageName: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        ExcludeDevicesDeployedInOtherStage: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_studio_lifecycle_configs(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        NameContains: str | None = None,
        AppTypeEquals: str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        ModifiedTimeBefore: datetime.datetime | str | None = None,
        ModifiedTimeAfter: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_subscribed_workteams(
        self,
        *,
        NameContains: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_training_jobs_for_hyper_parameter_tuning_job(
        self,
        *,
        HyperParameterTuningJobName: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        StatusEquals: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_training_plans(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        StartTimeAfter: datetime.datetime | str | None = None,
        StartTimeBefore: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_training_sessions(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        NameContains: str | None = None,
        StatusEquals: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_transform_jobs(
        self,
        *,
        CreationTimeAfter: datetime.datetime | str | None = None,
        CreationTimeBefore: datetime.datetime | str | None = None,
        LastModifiedTimeAfter: datetime.datetime | str | None = None,
        LastModifiedTimeBefore: datetime.datetime | str | None = None,
        NameContains: str | None = None,
        StatusEquals: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_trial_components(
        self,
        *,
        ExperimentName: str | None = None,
        TrialName: str | None = None,
        SourceArn: str | None = None,
        CreatedAfter: datetime.datetime | str | None = None,
        CreatedBefore: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_trials(
        self,
        *,
        ExperimentName: str | None = None,
        TrialComponentName: str | None = None,
        CreatedAfter: datetime.datetime | str | None = None,
        CreatedBefore: datetime.datetime | str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_ultra_servers_by_reserved_capacity(
        self,
        *,
        ReservedCapacityArn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_user_profiles(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SortOrder: str | None = None,
        SortBy: str | None = None,
        DomainIdEquals: str | None = None,
        UserProfileNameContains: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_workforces(
        self,
        *,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NameContains: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_workteams(
        self,
        *,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NameContains: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def move_cluster_nodes(
        self,
        *,
        SourceClusterArn: str,
        SourceInstanceGroupName: str,
        TargetClusterArn: str,
        TargetInstanceGroupName: str,
        InstanceCount: int | None = None,
        NodeIds: list[str] | None = None,
        NodeLogicalIds: list[str] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_endpoint_policy(
        self,
        *,
        EndpointName: str,
        ResourcePolicy: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_model_package_group_policy(
        self,
        *,
        ModelPackageGroupName: str,
        ResourcePolicy: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def query_lineage(
        self,
        *,
        StartArns: list[str] | None = None,
        Direction: str | None = None,
        IncludeEdges: bool | None = None,
        Filters: dict[str, Any] | None = None,
        MaxDepth: int | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_devices(
        self,
        *,
        DeviceFleetName: str,
        Devices: list[dict[str, Any]],
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_inference_gateway(
        self,
        *,
        Identifier: str,
        ClusterArn: str,
        Namespace: str,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def render_ui_template(
        self,
        *,
        Task: dict[str, Any],
        RoleArn: str,
        UiTemplate: dict[str, Any] | None = None,
        HumanTaskUiArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def retry_pipeline_execution(
        self,
        *,
        PipelineExecutionArn: str,
        ClientRequestToken: str,
        ParallelismConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search(
        self,
        *,
        Resource: str,
        SearchExpression: dict[str, Any] | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        CrossAccountFilterOption: str | None = None,
        VisibilityConditions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_training_plan_offerings(
        self,
        *,
        InstanceType: str | None = None,
        InstanceCount: int | None = None,
        UltraServerType: str | None = None,
        UltraServerCount: int | None = None,
        StartTimeAfter: datetime.datetime | str | None = None,
        EndTimeBefore: datetime.datetime | str | None = None,
        DurationHours: int | None = None,
        TargetResources: list[str] | None = None,
        TrainingPlanArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_pipeline_execution_step_failure(
        self,
        *,
        CallbackToken: str,
        FailureReason: str | None = None,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_pipeline_execution_step_success(
        self,
        *,
        CallbackToken: str,
        OutputParameters: list[dict[str, Any]] | None = None,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_cluster_health_check(
        self,
        *,
        ClusterName: str,
        DeepHealthCheckConfigurations: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_edge_deployment_stage(
        self,
        *,
        EdgeDeploymentPlanName: str,
        StageName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_inference_experiment(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_mlflow_tracking_server(
        self,
        *,
        TrackingServerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_monitoring_schedule(
        self,
        *,
        MonitoringScheduleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_session(
        self,
        *,
        ResourceIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_ai_benchmark_job(
        self,
        *,
        AIBenchmarkJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_ai_recommendation_job(
        self,
        *,
        AIRecommendationJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_auto_ml_job(
        self,
        *,
        AutoMLJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_compilation_job(
        self,
        *,
        CompilationJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_edge_deployment_stage(
        self,
        *,
        EdgeDeploymentPlanName: str,
        StageName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_edge_packaging_job(
        self,
        *,
        EdgePackagingJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_hyper_parameter_tuning_job(
        self,
        *,
        HyperParameterTuningJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_inference_experiment(
        self,
        *,
        Name: str,
        ModelVariantActions: dict[str, str],
        DesiredModelVariants: list[dict[str, Any]] | None = None,
        DesiredState: str | None = None,
        Reason: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_inference_recommendations_job(
        self,
        *,
        JobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_job(
        self,
        *,
        JobName: str,
        JobCategory: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_labeling_job(
        self,
        *,
        LabelingJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_mlflow_tracking_server(
        self,
        *,
        TrackingServerName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_monitoring_schedule(
        self,
        *,
        MonitoringScheduleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_optimization_job(
        self,
        *,
        OptimizationJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_pipeline_execution(
        self,
        *,
        PipelineExecutionArn: str,
        ClientRequestToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_training_session(
        self,
        *,
        TrainingSessionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_transform_job(
        self,
        *,
        TransformJobName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_action(
        self,
        *,
        ActionName: str,
        Description: str | None = None,
        Status: str | None = None,
        Properties: dict[str, str] | None = None,
        PropertiesToRemove: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_app_image_config(
        self,
        *,
        AppImageConfigName: str,
        KernelGatewayImageConfig: dict[str, Any] | None = None,
        JupyterLabAppImageConfig: dict[str, Any] | None = None,
        CodeEditorAppImageConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_artifact(
        self,
        *,
        ArtifactArn: str,
        ArtifactName: str | None = None,
        Properties: dict[str, str] | None = None,
        PropertiesToRemove: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_cluster(
        self,
        *,
        ClusterName: str,
        InstanceGroups: list[dict[str, Any]] | None = None,
        RestrictedInstanceGroups: list[dict[str, Any]] | None = None,
        RestrictedInstanceGroupsConfig: dict[str, Any] | None = None,
        TieredStorageConfig: dict[str, Any] | None = None,
        NodeRecovery: str | None = None,
        InstanceGroupsToDelete: list[str] | None = None,
        NodeProvisioningMode: str | None = None,
        ClusterRole: str | None = None,
        AutoScaling: dict[str, Any] | None = None,
        Orchestrator: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_cluster_extension(
        self,
        *,
        ClusterArn: str,
        ExtensionArn: str,
        ExtensionVersion: str | None = None,
        ConfigurationValues: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_cluster_scheduler_config(
        self,
        *,
        ClusterSchedulerConfigId: str,
        TargetVersion: int,
        SchedulerConfig: dict[str, Any] | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_cluster_software(
        self,
        *,
        ClusterName: str,
        InstanceGroups: list[dict[str, Any]] | None = None,
        DeploymentConfig: dict[str, Any] | None = None,
        ImageId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_code_repository(
        self,
        *,
        CodeRepositoryName: str,
        GitConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_compute_quota(
        self,
        *,
        ComputeQuotaId: str,
        TargetVersion: int,
        ComputeQuotaConfig: dict[str, Any] | None = None,
        ComputeQuotaTarget: dict[str, Any] | None = None,
        ActivationState: str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_context(
        self,
        *,
        ContextName: str,
        Description: str | None = None,
        Properties: dict[str, str] | None = None,
        PropertiesToRemove: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_device_fleet(
        self,
        *,
        DeviceFleetName: str,
        OutputConfig: dict[str, Any],
        RoleArn: str | None = None,
        Description: str | None = None,
        EnableIotRoleAlias: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_devices(
        self,
        *,
        DeviceFleetName: str,
        Devices: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_domain(
        self,
        *,
        DomainId: str,
        DefaultUserSettings: dict[str, Any] | None = None,
        DomainSettingsForUpdate: dict[str, Any] | None = None,
        AppSecurityGroupManagement: str | None = None,
        DefaultSpaceSettings: dict[str, Any] | None = None,
        SubnetIds: list[str] | None = None,
        AppNetworkAccessType: str | None = None,
        TagPropagation: str | None = None,
        HomeEfsFileSystemCreation: str | None = None,
        VpcId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_endpoint_weights_and_capacities(
        self,
        *,
        EndpointName: str,
        DesiredWeightsAndCapacities: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_experiment(
        self,
        *,
        ExperimentName: str,
        DisplayName: str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_feature_group(
        self,
        *,
        FeatureGroupName: str,
        FeatureAdditions: list[dict[str, Any]] | None = None,
        OnlineStoreConfig: dict[str, Any] | None = None,
        ThroughputConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_feature_metadata(
        self,
        *,
        FeatureGroupName: str,
        FeatureName: str,
        Description: str | None = None,
        ParameterAdditions: list[dict[str, Any]] | None = None,
        ParameterRemovals: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_global_inference_gateway(
        self,
        *,
        Identifier: str,
        Routing: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_hub(
        self,
        *,
        HubName: str,
        HubDescription: str | None = None,
        HubDisplayName: str | None = None,
        HubSearchKeywords: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_hub_content(
        self,
        *,
        HubName: str,
        HubContentName: str,
        HubContentType: str,
        HubContentVersion: str,
        HubContentDisplayName: str | None = None,
        HubContentDescription: str | None = None,
        HubContentMarkdown: str | None = None,
        HubContentSearchKeywords: list[str] | None = None,
        SupportStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_hub_content_reference(
        self,
        *,
        HubName: str,
        HubContentName: str,
        HubContentType: str,
        MinVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_image(
        self,
        *,
        ImageName: str,
        DeleteProperties: list[str] | None = None,
        Description: str | None = None,
        DisplayName: str | None = None,
        RoleArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_image_version(
        self,
        *,
        ImageName: str,
        Alias: str | None = None,
        Version: int | None = None,
        AliasesToAdd: list[str] | None = None,
        AliasesToDelete: list[str] | None = None,
        VendorGuidance: str | None = None,
        JobType: str | None = None,
        MLFramework: str | None = None,
        ProgrammingLang: str | None = None,
        Processor: str | None = None,
        Horovod: bool | None = None,
        ReleaseNotes: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_inference_component(
        self,
        *,
        InferenceComponentName: str,
        Specification: dict[str, Any] | None = None,
        Specifications: list[dict[str, Any]] | None = None,
        RuntimeConfig: dict[str, Any] | None = None,
        DeploymentConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_inference_component_runtime_config(
        self,
        *,
        InferenceComponentName: str,
        DesiredRuntimeConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_inference_experiment(
        self,
        *,
        Name: str,
        Schedule: dict[str, Any] | None = None,
        Description: str | None = None,
        ModelVariants: list[dict[str, Any]] | None = None,
        DataStorageConfig: dict[str, Any] | None = None,
        ShadowModeConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_inference_router(
        self,
        *,
        InferenceRouterName: str,
        RoutingTargets: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_mlflow_app(
        self,
        *,
        Arn: str,
        Name: str | None = None,
        ArtifactStoreUri: str | None = None,
        ModelRegistrationMode: str | None = None,
        WeeklyMaintenanceWindowStart: str | None = None,
        DefaultDomainIdList: list[str] | None = None,
        AccountDefaultStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_mlflow_tracking_server(
        self,
        *,
        TrackingServerName: str,
        ArtifactStoreUri: str | None = None,
        TrackingServerSize: str | None = None,
        AutomaticModelRegistration: bool | None = None,
        WeeklyMaintenanceWindowStart: str | None = None,
        S3BucketOwnerAccountId: str | None = None,
        S3BucketOwnerVerification: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_model_card(
        self,
        *,
        ModelCardName: str,
        Content: str | None = None,
        ModelCardStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_model_package(
        self,
        *,
        ModelPackageArn: str,
        ModelApprovalStatus: str | None = None,
        ModelPackageRegistrationType: str | None = None,
        ApprovalDescription: str | None = None,
        CustomerMetadataProperties: dict[str, str] | None = None,
        CustomerMetadataPropertiesToRemove: list[str] | None = None,
        AdditionalInferenceSpecificationsToAdd: list[dict[str, Any]] | None = None,
        InferenceSpecification: dict[str, Any] | None = None,
        SourceUri: str | None = None,
        ModelCard: dict[str, Any] | None = None,
        ModelLifeCycle: dict[str, Any] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_monitoring_alert(
        self,
        *,
        MonitoringScheduleName: str,
        MonitoringAlertName: str,
        DatapointsToAlert: int,
        EvaluationPeriod: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_monitoring_schedule(
        self,
        *,
        MonitoringScheduleName: str,
        MonitoringScheduleConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_notebook_instance(
        self,
        *,
        NotebookInstanceName: str,
        InstanceType: str | None = None,
        IpAddressType: str | None = None,
        PlatformIdentifier: str | None = None,
        RoleArn: str | None = None,
        LifecycleConfigName: str | None = None,
        DisassociateLifecycleConfig: bool | None = None,
        VolumeSizeInGB: int | None = None,
        DefaultCodeRepository: str | None = None,
        AdditionalCodeRepositories: list[str] | None = None,
        AcceleratorTypes: list[str] | None = None,
        DisassociateAcceleratorTypes: bool | None = None,
        DisassociateDefaultCodeRepository: bool | None = None,
        DisassociateAdditionalCodeRepositories: bool | None = None,
        RootAccess: str | None = None,
        InstanceMetadataServiceConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_notebook_instance_lifecycle_config(
        self,
        *,
        NotebookInstanceLifecycleConfigName: str,
        OnCreate: list[dict[str, Any]] | None = None,
        OnStart: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_partner_app(
        self,
        *,
        Arn: str,
        MaintenanceConfig: dict[str, Any] | None = None,
        Tier: str | None = None,
        ApplicationConfig: dict[str, Any] | None = None,
        IdcConfig: dict[str, Any] | None = None,
        AuthType: str | None = None,
        EnableIamSessionBasedIdentity: bool | None = None,
        EnableAutoMinorVersionUpgrade: bool | None = None,
        AppVersion: str | None = None,
        ClientToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_pipeline(
        self,
        *,
        PipelineName: str,
        PipelineDisplayName: str | None = None,
        PipelineDefinition: str | None = None,
        PipelineDefinitionS3Location: dict[str, Any] | None = None,
        PipelineDescription: str | None = None,
        RoleArn: str | None = None,
        ParallelismConfiguration: dict[str, Any] | None = None,
        PipelineVersionAliases: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_pipeline_execution(
        self,
        *,
        PipelineExecutionArn: str,
        PipelineExecutionDescription: str | None = None,
        PipelineExecutionDisplayName: str | None = None,
        ParallelismConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_pipeline_version(
        self,
        *,
        PipelineArn: str,
        PipelineVersionId: int,
        PipelineVersionDisplayName: str | None = None,
        PipelineVersionDescription: str | None = None,
        PipelineVersionAliasOperations: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_project(
        self,
        *,
        ProjectName: str,
        ProjectDescription: str | None = None,
        ServiceCatalogProvisioningUpdateDetails: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        TemplateProvidersToUpdate: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_space(
        self,
        *,
        DomainId: str,
        SpaceName: str,
        SpaceSettings: dict[str, Any] | None = None,
        SpaceDisplayName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_training_job(
        self,
        *,
        TrainingJobName: str,
        ProfilerConfig: dict[str, Any] | None = None,
        ProfilerRuleConfigurations: list[dict[str, Any]] | None = None,
        ResourceConfig: dict[str, Any] | None = None,
        RemoteDebugConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_trial(
        self,
        *,
        TrialName: str,
        DisplayName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_trial_component(
        self,
        *,
        TrialComponentName: str,
        DisplayName: str | None = None,
        Status: dict[str, Any] | None = None,
        StartTime: datetime.datetime | str | None = None,
        EndTime: datetime.datetime | str | None = None,
        Parameters: dict[str, dict[str, Any]] | None = None,
        ParametersToRemove: list[str] | None = None,
        InputArtifacts: dict[str, dict[str, Any]] | None = None,
        InputArtifactsToRemove: list[str] | None = None,
        OutputArtifacts: dict[str, dict[str, Any]] | None = None,
        OutputArtifactsToRemove: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user_profile(
        self,
        *,
        DomainId: str,
        UserProfileName: str,
        UserSettings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_workforce(
        self,
        *,
        WorkforceName: str,
        SourceIpConfig: dict[str, Any] | None = None,
        OidcConfig: dict[str, Any] | None = None,
        WorkforceVpcConfig: dict[str, Any] | None = None,
        IpAddressType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_workteam(
        self,
        *,
        WorkteamName: str,
        MemberDefinitions: list[dict[str, Any]] | None = None,
        Description: str | None = None,
        NotificationConfiguration: dict[str, Any] | None = None,
        WorkerAccessConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
