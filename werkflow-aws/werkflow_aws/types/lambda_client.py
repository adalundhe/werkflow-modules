from abc import ABC, abstractmethod
import datetime
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class LambdaClient(ABC):

    @abstractmethod
    def list_functions(
        self,
        *,
        MasterRegion: str | None = None,
        FunctionVersion: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_function(
        self,
        *,
        FunctionName: str,
        Qualifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_function_configuration(
        self,
        *,
        FunctionName: str,
        Qualifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_function(
        self,
        *,
        FunctionName: str,
        Role: str,
        Code: dict[str, Any],
        Runtime: str | None = None,
        Handler: str | None = None,
        Description: str | None = None,
        Timeout: int | None = None,
        MemorySize: int | None = None,
        Publish: bool | None = None,
        PublishTo: str | None = None,
        VpcConfig: dict[str, Any] | None = None,
        PackageType: str | None = None,
        DeadLetterConfig: dict[str, Any] | None = None,
        Environment: dict[str, Any] | None = None,
        KMSKeyArn: str | None = None,
        TracingConfig: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
        Layers: list[str] | None = None,
        FileSystemConfigs: list[dict[str, Any]] | None = None,
        CodeSigningConfigArn: str | None = None,
        ImageConfig: dict[str, Any] | None = None,
        Architectures: list[str] | None = None,
        EphemeralStorage: dict[str, Any] | None = None,
        SnapStart: dict[str, Any] | None = None,
        LoggingConfig: dict[str, Any] | None = None,
        TenancyConfig: dict[str, Any] | None = None,
        CapacityProviderConfig: dict[str, Any] | None = None,
        DurableConfig: dict[str, Any] | None = None,
        RuntimeConfig: dict[str, Any] | None = None,
        AcceleratorConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_function(
        self,
        *,
        FunctionName: str,
        Qualifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_function_code(
        self,
        *,
        FunctionName: str,
        ZipFile: bytes | BinaryIO | str | None = None,
        S3Bucket: str | None = None,
        S3Key: str | None = None,
        S3ObjectVersion: str | None = None,
        S3ObjectStorageMode: str | None = None,
        ImageUri: str | None = None,
        Architectures: list[str] | None = None,
        Publish: bool | None = None,
        PublishTo: str | None = None,
        DryRun: bool | None = None,
        RevisionId: str | None = None,
        SourceKMSKeyArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_function_configuration(
        self,
        *,
        FunctionName: str,
        Role: str | None = None,
        Handler: str | None = None,
        Description: str | None = None,
        Timeout: int | None = None,
        MemorySize: int | None = None,
        VpcConfig: dict[str, Any] | None = None,
        Environment: dict[str, Any] | None = None,
        Runtime: str | None = None,
        DeadLetterConfig: dict[str, Any] | None = None,
        KMSKeyArn: str | None = None,
        TracingConfig: dict[str, Any] | None = None,
        RevisionId: str | None = None,
        Layers: list[str] | None = None,
        FileSystemConfigs: list[dict[str, Any]] | None = None,
        ImageConfig: dict[str, Any] | None = None,
        EphemeralStorage: dict[str, Any] | None = None,
        SnapStart: dict[str, Any] | None = None,
        LoggingConfig: dict[str, Any] | None = None,
        CapacityProviderConfig: dict[str, Any] | None = None,
        DurableConfig: dict[str, Any] | None = None,
        RuntimeConfig: dict[str, Any] | None = None,
        AcceleratorConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def invoke(
        self,
        *,
        FunctionName: str,
        InvocationType: str | None = None,
        LogType: str | None = None,
        ClientContext: str | None = None,
        DurableExecutionName: str | None = None,
        Payload: bytes | BinaryIO | str | None = None,
        Qualifier: str | None = None,
        TenantId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def publish_version(
        self,
        *,
        FunctionName: str,
        CodeSha256: str | None = None,
        Description: str | None = None,
        RevisionId: str | None = None,
        PublishTo: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_versions_by_function(
        self,
        *,
        FunctionName: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_alias(
        self,
        *,
        FunctionName: str,
        Name: str,
        FunctionVersion: str,
        Description: str | None = None,
        RoutingConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_alias(
        self,
        *,
        FunctionName: str,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_alias(
        self,
        *,
        FunctionName: str,
        Name: str,
        FunctionVersion: str | None = None,
        Description: str | None = None,
        RoutingConfig: dict[str, Any] | None = None,
        RevisionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_alias(
        self,
        *,
        FunctionName: str,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_aliases(
        self,
        *,
        FunctionName: str,
        FunctionVersion: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_layers(
        self,
        *,
        CompatibleArchitecture: str | None = None,
        CompatibleRuntime: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_event_source_mappings(
        self,
        *,
        EventSourceArn: str | None = None,
        FunctionName: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_event_source_mapping(
        self,
        *,
        FunctionName: str,
        EventSourceArn: str | None = None,
        Enabled: bool | None = None,
        BatchSize: int | None = None,
        FilterCriteria: dict[str, Any] | None = None,
        KMSKeyArn: str | None = None,
        MetricsConfig: dict[str, Any] | None = None,
        LoggingConfig: dict[str, Any] | None = None,
        ScalingConfig: dict[str, Any] | None = None,
        MaximumBatchingWindowInSeconds: int | None = None,
        ParallelizationFactor: int | None = None,
        StartingPosition: str | None = None,
        StartingPositionTimestamp: datetime.datetime | str | None = None,
        DestinationConfig: dict[str, Any] | None = None,
        MaximumRecordAgeInSeconds: int | None = None,
        BisectBatchOnFunctionError: bool | None = None,
        MaximumRetryAttempts: int | None = None,
        Tags: dict[str, str] | None = None,
        TumblingWindowInSeconds: int | None = None,
        Topics: list[str] | None = None,
        Queues: list[str] | None = None,
        SourceAccessConfigurations: list[dict[str, Any]] | None = None,
        SelfManagedEventSource: dict[str, Any] | None = None,
        FunctionResponseTypes: list[str] | None = None,
        AmazonManagedKafkaEventSourceConfig: dict[str, Any] | None = None,
        SelfManagedKafkaEventSourceConfig: dict[str, Any] | None = None,
        DocumentDBEventSourceConfig: dict[str, Any] | None = None,
        ProvisionedPollerConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_event_source_mapping(
        self,
        *,
        UUID: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags(
        self,
        *,
        Resource: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        Resource: str,
        Tags: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        Resource: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_layer_version_permission(
        self,
        *,
        LayerName: str,
        VersionNumber: int,
        StatementId: str,
        Action: str,
        Principal: str,
        OrganizationId: str | None = None,
        RevisionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_permission(
        self,
        *,
        FunctionName: str,
        StatementId: str,
        Action: str,
        Principal: str,
        SourceArn: str | None = None,
        FunctionUrlAuthType: str | None = None,
        InvokedViaFunctionUrl: bool | None = None,
        SourceAccount: str | None = None,
        EventSourceToken: str | None = None,
        Qualifier: str | None = None,
        RevisionId: str | None = None,
        PrincipalOrgID: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def checkpoint_durable_execution(
        self,
        *,
        DurableExecutionArn: str,
        CheckpointToken: str,
        Updates: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_capacity_provider(
        self,
        *,
        CapacityProviderName: str,
        VpcConfig: dict[str, Any],
        PermissionsConfig: dict[str, Any],
        InstanceRequirements: dict[str, Any] | None = None,
        CapacityProviderScalingConfig: dict[str, Any] | None = None,
        KmsKeyArn: str | None = None,
        Tags: dict[str, str] | None = None,
        PropagateTags: dict[str, Any] | None = None,
        TelemetryConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_code_signing_config(
        self,
        *,
        AllowedPublishers: dict[str, Any],
        Description: str | None = None,
        CodeSigningPolicies: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_function_url_config(
        self,
        *,
        FunctionName: str,
        AuthType: str,
        Qualifier: str | None = None,
        Cors: dict[str, Any] | None = None,
        InvokeMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_capacity_provider(
        self,
        *,
        CapacityProviderName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_code_signing_config(
        self,
        *,
        CodeSigningConfigArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_durable_execution(
        self,
        *,
        DurableExecutionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_function_code_signing_config(
        self,
        *,
        FunctionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_function_concurrency(
        self,
        *,
        FunctionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_function_event_invoke_config(
        self,
        *,
        FunctionName: str,
        Qualifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_function_url_config(
        self,
        *,
        FunctionName: str,
        Qualifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_layer_version(
        self,
        *,
        LayerName: str,
        VersionNumber: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_provisioned_concurrency_config(
        self,
        *,
        FunctionName: str,
        Qualifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_policy(
        self,
        *,
        ResourceArn: str,
        RevisionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_account_settings(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_capacity_provider(
        self,
        *,
        CapacityProviderName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_code_signing_config(
        self,
        *,
        CodeSigningConfigArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_durable_execution(
        self,
        *,
        DurableExecutionArn: str,
        IncludeExecutionData: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_durable_execution_history(
        self,
        *,
        DurableExecutionArn: str,
        IncludeExecutionData: bool | None = None,
        MaxItems: int | None = None,
        Marker: str | None = None,
        ReverseOrder: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_durable_execution_state(
        self,
        *,
        DurableExecutionArn: str,
        CheckpointToken: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_event_source_mapping(
        self,
        *,
        UUID: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_function_code_signing_config(
        self,
        *,
        FunctionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_function_concurrency(
        self,
        *,
        FunctionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_function_event_invoke_config(
        self,
        *,
        FunctionName: str,
        Qualifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_function_recursion_config(
        self,
        *,
        FunctionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_function_scaling_config(
        self,
        *,
        FunctionName: str,
        Qualifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_function_url_config(
        self,
        *,
        FunctionName: str,
        Qualifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_layer_version(
        self,
        *,
        LayerName: str,
        VersionNumber: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_layer_version_by_arn(
        self,
        *,
        Arn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_layer_version_policy(
        self,
        *,
        LayerName: str,
        VersionNumber: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_policy(
        self,
        *,
        FunctionName: str,
        Qualifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_provisioned_concurrency_config(
        self,
        *,
        FunctionName: str,
        Qualifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_policy(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_runtime_management_config(
        self,
        *,
        FunctionName: str,
        Qualifier: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def invoke_async(
        self,
        *,
        FunctionName: str,
        InvokeArgs: bytes | BinaryIO | str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def invoke_with_response_stream(
        self,
        *,
        FunctionName: str,
        LogType: str | None = None,
        ClientContext: str | None = None,
        Qualifier: str | None = None,
        Payload: bytes | BinaryIO | str | None = None,
        TenantId: str | None = None,
        InvocationType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_capacity_providers(
        self,
        *,
        State: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_code_signing_configs(
        self,
        *,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_durable_executions_by_function(
        self,
        *,
        FunctionName: str,
        Qualifier: str | None = None,
        DurableExecutionName: str | None = None,
        Statuses: list[str] | None = None,
        StartedAfter: datetime.datetime | str | None = None,
        StartedBefore: datetime.datetime | str | None = None,
        ReverseOrder: bool | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_function_event_invoke_configs(
        self,
        *,
        FunctionName: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_function_url_configs(
        self,
        *,
        FunctionName: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_function_versions_by_capacity_provider(
        self,
        *,
        CapacityProviderName: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_functions_by_code_signing_config(
        self,
        *,
        CodeSigningConfigArn: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_layer_versions(
        self,
        *,
        LayerName: str,
        CompatibleArchitecture: str | None = None,
        CompatibleRuntime: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_provisioned_concurrency_configs(
        self,
        *,
        FunctionName: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def pause_durable_execution(
        self,
        *,
        DurableExecutionArn: str,
        ClientToken: str | None = None,
        Reason: str | None = None,
        ExecutionTimeoutPaused: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def publish_layer_version(
        self,
        *,
        LayerName: str,
        Content: dict[str, Any],
        Description: str | None = None,
        CompatibleArchitectures: list[str] | None = None,
        CompatibleRuntimes: list[str] | None = None,
        LicenseInfo: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_function_code_signing_config(
        self,
        *,
        CodeSigningConfigArn: str,
        FunctionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_function_concurrency(
        self,
        *,
        FunctionName: str,
        ReservedConcurrentExecutions: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_function_event_invoke_config(
        self,
        *,
        FunctionName: str,
        Qualifier: str | None = None,
        MaximumRetryAttempts: int | None = None,
        MaximumEventAgeInSeconds: int | None = None,
        DestinationConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_function_recursion_config(
        self,
        *,
        FunctionName: str,
        RecursiveLoop: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_function_scaling_config(
        self,
        *,
        FunctionName: str,
        Qualifier: str,
        FunctionScalingConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_provisioned_concurrency_config(
        self,
        *,
        FunctionName: str,
        Qualifier: str,
        ProvisionedConcurrentExecutions: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_resource_policy(
        self,
        *,
        ResourceArn: str,
        Policy: str,
        RevisionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_runtime_management_config(
        self,
        *,
        FunctionName: str,
        UpdateRuntimeOn: str,
        Qualifier: str | None = None,
        RuntimeVersionArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_layer_version_permission(
        self,
        *,
        LayerName: str,
        VersionNumber: int,
        StatementId: str,
        RevisionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_permission(
        self,
        *,
        FunctionName: str,
        StatementId: str,
        Qualifier: str | None = None,
        RevisionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def resume_durable_execution(
        self,
        *,
        DurableExecutionArn: str,
        ClientToken: str | None = None,
        Reason: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_durable_execution_callback_failure(
        self,
        *,
        CallbackId: str,
        Error: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_durable_execution_callback_heartbeat(
        self,
        *,
        CallbackId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_durable_execution_callback_success(
        self,
        *,
        CallbackId: str,
        Result: bytes | BinaryIO | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_durable_execution(
        self,
        *,
        DurableExecutionArn: str,
        Error: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_capacity_provider(
        self,
        *,
        CapacityProviderName: str,
        CapacityProviderScalingConfig: dict[str, Any] | None = None,
        PropagateTags: dict[str, Any] | None = None,
        TelemetryConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_code_signing_config(
        self,
        *,
        CodeSigningConfigArn: str,
        Description: str | None = None,
        AllowedPublishers: dict[str, Any] | None = None,
        CodeSigningPolicies: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_event_source_mapping(
        self,
        *,
        UUID: str,
        FunctionName: str | None = None,
        Enabled: bool | None = None,
        BatchSize: int | None = None,
        FilterCriteria: dict[str, Any] | None = None,
        KMSKeyArn: str | None = None,
        MetricsConfig: dict[str, Any] | None = None,
        LoggingConfig: dict[str, Any] | None = None,
        ScalingConfig: dict[str, Any] | None = None,
        MaximumBatchingWindowInSeconds: int | None = None,
        ParallelizationFactor: int | None = None,
        DestinationConfig: dict[str, Any] | None = None,
        MaximumRecordAgeInSeconds: int | None = None,
        BisectBatchOnFunctionError: bool | None = None,
        MaximumRetryAttempts: int | None = None,
        TumblingWindowInSeconds: int | None = None,
        SourceAccessConfigurations: list[dict[str, Any]] | None = None,
        FunctionResponseTypes: list[str] | None = None,
        AmazonManagedKafkaEventSourceConfig: dict[str, Any] | None = None,
        SelfManagedKafkaEventSourceConfig: dict[str, Any] | None = None,
        DocumentDBEventSourceConfig: dict[str, Any] | None = None,
        ProvisionedPollerConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_function_event_invoke_config(
        self,
        *,
        FunctionName: str,
        Qualifier: str | None = None,
        MaximumRetryAttempts: int | None = None,
        MaximumEventAgeInSeconds: int | None = None,
        DestinationConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_function_url_config(
        self,
        *,
        FunctionName: str,
        Qualifier: str | None = None,
        AuthType: str | None = None,
        Cors: dict[str, Any] | None = None,
        InvokeMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
