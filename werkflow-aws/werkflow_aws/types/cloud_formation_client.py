from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class CloudFormationClient(ABC):

    @abstractmethod
    def activate_organizations_access(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def activate_type(
        self,
        *,
        Type: str | None = None,
        PublicTypeArn: str | None = None,
        PublisherId: str | None = None,
        TypeName: str | None = None,
        TypeNameAlias: str | None = None,
        AutoUpdate: bool | None = None,
        LoggingConfig: dict[str, Any] | None = None,
        ExecutionRoleArn: str | None = None,
        VersionBump: str | None = None,
        MajorVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_describe_type_configurations(
        self,
        *,
        TypeConfigurationIdentifiers: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_update_stack(
        self,
        *,
        StackName: str,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def continue_update_rollback(
        self,
        *,
        StackName: str,
        RoleARN: str | None = None,
        ResourcesToSkip: list[str] | None = None,
        ClientRequestToken: str | None = None,
        ForceRollback: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_change_set(
        self,
        *,
        StackName: str,
        ChangeSetName: str,
        TemplateBody: str | None = None,
        TemplateURL: str | None = None,
        UsePreviousTemplate: bool | None = None,
        Parameters: list[dict[str, Any]] | None = None,
        Capabilities: list[str] | None = None,
        ResourceTypes: list[str] | None = None,
        RoleARN: str | None = None,
        RollbackConfiguration: dict[str, Any] | None = None,
        NotificationARNs: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
        Description: str | None = None,
        ChangeSetType: str | None = None,
        ResourcesToImport: list[dict[str, Any]] | None = None,
        IncludeNestedStacks: bool | None = None,
        OnStackFailure: str | None = None,
        ImportExistingResources: bool | None = None,
        DeploymentMode: str | None = None,
        DeploymentConfig: dict[str, Any] | None = None,
        DisableValidation: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_generated_template(
        self,
        *,
        GeneratedTemplateName: str,
        Resources: list[dict[str, Any]] | None = None,
        StackName: str | None = None,
        TemplateConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_stack(
        self,
        *,
        StackName: str,
        TemplateBody: str | None = None,
        TemplateURL: str | None = None,
        Parameters: list[dict[str, Any]] | None = None,
        DisableRollback: bool | None = None,
        RollbackConfiguration: dict[str, Any] | None = None,
        TimeoutInMinutes: int | None = None,
        NotificationARNs: list[str] | None = None,
        Capabilities: list[str] | None = None,
        ResourceTypes: list[str] | None = None,
        RoleARN: str | None = None,
        OnFailure: str | None = None,
        StackPolicyBody: str | None = None,
        StackPolicyURL: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ClientRequestToken: str | None = None,
        EnableTerminationProtection: bool | None = None,
        RetainExceptOnCreate: bool | None = None,
        DeploymentConfig: dict[str, Any] | None = None,
        DisableValidation: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_stack_instances(
        self,
        *,
        StackSetName: str,
        Regions: list[str],
        Accounts: list[str] | None = None,
        DeploymentTargets: dict[str, Any] | None = None,
        ParameterOverrides: list[dict[str, Any]] | None = None,
        OperationPreferences: dict[str, Any] | None = None,
        OperationId: str | None = None,
        CallAs: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_stack_refactor(
        self,
        *,
        StackDefinitions: list[dict[str, Any]],
        Description: str | None = None,
        EnableStackCreation: bool | None = None,
        ResourceMappings: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_stack_set(
        self,
        *,
        StackSetName: str,
        Description: str | None = None,
        TemplateBody: str | None = None,
        TemplateURL: str | None = None,
        StackId: str | None = None,
        Parameters: list[dict[str, Any]] | None = None,
        Capabilities: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        AdministrationRoleARN: str | None = None,
        ExecutionRoleName: str | None = None,
        PermissionModel: str | None = None,
        AutoDeployment: dict[str, Any] | None = None,
        CallAs: str | None = None,
        ClientRequestToken: str | None = None,
        ManagedExecution: dict[str, Any] | None = None,
        ExecutionRoleTemplateBody: str | None = None,
        ExecutionRoleTemplateUrl: str | None = None,
        StackSetOutputBucket: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deactivate_organizations_access(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def deactivate_type(
        self,
        *,
        TypeName: str | None = None,
        Type: str | None = None,
        Arn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_change_set(
        self,
        *,
        ChangeSetName: str,
        StackName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_generated_template(
        self,
        *,
        GeneratedTemplateName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_stack(
        self,
        *,
        StackName: str,
        RetainResources: list[str] | None = None,
        RoleARN: str | None = None,
        ClientRequestToken: str | None = None,
        DeletionMode: str | None = None,
        DeploymentConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_stack_instances(
        self,
        *,
        StackSetName: str,
        Regions: list[str],
        RetainStacks: bool,
        Accounts: list[str] | None = None,
        DeploymentTargets: dict[str, Any] | None = None,
        OperationPreferences: dict[str, Any] | None = None,
        OperationId: str | None = None,
        CallAs: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_stack_set(
        self,
        *,
        StackSetName: str,
        CallAs: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_type(
        self,
        *,
        Arn: str | None = None,
        Type: str | None = None,
        TypeName: str | None = None,
        VersionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_limits(
        self,
        *,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_change_set(
        self,
        *,
        ChangeSetName: str,
        StackName: str | None = None,
        NextToken: str | None = None,
        IncludePropertyValues: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_change_set_hooks(
        self,
        *,
        ChangeSetName: str,
        StackName: str | None = None,
        NextToken: str | None = None,
        LogicalResourceId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_events(
        self,
        *,
        StackName: str | None = None,
        ChangeSetName: str | None = None,
        OperationId: str | None = None,
        Filters: dict[str, Any] | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_generated_template(
        self,
        *,
        GeneratedTemplateName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_organizations_access(
        self,
        *,
        CallAs: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_publisher(
        self,
        *,
        PublisherId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_resource_scan(
        self,
        *,
        ResourceScanId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_stack_drift_detection_status(
        self,
        *,
        StackDriftDetectionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_stack_events(
        self,
        *,
        StackName: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_stack_instance(
        self,
        *,
        StackSetName: str,
        StackInstanceAccount: str,
        StackInstanceRegion: str,
        CallAs: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_stack_refactor(
        self,
        *,
        StackRefactorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_stack_resource(
        self,
        *,
        StackName: str,
        LogicalResourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_stack_resource_drifts(
        self,
        *,
        StackName: str,
        StackResourceDriftStatusFilters: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_stack_resources(
        self,
        *,
        StackName: str | None = None,
        LogicalResourceId: str | None = None,
        PhysicalResourceId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_stack_set(
        self,
        *,
        StackSetName: str,
        CallAs: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_stack_set_operation(
        self,
        *,
        StackSetName: str,
        OperationId: str,
        CallAs: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_stacks(
        self,
        *,
        StackName: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_type(
        self,
        *,
        Type: str | None = None,
        TypeName: str | None = None,
        Arn: str | None = None,
        VersionId: str | None = None,
        PublisherId: str | None = None,
        PublicVersionNumber: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_type_registration(
        self,
        *,
        RegistrationToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detect_stack_drift(
        self,
        *,
        StackName: str,
        LogicalResourceIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detect_stack_resource_drift(
        self,
        *,
        StackName: str,
        LogicalResourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detect_stack_set_drift(
        self,
        *,
        StackSetName: str,
        OperationPreferences: dict[str, Any] | None = None,
        OperationId: str | None = None,
        CallAs: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def estimate_template_cost(
        self,
        *,
        TemplateBody: str | None = None,
        TemplateURL: str | None = None,
        Parameters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def execute_change_set(
        self,
        *,
        ChangeSetName: str,
        StackName: str | None = None,
        ClientRequestToken: str | None = None,
        DisableRollback: bool | None = None,
        RetainExceptOnCreate: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def execute_stack_refactor(
        self,
        *,
        StackRefactorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_generated_template(
        self,
        *,
        GeneratedTemplateName: str,
        Format: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_hook_result(
        self,
        *,
        HookResultId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_stack_policy(
        self,
        *,
        StackName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_template(
        self,
        *,
        StackName: str | None = None,
        ChangeSetName: str | None = None,
        TemplateStage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_template_summary(
        self,
        *,
        TemplateBody: str | None = None,
        TemplateURL: str | None = None,
        StackName: str | None = None,
        StackSetName: str | None = None,
        CallAs: str | None = None,
        TemplateSummaryConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_stacks_to_stack_set(
        self,
        *,
        StackSetName: str,
        StackIds: list[str] | None = None,
        StackIdsUrl: str | None = None,
        OrganizationalUnitIds: list[str] | None = None,
        OperationPreferences: dict[str, Any] | None = None,
        OperationId: str | None = None,
        CallAs: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_change_sets(
        self,
        *,
        StackName: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_exports(
        self,
        *,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_generated_templates(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_hook_results(
        self,
        *,
        TargetType: str | None = None,
        TargetId: str | None = None,
        TypeArn: str | None = None,
        Status: str | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_imports(
        self,
        *,
        ExportName: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resource_scan_related_resources(
        self,
        *,
        ResourceScanId: str,
        Resources: list[dict[str, Any]],
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resource_scan_resources(
        self,
        *,
        ResourceScanId: str,
        ResourceIdentifier: str | None = None,
        ResourceTypePrefix: str | None = None,
        TagKey: str | None = None,
        TagValue: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resource_scans(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        ScanTypeFilter: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_stack_instance_resource_drifts(
        self,
        *,
        StackSetName: str,
        StackInstanceAccount: str,
        StackInstanceRegion: str,
        OperationId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        StackInstanceResourceDriftStatuses: list[str] | None = None,
        CallAs: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_stack_instances(
        self,
        *,
        StackSetName: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
        StackInstanceAccount: str | None = None,
        StackInstanceRegion: str | None = None,
        CallAs: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_stack_refactor_actions(
        self,
        *,
        StackRefactorId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_stack_refactors(
        self,
        *,
        ExecutionStatusFilter: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_stack_resources(
        self,
        *,
        StackName: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_stack_set_auto_deployment_targets(
        self,
        *,
        StackSetName: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        CallAs: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_stack_set_operation_results(
        self,
        *,
        StackSetName: str,
        OperationId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        CallAs: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_stack_set_operations(
        self,
        *,
        StackSetName: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        CallAs: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_stack_sets(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Status: str | None = None,
        CallAs: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_stacks(
        self,
        *,
        NextToken: str | None = None,
        StackStatusFilter: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_type_registrations(
        self,
        *,
        Type: str | None = None,
        TypeName: str | None = None,
        TypeArn: str | None = None,
        RegistrationStatusFilter: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_type_versions(
        self,
        *,
        Type: str | None = None,
        TypeName: str | None = None,
        Arn: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        DeprecatedStatus: str | None = None,
        PublisherId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_types(
        self,
        *,
        Visibility: str | None = None,
        ProvisioningType: str | None = None,
        DeprecatedStatus: str | None = None,
        Type: str | None = None,
        Filters: dict[str, Any] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def publish_type(
        self,
        *,
        Type: str | None = None,
        Arn: str | None = None,
        TypeName: str | None = None,
        PublicVersionNumber: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def record_handler_progress(
        self,
        *,
        BearerToken: str,
        OperationStatus: str,
        CurrentOperationStatus: str | None = None,
        StatusMessage: str | None = None,
        ErrorCode: str | None = None,
        ResourceModel: str | None = None,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_publisher(
        self,
        *,
        AcceptTermsAndConditions: bool | None = None,
        ConnectionArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_type(
        self,
        *,
        TypeName: str,
        SchemaHandlerPackage: str,
        Type: str | None = None,
        LoggingConfig: dict[str, Any] | None = None,
        ExecutionRoleArn: str | None = None,
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_alias(
        self,
        *,
        AliasName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def rollback_stack(
        self,
        *,
        StackName: str,
        RoleARN: str | None = None,
        ClientRequestToken: str | None = None,
        RetainExceptOnCreate: bool | None = None,
        DeploymentConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_alias(
        self,
        *,
        StackName: str,
        AliasName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_stack_policy(
        self,
        *,
        StackName: str,
        StackPolicyBody: str | None = None,
        StackPolicyURL: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_type_configuration(
        self,
        *,
        Configuration: str,
        TypeArn: str | None = None,
        ConfigurationAlias: str | None = None,
        TypeName: str | None = None,
        Type: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_type_default_version(
        self,
        *,
        Arn: str | None = None,
        Type: str | None = None,
        TypeName: str | None = None,
        VersionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def signal_resource(
        self,
        *,
        StackName: str,
        LogicalResourceId: str,
        UniqueId: str,
        Status: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_resource_scan(
        self,
        *,
        ClientRequestToken: str | None = None,
        ScanFilters: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_stack_set_operation(
        self,
        *,
        StackSetName: str,
        OperationId: str,
        CallAs: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def test_type(
        self,
        *,
        Arn: str | None = None,
        Type: str | None = None,
        TypeName: str | None = None,
        VersionId: str | None = None,
        LogDeliveryBucket: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_generated_template(
        self,
        *,
        GeneratedTemplateName: str,
        NewGeneratedTemplateName: str | None = None,
        AddResources: list[dict[str, Any]] | None = None,
        RemoveResources: list[str] | None = None,
        RefreshAllResources: bool | None = None,
        TemplateConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_stack(
        self,
        *,
        StackName: str,
        TemplateBody: str | None = None,
        TemplateURL: str | None = None,
        UsePreviousTemplate: bool | None = None,
        StackPolicyDuringUpdateBody: str | None = None,
        StackPolicyDuringUpdateURL: str | None = None,
        Parameters: list[dict[str, Any]] | None = None,
        Capabilities: list[str] | None = None,
        ResourceTypes: list[str] | None = None,
        RoleARN: str | None = None,
        RollbackConfiguration: dict[str, Any] | None = None,
        StackPolicyBody: str | None = None,
        StackPolicyURL: str | None = None,
        NotificationARNs: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        DisableRollback: bool | None = None,
        ClientRequestToken: str | None = None,
        RetainExceptOnCreate: bool | None = None,
        DeploymentConfig: dict[str, Any] | None = None,
        DisableValidation: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_stack_instances(
        self,
        *,
        StackSetName: str,
        Regions: list[str],
        Accounts: list[str] | None = None,
        DeploymentTargets: dict[str, Any] | None = None,
        ParameterOverrides: list[dict[str, Any]] | None = None,
        OperationPreferences: dict[str, Any] | None = None,
        OperationId: str | None = None,
        CallAs: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_stack_set(
        self,
        *,
        StackSetName: str,
        Description: str | None = None,
        TemplateBody: str | None = None,
        TemplateURL: str | None = None,
        UsePreviousTemplate: bool | None = None,
        Parameters: list[dict[str, Any]] | None = None,
        Capabilities: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        OperationPreferences: dict[str, Any] | None = None,
        AdministrationRoleARN: str | None = None,
        ExecutionRoleName: str | None = None,
        DeploymentTargets: dict[str, Any] | None = None,
        PermissionModel: str | None = None,
        AutoDeployment: dict[str, Any] | None = None,
        OperationId: str | None = None,
        Accounts: list[str] | None = None,
        Regions: list[str] | None = None,
        CallAs: str | None = None,
        ManagedExecution: dict[str, Any] | None = None,
        ExecutionRoleTemplateBody: str | None = None,
        ExecutionRoleTemplateUrl: str | None = None,
        UseAdminExecutionRole: bool | None = None,
        StackSetOutputBucket: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_termination_protection(
        self,
        *,
        EnableTerminationProtection: bool,
        StackName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def validate_template(
        self,
        *,
        TemplateBody: str | None = None,
        TemplateURL: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
