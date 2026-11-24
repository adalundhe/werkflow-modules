from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class ConnectClient(ABC):

    @abstractmethod
    def activate_evaluation_form(
        self,
        *,
        InstanceId: str,
        EvaluationFormId: str,
        EvaluationFormVersion: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_analytics_data_set(
        self,
        *,
        InstanceId: str,
        DataSetId: str,
        TargetAccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_approved_origin(
        self,
        *,
        InstanceId: str,
        Origin: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_bot(
        self,
        *,
        InstanceId: str,
        LexBot: dict[str, Any] | None = None,
        LexV2Bot: dict[str, Any] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_contact_with_user(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        UserId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_default_vocabulary(
        self,
        *,
        InstanceId: str,
        LanguageCode: str,
        VocabularyId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_email_address_alias(
        self,
        *,
        EmailAddressId: str,
        InstanceId: str,
        AliasConfiguration: dict[str, Any],
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_flow(
        self,
        *,
        InstanceId: str,
        ResourceId: str,
        FlowId: str,
        ResourceType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_hours_of_operations(
        self,
        *,
        InstanceId: str,
        HoursOfOperationId: str,
        ParentHoursOfOperationConfigs: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_instance_storage_config(
        self,
        *,
        InstanceId: str,
        ResourceType: str,
        StorageConfig: dict[str, Any],
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_lambda_function(
        self,
        *,
        InstanceId: str,
        FunctionArn: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_lex_bot(
        self,
        *,
        InstanceId: str,
        LexBot: dict[str, Any],
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_phone_number_contact_flow(
        self,
        *,
        PhoneNumberId: str,
        InstanceId: str,
        ContactFlowId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_queue_email_addresses(
        self,
        *,
        InstanceId: str,
        QueueId: str,
        EmailAddressesConfig: list[dict[str, Any]],
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_queue_quick_connects(
        self,
        *,
        InstanceId: str,
        QueueId: str,
        QuickConnectIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_routing_profile_queues(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
        QueueConfigs: list[dict[str, Any]] | None = None,
        ManualAssignmentQueueConfigs: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_security_key(
        self,
        *,
        InstanceId: str,
        Key: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_security_profiles(
        self,
        *,
        InstanceId: str,
        SecurityProfiles: list[dict[str, Any]],
        EntityType: str,
        EntityArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_traffic_distribution_group_user(
        self,
        *,
        TrafficDistributionGroupId: str,
        UserId: str,
        InstanceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_user_proficiencies(
        self,
        *,
        InstanceId: str,
        UserId: str,
        UserProficiencies: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_workspace(
        self,
        *,
        InstanceId: str,
        WorkspaceId: str,
        ResourceArns: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_associate_analytics_data_set(
        self,
        *,
        InstanceId: str,
        DataSetIds: list[str],
        TargetAccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_create_data_table_value(
        self,
        *,
        InstanceId: str,
        DataTableId: str,
        Values: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_delete_data_table_value(
        self,
        *,
        InstanceId: str,
        DataTableId: str,
        Values: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_describe_data_table_value(
        self,
        *,
        InstanceId: str,
        DataTableId: str,
        Values: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_disassociate_analytics_data_set(
        self,
        *,
        InstanceId: str,
        DataSetIds: list[str],
        TargetAccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_attached_file_metadata(
        self,
        *,
        FileIds: list[str],
        InstanceId: str,
        AssociatedResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_flow_association(
        self,
        *,
        InstanceId: str,
        ResourceIds: list[str],
        ResourceType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_put_contact(
        self,
        *,
        InstanceId: str,
        ContactDataRequestList: list[dict[str, Any]],
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_update_data_table_value(
        self,
        *,
        InstanceId: str,
        DataTableId: str,
        Values: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def claim_phone_number(
        self,
        *,
        PhoneNumber: str,
        TargetArn: str | None = None,
        InstanceId: str | None = None,
        PhoneNumberDescription: str | None = None,
        Tags: dict[str, str] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def complete_attached_file_upload(
        self,
        *,
        InstanceId: str,
        FileId: str,
        AssociatedResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_agent_status(
        self,
        *,
        InstanceId: str,
        Name: str,
        State: str,
        Description: str | None = None,
        DisplayOrder: int | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_attached_file(
        self,
        *,
        InstanceId: str,
        FileUseCaseType: str,
        FileSourceUri: str,
        AssociatedResourceArn: str,
        ClientToken: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_auth_code(
        self,
        *,
        InstanceId: str,
        Scope: dict[str, Any],
        SessionInactivityDurationMinutes: int,
        MaxSessionDurationMinutes: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_contact(
        self,
        *,
        InstanceId: str,
        Channel: str,
        InitiationMethod: str,
        ClientToken: str | None = None,
        RelatedContactId: str | None = None,
        Attributes: dict[str, str] | None = None,
        References: dict[str, dict[str, Any]] | None = None,
        ExpiryDurationInMinutes: int | None = None,
        UserInfo: dict[str, Any] | None = None,
        InitiateAs: str | None = None,
        Name: str | None = None,
        Description: str | None = None,
        SegmentAttributes: dict[str, dict[str, Any]] | None = None,
        PreviousContactId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_contact_flow(
        self,
        *,
        InstanceId: str,
        Name: str,
        Type: str,
        Content: str,
        Description: str | None = None,
        Status: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_contact_flow_alias(
        self,
        *,
        InstanceId: str,
        ContactFlowId: str,
        ContactFlowVersion: int,
        AliasName: str,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_contact_flow_module(
        self,
        *,
        InstanceId: str,
        Name: str,
        Content: str,
        Description: str | None = None,
        Tags: dict[str, str] | None = None,
        ClientToken: str | None = None,
        Settings: str | None = None,
        ExternalInvocationConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_contact_flow_module_alias(
        self,
        *,
        InstanceId: str,
        ContactFlowModuleId: str,
        ContactFlowModuleVersion: int,
        AliasName: str,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_contact_flow_module_version(
        self,
        *,
        InstanceId: str,
        ContactFlowModuleId: str,
        Description: str | None = None,
        FlowModuleContentSha256: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_contact_flow_version(
        self,
        *,
        InstanceId: str,
        ContactFlowId: str,
        Description: str | None = None,
        FlowContentSha256: str | None = None,
        ContactFlowVersion: int | None = None,
        LastModifiedTime: datetime.datetime | str | None = None,
        LastModifiedRegion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_table(
        self,
        *,
        InstanceId: str,
        Name: str,
        TimeZone: str,
        ValueLockLevel: str,
        Status: str,
        Description: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_data_table_attribute(
        self,
        *,
        InstanceId: str,
        DataTableId: str,
        Name: str,
        ValueType: str,
        Description: str | None = None,
        Primary: bool | None = None,
        Validation: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_email_address(
        self,
        *,
        InstanceId: str,
        EmailAddress: str,
        Description: str | None = None,
        DisplayName: str | None = None,
        Tags: dict[str, str] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_evaluation_form(
        self,
        *,
        InstanceId: str,
        Title: str,
        Items: list[dict[str, Any]],
        Description: str | None = None,
        ScoringStrategy: dict[str, Any] | None = None,
        AutoEvaluationConfiguration: dict[str, Any] | None = None,
        ClientToken: str | None = None,
        AsDraft: bool | None = None,
        Tags: dict[str, str] | None = None,
        ReviewConfiguration: dict[str, Any] | None = None,
        TargetConfiguration: dict[str, Any] | None = None,
        LanguageConfiguration: dict[str, Any] | None = None,
        AIVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_extraction_definition(
        self,
        *,
        InstanceId: str,
        Name: str,
        ExtractionConfiguration: dict[str, Any],
        ClientToken: str | None = None,
        Display: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_hours_of_operation(
        self,
        *,
        InstanceId: str,
        Name: str,
        TimeZone: str,
        Config: list[dict[str, Any]],
        Description: str | None = None,
        ParentHoursOfOperationConfigs: list[dict[str, Any]] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_hours_of_operation_override(
        self,
        *,
        InstanceId: str,
        HoursOfOperationId: str,
        Name: str,
        Config: list[dict[str, Any]],
        EffectiveFrom: str,
        EffectiveTill: str,
        Description: str | None = None,
        RecurrenceConfig: dict[str, Any] | None = None,
        OverrideType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_instance(
        self,
        *,
        IdentityManagementType: str,
        InboundCallsEnabled: bool,
        OutboundCallsEnabled: bool,
        ClientToken: str | None = None,
        InstanceAlias: str | None = None,
        DirectoryId: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_integration_association(
        self,
        *,
        InstanceId: str,
        IntegrationType: str,
        IntegrationArn: str,
        SourceApplicationUrl: str | None = None,
        SourceApplicationName: str | None = None,
        SourceType: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_metric(
        self,
        *,
        InstanceId: str,
        Name: str,
        MetricCalculation: dict[str, Any],
        Unit: str,
        Status: str | None = None,
        ClientToken: str | None = None,
        Description: str | None = None,
        PositiveTrendIndicator: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_notification(
        self,
        *,
        InstanceId: str,
        Recipients: list[str],
        Content: dict[str, str],
        ExpiresAt: datetime.datetime | str | None = None,
        Priority: str | None = None,
        Tags: dict[str, str] | None = None,
        PredefinedNotificationId: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_participant(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        ParticipantDetails: dict[str, Any],
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_persistent_contact_association(
        self,
        *,
        InstanceId: str,
        InitialContactId: str,
        RehydrationType: str,
        SourceContactId: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_predefined_attribute(
        self,
        *,
        InstanceId: str,
        Name: str,
        Values: dict[str, Any] | None = None,
        Purposes: list[str] | None = None,
        AttributeConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_prompt(
        self,
        *,
        InstanceId: str,
        Name: str,
        S3Uri: str,
        Description: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_push_notification_registration(
        self,
        *,
        InstanceId: str,
        PinpointAppArn: str,
        DeviceToken: str,
        DeviceType: str,
        ContactConfiguration: dict[str, Any],
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_queue(
        self,
        *,
        InstanceId: str,
        Name: str,
        HoursOfOperationId: str,
        Description: str | None = None,
        OutboundCallerConfig: dict[str, Any] | None = None,
        OutboundEmailConfig: dict[str, Any] | None = None,
        MaxContacts: int | None = None,
        QuickConnectIds: list[str] | None = None,
        EmailAddressesConfig: list[dict[str, Any]] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_quick_connect(
        self,
        *,
        InstanceId: str,
        Name: str,
        QuickConnectConfig: dict[str, Any],
        Description: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_routing_profile(
        self,
        *,
        InstanceId: str,
        Name: str,
        Description: str,
        DefaultOutboundQueueId: str,
        MediaConcurrencies: list[dict[str, Any]],
        QueueConfigs: list[dict[str, Any]] | None = None,
        ManualAssignmentQueueConfigs: list[dict[str, Any]] | None = None,
        Tags: dict[str, str] | None = None,
        AgentAvailabilityTimer: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_rule(
        self,
        *,
        InstanceId: str,
        Name: str,
        TriggerEventSource: dict[str, Any],
        Function: str,
        Actions: list[dict[str, Any]],
        PublishStatus: str,
        PreEvaluationFilters: dict[str, Any] | None = None,
        ClientToken: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_security_profile(
        self,
        *,
        SecurityProfileName: str,
        InstanceId: str,
        Description: str | None = None,
        Permissions: list[str] | None = None,
        Tags: dict[str, str] | None = None,
        AllowedAccessControlTags: dict[str, str] | None = None,
        TagRestrictedResources: list[str] | None = None,
        Applications: list[dict[str, Any]] | None = None,
        HierarchyRestrictedResources: list[str] | None = None,
        AllowedAccessControlHierarchyGroupId: str | None = None,
        AllowedFlowModules: list[dict[str, Any]] | None = None,
        AllowedAIAgents: list[dict[str, Any]] | None = None,
        GranularAccessControlConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_task_template(
        self,
        *,
        InstanceId: str,
        Name: str,
        Fields: list[dict[str, Any]],
        Description: str | None = None,
        ContactFlowId: str | None = None,
        SelfAssignFlowId: str | None = None,
        ContactHooks: dict[str, Any] | None = None,
        Constraints: dict[str, Any] | None = None,
        Defaults: dict[str, Any] | None = None,
        Status: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_test_case(
        self,
        *,
        InstanceId: str,
        Name: str,
        Content: str,
        Description: str | None = None,
        EntryPoint: dict[str, Any] | None = None,
        InitializationData: str | None = None,
        Status: str | None = None,
        TestCaseId: str | None = None,
        Tags: dict[str, str] | None = None,
        LastModifiedTime: datetime.datetime | str | None = None,
        LastModifiedRegion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_traffic_distribution_group(
        self,
        *,
        Name: str,
        InstanceId: str,
        Description: str | None = None,
        ClientToken: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_use_case(
        self,
        *,
        InstanceId: str,
        IntegrationAssociationId: str,
        UseCaseType: str,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_user(
        self,
        *,
        Username: str,
        SecurityProfileIds: list[str],
        RoutingProfileId: str,
        InstanceId: str,
        Password: str | None = None,
        IdentityInfo: dict[str, Any] | None = None,
        PhoneConfig: dict[str, Any] | None = None,
        DirectoryUserId: str | None = None,
        HierarchyGroupId: str | None = None,
        AutoAcceptConfigs: list[dict[str, Any]] | None = None,
        AfterContactWorkConfigs: list[dict[str, Any]] | None = None,
        PhoneNumberConfigs: list[dict[str, Any]] | None = None,
        PersistentConnectionConfigs: list[dict[str, Any]] | None = None,
        VoiceEnhancementConfigs: list[dict[str, Any]] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_user_hierarchy_group(
        self,
        *,
        Name: str,
        InstanceId: str,
        ParentGroupId: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_view(
        self,
        *,
        InstanceId: str,
        Status: str,
        Content: dict[str, Any],
        Name: str,
        ClientToken: str | None = None,
        Description: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_view_version(
        self,
        *,
        InstanceId: str,
        ViewId: str,
        VersionDescription: str | None = None,
        ViewContentSha256: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_vocabulary(
        self,
        *,
        InstanceId: str,
        VocabularyName: str,
        LanguageCode: str,
        Content: str,
        ClientToken: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_workspace(
        self,
        *,
        InstanceId: str,
        Name: str,
        Description: str | None = None,
        Theme: dict[str, Any] | None = None,
        Title: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_workspace_page(
        self,
        *,
        InstanceId: str,
        WorkspaceId: str,
        ResourceArn: str,
        Page: str,
        Slug: str | None = None,
        InputData: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deactivate_evaluation_form(
        self,
        *,
        InstanceId: str,
        EvaluationFormId: str,
        EvaluationFormVersion: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_all_entity_sessions(
        self,
        *,
        InstanceId: str,
        EntityId: str,
        EntityType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_attached_file(
        self,
        *,
        InstanceId: str,
        FileId: str,
        AssociatedResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_contact_data(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        ContactFields: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_contact_evaluation(
        self,
        *,
        InstanceId: str,
        EvaluationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_contact_flow(
        self,
        *,
        InstanceId: str,
        ContactFlowId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_contact_flow_alias(
        self,
        *,
        InstanceId: str,
        ContactFlowId: str,
        AliasId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_contact_flow_module(
        self,
        *,
        InstanceId: str,
        ContactFlowModuleId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_contact_flow_module_alias(
        self,
        *,
        InstanceId: str,
        ContactFlowModuleId: str,
        AliasId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_contact_flow_module_version(
        self,
        *,
        InstanceId: str,
        ContactFlowModuleId: str,
        ContactFlowModuleVersion: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_contact_flow_version(
        self,
        *,
        InstanceId: str,
        ContactFlowId: str,
        ContactFlowVersion: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_table(
        self,
        *,
        InstanceId: str,
        DataTableId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_data_table_attribute(
        self,
        *,
        InstanceId: str,
        DataTableId: str,
        AttributeName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_email_address(
        self,
        *,
        InstanceId: str,
        EmailAddressId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_evaluation_form(
        self,
        *,
        InstanceId: str,
        EvaluationFormId: str,
        EvaluationFormVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_extraction_definition(
        self,
        *,
        InstanceId: str,
        ExtractionDefinitionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_hours_of_operation(
        self,
        *,
        InstanceId: str,
        HoursOfOperationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_hours_of_operation_override(
        self,
        *,
        InstanceId: str,
        HoursOfOperationId: str,
        HoursOfOperationOverrideId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_instance(
        self,
        *,
        InstanceId: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_integration_association(
        self,
        *,
        InstanceId: str,
        IntegrationAssociationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_metric(
        self,
        *,
        InstanceId: str,
        MetricId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_notification(
        self,
        *,
        InstanceId: str,
        NotificationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_predefined_attribute(
        self,
        *,
        InstanceId: str,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_prompt(
        self,
        *,
        InstanceId: str,
        PromptId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_push_notification_registration(
        self,
        *,
        InstanceId: str,
        RegistrationId: str,
        ContactId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_queue(
        self,
        *,
        InstanceId: str,
        QueueId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_quick_connect(
        self,
        *,
        InstanceId: str,
        QuickConnectId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_routing_profile(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_rule(
        self,
        *,
        InstanceId: str,
        RuleId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_security_profile(
        self,
        *,
        InstanceId: str,
        SecurityProfileId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_session(
        self,
        *,
        InstanceId: str,
        SessionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_task_template(
        self,
        *,
        InstanceId: str,
        TaskTemplateId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_test_case(
        self,
        *,
        InstanceId: str,
        TestCaseId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_traffic_distribution_group(
        self,
        *,
        TrafficDistributionGroupId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_use_case(
        self,
        *,
        InstanceId: str,
        IntegrationAssociationId: str,
        UseCaseId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user(
        self,
        *,
        InstanceId: str,
        UserId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user_hierarchy_group(
        self,
        *,
        HierarchyGroupId: str,
        InstanceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_view(
        self,
        *,
        InstanceId: str,
        ViewId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_view_version(
        self,
        *,
        InstanceId: str,
        ViewId: str,
        ViewVersion: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_vocabulary(
        self,
        *,
        InstanceId: str,
        VocabularyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_workspace(
        self,
        *,
        InstanceId: str,
        WorkspaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_workspace_media(
        self,
        *,
        InstanceId: str,
        WorkspaceId: str,
        MediaType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_workspace_page(
        self,
        *,
        InstanceId: str,
        WorkspaceId: str,
        Page: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_agent_status(
        self,
        *,
        InstanceId: str,
        AgentStatusId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_attached_files_configuration(
        self,
        *,
        InstanceId: str,
        AttachmentScope: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_authentication_profile(
        self,
        *,
        AuthenticationProfileId: str,
        InstanceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_contact(
        self,
        *,
        InstanceId: str,
        ContactId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_contact_evaluation(
        self,
        *,
        InstanceId: str,
        EvaluationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_contact_flow(
        self,
        *,
        InstanceId: str,
        ContactFlowId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_contact_flow_alias(
        self,
        *,
        InstanceId: str,
        ContactFlowId: str,
        AliasId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_contact_flow_module(
        self,
        *,
        InstanceId: str,
        ContactFlowModuleId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_contact_flow_module_alias(
        self,
        *,
        InstanceId: str,
        ContactFlowModuleId: str,
        AliasId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_data_table(
        self,
        *,
        InstanceId: str,
        DataTableId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_data_table_attribute(
        self,
        *,
        InstanceId: str,
        DataTableId: str,
        AttributeName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_email_address(
        self,
        *,
        InstanceId: str,
        EmailAddressId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_evaluation_form(
        self,
        *,
        InstanceId: str,
        EvaluationFormId: str,
        EvaluationFormVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_extraction_definition(
        self,
        *,
        InstanceId: str,
        ExtractionDefinitionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_hours_of_operation(
        self,
        *,
        InstanceId: str,
        HoursOfOperationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_hours_of_operation_override(
        self,
        *,
        InstanceId: str,
        HoursOfOperationId: str,
        HoursOfOperationOverrideId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance(
        self,
        *,
        InstanceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_attribute(
        self,
        *,
        InstanceId: str,
        AttributeType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_instance_storage_config(
        self,
        *,
        InstanceId: str,
        AssociationId: str,
        ResourceType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_metric(
        self,
        *,
        InstanceId: str,
        MetricId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_notification(
        self,
        *,
        InstanceId: str,
        NotificationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_phone_number(
        self,
        *,
        PhoneNumberId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_predefined_attribute(
        self,
        *,
        InstanceId: str,
        Name: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_prompt(
        self,
        *,
        InstanceId: str,
        PromptId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_queue(
        self,
        *,
        InstanceId: str,
        QueueId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_quick_connect(
        self,
        *,
        InstanceId: str,
        QuickConnectId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_routing_profile(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_rule(
        self,
        *,
        InstanceId: str,
        RuleId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_security_profile(
        self,
        *,
        SecurityProfileId: str,
        InstanceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_test_case(
        self,
        *,
        InstanceId: str,
        TestCaseId: str,
        Status: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_traffic_distribution_group(
        self,
        *,
        TrafficDistributionGroupId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_user(
        self,
        *,
        UserId: str,
        InstanceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_user_hierarchy_group(
        self,
        *,
        HierarchyGroupId: str,
        InstanceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_user_hierarchy_structure(
        self,
        *,
        InstanceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_view(
        self,
        *,
        InstanceId: str,
        ViewId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_vocabulary(
        self,
        *,
        InstanceId: str,
        VocabularyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_workspace(
        self,
        *,
        InstanceId: str,
        WorkspaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_analytics_data_set(
        self,
        *,
        InstanceId: str,
        DataSetId: str,
        TargetAccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_approved_origin(
        self,
        *,
        InstanceId: str,
        Origin: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_bot(
        self,
        *,
        InstanceId: str,
        LexBot: dict[str, Any] | None = None,
        LexV2Bot: dict[str, Any] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_email_address_alias(
        self,
        *,
        EmailAddressId: str,
        InstanceId: str,
        AliasConfiguration: dict[str, Any],
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_flow(
        self,
        *,
        InstanceId: str,
        ResourceId: str,
        ResourceType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_hours_of_operations(
        self,
        *,
        InstanceId: str,
        HoursOfOperationId: str,
        ParentHoursOfOperationIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_instance_storage_config(
        self,
        *,
        InstanceId: str,
        AssociationId: str,
        ResourceType: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_lambda_function(
        self,
        *,
        InstanceId: str,
        FunctionArn: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_lex_bot(
        self,
        *,
        InstanceId: str,
        BotName: str,
        LexRegion: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_phone_number_contact_flow(
        self,
        *,
        PhoneNumberId: str,
        InstanceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_queue_email_addresses(
        self,
        *,
        InstanceId: str,
        QueueId: str,
        EmailAddressesId: list[str],
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_queue_quick_connects(
        self,
        *,
        InstanceId: str,
        QueueId: str,
        QuickConnectIds: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_routing_profile_queues(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
        QueueReferences: list[dict[str, Any]] | None = None,
        ManualAssignmentQueueReferences: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_security_key(
        self,
        *,
        InstanceId: str,
        AssociationId: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_security_profiles(
        self,
        *,
        InstanceId: str,
        SecurityProfiles: list[dict[str, Any]],
        EntityType: str,
        EntityArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_traffic_distribution_group_user(
        self,
        *,
        TrafficDistributionGroupId: str,
        UserId: str,
        InstanceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_user_proficiencies(
        self,
        *,
        InstanceId: str,
        UserId: str,
        UserProficiencies: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_workspace(
        self,
        *,
        InstanceId: str,
        WorkspaceId: str,
        ResourceArns: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def dismiss_user_contact(
        self,
        *,
        UserId: str,
        InstanceId: str,
        ContactId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def evaluate_data_table_values(
        self,
        *,
        InstanceId: str,
        DataTableId: str,
        Values: list[dict[str, Any]],
        TimeZone: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_attached_file(
        self,
        *,
        InstanceId: str,
        FileId: str,
        AssociatedResourceArn: str,
        UrlExpiryInSeconds: int | None = None,
        UrlContentDisposition: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_contact_attributes(
        self,
        *,
        InstanceId: str,
        InitialContactId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_contact_metrics(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        Metrics: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_cross_region_routing(
        self,
        *,
        InstanceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_current_metric_data(
        self,
        *,
        InstanceId: str,
        Filters: dict[str, Any],
        CurrentMetrics: list[dict[str, Any]],
        Groupings: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SortCriteria: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_current_user_data(
        self,
        *,
        InstanceId: str,
        Filters: dict[str, Any],
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_effective_hours_of_operations(
        self,
        *,
        InstanceId: str,
        HoursOfOperationId: str,
        FromDate: str,
        ToDate: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_evaluation_form_validation(
        self,
        *,
        InstanceId: str,
        EvaluationFormId: str,
        EvaluationFormVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_federation_token(
        self,
        *,
        InstanceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_flow_association(
        self,
        *,
        InstanceId: str,
        ResourceId: str,
        ResourceType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_metric_data(
        self,
        *,
        InstanceId: str,
        StartTime: datetime.datetime | str,
        EndTime: datetime.datetime | str,
        Filters: dict[str, Any],
        HistoricalMetrics: list[dict[str, Any]],
        Groupings: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_metric_data_v2(
        self,
        *,
        ResourceArn: str,
        StartTime: datetime.datetime | str,
        EndTime: datetime.datetime | str,
        Filters: list[dict[str, Any]],
        Metrics: list[dict[str, Any]],
        Interval: dict[str, Any] | None = None,
        Groupings: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_prompt_file(
        self,
        *,
        InstanceId: str,
        PromptId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_task_template(
        self,
        *,
        InstanceId: str,
        TaskTemplateId: str,
        SnapshotVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_test_case_execution_summary(
        self,
        *,
        InstanceId: str,
        TestCaseId: str,
        TestCaseExecutionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_traffic_distribution(
        self,
        *,
        Id: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_phone_number(
        self,
        *,
        InstanceId: str,
        SourcePhoneNumberArn: str,
        PhoneNumberDescription: str | None = None,
        Tags: dict[str, str] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_workspace_media(
        self,
        *,
        InstanceId: str,
        WorkspaceId: str,
        MediaType: str,
        MediaSource: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_agent_statuses(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        AgentStatusTypes: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_analytics_data_associations(
        self,
        *,
        InstanceId: str,
        DataSetId: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_analytics_data_lake_data_sets(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_approved_origins(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_associated_contacts(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_attached_files_configurations(
        self,
        *,
        InstanceId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_authentication_profiles(
        self,
        *,
        InstanceId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_bots(
        self,
        *,
        InstanceId: str,
        LexVersion: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_child_hours_of_operations(
        self,
        *,
        InstanceId: str,
        HoursOfOperationId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_contact_evaluations(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_contact_flow_aliases(
        self,
        *,
        InstanceId: str,
        ContactFlowId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_contact_flow_module_aliases(
        self,
        *,
        InstanceId: str,
        ContactFlowModuleId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_contact_flow_module_versions(
        self,
        *,
        InstanceId: str,
        ContactFlowModuleId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_contact_flow_modules(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        ContactFlowModuleState: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_contact_flow_versions(
        self,
        *,
        InstanceId: str,
        ContactFlowId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_contact_flows(
        self,
        *,
        InstanceId: str,
        ContactFlowTypes: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_contact_references(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        ReferenceTypes: list[str],
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_table_attributes(
        self,
        *,
        InstanceId: str,
        DataTableId: str,
        AttributeIds: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_table_primary_values(
        self,
        *,
        InstanceId: str,
        DataTableId: str,
        RecordIds: list[str] | None = None,
        PrimaryAttributeValues: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_table_values(
        self,
        *,
        InstanceId: str,
        DataTableId: str,
        RecordIds: list[str] | None = None,
        PrimaryAttributeValues: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_data_tables(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_default_vocabularies(
        self,
        *,
        InstanceId: str,
        LanguageCode: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_entity_security_profiles(
        self,
        *,
        InstanceId: str,
        EntityType: str,
        EntityArn: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_evaluation_form_ai_versions(
        self,
        *,
        InstanceId: str,
        ContactInteractionType: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_evaluation_form_versions(
        self,
        *,
        InstanceId: str,
        EvaluationFormId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_evaluation_forms(
        self,
        *,
        InstanceId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_extraction_definitions(
        self,
        *,
        InstanceId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_flow_associations(
        self,
        *,
        InstanceId: str,
        ResourceType: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_hours_of_operation_overrides(
        self,
        *,
        InstanceId: str,
        HoursOfOperationId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_hours_of_operations(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_instance_attributes(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_instance_storage_configs(
        self,
        *,
        InstanceId: str,
        ResourceType: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_instances(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_integration_associations(
        self,
        *,
        InstanceId: str,
        IntegrationType: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        IntegrationArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_lambda_functions(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_lex_bots(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_metrics(
        self,
        *,
        InstanceId: str,
        Type: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_notifications(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_phone_numbers(
        self,
        *,
        InstanceId: str,
        PhoneNumberTypes: list[str] | None = None,
        PhoneNumberCountryCodes: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_phone_numbers_v2(
        self,
        *,
        TargetArn: str | None = None,
        InstanceId: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        PhoneNumberCountryCodes: list[str] | None = None,
        PhoneNumberTypes: list[str] | None = None,
        PhoneNumberPrefix: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_predefined_attributes(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_prompts(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_queue_email_addresses(
        self,
        *,
        InstanceId: str,
        QueueId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_queue_quick_connects(
        self,
        *,
        InstanceId: str,
        QueueId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_queues(
        self,
        *,
        InstanceId: str,
        QueueTypes: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_quick_connects(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        QuickConnectTypes: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_realtime_contact_analysis_segments_v2(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        OutputType: str,
        SegmentTypes: list[str],
        MaxResults: int | None = None,
        NextToken: str | None = None,
        ListFilter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_replication_findings(
        self,
        *,
        InstanceId: str,
        ResourceType: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_routing_profile_manual_assignment_queues(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_routing_profile_queues(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_routing_profiles(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_rules(
        self,
        *,
        InstanceId: str,
        PublishStatus: str | None = None,
        EventSourceName: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_security_keys(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_security_profile_ai_agents(
        self,
        *,
        SecurityProfileId: str,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_security_profile_applications(
        self,
        *,
        SecurityProfileId: str,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_security_profile_flow_modules(
        self,
        *,
        SecurityProfileId: str,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_security_profile_permissions(
        self,
        *,
        SecurityProfileId: str,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_security_profiles(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        resourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_task_templates(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Status: str | None = None,
        Name: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_test_case_execution_records(
        self,
        *,
        InstanceId: str,
        TestCaseId: str,
        TestCaseExecutionId: str,
        Status: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_test_case_executions(
        self,
        *,
        InstanceId: str,
        TestCaseId: str | None = None,
        TestCaseName: str | None = None,
        StartTime: int | None = None,
        EndTime: int | None = None,
        Status: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_test_cases(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_traffic_distribution_group_users(
        self,
        *,
        TrafficDistributionGroupId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_traffic_distribution_groups(
        self,
        *,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        InstanceId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_use_cases(
        self,
        *,
        InstanceId: str,
        IntegrationAssociationId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_user_hierarchy_groups(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_user_notifications(
        self,
        *,
        InstanceId: str,
        UserId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_user_proficiencies(
        self,
        *,
        InstanceId: str,
        UserId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_users(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_view_versions(
        self,
        *,
        InstanceId: str,
        ViewId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_views(
        self,
        *,
        InstanceId: str,
        Type: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_workspace_media(
        self,
        *,
        InstanceId: str,
        WorkspaceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_workspace_pages(
        self,
        *,
        InstanceId: str,
        WorkspaceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_workspaces(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def monitor_contact(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        UserId: str,
        AllowedMonitorCapabilities: list[str] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def pause_contact(
        self,
        *,
        ContactId: str,
        InstanceId: str,
        ContactFlowId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_user_status(
        self,
        *,
        UserId: str,
        InstanceId: str,
        AgentStatusId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def release_phone_number(
        self,
        *,
        PhoneNumberId: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def replicate_instance(
        self,
        *,
        InstanceId: str,
        ReplicaRegion: str,
        ClientToken: str | None = None,
        ReplicaAlias: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def resume_contact(
        self,
        *,
        ContactId: str,
        InstanceId: str,
        ContactFlowId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def resume_contact_recording(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        InitialContactId: str,
        ContactRecordingType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_agent_statuses(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchFilter: dict[str, Any] | None = None,
        SearchCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_available_phone_numbers(
        self,
        *,
        PhoneNumberCountryCode: str,
        PhoneNumberType: str,
        TargetArn: str | None = None,
        InstanceId: str | None = None,
        PhoneNumberPrefix: str | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_contact_evaluations(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchCriteria: dict[str, Any] | None = None,
        SearchFilter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_contact_flow_modules(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchFilter: dict[str, Any] | None = None,
        SearchCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_contact_flows(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchFilter: dict[str, Any] | None = None,
        SearchCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_contacts(
        self,
        *,
        InstanceId: str,
        TimeRange: dict[str, Any],
        SearchCriteria: dict[str, Any] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        Sort: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_data_tables(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchFilter: dict[str, Any] | None = None,
        SearchCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_email_addresses(
        self,
        *,
        InstanceId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        SearchCriteria: dict[str, Any] | None = None,
        SearchFilter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_evaluation_forms(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchCriteria: dict[str, Any] | None = None,
        SearchFilter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_hours_of_operation_overrides(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchFilter: dict[str, Any] | None = None,
        SearchCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_hours_of_operations(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchFilter: dict[str, Any] | None = None,
        SearchCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_metrics(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchFilter: dict[str, Any] | None = None,
        SearchCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_notifications(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchFilter: dict[str, Any] | None = None,
        SearchCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_predefined_attributes(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_prompts(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchFilter: dict[str, Any] | None = None,
        SearchCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_queues(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchFilter: dict[str, Any] | None = None,
        SearchCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_quick_connects(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchFilter: dict[str, Any] | None = None,
        SearchCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_resource_tags(
        self,
        *,
        InstanceId: str,
        ResourceTypes: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_routing_profiles(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchFilter: dict[str, Any] | None = None,
        SearchCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_rules(
        self,
        *,
        InstanceId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        SearchCriteria: dict[str, Any] | None = None,
        SearchFilter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_security_profiles(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchCriteria: dict[str, Any] | None = None,
        SearchFilter: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_test_cases(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchFilter: dict[str, Any] | None = None,
        SearchCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_user_hierarchy_groups(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchFilter: dict[str, Any] | None = None,
        SearchCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_users(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchFilter: dict[str, Any] | None = None,
        SearchCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_views(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchFilter: dict[str, Any] | None = None,
        SearchCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_vocabularies(
        self,
        *,
        InstanceId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        State: str | None = None,
        NameStartsWith: str | None = None,
        LanguageCode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_workspace_associations(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchFilter: dict[str, Any] | None = None,
        SearchCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_workspaces(
        self,
        *,
        InstanceId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        SearchFilter: dict[str, Any] | None = None,
        SearchCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_chat_integration_event(
        self,
        *,
        SourceId: str,
        DestinationId: str,
        Event: dict[str, Any],
        Subtype: str | None = None,
        NewSessionDetails: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_outbound_email(
        self,
        *,
        InstanceId: str,
        FromEmailAddress: dict[str, Any],
        DestinationEmailAddress: dict[str, Any],
        EmailMessage: dict[str, Any],
        TrafficType: str,
        AdditionalRecipients: dict[str, Any] | None = None,
        SourceCampaign: dict[str, Any] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_outbound_web_notification(
        self,
        *,
        InstanceId: str,
        BrowserId: str,
        SessionId: str,
        ExpiresAt: datetime.datetime | str,
        Source: dict[str, Any],
        Destination: dict[str, Any],
        Content: dict[str, Any],
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_assistant_contact(
        self,
        *,
        InstanceId: str,
        AiAgent: dict[str, Any],
        ParticipantDetails: dict[str, Any],
        InitialMessage: dict[str, Any] | None = None,
        Attributes: dict[str, str] | None = None,
        ClientToken: str | None = None,
        PersistentChat: dict[str, Any] | None = None,
        RelatedContactId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_attached_file_upload(
        self,
        *,
        InstanceId: str,
        FileName: str,
        FileSizeInBytes: int,
        FileUseCaseType: str,
        AssociatedResourceArn: str,
        ClientToken: str | None = None,
        UrlExpiryInSeconds: int | None = None,
        CreatedBy: dict[str, Any] | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_chat_contact(
        self,
        *,
        InstanceId: str,
        ContactFlowId: str,
        ParticipantDetails: dict[str, Any],
        Attributes: dict[str, str] | None = None,
        ParticipantConfiguration: dict[str, Any] | None = None,
        InitialMessage: dict[str, Any] | None = None,
        ClientToken: str | None = None,
        ChatDurationInMinutes: int | None = None,
        SupportedMessagingContentTypes: list[str] | None = None,
        PersistentChat: dict[str, Any] | None = None,
        RelatedContactId: str | None = None,
        SegmentAttributes: dict[str, dict[str, Any]] | None = None,
        CustomerId: str | None = None,
        DisconnectOnCustomerExit: list[str] | None = None,
        ConnectionTypes: list[str] | None = None,
        ChatStreamingConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_contact_conversational_analytics_job(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        AnalyticsModes: list[str],
        AnalyticsConfiguration: dict[str, Any],
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_contact_evaluation(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        EvaluationFormId: str,
        AutoEvaluationConfiguration: dict[str, Any] | None = None,
        ClientToken: str | None = None,
        Tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_contact_media_processing(
        self,
        *,
        InstanceId: str | None = None,
        ContactId: str | None = None,
        ProcessorArn: str | None = None,
        FailureMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_contact_recording(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        InitialContactId: str,
        VoiceRecordingConfiguration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_contact_streaming(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        ChatStreamingConfiguration: dict[str, Any],
        ClientToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_email_contact(
        self,
        *,
        InstanceId: str,
        FromEmailAddress: dict[str, Any],
        DestinationEmailAddress: str,
        EmailMessage: dict[str, Any],
        Description: str | None = None,
        References: dict[str, dict[str, Any]] | None = None,
        Name: str | None = None,
        AdditionalRecipients: dict[str, Any] | None = None,
        Attachments: list[dict[str, Any]] | None = None,
        ContactFlowId: str | None = None,
        RelatedContactId: str | None = None,
        Attributes: dict[str, str] | None = None,
        SegmentAttributes: dict[str, dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_evaluation_form_validation(
        self,
        *,
        InstanceId: str,
        EvaluationFormId: str,
        EvaluationFormVersion: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_outbound_chat_contact(
        self,
        *,
        SourceEndpoint: dict[str, Any],
        DestinationEndpoint: dict[str, Any],
        InstanceId: str,
        SegmentAttributes: dict[str, dict[str, Any]],
        ContactFlowId: str,
        Attributes: dict[str, str] | None = None,
        ChatDurationInMinutes: int | None = None,
        ParticipantDetails: dict[str, Any] | None = None,
        InitialSystemMessage: dict[str, Any] | None = None,
        InitialTemplatedSystemMessage: dict[str, Any] | None = None,
        RelatedContactId: str | None = None,
        SupportedMessagingContentTypes: list[str] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_outbound_email_contact(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        DestinationEmailAddress: dict[str, Any],
        EmailMessage: dict[str, Any],
        FromEmailAddress: dict[str, Any] | None = None,
        AdditionalRecipients: dict[str, Any] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_outbound_voice_contact(
        self,
        *,
        DestinationPhoneNumber: str,
        ContactFlowId: str,
        InstanceId: str,
        Name: str | None = None,
        Description: str | None = None,
        References: dict[str, dict[str, Any]] | None = None,
        RelatedContactId: str | None = None,
        ClientToken: str | None = None,
        SourcePhoneNumber: str | None = None,
        QueueId: str | None = None,
        Attributes: dict[str, str] | None = None,
        AnswerMachineDetectionConfig: dict[str, Any] | None = None,
        CampaignId: str | None = None,
        TrafficType: str | None = None,
        OutboundStrategy: dict[str, Any] | None = None,
        RingTimeoutInSeconds: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_screen_sharing(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_task_contact(
        self,
        *,
        InstanceId: str,
        Name: str,
        PreviousContactId: str | None = None,
        ContactFlowId: str | None = None,
        Attributes: dict[str, str] | None = None,
        References: dict[str, dict[str, Any]] | None = None,
        Description: str | None = None,
        ClientToken: str | None = None,
        ScheduledTime: datetime.datetime | str | None = None,
        TaskTemplateId: str | None = None,
        QuickConnectId: str | None = None,
        RelatedContactId: str | None = None,
        SegmentAttributes: dict[str, dict[str, Any]] | None = None,
        Attachments: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_test_case_execution(
        self,
        *,
        InstanceId: str,
        TestCaseId: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_web_rtc_contact(
        self,
        *,
        ContactFlowId: str,
        InstanceId: str,
        ParticipantDetails: dict[str, Any],
        Attributes: dict[str, str] | None = None,
        ClientToken: str | None = None,
        AllowedCapabilities: dict[str, Any] | None = None,
        RelatedContactId: str | None = None,
        References: dict[str, dict[str, Any]] | None = None,
        Description: str | None = None,
        SegmentAttributes: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_contact(
        self,
        *,
        ContactId: str,
        InstanceId: str,
        DisconnectReason: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_contact_media_processing(
        self,
        *,
        InstanceId: str | None = None,
        ContactId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_contact_recording(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        InitialContactId: str,
        ContactRecordingType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_contact_streaming(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        StreamingId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_test_case_execution(
        self,
        *,
        InstanceId: str,
        TestCaseExecutionId: str,
        TestCaseId: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def submit_contact_evaluation(
        self,
        *,
        InstanceId: str,
        EvaluationId: str,
        Answers: dict[str, dict[str, Any]] | None = None,
        Notes: dict[str, dict[str, Any]] | None = None,
        SubmittedBy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def suspend_contact_recording(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        InitialContactId: str,
        ContactRecordingType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_contact(
        self,
        *,
        ContactId: str,
        InstanceId: str,
        Tags: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        resourceArn: str,
        tags: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def transfer_contact(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        ContactFlowId: str,
        QueueId: str | None = None,
        UserId: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_contact(
        self,
        *,
        ContactId: str,
        InstanceId: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        resourceArn: str,
        tagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_agent_status(
        self,
        *,
        InstanceId: str,
        AgentStatusId: str,
        Name: str | None = None,
        Description: str | None = None,
        State: str | None = None,
        DisplayOrder: int | None = None,
        ResetOrderNumber: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_attached_files_configuration(
        self,
        *,
        InstanceId: str,
        AttachmentScope: str,
        MaximumSizeLimitInBytes: int | None = None,
        ExtensionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_authentication_profile(
        self,
        *,
        AuthenticationProfileId: str,
        InstanceId: str,
        Name: str | None = None,
        Description: str | None = None,
        AllowedIps: list[str] | None = None,
        BlockedIps: list[str] | None = None,
        PeriodicSessionDuration: int | None = None,
        SessionInactivityDuration: int | None = None,
        SessionInactivityHandlingEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_contact(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        Name: str | None = None,
        Description: str | None = None,
        References: dict[str, dict[str, Any]] | None = None,
        SegmentAttributes: dict[str, dict[str, Any]] | None = None,
        QueueInfo: dict[str, Any] | None = None,
        UserInfo: dict[str, Any] | None = None,
        CustomerEndpoint: dict[str, Any] | None = None,
        SystemEndpoint: dict[str, Any] | None = None,
        AdditionalRecipients: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_contact_attributes(
        self,
        *,
        InitialContactId: str,
        InstanceId: str,
        Attributes: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_contact_evaluation(
        self,
        *,
        InstanceId: str,
        EvaluationId: str,
        Answers: dict[str, dict[str, Any]] | None = None,
        Notes: dict[str, dict[str, Any]] | None = None,
        UpdatedBy: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_contact_flow_alias(
        self,
        *,
        InstanceId: str,
        ContactFlowId: str,
        AliasId: str,
        Name: str | None = None,
        Description: str | None = None,
        ContactFlowVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_contact_flow_content(
        self,
        *,
        InstanceId: str,
        ContactFlowId: str,
        Content: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_contact_flow_metadata(
        self,
        *,
        InstanceId: str,
        ContactFlowId: str,
        Name: str | None = None,
        Description: str | None = None,
        ContactFlowState: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_contact_flow_module_alias(
        self,
        *,
        InstanceId: str,
        ContactFlowModuleId: str,
        AliasId: str,
        Name: str | None = None,
        Description: str | None = None,
        ContactFlowModuleVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_contact_flow_module_content(
        self,
        *,
        InstanceId: str,
        ContactFlowModuleId: str,
        Content: str | None = None,
        Settings: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_contact_flow_module_metadata(
        self,
        *,
        InstanceId: str,
        ContactFlowModuleId: str,
        Name: str | None = None,
        Description: str | None = None,
        State: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_contact_flow_name(
        self,
        *,
        InstanceId: str,
        ContactFlowId: str,
        Name: str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_contact_routing_data(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        QueueTimeAdjustmentSeconds: int | None = None,
        QueuePriority: int | None = None,
        RoutingCriteria: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_contact_schedule(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        ScheduledTime: datetime.datetime | str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_contact_task_template(
        self,
        *,
        InstanceId: str,
        TaskTemplateId: str,
        ContactId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_cross_region_routing(
        self,
        *,
        InstanceId: str,
        IsolatedAll: bool,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_table_attribute(
        self,
        *,
        InstanceId: str,
        DataTableId: str,
        AttributeName: str,
        Name: str,
        ValueType: str,
        Description: str | None = None,
        Primary: bool | None = None,
        Validation: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_table_metadata(
        self,
        *,
        InstanceId: str,
        DataTableId: str,
        Name: str,
        ValueLockLevel: str,
        TimeZone: str,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_data_table_primary_values(
        self,
        *,
        InstanceId: str,
        DataTableId: str,
        PrimaryValues: list[dict[str, Any]],
        NewPrimaryValues: list[dict[str, Any]],
        LockVersion: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_email_address_metadata(
        self,
        *,
        InstanceId: str,
        EmailAddressId: str,
        Description: str | None = None,
        DisplayName: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_evaluation_form(
        self,
        *,
        InstanceId: str,
        EvaluationFormId: str,
        EvaluationFormVersion: int,
        Title: str,
        Items: list[dict[str, Any]],
        CreateNewVersion: bool | None = None,
        Description: str | None = None,
        ScoringStrategy: dict[str, Any] | None = None,
        AutoEvaluationConfiguration: dict[str, Any] | None = None,
        ReviewConfiguration: dict[str, Any] | None = None,
        AsDraft: bool | None = None,
        ClientToken: str | None = None,
        TargetConfiguration: dict[str, Any] | None = None,
        LanguageConfiguration: dict[str, Any] | None = None,
        AIVersion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_extraction_definition(
        self,
        *,
        ExtractionDefinitionId: str,
        InstanceId: str,
        Name: str,
        ExtractionConfiguration: dict[str, Any],
        ClientToken: str | None = None,
        Display: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_hours_of_operation(
        self,
        *,
        InstanceId: str,
        HoursOfOperationId: str,
        Name: str | None = None,
        Description: str | None = None,
        TimeZone: str | None = None,
        Config: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_hours_of_operation_override(
        self,
        *,
        InstanceId: str,
        HoursOfOperationId: str,
        HoursOfOperationOverrideId: str,
        Name: str | None = None,
        Description: str | None = None,
        Config: list[dict[str, Any]] | None = None,
        EffectiveFrom: str | None = None,
        EffectiveTill: str | None = None,
        RecurrenceConfig: dict[str, Any] | None = None,
        OverrideType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_instance_attribute(
        self,
        *,
        InstanceId: str,
        AttributeType: str,
        Value: str,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_instance_storage_config(
        self,
        *,
        InstanceId: str,
        AssociationId: str,
        ResourceType: str,
        StorageConfig: dict[str, Any],
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_metric_content(
        self,
        *,
        InstanceId: str,
        MetricId: str,
        MetricCalculation: dict[str, Any] | None = None,
        Unit: str | None = None,
        PositiveTrendIndicator: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_metric_metadata(
        self,
        *,
        InstanceId: str,
        MetricId: str,
        Name: str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_notification_content(
        self,
        *,
        InstanceId: str,
        NotificationId: str,
        Content: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_outbound_email_contact_message(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        EmailMessage: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_participant_authentication(
        self,
        *,
        State: str,
        InstanceId: str,
        Code: str | None = None,
        Error: str | None = None,
        ErrorDescription: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_participant_role_config(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        ChannelConfiguration: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_phone_number(
        self,
        *,
        PhoneNumberId: str,
        TargetArn: str | None = None,
        InstanceId: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_phone_number_metadata(
        self,
        *,
        PhoneNumberId: str,
        PhoneNumberDescription: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_predefined_attribute(
        self,
        *,
        InstanceId: str,
        Name: str,
        Values: dict[str, Any] | None = None,
        Purposes: list[str] | None = None,
        AttributeConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_prompt(
        self,
        *,
        InstanceId: str,
        PromptId: str,
        Name: str | None = None,
        Description: str | None = None,
        S3Uri: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_queue_hours_of_operation(
        self,
        *,
        InstanceId: str,
        QueueId: str,
        HoursOfOperationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_queue_max_contacts(
        self,
        *,
        InstanceId: str,
        QueueId: str,
        MaxContacts: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_queue_name(
        self,
        *,
        InstanceId: str,
        QueueId: str,
        Name: str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_queue_outbound_caller_config(
        self,
        *,
        InstanceId: str,
        QueueId: str,
        OutboundCallerConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_queue_outbound_email_config(
        self,
        *,
        InstanceId: str,
        QueueId: str,
        OutboundEmailConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_queue_status(
        self,
        *,
        InstanceId: str,
        QueueId: str,
        Status: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_quick_connect_config(
        self,
        *,
        InstanceId: str,
        QuickConnectId: str,
        QuickConnectConfig: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_quick_connect_name(
        self,
        *,
        InstanceId: str,
        QuickConnectId: str,
        Name: str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_routing_profile_agent_availability_timer(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
        AgentAvailabilityTimer: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_routing_profile_concurrency(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
        MediaConcurrencies: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_routing_profile_default_outbound_queue(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
        DefaultOutboundQueueId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_routing_profile_name(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
        Name: str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_routing_profile_queues(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
        QueueConfigs: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_rule(
        self,
        *,
        RuleId: str,
        InstanceId: str,
        Name: str,
        Function: str,
        Actions: list[dict[str, Any]],
        PublishStatus: str,
        PreEvaluationFilters: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_security_profile(
        self,
        *,
        SecurityProfileId: str,
        InstanceId: str,
        Description: str | None = None,
        Permissions: list[str] | None = None,
        AllowedAccessControlTags: dict[str, str] | None = None,
        TagRestrictedResources: list[str] | None = None,
        Applications: list[dict[str, Any]] | None = None,
        HierarchyRestrictedResources: list[str] | None = None,
        AllowedAccessControlHierarchyGroupId: str | None = None,
        AllowedFlowModules: list[dict[str, Any]] | None = None,
        AllowedAIAgents: list[dict[str, Any]] | None = None,
        GranularAccessControlConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_task_template(
        self,
        *,
        TaskTemplateId: str,
        InstanceId: str,
        Name: str | None = None,
        Description: str | None = None,
        ContactFlowId: str | None = None,
        SelfAssignFlowId: str | None = None,
        ContactHooks: dict[str, Any] | None = None,
        Constraints: dict[str, Any] | None = None,
        Defaults: dict[str, Any] | None = None,
        Status: str | None = None,
        Fields: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_test_case(
        self,
        *,
        InstanceId: str,
        TestCaseId: str,
        Content: str | None = None,
        EntryPoint: dict[str, Any] | None = None,
        InitializationData: str | None = None,
        Name: str | None = None,
        Description: str | None = None,
        Status: str | None = None,
        LastModifiedTime: datetime.datetime | str | None = None,
        LastModifiedRegion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_traffic_distribution(
        self,
        *,
        Id: str,
        TelephonyConfig: dict[str, Any] | None = None,
        SignInConfig: dict[str, Any] | None = None,
        AgentConfig: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user_config(
        self,
        *,
        UserId: str,
        InstanceId: str,
        AutoAcceptConfigs: list[dict[str, Any]] | None = None,
        AfterContactWorkConfigs: list[dict[str, Any]] | None = None,
        PhoneNumberConfigs: list[dict[str, Any]] | None = None,
        PersistentConnectionConfigs: list[dict[str, Any]] | None = None,
        VoiceEnhancementConfigs: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user_hierarchy(
        self,
        *,
        UserId: str,
        InstanceId: str,
        HierarchyGroupId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user_hierarchy_group_name(
        self,
        *,
        Name: str,
        HierarchyGroupId: str,
        InstanceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user_hierarchy_structure(
        self,
        *,
        HierarchyStructure: dict[str, Any],
        InstanceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user_identity_info(
        self,
        *,
        IdentityInfo: dict[str, Any],
        UserId: str,
        InstanceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user_notification_status(
        self,
        *,
        InstanceId: str,
        NotificationId: str,
        UserId: str,
        Status: str,
        LastModifiedTime: datetime.datetime | str | None = None,
        LastModifiedRegion: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user_phone_config(
        self,
        *,
        PhoneConfig: dict[str, Any],
        UserId: str,
        InstanceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user_proficiencies(
        self,
        *,
        InstanceId: str,
        UserId: str,
        UserProficiencies: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user_routing_profile(
        self,
        *,
        RoutingProfileId: str,
        UserId: str,
        InstanceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user_security_profiles(
        self,
        *,
        SecurityProfileIds: list[str],
        UserId: str,
        InstanceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_view_content(
        self,
        *,
        InstanceId: str,
        ViewId: str,
        Status: str,
        Content: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_view_metadata(
        self,
        *,
        InstanceId: str,
        ViewId: str,
        Name: str | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_workspace_metadata(
        self,
        *,
        InstanceId: str,
        WorkspaceId: str,
        Name: str | None = None,
        Description: str | None = None,
        Title: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_workspace_page(
        self,
        *,
        InstanceId: str,
        WorkspaceId: str,
        Page: str,
        NewPage: str | None = None,
        ResourceArn: str | None = None,
        Slug: str | None = None,
        InputData: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_workspace_theme(
        self,
        *,
        InstanceId: str,
        WorkspaceId: str,
        Theme: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_workspace_visibility(
        self,
        *,
        InstanceId: str,
        WorkspaceId: str,
        Visibility: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
