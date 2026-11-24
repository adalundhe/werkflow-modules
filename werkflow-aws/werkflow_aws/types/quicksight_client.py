from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class QuickSightClient(ABC):

    @abstractmethod
    def batch_create_topic_reviewed_answer(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
        Answers: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_knowledge_base(
        self,
        *,
        AwsAccountId: str,
        KnowledgeBaseIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_policy_assignment_by_policy(
        self,
        *,
        AccountId: str,
        PolicyArn: str,
        PrincipalArns: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_topic_reviewed_answer(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
        AnswerIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_describe_user_limits(
        self,
        *,
        accountId: str,
        users: list[dict[str, Any]] | None = None,
        resourceTypes: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_put_policy_assignment_by_policy(
        self,
        *,
        AccountId: str,
        PolicyArn: str,
        Assignments: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_ingestion(
        self,
        *,
        AwsAccountId: str,
        DataSetId: str,
        IngestionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_access_control_application(
        self,
        *,
        AwsAccountId: str,
        ApplicationId: str,
        Name: str,
        Namespace: str,
        AuthenticationType: str,
        IdpAuthorizingConfiguration: dict[str, Any],
        QuickAuthenticationConfiguration: dict[str, Any],
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_access_control_application_secret(
        self,
        *,
        AwsAccountId: str,
        ApplicationId: str,
        ClientSecretConfiguration: dict[str, Any],
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_account_customization(
        self,
        *,
        AwsAccountId: str,
        AccountCustomization: dict[str, Any],
        Namespace: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_account_subscription(
        self,
        *,
        AuthenticationMethod: str,
        AwsAccountId: str,
        AccountName: str,
        NotificationEmail: str,
        Edition: str | None = None,
        ActiveDirectoryName: str | None = None,
        Realm: str | None = None,
        DirectoryId: str | None = None,
        AdminGroup: list[str] | None = None,
        AuthorGroup: list[str] | None = None,
        ReaderGroup: list[str] | None = None,
        AdminProGroup: list[str] | None = None,
        AuthorProGroup: list[str] | None = None,
        ReaderProGroup: list[str] | None = None,
        FirstName: str | None = None,
        LastName: str | None = None,
        EmailAddress: str | None = None,
        ContactNumber: str | None = None,
        IAMIdentityCenterInstanceArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_action_connector(
        self,
        *,
        AwsAccountId: str,
        ActionConnectorId: str,
        Name: str,
        Type: str,
        AuthenticationConfig: dict[str, Any],
        Description: str | None = None,
        Permissions: list[dict[str, Any]] | None = None,
        VpcConnectionArn: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_agent(
        self,
        *,
        AwsAccountId: str,
        AgentId: str,
        Name: str,
        Spaces: list[str] | None = None,
        ActionConnectors: list[str] | None = None,
        Description: str | None = None,
        IconId: str | None = None,
        StarterPrompts: list[str] | None = None,
        WelcomeMessage: str | None = None,
        AgentLifecycle: str | None = None,
        CustomPromptInput: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_analysis(
        self,
        *,
        AwsAccountId: str,
        AnalysisId: str,
        Name: str,
        Parameters: dict[str, Any] | None = None,
        Permissions: list[dict[str, Any]] | None = None,
        SourceEntity: dict[str, Any] | None = None,
        ThemeArn: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        Definition: dict[str, Any] | None = None,
        ValidationStrategy: dict[str, Any] | None = None,
        FolderArns: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_approval_policy(
        self,
        *,
        PolicyId: str,
        Name: str,
        Actions: list[str],
        AssetTypes: list[str],
        ApplicableTo: dict[str, Any],
        ApprovalGroups: list[str],
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_brand(
        self,
        *,
        AwsAccountId: str,
        BrandId: str,
        BrandDefinition: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_custom_permissions(
        self,
        *,
        AwsAccountId: str,
        CustomPermissionsName: str,
        Capabilities: dict[str, Any] | None = None,
        Governance: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_dashboard(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        Name: str,
        Parameters: dict[str, Any] | None = None,
        Permissions: list[dict[str, Any]] | None = None,
        SourceEntity: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        VersionDescription: str | None = None,
        DashboardPublishOptions: dict[str, Any] | None = None,
        ThemeArn: str | None = None,
        Definition: dict[str, Any] | None = None,
        ValidationStrategy: dict[str, Any] | None = None,
        FolderArns: list[str] | None = None,
        LinkSharingConfiguration: dict[str, Any] | None = None,
        LinkEntities: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_set(
        self,
        *,
        AwsAccountId: str,
        DataSetId: str,
        Name: str,
        PhysicalTableMap: dict[str, dict[str, Any]],
        ImportMode: str,
        LogicalTableMap: dict[str, dict[str, Any]] | None = None,
        ColumnGroups: list[dict[str, Any]] | None = None,
        FieldFolders: dict[str, dict[str, Any]] | None = None,
        Permissions: list[dict[str, Any]] | None = None,
        RowLevelPermissionDataSet: dict[str, Any] | None = None,
        RowLevelPermissionTagConfiguration: dict[str, Any] | None = None,
        ColumnLevelPermissionRules: list[dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        DataSetUsageConfiguration: dict[str, Any] | None = None,
        DatasetParameters: list[dict[str, Any]] | None = None,
        FolderArns: list[str] | None = None,
        PerformanceConfiguration: dict[str, Any] | None = None,
        UseAs: str | None = None,
        DataPrepConfiguration: dict[str, Any] | None = None,
        SemanticModelConfiguration: dict[str, Any] | None = None,
        UnmaterializedCalculatedColumns: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_source(
        self,
        *,
        AwsAccountId: str,
        DataSourceId: str,
        Name: str,
        Type: str,
        DataSourceParameters: dict[str, Any] | None = None,
        Credentials: dict[str, Any] | None = None,
        Permissions: list[dict[str, Any]] | None = None,
        VpcConnectionProperties: dict[str, Any] | None = None,
        SslProperties: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        FolderArns: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_dlp_setting(
        self,
        *,
        AwsAccountId: str,
        DlpSettingId: str,
        Name: str,
        ProviderType: str,
        ProviderConfig: dict[str, Any],
        ProviderOutageAction: str,
        Enabled: bool,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_flow(
        self,
        *,
        AwsAccountId: str,
        Name: str,
        FlowDefinition: dict[str, Any],
        Description: str | None = None,
        Permissions: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_folder(
        self,
        *,
        AwsAccountId: str,
        FolderId: str,
        Name: str | None = None,
        FolderType: str | None = None,
        ParentFolderArn: str | None = None,
        Permissions: list[dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        SharingModel: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_folder_membership(
        self,
        *,
        AwsAccountId: str,
        FolderId: str,
        MemberId: str,
        MemberType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_group(
        self,
        *,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_group_membership(
        self,
        *,
        MemberName: str,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_iam_policy_assignment(
        self,
        *,
        AwsAccountId: str,
        AssignmentName: str,
        AssignmentStatus: str,
        Namespace: str,
        PolicyArn: str | None = None,
        Identities: dict[str, list[str]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_inbound_connector(
        self,
        *,
        AwsAccountId: str,
        InboundConnectorId: str,
        Name: str,
        InboundConnectorConfiguration: dict[str, Any],
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_ingestion(
        self,
        *,
        DataSetId: str,
        IngestionId: str,
        AwsAccountId: str,
        IngestionType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_knowledge_base(
        self,
        *,
        AwsAccountId: str,
        KnowledgeBaseId: str,
        Name: str,
        DataSourceArn: str,
        KnowledgeBaseConfiguration: dict[str, Any],
        Description: str | None = None,
        Permissions: list[dict[str, Any]] | None = None,
        MediaExtractionConfiguration: dict[str, Any] | None = None,
        AccessControlConfiguration: dict[str, Any] | None = None,
        PrimaryOwnerArn: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_knowledge_base_refresh_schedule(
        self,
        *,
        AwsAccountId: str,
        KnowledgeBaseId: str,
        ScheduleId: str,
        ScheduleFrequency: dict[str, Any],
        StartTime: datetime.datetime | str | None = None,
        State: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_limits_profile(
        self,
        *,
        accountId: str,
        profileName: str,
        resourceLimits: dict[str, dict[str, Any]],
        clientToken: str,
        description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_namespace(
        self,
        *,
        AwsAccountId: str,
        Namespace: str,
        IdentityStore: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_o_auth_client_application(
        self,
        *,
        AwsAccountId: str,
        OAuthClientApplicationId: str,
        Name: str,
        OAuthClientAuthenticationType: str,
        ClientId: str,
        ClientSecret: str,
        OAuthTokenEndpointUrl: str,
        OAuthAuthorizationEndpointUrl: str | None = None,
        OAuthScopes: str | None = None,
        DataSourceType: str | None = None,
        IdentityProviderVpcConnectionProperties: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_refresh_schedule(
        self,
        *,
        DataSetId: str,
        AwsAccountId: str,
        Schedule: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_role_membership(
        self,
        *,
        MemberName: str,
        AwsAccountId: str,
        Namespace: str,
        Role: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_space(
        self,
        *,
        AwsAccountId: str,
        SpaceId: str,
        Name: str,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_template(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        Name: str | None = None,
        Permissions: list[dict[str, Any]] | None = None,
        SourceEntity: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        VersionDescription: str | None = None,
        Definition: dict[str, Any] | None = None,
        ValidationStrategy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_template_alias(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        AliasName: str,
        TemplateVersionNumber: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_theme(
        self,
        *,
        AwsAccountId: str,
        ThemeId: str,
        Name: str,
        BaseThemeId: str,
        Configuration: dict[str, Any],
        VersionDescription: str | None = None,
        Permissions: list[dict[str, Any]] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_theme_alias(
        self,
        *,
        AwsAccountId: str,
        ThemeId: str,
        AliasName: str,
        ThemeVersionNumber: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_topic(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
        Topic: dict[str, Any],
        Tags: list[dict[str, Any]] | None = None,
        FolderArns: list[str] | None = None,
        CustomInstructions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_topic_refresh_schedule(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
        DatasetArn: str,
        RefreshSchedule: dict[str, Any],
        DatasetName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_topic_v2(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
        Topic: dict[str, Any],
        Tags: list[dict[str, Any]] | None = None,
        FolderArns: list[str] | None = None,
        CustomInstructions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vpc_connection(
        self,
        *,
        AwsAccountId: str,
        VPCConnectionId: str,
        Name: str,
        SubnetIds: list[str],
        SecurityGroupIds: list[str],
        RoleArn: str,
        DnsResolvers: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_access_control_application(
        self,
        *,
        AwsAccountId: str,
        ApplicationId: str | None = None,
        IdcApplicationArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_access_control_application_secret(
        self,
        *,
        AwsAccountId: str,
        ApplicationId: str,
        ClientSecretId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_account_custom_permission(
        self,
        *,
        AwsAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_account_customization(
        self,
        *,
        AwsAccountId: str,
        Namespace: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_account_subscription(
        self,
        *,
        AwsAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_action_connector(
        self,
        *,
        AwsAccountId: str,
        ActionConnectorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_agent(
        self,
        *,
        AgentId: str,
        AwsAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_analysis(
        self,
        *,
        AwsAccountId: str,
        AnalysisId: str,
        RecoveryWindowInDays: int | None = None,
        ForceDeleteWithoutRecovery: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_app(
        self,
        *,
        AwsAccountId: str,
        AppId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_approval_policy(
        self,
        *,
        PolicyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_brand(
        self,
        *,
        AwsAccountId: str,
        BrandId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_brand_assignment(
        self,
        *,
        AwsAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_custom_permissions(
        self,
        *,
        AwsAccountId: str,
        CustomPermissionsName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_dashboard(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        VersionNumber: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_set(
        self,
        *,
        AwsAccountId: str,
        DataSetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_set_refresh_properties(
        self,
        *,
        AwsAccountId: str,
        DataSetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_source(
        self,
        *,
        AwsAccountId: str,
        DataSourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_default_q_business_application(
        self,
        *,
        AwsAccountId: str,
        Namespace: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_dlp_setting(
        self,
        *,
        AwsAccountId: str,
        DlpSettingId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_flow(
        self,
        *,
        AwsAccountId: str,
        FlowId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_folder(
        self,
        *,
        AwsAccountId: str,
        FolderId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_folder_membership(
        self,
        *,
        AwsAccountId: str,
        FolderId: str,
        MemberId: str,
        MemberType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_group(
        self,
        *,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_group_membership(
        self,
        *,
        MemberName: str,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_iam_policy_assignment(
        self,
        *,
        AwsAccountId: str,
        AssignmentName: str,
        Namespace: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_identity_propagation_config(
        self,
        *,
        AwsAccountId: str,
        Service: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_inbound_connector(
        self,
        *,
        AwsAccountId: str,
        InboundConnectorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_knowledge_base(
        self,
        *,
        AwsAccountId: str,
        KnowledgeBaseId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_knowledge_base_refresh_schedule(
        self,
        *,
        AwsAccountId: str,
        KnowledgeBaseId: str,
        ScheduleId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_limits_profile(
        self,
        *,
        profileId: str,
        accountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_namespace(
        self,
        *,
        AwsAccountId: str,
        Namespace: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_o_auth_client_application(
        self,
        *,
        AwsAccountId: str,
        OAuthClientApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_policy_assignment(
        self,
        *,
        AccountId: str,
        PolicyArn: str,
        PrincipalArn: str,
        Revision: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_refresh_schedule(
        self,
        *,
        DataSetId: str,
        AwsAccountId: str,
        ScheduleId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_role_custom_permission(
        self,
        *,
        Role: str,
        AwsAccountId: str,
        Namespace: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_role_membership(
        self,
        *,
        MemberName: str,
        Role: str,
        AwsAccountId: str,
        Namespace: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_space(
        self,
        *,
        AwsAccountId: str,
        SpaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_template(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        VersionNumber: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_template_alias(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        AliasName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_theme(
        self,
        *,
        AwsAccountId: str,
        ThemeId: str,
        VersionNumber: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_theme_alias(
        self,
        *,
        AwsAccountId: str,
        ThemeId: str,
        AliasName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_topic(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_topic_refresh_schedule(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
        DatasetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_topic_v2(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user(
        self,
        *,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user_by_principal_id(
        self,
        *,
        PrincipalId: str,
        AwsAccountId: str,
        Namespace: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user_custom_permission(
        self,
        *,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vpc_connection(
        self,
        *,
        AwsAccountId: str,
        VPCConnectionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_access_control_application(
        self,
        *,
        AwsAccountId: str,
        ApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_custom_permission(
        self,
        *,
        AwsAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_customization(
        self,
        *,
        AwsAccountId: str,
        Namespace: str | None = None,
        Resolved: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_settings(
        self,
        *,
        AwsAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_subscription(
        self,
        *,
        AwsAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_action_connector(
        self,
        *,
        AwsAccountId: str,
        ActionConnectorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_action_connector_permissions(
        self,
        *,
        AwsAccountId: str,
        ActionConnectorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_agent(
        self,
        *,
        AgentId: str,
        AwsAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_agent_permissions(
        self,
        *,
        AgentId: str,
        AwsAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_analysis(
        self,
        *,
        AwsAccountId: str,
        AnalysisId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_analysis_definition(
        self,
        *,
        AwsAccountId: str,
        AnalysisId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_analysis_permissions(
        self,
        *,
        AwsAccountId: str,
        AnalysisId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_app(
        self,
        *,
        AwsAccountId: str,
        AppId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_app_permissions(
        self,
        *,
        AwsAccountId: str,
        AppId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_approval_policy(
        self,
        *,
        PolicyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_asset_bundle_export_job(
        self,
        *,
        AwsAccountId: str,
        AssetBundleExportJobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_asset_bundle_import_job(
        self,
        *,
        AwsAccountId: str,
        AssetBundleImportJobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_automation_job(
        self,
        *,
        AwsAccountId: str,
        AutomationGroupId: str,
        AutomationId: str,
        JobId: str,
        IncludeInputPayload: bool | None = None,
        IncludeOutputPayload: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_brand(
        self,
        *,
        AwsAccountId: str,
        BrandId: str,
        VersionId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_brand_assignment(
        self,
        *,
        AwsAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_brand_published_version(
        self,
        *,
        AwsAccountId: str,
        BrandId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_custom_permissions(
        self,
        *,
        AwsAccountId: str,
        CustomPermissionsName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_dashboard(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        VersionNumber: int | None = None,
        AliasName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_dashboard_definition(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        VersionNumber: int | None = None,
        AliasName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_dashboard_permissions(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_dashboard_snapshot_job(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        SnapshotJobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_dashboard_snapshot_job_result(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        SnapshotJobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_dashboards_qa_configuration(
        self,
        *,
        AwsAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_data_set(
        self,
        *,
        AwsAccountId: str,
        DataSetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_data_set_permissions(
        self,
        *,
        AwsAccountId: str,
        DataSetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_data_set_refresh_properties(
        self,
        *,
        AwsAccountId: str,
        DataSetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_data_source(
        self,
        *,
        AwsAccountId: str,
        DataSourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_data_source_permissions(
        self,
        *,
        AwsAccountId: str,
        DataSourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_default_q_business_application(
        self,
        *,
        AwsAccountId: str,
        Namespace: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_dlp_setting(
        self,
        *,
        AwsAccountId: str,
        DlpSettingId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_flow(
        self,
        *,
        AwsAccountId: str,
        FlowId: str,
        PublishState: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_folder(
        self,
        *,
        AwsAccountId: str,
        FolderId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_folder_permissions(
        self,
        *,
        AwsAccountId: str,
        FolderId: str,
        Namespace: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_folder_resolved_permissions(
        self,
        *,
        AwsAccountId: str,
        FolderId: str,
        Namespace: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_group(
        self,
        *,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_group_membership(
        self,
        *,
        MemberName: str,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_iam_policy_assignment(
        self,
        *,
        AwsAccountId: str,
        AssignmentName: str,
        Namespace: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_inbound_connector(
        self,
        *,
        AwsAccountId: str,
        InboundConnectorId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ingestion(
        self,
        *,
        AwsAccountId: str,
        DataSetId: str,
        IngestionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_ip_restriction(
        self,
        *,
        AwsAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_key_registration(
        self,
        *,
        AwsAccountId: str,
        DefaultKeyOnly: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_knowledge_base(
        self,
        *,
        AwsAccountId: str,
        KnowledgeBaseId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_knowledge_base_permissions(
        self,
        *,
        AwsAccountId: str,
        KnowledgeBaseId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_knowledge_base_refresh_schedule(
        self,
        *,
        AwsAccountId: str,
        KnowledgeBaseId: str,
        ScheduleId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_limits_profile(
        self,
        *,
        profileId: str,
        accountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_namespace(
        self,
        *,
        AwsAccountId: str,
        Namespace: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_o_auth_client_application(
        self,
        *,
        AwsAccountId: str,
        OAuthClientApplicationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_q_personalization_configuration(
        self,
        *,
        AwsAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_quick_sight_q_search_configuration(
        self,
        *,
        AwsAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_refresh_schedule(
        self,
        *,
        AwsAccountId: str,
        DataSetId: str,
        ScheduleId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_resource_permissions(
        self,
        *,
        AwsAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_role_custom_permission(
        self,
        *,
        Role: str,
        AwsAccountId: str,
        Namespace: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_self_upgrade_configuration(
        self,
        *,
        AwsAccountId: str,
        Namespace: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_space(
        self,
        *,
        AwsAccountId: str,
        SpaceId: str,
        MaxContributors: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_space_permissions(
        self,
        *,
        AwsAccountId: str,
        SpaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_template(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        VersionNumber: int | None = None,
        AliasName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_template_alias(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        AliasName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_template_definition(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        VersionNumber: int | None = None,
        AliasName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_template_permissions(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_theme(
        self,
        *,
        AwsAccountId: str,
        ThemeId: str,
        VersionNumber: int | None = None,
        AliasName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_theme_alias(
        self,
        *,
        AwsAccountId: str,
        ThemeId: str,
        AliasName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_theme_permissions(
        self,
        *,
        AwsAccountId: str,
        ThemeId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_topic(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_topic_permissions(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_topic_permissions_v2(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_topic_refresh(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
        RefreshId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_topic_refresh_schedule(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
        DatasetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_topic_v2(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_user(
        self,
        *,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vpc_connection(
        self,
        *,
        AwsAccountId: str,
        VPCConnectionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def generate_embed_url_for_anonymous_user(
        self,
        *,
        AwsAccountId: str,
        Namespace: str,
        AuthorizedResourceArns: list[str],
        ExperienceConfiguration: dict[str, Any],
        SessionLifetimeInMinutes: int | None = None,
        SessionTags: list[dict[str, Any]] | None = None,
        AllowedDomains: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def generate_embed_url_for_registered_user(
        self,
        *,
        AwsAccountId: str,
        UserArn: str,
        ExperienceConfiguration: dict[str, Any],
        SessionLifetimeInMinutes: int | None = None,
        AllowedDomains: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def generate_embed_url_for_registered_user_with_identity(
        self,
        *,
        AwsAccountId: str,
        ExperienceConfiguration: dict[str, Any],
        SessionLifetimeInMinutes: int | None = None,
        AllowedDomains: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_dashboard_embed_url(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        IdentityType: str,
        SessionLifetimeInMinutes: int | None = None,
        UndoRedoDisabled: bool | None = None,
        ResetDisabled: bool | None = None,
        StatePersistenceEnabled: bool | None = None,
        UserArn: str | None = None,
        Namespace: str | None = None,
        AdditionalDashboardIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_flow_metadata(
        self,
        *,
        AwsAccountId: str,
        FlowId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_flow_permissions(
        self,
        *,
        AwsAccountId: str,
        FlowId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_identity_context(
        self,
        *,
        AwsAccountId: str,
        UserIdentifier: dict[str, Any],
        Namespace: str | None = None,
        SessionExpiresAt: datetime.datetime | str | None = None,
        ContextRegion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_policy_assignment(
        self,
        *,
        AccountId: str,
        PolicyType: str,
        PrincipalArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_session_embed_url(
        self,
        *,
        AwsAccountId: str,
        EntryPoint: str | None = None,
        SessionLifetimeInMinutes: int | None = None,
        UserArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_access_control_applications(
        self,
        *,
        AwsAccountId: str,
        Namespace: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_action_connectors(
        self,
        *,
        AwsAccountId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_agents(
        self,
        *,
        AwsAccountId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_analyses(
        self,
        *,
        AwsAccountId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_approval_policies(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_apps(
        self,
        *,
        AwsAccountId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_asset_bundle_export_jobs(
        self,
        *,
        AwsAccountId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_asset_bundle_import_jobs(
        self,
        *,
        AwsAccountId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_brands(
        self,
        *,
        AwsAccountId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_custom_permissions(
        self,
        *,
        AwsAccountId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_dashboard_versions(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_dashboards(
        self,
        *,
        AwsAccountId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_sets(
        self,
        *,
        AwsAccountId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_sources(
        self,
        *,
        AwsAccountId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_dlp_settings(
        self,
        *,
        AwsAccountId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_flows(
        self,
        *,
        AwsAccountId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_folder_members(
        self,
        *,
        AwsAccountId: str,
        FolderId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_folders(
        self,
        *,
        AwsAccountId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_folders_for_resource(
        self,
        *,
        AwsAccountId: str,
        ResourceArn: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_group_memberships(
        self,
        *,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_groups(
        self,
        *,
        AwsAccountId: str,
        Namespace: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_iam_policy_assignments(
        self,
        *,
        AwsAccountId: str,
        Namespace: str,
        AssignmentStatus: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_iam_policy_assignments_for_user(
        self,
        *,
        AwsAccountId: str,
        UserName: str,
        Namespace: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_identity_propagation_configs(
        self,
        *,
        AwsAccountId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_inbound_connector_application_associations(
        self,
        *,
        AwsAccountId: str,
        InboundConnectorId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_inbound_connectors(
        self,
        *,
        AwsAccountId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Type: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_ingestions(
        self,
        *,
        DataSetId: str,
        AwsAccountId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_knowledge_base_refresh_schedules(
        self,
        *,
        AwsAccountId: str,
        KnowledgeBaseId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_knowledge_bases(
        self,
        *,
        AwsAccountId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_limits_profiles(
        self,
        *,
        accountId: str,
        resourceType: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_namespaces(
        self,
        *,
        AwsAccountId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_o_auth_client_applications(
        self,
        *,
        AwsAccountId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_principals_for_policy(
        self,
        *,
        AccountId: str,
        PolicyArn: str,
        PrincipalType: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_refresh_schedules(
        self,
        *,
        AwsAccountId: str,
        DataSetId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_role_memberships(
        self,
        *,
        Role: str,
        AwsAccountId: str,
        Namespace: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_self_upgrades(
        self,
        *,
        AwsAccountId: str,
        Namespace: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_space_resources(
        self,
        *,
        AwsAccountId: str,
        SpaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_spaces(
        self,
        *,
        AwsAccountId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_template_aliases(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_template_versions(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_templates(
        self,
        *,
        AwsAccountId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_theme_aliases(
        self,
        *,
        AwsAccountId: str,
        ThemeId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_theme_versions(
        self,
        *,
        AwsAccountId: str,
        ThemeId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_themes(
        self,
        *,
        AwsAccountId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Type: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_topic_refresh_schedules(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_topic_reviewed_answers(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_topics(
        self,
        *,
        AwsAccountId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_topics_v2(
        self,
        *,
        AwsAccountId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_user_groups(
        self,
        *,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_users(
        self,
        *,
        AwsAccountId: str,
        Namespace: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_users_index_capacity(
        self,
        *,
        awsAccountId: str,
        namespace: str | None = None,
        filters: list[dict[str, Any]] | None = None,
        sortBy: str | None = None,
        sortOrder: str | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_vpc_connections(
        self,
        *,
        AwsAccountId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def predict_qa_results(
        self,
        *,
        AwsAccountId: str,
        QueryText: str,
        IncludeQuickSightQIndex: str | None = None,
        IncludeGeneratedAnswer: str | None = None,
        MaxTopicsToConsider: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_data_set_refresh_properties(
        self,
        *,
        AwsAccountId: str,
        DataSetId: str,
        DataSetRefreshProperties: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_policy_assignment(
        self,
        *,
        AccountId: str,
        PolicyArn: str,
        PrincipalArn: str,
        ExistingPolicyArn: str | None = None,
        Revision: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_user(
        self,
        *,
        IdentityType: str,
        Email: str,
        UserRole: str,
        AwsAccountId: str,
        Namespace: str,
        IamArn: str | None = None,
        SessionName: str | None = None,
        UserName: str | None = None,
        CustomPermissionsName: str | None = None,
        ExternalLoginFederationProviderType: str | None = None,
        CustomFederationProviderUrl: str | None = None,
        ExternalLoginId: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def restore_analysis(
        self,
        *,
        AwsAccountId: str,
        AnalysisId: str,
        RestoreToFolders: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_action_connectors(
        self,
        *,
        AwsAccountId: str,
        Filters: list[dict[str, Any]],
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_agents(
        self,
        *,
        AwsAccountId: str,
        Filters: list[dict[str, Any]],
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_analyses(
        self,
        *,
        AwsAccountId: str,
        Filters: list[dict[str, Any]],
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_apps(
        self,
        *,
        AwsAccountId: str,
        Filters: list[dict[str, Any]],
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_dashboards(
        self,
        *,
        AwsAccountId: str,
        Filters: list[dict[str, Any]],
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_data_sets(
        self,
        *,
        AwsAccountId: str,
        Filters: list[dict[str, Any]],
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_data_sources(
        self,
        *,
        AwsAccountId: str,
        Filters: list[dict[str, Any]],
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_flows(
        self,
        *,
        AwsAccountId: str,
        Filters: list[dict[str, Any]],
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_folders(
        self,
        *,
        AwsAccountId: str,
        Filters: list[dict[str, Any]],
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_groups(
        self,
        *,
        AwsAccountId: str,
        Namespace: str,
        Filters: list[dict[str, Any]],
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_knowledge_bases(
        self,
        *,
        AwsAccountId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Filters: list[dict[str, Any]] | None = None,
        SortBy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_spaces(
        self,
        *,
        AwsAccountId: str,
        Filters: list[dict[str, Any]],
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_topics(
        self,
        *,
        AwsAccountId: str,
        Filters: list[dict[str, Any]],
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_topics_v2(
        self,
        *,
        AwsAccountId: str,
        Filters: list[dict[str, Any]],
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_asset_bundle_export_job(
        self,
        *,
        AwsAccountId: str,
        AssetBundleExportJobId: str,
        ResourceArns: list[str],
        ExportFormat: str,
        IncludeAllDependencies: bool | None = None,
        CloudFormationOverridePropertyConfiguration: dict[str, Any] | None = None,
        IncludePermissions: bool | None = None,
        IncludeTags: bool | None = None,
        ValidationStrategy: dict[str, Any] | None = None,
        IncludeFolderMemberships: bool | None = None,
        IncludeFolderMembers: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_asset_bundle_import_job(
        self,
        *,
        AwsAccountId: str,
        AssetBundleImportJobId: str,
        AssetBundleImportSource: dict[str, Any],
        OverrideParameters: dict[str, Any] | None = None,
        FailureAction: str | None = None,
        OverridePermissions: dict[str, Any] | None = None,
        OverrideTags: dict[str, Any] | None = None,
        OverrideValidationStrategy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_automation_job(
        self,
        *,
        AwsAccountId: str,
        AutomationGroupId: str,
        AutomationId: str,
        InputPayload: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_dashboard_snapshot_job(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        SnapshotJobId: str,
        SnapshotConfiguration: dict[str, Any],
        UserConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_dashboard_snapshot_job_schedule(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        ScheduleId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceArn: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceArn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_access_control_application(
        self,
        *,
        AwsAccountId: str,
        ApplicationId: str,
        Name: str | None = None,
        Description: str | None = None,
        IdpAuthorizingConfiguration: dict[str, Any] | None = None,
        QuickAuthenticationConfiguration: dict[str, Any] | None = None,
        Status: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_access_control_application_secret(
        self,
        *,
        AwsAccountId: str,
        ApplicationId: str,
        ClientSecretId: str,
        UpdateRegionalSecretManagerArns: dict[str, str] | None = None,
        RemoveRegionalSecretManagerArns: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_account_custom_permission(
        self,
        *,
        CustomPermissionsName: str,
        AwsAccountId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_account_customization(
        self,
        *,
        AwsAccountId: str,
        AccountCustomization: dict[str, Any],
        Namespace: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_account_settings(
        self,
        *,
        AwsAccountId: str,
        DefaultNamespace: str,
        NotificationEmail: str | None = None,
        TerminationProtectionEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_action_connector(
        self,
        *,
        AwsAccountId: str,
        ActionConnectorId: str,
        Name: str,
        AuthenticationConfig: dict[str, Any],
        Description: str | None = None,
        VpcConnectionArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_action_connector_permissions(
        self,
        *,
        AwsAccountId: str,
        ActionConnectorId: str,
        GrantPermissions: list[dict[str, Any]] | None = None,
        RevokePermissions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_agent(
        self,
        *,
        AgentId: str,
        AwsAccountId: str,
        Name: str,
        Description: str | None = None,
        IconId: str | None = None,
        StarterPrompts: list[str] | None = None,
        WelcomeMessage: str | None = None,
        CustomPromptInput: dict[str, Any] | None = None,
        SpacesToAdd: list[str] | None = None,
        SpacesToRemove: list[str] | None = None,
        ActionConnectorsToAdd: list[str] | None = None,
        ActionConnectorsToRemove: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_agent_permissions(
        self,
        *,
        AgentId: str,
        AwsAccountId: str,
        GrantPermissions: list[dict[str, Any]] | None = None,
        RevokePermissions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_analysis(
        self,
        *,
        AwsAccountId: str,
        AnalysisId: str,
        Name: str,
        Parameters: dict[str, Any] | None = None,
        SourceEntity: dict[str, Any] | None = None,
        ThemeArn: str | None = None,
        Definition: dict[str, Any] | None = None,
        ValidationStrategy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_analysis_permissions(
        self,
        *,
        AwsAccountId: str,
        AnalysisId: str,
        GrantPermissions: list[dict[str, Any]] | None = None,
        RevokePermissions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_app_permissions(
        self,
        *,
        AwsAccountId: str,
        AppId: str,
        GrantPermissions: list[dict[str, Any]] | None = None,
        RevokePermissions: list[dict[str, Any]] | None = None,
        Visibility: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_application_with_token_exchange_grant(
        self,
        *,
        AwsAccountId: str,
        Namespace: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_approval_policy(
        self,
        *,
        PolicyId: str,
        Name: str | None = None,
        Description: str | None = None,
        Actions: list[str] | None = None,
        AssetTypes: list[str] | None = None,
        ApplicableTo: dict[str, Any] | None = None,
        ApprovalGroups: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_brand(
        self,
        *,
        AwsAccountId: str,
        BrandId: str,
        BrandDefinition: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_brand_assignment(
        self,
        *,
        AwsAccountId: str,
        BrandArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_brand_published_version(
        self,
        *,
        AwsAccountId: str,
        BrandId: str,
        VersionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_custom_permissions(
        self,
        *,
        AwsAccountId: str,
        CustomPermissionsName: str,
        Capabilities: dict[str, Any] | None = None,
        Governance: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_dashboard(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        Name: str,
        SourceEntity: dict[str, Any] | None = None,
        Parameters: dict[str, Any] | None = None,
        VersionDescription: str | None = None,
        DashboardPublishOptions: dict[str, Any] | None = None,
        ThemeArn: str | None = None,
        Definition: dict[str, Any] | None = None,
        ValidationStrategy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_dashboard_links(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        LinkEntities: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_dashboard_permissions(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        GrantPermissions: list[dict[str, Any]] | None = None,
        RevokePermissions: list[dict[str, Any]] | None = None,
        GrantLinkPermissions: list[dict[str, Any]] | None = None,
        RevokeLinkPermissions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_dashboard_published_version(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        VersionNumber: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_dashboards_qa_configuration(
        self,
        *,
        AwsAccountId: str,
        DashboardsQAStatus: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_set(
        self,
        *,
        AwsAccountId: str,
        DataSetId: str,
        Name: str,
        PhysicalTableMap: dict[str, dict[str, Any]],
        ImportMode: str,
        LogicalTableMap: dict[str, dict[str, Any]] | None = None,
        ColumnGroups: list[dict[str, Any]] | None = None,
        FieldFolders: dict[str, dict[str, Any]] | None = None,
        RowLevelPermissionDataSet: dict[str, Any] | None = None,
        RowLevelPermissionTagConfiguration: dict[str, Any] | None = None,
        ColumnLevelPermissionRules: list[dict[str, Any]] | None = None,
        DataSetUsageConfiguration: dict[str, Any] | None = None,
        DatasetParameters: list[dict[str, Any]] | None = None,
        PerformanceConfiguration: dict[str, Any] | None = None,
        DataPrepConfiguration: dict[str, Any] | None = None,
        SemanticModelConfiguration: dict[str, Any] | None = None,
        UnmaterializedCalculatedColumns: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_set_permissions(
        self,
        *,
        AwsAccountId: str,
        DataSetId: str,
        GrantPermissions: list[dict[str, Any]] | None = None,
        RevokePermissions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_source(
        self,
        *,
        AwsAccountId: str,
        DataSourceId: str,
        Name: str,
        DataSourceParameters: dict[str, Any] | None = None,
        Credentials: dict[str, Any] | None = None,
        VpcConnectionProperties: dict[str, Any] | None = None,
        SslProperties: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_source_permissions(
        self,
        *,
        AwsAccountId: str,
        DataSourceId: str,
        GrantPermissions: list[dict[str, Any]] | None = None,
        RevokePermissions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_default_q_business_application(
        self,
        *,
        AwsAccountId: str,
        ApplicationId: str,
        Namespace: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_dlp_setting(
        self,
        *,
        AwsAccountId: str,
        DlpSettingId: str,
        Name: str | None = None,
        ProviderType: str | None = None,
        ProviderConfig: dict[str, Any] | None = None,
        ProviderOutageAction: str | None = None,
        Enabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_flow(
        self,
        *,
        AwsAccountId: str,
        FlowId: str,
        Name: str | None = None,
        Description: str | None = None,
        FlowDefinition: dict[str, Any] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_flow_permissions(
        self,
        *,
        AwsAccountId: str,
        FlowId: str,
        GrantPermissions: list[dict[str, Any]] | None = None,
        RevokePermissions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_folder(
        self,
        *,
        AwsAccountId: str,
        FolderId: str,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_folder_permissions(
        self,
        *,
        AwsAccountId: str,
        FolderId: str,
        GrantPermissions: list[dict[str, Any]] | None = None,
        RevokePermissions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_group(
        self,
        *,
        GroupName: str,
        AwsAccountId: str,
        Namespace: str,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_iam_policy_assignment(
        self,
        *,
        AwsAccountId: str,
        AssignmentName: str,
        Namespace: str,
        AssignmentStatus: str | None = None,
        PolicyArn: str | None = None,
        Identities: dict[str, list[str]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_identity_propagation_config(
        self,
        *,
        AwsAccountId: str,
        Service: str,
        AuthorizedTargets: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_inbound_connector(
        self,
        *,
        AwsAccountId: str,
        InboundConnectorId: str,
        Name: str | None = None,
        Description: str | None = None,
        InboundConnectorConfiguration: dict[str, Any] | None = None,
        InboundConnectorStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_inbound_connector_application_associations(
        self,
        *,
        AwsAccountId: str,
        InboundConnectorId: str,
        AssociateAccessControlApplications: list[str] | None = None,
        DisassociateAccessControlApplications: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_ip_restriction(
        self,
        *,
        AwsAccountId: str,
        IpRestrictionRuleMap: dict[str, str] | None = None,
        VpcIdRestrictionRuleMap: dict[str, str] | None = None,
        VpcEndpointIdRestrictionRuleMap: dict[str, str] | None = None,
        Enabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_key_registration(
        self,
        *,
        AwsAccountId: str,
        KeyRegistration: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_knowledge_base(
        self,
        *,
        AwsAccountId: str,
        KnowledgeBaseId: str,
        Name: str | None = None,
        Description: str | None = None,
        KnowledgeBaseConfiguration: dict[str, Any] | None = None,
        MediaExtractionConfiguration: dict[str, Any] | None = None,
        IsEmailNotificationOptedForIngestionFailures: bool | None = None,
        AccessControlConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_knowledge_base_permissions(
        self,
        *,
        AwsAccountId: str,
        KnowledgeBaseId: str,
        GrantPermissions: list[dict[str, Any]] | None = None,
        RevokePermissions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_knowledge_base_refresh_schedule(
        self,
        *,
        AwsAccountId: str,
        KnowledgeBaseId: str,
        ScheduleId: str,
        ScheduleFrequency: dict[str, Any] | None = None,
        StartTime: datetime.datetime | str | None = None,
        State: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_limits_profile(
        self,
        *,
        profileId: str,
        accountId: str,
        profileName: str | None = None,
        description: str | None = None,
        resourceLimits: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_o_auth_client_application(
        self,
        *,
        AwsAccountId: str,
        OAuthClientApplicationId: str,
        Name: str,
        ClientId: str | None = None,
        ClientSecret: str | None = None,
        OAuthTokenEndpointUrl: str | None = None,
        OAuthAuthorizationEndpointUrl: str | None = None,
        OAuthScopes: str | None = None,
        DataSourceType: str | None = None,
        IdentityProviderVpcConnectionProperties: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_public_sharing_settings(
        self,
        *,
        AwsAccountId: str,
        PublicSharingEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_q_personalization_configuration(
        self,
        *,
        AwsAccountId: str,
        PersonalizationMode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_quick_sight_q_search_configuration(
        self,
        *,
        AwsAccountId: str,
        QSearchStatus: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_refresh_schedule(
        self,
        *,
        DataSetId: str,
        AwsAccountId: str,
        Schedule: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_resource_permissions(
        self,
        *,
        AwsAccountId: str,
        RoleType: str,
        CustomerManagedRoleArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_role_custom_permission(
        self,
        *,
        CustomPermissionsName: str,
        Role: str,
        AwsAccountId: str,
        Namespace: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_spice_capacity_configuration(
        self,
        *,
        AwsAccountId: str,
        PurchaseMode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_self_upgrade(
        self,
        *,
        AwsAccountId: str,
        Namespace: str,
        UpgradeRequestId: str,
        Action: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_self_upgrade_configuration(
        self,
        *,
        AwsAccountId: str,
        Namespace: str,
        SelfUpgradeStatus: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_space(
        self,
        *,
        AwsAccountId: str,
        SpaceId: str,
        Name: str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_space_permissions(
        self,
        *,
        AwsAccountId: str,
        SpaceId: str,
        GrantPermissions: list[dict[str, Any]] | None = None,
        RevokePermissions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_space_resources(
        self,
        *,
        AwsAccountId: str,
        SpaceId: str,
        AddResources: list[dict[str, Any]] | None = None,
        RemoveResources: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_template(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        SourceEntity: dict[str, Any] | None = None,
        VersionDescription: str | None = None,
        Name: str | None = None,
        Definition: dict[str, Any] | None = None,
        ValidationStrategy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_template_alias(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        AliasName: str,
        TemplateVersionNumber: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_template_permissions(
        self,
        *,
        AwsAccountId: str,
        TemplateId: str,
        GrantPermissions: list[dict[str, Any]] | None = None,
        RevokePermissions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_theme(
        self,
        *,
        AwsAccountId: str,
        ThemeId: str,
        BaseThemeId: str,
        Name: str | None = None,
        VersionDescription: str | None = None,
        Configuration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_theme_alias(
        self,
        *,
        AwsAccountId: str,
        ThemeId: str,
        AliasName: str,
        ThemeVersionNumber: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_theme_permissions(
        self,
        *,
        AwsAccountId: str,
        ThemeId: str,
        GrantPermissions: list[dict[str, Any]] | None = None,
        RevokePermissions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_topic(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
        Topic: dict[str, Any],
        CustomInstructions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_topic_permissions(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
        GrantPermissions: list[dict[str, Any]] | None = None,
        RevokePermissions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_topic_permissions_v2(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
        GrantPermissions: list[dict[str, Any]] | None = None,
        RevokePermissions: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_topic_refresh_schedule(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
        DatasetId: str,
        RefreshSchedule: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_topic_v2(
        self,
        *,
        AwsAccountId: str,
        TopicId: str,
        Topic: dict[str, Any],
        CustomInstructions: dict[str, Any] | None = None,
        PublishOption: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user(
        self,
        *,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
        Email: str,
        Role: str,
        CustomPermissionsName: str | None = None,
        UnapplyCustomPermissions: bool | None = None,
        ExternalLoginFederationProviderType: str | None = None,
        CustomFederationProviderUrl: str | None = None,
        ExternalLoginId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user_custom_permission(
        self,
        *,
        UserName: str,
        AwsAccountId: str,
        Namespace: str,
        CustomPermissionsName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_vpc_connection(
        self,
        *,
        AwsAccountId: str,
        VPCConnectionId: str,
        Name: str,
        SubnetIds: list[str],
        SecurityGroupIds: list[str],
        RoleArn: str,
        DnsResolvers: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
