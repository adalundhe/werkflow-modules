from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class SSMClient(ABC):

    @abstractmethod
    def add_tags_to_resource(
        self,
        *,
        ResourceType: str,
        ResourceId: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_ops_item_related_item(
        self,
        *,
        OpsItemId: str,
        AssociationType: str,
        ResourceType: str,
        ResourceUri: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_command(
        self,
        *,
        CommandId: str,
        InstanceIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_maintenance_window_execution(
        self,
        *,
        WindowExecutionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_activation(
        self,
        *,
        IamRole: str,
        Description: str | None = None,
        DefaultInstanceName: str | None = None,
        RegistrationLimit: int | None = None,
        ExpirationDate: datetime.datetime | str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        RegistrationMetadata: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_association(
        self,
        *,
        Name: str,
        DocumentVersion: str | None = None,
        InstanceId: str | None = None,
        Parameters: dict[str, list[str]] | None = None,
        Targets: list[dict[str, Any]] | None = None,
        ScheduleExpression: str | None = None,
        OutputLocation: dict[str, Any] | None = None,
        AssociationName: str | None = None,
        AutomationTargetParameterName: str | None = None,
        MaxErrors: str | None = None,
        MaxConcurrency: str | None = None,
        ComplianceSeverity: str | None = None,
        SyncCompliance: str | None = None,
        ApplyOnlyAtCronInterval: bool | None = None,
        CalendarNames: list[str] | None = None,
        TargetLocations: list[dict[str, Any]] | None = None,
        ScheduleOffset: int | None = None,
        Duration: int | None = None,
        TargetMaps: list[dict[str, list[Any]]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        AlarmConfiguration: dict[str, Any] | None = None,
        AssociationDispatchAssumeRole: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_association_batch(
        self,
        *,
        Entries: list[dict[str, Any]],
        AssociationDispatchAssumeRole: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cloud_connector(
        self,
        *,
        DisplayName: str,
        RoleArn: str,
        Configuration: dict[str, Any],
        Description: str | None = None,
        ConfigConnectorArn: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_document(
        self,
        *,
        Content: str,
        Name: str,
        Requires: list[dict[str, Any]] | None = None,
        Attachments: list[dict[str, Any]] | None = None,
        DisplayName: str | None = None,
        VersionName: str | None = None,
        DocumentType: str | None = None,
        DocumentFormat: str | None = None,
        TargetType: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        CloudProviders: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_maintenance_window(
        self,
        *,
        Name: str,
        Schedule: str,
        Duration: int,
        Cutoff: int,
        AllowUnassociatedTargets: bool,
        Description: str | None = None,
        StartDate: str | None = None,
        EndDate: str | None = None,
        ScheduleTimezone: str | None = None,
        ScheduleOffset: int | None = None,
        ClientToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ops_item(
        self,
        *,
        Description: str,
        Source: str,
        Title: str,
        OpsItemType: str | None = None,
        OperationalData: dict[str, dict[str, Any]] | None = None,
        Notifications: list[dict[str, Any]] | None = None,
        Priority: int | None = None,
        RelatedOpsItems: list[dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        Category: str | None = None,
        Severity: str | None = None,
        ActualStartTime: datetime.datetime | str | None = None,
        ActualEndTime: datetime.datetime | str | None = None,
        PlannedStartTime: datetime.datetime | str | None = None,
        PlannedEndTime: datetime.datetime | str | None = None,
        AccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ops_metadata(
        self,
        *,
        ResourceId: str,
        Metadata: dict[str, dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_patch_baseline(
        self,
        *,
        Name: str,
        OperatingSystem: str | None = None,
        GlobalFilters: dict[str, Any] | None = None,
        ApprovalRules: dict[str, Any] | None = None,
        ApprovedPatches: list[str] | None = None,
        ApprovedPatchesComplianceLevel: str | None = None,
        ApprovedPatchesEnableNonSecurity: bool | None = None,
        RejectedPatches: list[str] | None = None,
        RejectedPatchesAction: str | None = None,
        Description: str | None = None,
        Sources: list[dict[str, Any]] | None = None,
        AvailableSecurityUpdatesComplianceStatus: str | None = None,
        ClientToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_resource_data_sync(
        self,
        *,
        SyncName: str,
        S3Destination: dict[str, Any] | None = None,
        SyncType: str | None = None,
        SyncSource: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_activation(
        self,
        *,
        ActivationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_association(
        self,
        *,
        Name: str | None = None,
        InstanceId: str | None = None,
        AssociationId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cloud_connector(
        self,
        *,
        CloudConnectorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_document(
        self,
        *,
        Name: str,
        DocumentVersion: str | None = None,
        VersionName: str | None = None,
        Force: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_inventory(
        self,
        *,
        TypeName: str,
        SchemaDeleteOption: str | None = None,
        DryRun: bool | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_maintenance_window(
        self,
        *,
        WindowId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ops_item(
        self,
        *,
        OpsItemId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ops_metadata(
        self,
        *,
        OpsMetadataArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_parameter(
        self,
        *,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_parameters(
        self,
        *,
        Names: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_patch_baseline(
        self,
        *,
        BaselineId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_data_sync(
        self,
        *,
        SyncName: str,
        SyncType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_policy(
        self,
        *,
        ResourceArn: str,
        PolicyId: str,
        PolicyHash: str,
        DeletionMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_default_host_management_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_managed_instance(
        self,
        *,
        InstanceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_patch_baseline_for_patch_group(
        self,
        *,
        BaselineId: str,
        PatchGroup: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_target_from_maintenance_window(
        self,
        *,
        WindowId: str,
        WindowTargetId: str,
        Safe: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_task_from_maintenance_window(
        self,
        *,
        WindowId: str,
        WindowTaskId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_activations(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_association(
        self,
        *,
        Name: str | None = None,
        InstanceId: str | None = None,
        AssociationId: str | None = None,
        AssociationVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_association_execution_targets(
        self,
        *,
        AssociationId: str,
        ExecutionId: str,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_association_executions(
        self,
        *,
        AssociationId: str,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_automation_executions(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_automation_step_executions(
        self,
        *,
        AutomationExecutionId: str,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        ReverseOrder: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_available_patches(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_document(
        self,
        *,
        Name: str,
        DocumentVersion: str | None = None,
        VersionName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_document_permission(
        self,
        *,
        Name: str,
        PermissionType: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_effective_instance_associations(
        self,
        *,
        InstanceId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_effective_patches_for_patch_baseline(
        self,
        *,
        BaselineId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_associations_status(
        self,
        *,
        InstanceId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_information(
        self,
        *,
        InstanceInformationFilterList: list[dict[str, Any]] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_patch_states(
        self,
        *,
        InstanceIds: list[str],
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_patch_states_for_patch_group(
        self,
        *,
        PatchGroup: str,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_patches(
        self,
        *,
        InstanceId: str,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_properties(
        self,
        *,
        InstancePropertyFilterList: list[dict[str, Any]] | None = None,
        FiltersWithOperator: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_inventory_deletions(
        self,
        *,
        DeletionId: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_maintenance_window_execution_task_invocations(
        self,
        *,
        WindowExecutionId: str,
        TaskId: str,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_maintenance_window_execution_tasks(
        self,
        *,
        WindowExecutionId: str,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_maintenance_window_executions(
        self,
        *,
        WindowId: str,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_maintenance_window_schedule(
        self,
        *,
        WindowId: str | None = None,
        Targets: list[dict[str, Any]] | None = None,
        ResourceType: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_maintenance_window_targets(
        self,
        *,
        WindowId: str,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_maintenance_window_tasks(
        self,
        *,
        WindowId: str,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_maintenance_windows(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_maintenance_windows_for_target(
        self,
        *,
        Targets: list[dict[str, Any]],
        ResourceType: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ops_items(
        self,
        *,
        OpsItemFilters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_parameters(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        ParameterFilters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Shared: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_patch_baselines(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_patch_group_state(
        self,
        *,
        PatchGroup: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_patch_groups(
        self,
        *,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_patch_properties(
        self,
        *,
        OperatingSystem: str,
        Property: str,
        PatchSet: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_sessions(
        self,
        *,
        State: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_ops_item_related_item(
        self,
        *,
        OpsItemId: str,
        AssociationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_access_token(
        self,
        *,
        AccessRequestId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_automation_execution(
        self,
        *,
        AutomationExecutionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_calendar_state(
        self,
        *,
        CalendarNames: list[str],
        AtTime: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_cloud_connector(
        self,
        *,
        CloudConnectorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_command_invocation(
        self,
        *,
        CommandId: str,
        InstanceId: str,
        PluginName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_connection_status(
        self,
        *,
        Target: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_default_patch_baseline(
        self,
        *,
        OperatingSystem: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_deployable_patch_snapshot_for_instance(
        self,
        *,
        InstanceId: str,
        SnapshotId: str,
        BaselineOverride: dict[str, Any] | None = None,
        UseS3DualStackEndpoint: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_document(
        self,
        *,
        Name: str,
        VersionName: str | None = None,
        DocumentVersion: str | None = None,
        DocumentFormat: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_execution_preview(
        self,
        *,
        ExecutionPreviewId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_inventory(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        Aggregators: list[dict[str, Any]] | None = None,
        ResultAttributes: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_inventory_schema(
        self,
        *,
        TypeName: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Aggregator: bool | None = None,
        SubType: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_maintenance_window(
        self,
        *,
        WindowId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_maintenance_window_execution(
        self,
        *,
        WindowExecutionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_maintenance_window_execution_task(
        self,
        *,
        WindowExecutionId: str,
        TaskId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_maintenance_window_execution_task_invocation(
        self,
        *,
        WindowExecutionId: str,
        TaskId: str,
        InvocationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_maintenance_window_task(
        self,
        *,
        WindowId: str,
        WindowTaskId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ops_item(
        self,
        *,
        OpsItemId: str,
        OpsItemArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ops_metadata(
        self,
        *,
        OpsMetadataArn: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ops_summary(
        self,
        *,
        SyncName: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        Aggregators: list[dict[str, Any]] | None = None,
        ResultAttributes: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_parameter(
        self,
        *,
        Name: str,
        WithDecryption: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_parameter_history(
        self,
        *,
        Name: str,
        WithDecryption: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_parameters(
        self,
        *,
        Names: list[str],
        WithDecryption: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_parameters_by_path(
        self,
        *,
        Path: str,
        Recursive: bool | None = None,
        ParameterFilters: list[dict[str, Any]] | None = None,
        WithDecryption: bool | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_patch_baseline(
        self,
        *,
        BaselineId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_patch_baseline_for_patch_group(
        self,
        *,
        PatchGroup: str,
        OperatingSystem: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_resource_policies(
        self,
        *,
        ResourceArn: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_service_setting(
        self,
        *,
        SettingId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def label_parameter_version(
        self,
        *,
        Name: str,
        Labels: list[str],
        ParameterVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_association_versions(
        self,
        *,
        AssociationId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_associations(
        self,
        *,
        AssociationFilterList: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_cloud_connectors(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_command_invocations(
        self,
        *,
        CommandId: str | None = None,
        InstanceId: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        Details: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_commands(
        self,
        *,
        CommandId: str | None = None,
        InstanceId: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_compliance_items(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        ResourceIds: list[str] | None = None,
        ResourceTypes: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_compliance_summaries(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_document_metadata_history(
        self,
        *,
        Name: str,
        Metadata: str,
        DocumentVersion: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_document_versions(
        self,
        *,
        Name: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_documents(
        self,
        *,
        DocumentFilterList: list[dict[str, Any]] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_inventory_entries(
        self,
        *,
        InstanceId: str,
        TypeName: str,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_nodes(
        self,
        *,
        SyncName: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_nodes_summary(
        self,
        *,
        Aggregators: list[dict[str, Any]],
        SyncName: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_ops_item_events(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_ops_item_related_items(
        self,
        *,
        OpsItemId: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_ops_metadata(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resource_compliance_summaries(
        self,
        *,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resource_data_sync(
        self,
        *,
        SyncType: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceType: str,
        ResourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def modify_document_permission(
        self,
        *,
        Name: str,
        PermissionType: str,
        AccountIdsToAdd: list[str] | None = None,
        AccountIdsToRemove: list[str] | None = None,
        SharedDocumentVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_compliance_items(
        self,
        *,
        ResourceId: str,
        ResourceType: str,
        ComplianceType: str,
        ExecutionSummary: dict[str, Any],
        Items: list[dict[str, Any]],
        ItemContentHash: str | None = None,
        UploadType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_inventory(
        self,
        *,
        InstanceId: str,
        Items: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_parameter(
        self,
        *,
        Name: str,
        Value: str,
        Description: str | None = None,
        Type: str | None = None,
        KeyId: str | None = None,
        Overwrite: bool | None = None,
        AllowedPattern: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        Tier: str | None = None,
        Policies: str | None = None,
        DataType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_resource_policy(
        self,
        *,
        ResourceArn: str,
        Policy: str,
        PolicyId: str | None = None,
        PolicyHash: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_default_host_management_configuration(
        self,
        *,
        PermissionModel: str,
        RoleArn: str | None = None,
        Overwrite: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_default_patch_baseline(
        self,
        *,
        BaselineId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_patch_baseline_for_patch_group(
        self,
        *,
        BaselineId: str,
        PatchGroup: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_target_with_maintenance_window(
        self,
        *,
        WindowId: str,
        ResourceType: str,
        Targets: list[dict[str, Any]],
        OwnerInformation: str | None = None,
        Name: str | None = None,
        Description: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_task_with_maintenance_window(
        self,
        *,
        WindowId: str,
        TaskArn: str,
        TaskType: str,
        Targets: list[dict[str, Any]] | None = None,
        ServiceRoleArn: str | None = None,
        TaskParameters: dict[str, dict[str, Any]] | None = None,
        TaskInvocationParameters: dict[str, Any] | None = None,
        Priority: int | None = None,
        MaxConcurrency: str | None = None,
        MaxErrors: str | None = None,
        LoggingInfo: dict[str, Any] | None = None,
        Name: str | None = None,
        Description: str | None = None,
        ClientToken: str | None = None,
        CutoffBehavior: str | None = None,
        AlarmConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_tags_from_resource(
        self,
        *,
        ResourceType: str,
        ResourceId: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reset_service_setting(
        self,
        *,
        SettingId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def resume_session(
        self,
        *,
        SessionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_automation_signal(
        self,
        *,
        AutomationExecutionId: str,
        SignalType: str,
        Payload: dict[str, list[str]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_command(
        self,
        *,
        DocumentName: str,
        InstanceIds: list[str] | None = None,
        Targets: list[dict[str, Any]] | None = None,
        DocumentVersion: str | None = None,
        DocumentHash: str | None = None,
        DocumentHashType: str | None = None,
        TimeoutSeconds: int | None = None,
        Comment: str | None = None,
        Parameters: dict[str, list[str]] | None = None,
        OutputS3Region: str | None = None,
        OutputS3BucketName: str | None = None,
        OutputS3KeyPrefix: str | None = None,
        MaxConcurrency: str | None = None,
        MaxErrors: str | None = None,
        ServiceRoleArn: str | None = None,
        NotificationConfig: dict[str, Any] | None = None,
        CloudWatchOutputConfig: dict[str, Any] | None = None,
        AlarmConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_access_request(
        self,
        *,
        Reason: str,
        Targets: list[dict[str, Any]],
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_associations_once(
        self,
        *,
        AssociationIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_automation_execution(
        self,
        *,
        DocumentName: str,
        DocumentVersion: str | None = None,
        Parameters: dict[str, list[str]] | None = None,
        ClientToken: str | None = None,
        Mode: str | None = None,
        TargetParameterName: str | None = None,
        Targets: list[dict[str, Any]] | None = None,
        TargetMaps: list[dict[str, list[Any]]] | None = None,
        MaxConcurrency: str | None = None,
        MaxErrors: str | None = None,
        TargetLocations: list[dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        AlarmConfiguration: dict[str, Any] | None = None,
        TargetLocationsURL: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_change_request_execution(
        self,
        *,
        DocumentName: str,
        Runbooks: list[dict[str, Any]],
        ScheduledTime: datetime.datetime | str | None = None,
        DocumentVersion: str | None = None,
        Parameters: dict[str, list[str]] | None = None,
        ChangeRequestName: str | None = None,
        ClientToken: str | None = None,
        AutoApprove: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ScheduledEndTime: datetime.datetime | str | None = None,
        ChangeDetails: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_execution_preview(
        self,
        *,
        DocumentName: str,
        DocumentVersion: str | None = None,
        ExecutionInputs: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_session(
        self,
        *,
        Target: str,
        DocumentName: str | None = None,
        Reason: str | None = None,
        Parameters: dict[str, list[str]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_automation_execution(
        self,
        *,
        AutomationExecutionId: str,
        Type: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def terminate_session(
        self,
        *,
        SessionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def unlabel_parameter_version(
        self,
        *,
        Name: str,
        ParameterVersion: int,
        Labels: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_association(
        self,
        *,
        AssociationId: str,
        Parameters: dict[str, list[str]] | None = None,
        DocumentVersion: str | None = None,
        ScheduleExpression: str | None = None,
        OutputLocation: dict[str, Any] | None = None,
        Name: str | None = None,
        Targets: list[dict[str, Any]] | None = None,
        AssociationName: str | None = None,
        AssociationVersion: str | None = None,
        AutomationTargetParameterName: str | None = None,
        MaxErrors: str | None = None,
        MaxConcurrency: str | None = None,
        ComplianceSeverity: str | None = None,
        SyncCompliance: str | None = None,
        ApplyOnlyAtCronInterval: bool | None = None,
        CalendarNames: list[str] | None = None,
        TargetLocations: list[dict[str, Any]] | None = None,
        ScheduleOffset: int | None = None,
        Duration: int | None = None,
        TargetMaps: list[dict[str, list[Any]]] | None = None,
        AlarmConfiguration: dict[str, Any] | None = None,
        AssociationDispatchAssumeRole: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_association_status(
        self,
        *,
        Name: str,
        InstanceId: str,
        AssociationStatus: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_cloud_connector(
        self,
        *,
        CloudConnectorId: str,
        DisplayName: str | None = None,
        Configuration: dict[str, Any] | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_document(
        self,
        *,
        Content: str,
        Name: str,
        Attachments: list[dict[str, Any]] | None = None,
        DisplayName: str | None = None,
        VersionName: str | None = None,
        DocumentVersion: str | None = None,
        DocumentFormat: str | None = None,
        TargetType: str | None = None,
        CloudProviders: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_document_default_version(
        self,
        *,
        Name: str,
        DocumentVersion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_document_metadata(
        self,
        *,
        Name: str,
        DocumentReviews: dict[str, Any],
        DocumentVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_maintenance_window(
        self,
        *,
        WindowId: str,
        Name: str | None = None,
        Description: str | None = None,
        StartDate: str | None = None,
        EndDate: str | None = None,
        Schedule: str | None = None,
        ScheduleTimezone: str | None = None,
        ScheduleOffset: int | None = None,
        Duration: int | None = None,
        Cutoff: int | None = None,
        AllowUnassociatedTargets: bool | None = None,
        Enabled: bool | None = None,
        Replace: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_maintenance_window_target(
        self,
        *,
        WindowId: str,
        WindowTargetId: str,
        Targets: list[dict[str, Any]] | None = None,
        OwnerInformation: str | None = None,
        Name: str | None = None,
        Description: str | None = None,
        Replace: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_maintenance_window_task(
        self,
        *,
        WindowId: str,
        WindowTaskId: str,
        Targets: list[dict[str, Any]] | None = None,
        TaskArn: str | None = None,
        ServiceRoleArn: str | None = None,
        TaskParameters: dict[str, dict[str, Any]] | None = None,
        TaskInvocationParameters: dict[str, Any] | None = None,
        Priority: int | None = None,
        MaxConcurrency: str | None = None,
        MaxErrors: str | None = None,
        LoggingInfo: dict[str, Any] | None = None,
        Name: str | None = None,
        Description: str | None = None,
        Replace: bool | None = None,
        CutoffBehavior: str | None = None,
        AlarmConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_managed_instance_role(
        self,
        *,
        InstanceId: str,
        IamRole: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_ops_item(
        self,
        *,
        OpsItemId: str,
        Description: str | None = None,
        OperationalData: dict[str, dict[str, Any]] | None = None,
        OperationalDataToDelete: list[str] | None = None,
        Notifications: list[dict[str, Any]] | None = None,
        Priority: int | None = None,
        RelatedOpsItems: list[dict[str, Any]] | None = None,
        Status: str | None = None,
        Title: str | None = None,
        Category: str | None = None,
        Severity: str | None = None,
        ActualStartTime: datetime.datetime | str | None = None,
        ActualEndTime: datetime.datetime | str | None = None,
        PlannedStartTime: datetime.datetime | str | None = None,
        PlannedEndTime: datetime.datetime | str | None = None,
        OpsItemArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_ops_metadata(
        self,
        *,
        OpsMetadataArn: str,
        MetadataToUpdate: dict[str, dict[str, Any]] | None = None,
        KeysToDelete: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_patch_baseline(
        self,
        *,
        BaselineId: str,
        Name: str | None = None,
        GlobalFilters: dict[str, Any] | None = None,
        ApprovalRules: dict[str, Any] | None = None,
        ApprovedPatches: list[str] | None = None,
        ApprovedPatchesComplianceLevel: str | None = None,
        ApprovedPatchesEnableNonSecurity: bool | None = None,
        RejectedPatches: list[str] | None = None,
        RejectedPatchesAction: str | None = None,
        Description: str | None = None,
        Sources: list[dict[str, Any]] | None = None,
        AvailableSecurityUpdatesComplianceStatus: str | None = None,
        Replace: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_resource_data_sync(
        self,
        *,
        SyncName: str,
        SyncType: str,
        SyncSource: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_service_setting(
        self,
        *,
        SettingId: str,
        SettingValue: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def validate_cloud_connector(
        self,
        *,
        CloudConnectorId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
