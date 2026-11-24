from abc import ABC, abstractmethod
import datetime
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class EndUserMessagingClient(ABC):

    @abstractmethod
    def associate_origination_identity(
        self,
        *,
        PoolId: str,
        OriginationIdentity: str,
        IsoCountryCode: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_protect_configuration(
        self,
        *,
        ProtectConfigurationId: str,
        ConfigurationSetName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def carrier_lookup(
        self,
        *,
        PhoneNumber: str,
        EnableCleansing: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_configuration_set(
        self,
        *,
        ConfigurationSetName: str,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_event_destination(
        self,
        *,
        ConfigurationSetName: str,
        EventDestinationName: str,
        MatchingEventTypes: list[str],
        CloudWatchLogsDestination: dict[str, Any] | None = None,
        KinesisFirehoseDestination: dict[str, Any] | None = None,
        SnsDestination: dict[str, Any] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_notify_configuration(
        self,
        *,
        DisplayName: str,
        UseCase: str,
        EnabledChannels: list[str],
        DefaultTemplateId: str | None = None,
        PoolId: str | None = None,
        EnabledCountries: list[str] | None = None,
        DeletionProtectionEnabled: bool | None = None,
        ClientToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_opt_out_list(
        self,
        *,
        OptOutListName: str,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_pool(
        self,
        *,
        OriginationIdentity: str,
        MessageType: str,
        IsoCountryCode: str | None = None,
        DeletionProtectionEnabled: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_protect_configuration(
        self,
        *,
        ClientToken: str | None = None,
        DeletionProtectionEnabled: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_rcs_agent(
        self,
        *,
        DeletionProtectionEnabled: bool | None = None,
        OptOutListName: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_registration(
        self,
        *,
        RegistrationType: str,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_registration_association(
        self,
        *,
        RegistrationId: str,
        ResourceId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_registration_attachment(
        self,
        *,
        AttachmentBody: bytes | BinaryIO | str | None = None,
        AttachmentUrl: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_registration_version(
        self,
        *,
        RegistrationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_verified_destination_number(
        self,
        *,
        DestinationPhoneNumber: str,
        RcsAgentId: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_account_default_protect_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_configuration_set(
        self,
        *,
        ConfigurationSetName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_default_message_type(
        self,
        *,
        ConfigurationSetName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_default_sender_id(
        self,
        *,
        ConfigurationSetName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_event_destination(
        self,
        *,
        ConfigurationSetName: str,
        EventDestinationName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_keyword(
        self,
        *,
        OriginationIdentity: str,
        Keyword: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_media_message_spend_limit_override(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_notify_configuration(
        self,
        *,
        NotifyConfigurationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_notify_message_spend_limit_override(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_opt_out_list(
        self,
        *,
        OptOutListName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_opted_out_number(
        self,
        *,
        OptOutListName: str,
        OptedOutNumber: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_pool(
        self,
        *,
        PoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_protect_configuration(
        self,
        *,
        ProtectConfigurationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_protect_configuration_rule_set_number_override(
        self,
        *,
        ProtectConfigurationId: str,
        DestinationPhoneNumber: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_rcs_agent(
        self,
        *,
        RcsAgentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_rcs_message_spend_limit_override(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_registration(
        self,
        *,
        RegistrationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_registration_attachment(
        self,
        *,
        RegistrationAttachmentId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_registration_field_value(
        self,
        *,
        RegistrationId: str,
        FieldPath: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_policy(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_text_message_spend_limit_override(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_verified_destination_number(
        self,
        *,
        VerifiedDestinationNumberId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_voice_message_spend_limit_override(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_attributes(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_account_limits(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_configuration_sets(
        self,
        *,
        ConfigurationSetNames: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_keywords(
        self,
        *,
        OriginationIdentity: str,
        Keywords: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_notify_configurations(
        self,
        *,
        NotifyConfigurationIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_notify_templates(
        self,
        *,
        TemplateIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_opt_out_lists(
        self,
        *,
        OptOutListNames: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Owner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_opted_out_numbers(
        self,
        *,
        OptOutListName: str,
        OptedOutNumbers: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_phone_numbers(
        self,
        *,
        PhoneNumberIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Owner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_pools(
        self,
        *,
        PoolIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Owner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_protect_configurations(
        self,
        *,
        ProtectConfigurationIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_rcs_agent_country_launch_status(
        self,
        *,
        RcsAgentId: str,
        IsoCountryCodes: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_rcs_agents(
        self,
        *,
        RcsAgentIds: list[str] | None = None,
        Owner: str | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_registration_attachments(
        self,
        *,
        RegistrationAttachmentIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_registration_field_definitions(
        self,
        *,
        RegistrationType: str,
        SectionPath: str | None = None,
        FieldPaths: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_registration_field_values(
        self,
        *,
        RegistrationId: str,
        VersionNumber: int | None = None,
        SectionPath: str | None = None,
        FieldPaths: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_registration_section_definitions(
        self,
        *,
        RegistrationType: str,
        SectionPaths: list[str] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_registration_type_definitions(
        self,
        *,
        RegistrationTypes: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_registration_versions(
        self,
        *,
        RegistrationId: str,
        VersionNumbers: list[int] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_registrations(
        self,
        *,
        RegistrationIds: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_sender_ids(
        self,
        *,
        SenderIds: list[dict[str, Any]] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        Owner: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_spend_limits(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_verified_destination_numbers(
        self,
        *,
        VerifiedDestinationNumberIds: list[str] | None = None,
        DestinationPhoneNumbers: list[str] | None = None,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_origination_identity(
        self,
        *,
        PoolId: str,
        OriginationIdentity: str,
        IsoCountryCode: str | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_protect_configuration(
        self,
        *,
        ProtectConfigurationId: str,
        ConfigurationSetName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def discard_registration_version(
        self,
        *,
        RegistrationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_protect_configuration_country_rule_set(
        self,
        *,
        ProtectConfigurationId: str,
        NumberCapability: str,
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
    def list_available_phone_numbers(
        self,
        *,
        IsoCountryCode: str,
        NumberCapabilities: list[str],
        NumberType: str,
        RegistrationId: str | None = None,
        NumberPreference: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_notify_countries(
        self,
        *,
        Channels: list[str] | None = None,
        UseCases: list[str] | None = None,
        Tier: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_pool_origination_identities(
        self,
        *,
        PoolId: str,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_protect_configuration_rule_set_number_overrides(
        self,
        *,
        ProtectConfigurationId: str,
        Filters: list[dict[str, Any]] | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_registration_associations(
        self,
        *,
        RegistrationId: str,
        Filters: list[dict[str, Any]] | None = None,
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
    def put_keyword(
        self,
        *,
        OriginationIdentity: str,
        Keyword: str,
        KeywordMessage: str,
        KeywordAction: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_message_feedback(
        self,
        *,
        MessageId: str,
        MessageFeedbackStatus: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_opted_out_number(
        self,
        *,
        OptOutListName: str,
        OptedOutNumber: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_protect_configuration_rule_set_number_override(
        self,
        *,
        ProtectConfigurationId: str,
        DestinationPhoneNumber: str,
        Action: str,
        ClientToken: str | None = None,
        ExpirationTimestamp: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_registration_field_value(
        self,
        *,
        RegistrationId: str,
        FieldPath: str,
        SelectChoices: list[str] | None = None,
        TextValue: str | None = None,
        RegistrationAttachmentId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_resource_policy(
        self,
        *,
        ResourceArn: str,
        Policy: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def release_phone_number(
        self,
        *,
        PhoneNumberId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def release_sender_id(
        self,
        *,
        SenderId: str,
        IsoCountryCode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def request_phone_number(
        self,
        *,
        IsoCountryCode: str,
        MessageType: str,
        NumberCapabilities: list[str],
        NumberType: str,
        OptOutListName: str | None = None,
        PoolId: str | None = None,
        RegistrationId: str | None = None,
        NumberPreference: list[dict[str, Any]] | None = None,
        InternationalSendingEnabled: bool | None = None,
        DeletionProtectionEnabled: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def request_sender_id(
        self,
        *,
        SenderId: str,
        IsoCountryCode: str,
        MessageTypes: list[str] | None = None,
        DeletionProtectionEnabled: bool | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ClientToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_destination_number_verification_code(
        self,
        *,
        VerifiedDestinationNumberId: str,
        VerificationChannel: str,
        LanguageCode: str | None = None,
        OriginationIdentity: str | None = None,
        ConfigurationSetName: str | None = None,
        Context: dict[str, str] | None = None,
        DestinationCountryParameters: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_media_message(
        self,
        *,
        DestinationPhoneNumber: str,
        OriginationIdentity: str,
        MessageBody: str | None = None,
        MediaUrls: list[str] | None = None,
        ConfigurationSetName: str | None = None,
        MaxPrice: str | None = None,
        TimeToLive: int | None = None,
        Context: dict[str, str] | None = None,
        DryRun: bool | None = None,
        ProtectConfigurationId: str | None = None,
        MessageFeedbackEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_notify_text_message(
        self,
        *,
        NotifyConfigurationId: str,
        DestinationPhoneNumber: str,
        TemplateVariables: dict[str, str],
        TemplateId: str | None = None,
        TimeToLive: int | None = None,
        Context: dict[str, str] | None = None,
        ConfigurationSetName: str | None = None,
        DryRun: bool | None = None,
        MessageFeedbackEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_notify_voice_message(
        self,
        *,
        NotifyConfigurationId: str,
        DestinationPhoneNumber: str,
        TemplateVariables: dict[str, str],
        TemplateId: str | None = None,
        VoiceId: str | None = None,
        TimeToLive: int | None = None,
        Context: dict[str, str] | None = None,
        ConfigurationSetName: str | None = None,
        DryRun: bool | None = None,
        MessageFeedbackEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_rcs_message(
        self,
        *,
        DestinationPhoneNumber: str,
        OriginationIdentity: str,
        RcsMessageContent: dict[str, Any] | None = None,
        TimeToLive: int | None = None,
        MessageTrafficType: str | None = None,
        FallbackConfiguration: dict[str, Any] | None = None,
        ProtectConfigurationId: str | None = None,
        ConfigurationSetName: str | None = None,
        MaxPrice: str | None = None,
        DryRun: bool | None = None,
        Context: dict[str, str] | None = None,
        MessageFeedbackEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_text_message(
        self,
        *,
        DestinationPhoneNumber: str,
        OriginationIdentity: str | None = None,
        MessageBody: str | None = None,
        MessageType: str | None = None,
        Keyword: str | None = None,
        ConfigurationSetName: str | None = None,
        MaxPrice: str | None = None,
        TimeToLive: int | None = None,
        Context: dict[str, str] | None = None,
        DestinationCountryParameters: dict[str, str] | None = None,
        DryRun: bool | None = None,
        ProtectConfigurationId: str | None = None,
        MessageFeedbackEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_voice_message(
        self,
        *,
        DestinationPhoneNumber: str,
        OriginationIdentity: str,
        MessageBody: str | None = None,
        MessageBodyTextType: str | None = None,
        VoiceId: str | None = None,
        ConfigurationSetName: str | None = None,
        MaxPricePerMinute: str | None = None,
        TimeToLive: int | None = None,
        Context: dict[str, str] | None = None,
        DryRun: bool | None = None,
        ProtectConfigurationId: str | None = None,
        MessageFeedbackEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_account_default_protect_configuration(
        self,
        *,
        ProtectConfigurationId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_default_message_feedback_enabled(
        self,
        *,
        ConfigurationSetName: str,
        MessageFeedbackEnabled: bool,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_default_message_type(
        self,
        *,
        ConfigurationSetName: str,
        MessageType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_default_sender_id(
        self,
        *,
        ConfigurationSetName: str,
        SenderId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_media_message_spend_limit_override(
        self,
        *,
        MonthlyLimit: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_notify_message_spend_limit_override(
        self,
        *,
        MonthlyLimit: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_rcs_message_spend_limit_override(
        self,
        *,
        MonthlyLimit: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_text_message_spend_limit_override(
        self,
        *,
        MonthlyLimit: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_voice_message_spend_limit_override(
        self,
        *,
        MonthlyLimit: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def submit_registration_version(
        self,
        *,
        RegistrationId: str,
        AwsReview: bool | None = None,
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
    def update_event_destination(
        self,
        *,
        ConfigurationSetName: str,
        EventDestinationName: str,
        Enabled: bool | None = None,
        MatchingEventTypes: list[str] | None = None,
        CloudWatchLogsDestination: dict[str, Any] | None = None,
        KinesisFirehoseDestination: dict[str, Any] | None = None,
        SnsDestination: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_notify_configuration(
        self,
        *,
        NotifyConfigurationId: str,
        DefaultTemplateId: str | None = None,
        PoolId: str | None = None,
        EnabledCountries: list[str] | None = None,
        EnabledChannels: list[str] | None = None,
        DeletionProtectionEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_phone_number(
        self,
        *,
        PhoneNumberId: str,
        TwoWayEnabled: bool | None = None,
        TwoWayChannelArn: str | None = None,
        TwoWayChannelRole: str | None = None,
        SelfManagedOptOutsEnabled: bool | None = None,
        OptOutListName: str | None = None,
        InternationalSendingEnabled: bool | None = None,
        DeletionProtectionEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_pool(
        self,
        *,
        PoolId: str,
        TwoWayEnabled: bool | None = None,
        TwoWayChannelArn: str | None = None,
        TwoWayChannelRole: str | None = None,
        SelfManagedOptOutsEnabled: bool | None = None,
        OptOutListName: str | None = None,
        SharedRoutesEnabled: bool | None = None,
        DeletionProtectionEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_protect_configuration(
        self,
        *,
        ProtectConfigurationId: str,
        DeletionProtectionEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_protect_configuration_country_rule_set(
        self,
        *,
        ProtectConfigurationId: str,
        NumberCapability: str,
        CountryRuleSetUpdates: dict[str, dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_rcs_agent(
        self,
        *,
        RcsAgentId: str,
        DeletionProtectionEnabled: bool | None = None,
        OptOutListName: str | None = None,
        SelfManagedOptOutsEnabled: bool | None = None,
        TwoWayChannelArn: str | None = None,
        TwoWayChannelRole: str | None = None,
        TwoWayEnabled: bool | None = None,
        TwoWayMediaS3BucketName: str | None = None,
        TwoWayMediaS3KeyPrefix: str | None = None,
        TwoWayMediaS3Role: str | None = None,
        TwoWayRcsEventsEnabled: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_sender_id(
        self,
        *,
        SenderId: str,
        IsoCountryCode: str,
        DeletionProtectionEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def verify_destination_number(
        self,
        *,
        VerifiedDestinationNumberId: str,
        VerificationCode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
