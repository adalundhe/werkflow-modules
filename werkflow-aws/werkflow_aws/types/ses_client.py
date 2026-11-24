from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class SESClient(ABC):

    @abstractmethod
    def associate_email_identity_certificate(
        self,
        *,
        EmailIdentity: str,
        CertificateArn: str,
        FromAddress: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def batch_get_metric_data(
        self,
        *,
        Queries: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_export_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_configuration_set(
        self,
        *,
        ConfigurationSetName: str,
        TrackingOptions: dict[str, Any] | None = None,
        DeliveryOptions: dict[str, Any] | None = None,
        ReputationOptions: dict[str, Any] | None = None,
        SendingOptions: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        SuppressionOptions: dict[str, Any] | None = None,
        VdmOptions: dict[str, Any] | None = None,
        ArchivingOptions: dict[str, Any] | None = None,
        MessageSecurityOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_configuration_set_event_destination(
        self,
        *,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_contact(
        self,
        *,
        ContactListName: str,
        EmailAddress: str,
        TopicPreferences: list[dict[str, Any]] | None = None,
        UnsubscribeAll: bool | None = None,
        AttributesData: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_contact_list(
        self,
        *,
        ContactListName: str,
        Topics: list[dict[str, Any]] | None = None,
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_custom_verification_email_template(
        self,
        *,
        TemplateName: str,
        FromEmailAddress: str,
        TemplateSubject: str,
        TemplateContent: str,
        SuccessRedirectionURL: str,
        FailureRedirectionURL: str,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_dedicated_ip_pool(
        self,
        *,
        PoolName: str,
        Tags: list[dict[str, Any]] | None = None,
        ScalingMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_deliverability_test_report(
        self,
        *,
        FromEmailAddress: str,
        Content: dict[str, Any],
        ReportName: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_email_identity(
        self,
        *,
        EmailIdentity: str,
        Tags: list[dict[str, Any]] | None = None,
        DkimSigningAttributes: dict[str, Any] | None = None,
        ConfigurationSetName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_email_identity_policy(
        self,
        *,
        EmailIdentity: str,
        PolicyName: str,
        Policy: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_email_template(
        self,
        *,
        TemplateName: str,
        TemplateContent: dict[str, Any],
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_export_job(
        self,
        *,
        ExportDataSource: dict[str, Any],
        ExportDestination: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_import_job(
        self,
        *,
        ImportDestination: dict[str, Any],
        ImportDataSource: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_multi_region_endpoint(
        self,
        *,
        EndpointName: str,
        Details: dict[str, Any],
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_tenant(
        self,
        *,
        TenantName: str,
        Tags: list[dict[str, Any]] | None = None,
        SuppressionAttributes: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_tenant_resource_association(
        self,
        *,
        TenantName: str,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_configuration_set(
        self,
        *,
        ConfigurationSetName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_configuration_set_event_destination(
        self,
        *,
        ConfigurationSetName: str,
        EventDestinationName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_contact(
        self,
        *,
        ContactListName: str,
        EmailAddress: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_contact_list(
        self,
        *,
        ContactListName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_custom_verification_email_template(
        self,
        *,
        TemplateName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_dedicated_ip_pool(
        self,
        *,
        PoolName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_email_identity(
        self,
        *,
        EmailIdentity: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_email_identity_policy(
        self,
        *,
        EmailIdentity: str,
        PolicyName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_email_template(
        self,
        *,
        TemplateName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_multi_region_endpoint(
        self,
        *,
        EndpointName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_suppressed_destination(
        self,
        *,
        EmailAddress: str,
        TenantName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_tenant(
        self,
        *,
        TenantName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_tenant_resource_association(
        self,
        *,
        TenantName: str,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_email_identity_certificate(
        self,
        *,
        EmailIdentity: str,
        FromAddress: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_account(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_blacklist_reports(
        self,
        *,
        BlacklistItemNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_configuration_set(
        self,
        *,
        ConfigurationSetName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_configuration_set_event_destinations(
        self,
        *,
        ConfigurationSetName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_contact(
        self,
        *,
        ContactListName: str,
        EmailAddress: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_contact_list(
        self,
        *,
        ContactListName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_custom_verification_email_template(
        self,
        *,
        TemplateName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_dedicated_ip(
        self,
        *,
        Ip: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_dedicated_ip_pool(
        self,
        *,
        PoolName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_dedicated_ips(
        self,
        *,
        PoolName: str | None = None,
        NextToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_deliverability_dashboard_options(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_deliverability_test_report(
        self,
        *,
        ReportId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_domain_deliverability_campaign(
        self,
        *,
        CampaignId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_domain_statistics_report(
        self,
        *,
        Domain: str,
        StartDate: datetime.datetime | str,
        EndDate: datetime.datetime | str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_email_address_insights(
        self,
        *,
        EmailAddress: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_email_identity(
        self,
        *,
        EmailIdentity: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_email_identity_policies(
        self,
        *,
        EmailIdentity: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_email_template(
        self,
        *,
        TemplateName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_export_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_import_job(
        self,
        *,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_message_insights(
        self,
        *,
        MessageId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_multi_region_endpoint(
        self,
        *,
        EndpointName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_reputation_entity(
        self,
        *,
        ReputationEntityReference: str,
        ReputationEntityType: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_suppressed_destination(
        self,
        *,
        EmailAddress: str,
        TenantName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_tenant(
        self,
        *,
        TenantName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_configuration_sets(
        self,
        *,
        Filter: dict[str, str] | None = None,
        NextToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_contact_lists(
        self,
        *,
        PageSize: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_contacts(
        self,
        *,
        ContactListName: str,
        Filter: dict[str, Any] | None = None,
        PageSize: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_custom_verification_email_templates(
        self,
        *,
        NextToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_dedicated_ip_pools(
        self,
        *,
        NextToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_deliverability_test_reports(
        self,
        *,
        NextToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_domain_deliverability_campaigns(
        self,
        *,
        StartDate: datetime.datetime | str,
        EndDate: datetime.datetime | str,
        SubscribedDomain: str,
        NextToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_email_identities(
        self,
        *,
        Filter: dict[str, str] | None = None,
        NextToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_email_identity_certificates(
        self,
        *,
        EmailIdentity: str,
        NextToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_email_templates(
        self,
        *,
        NextToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_export_jobs(
        self,
        *,
        NextToken: str | None = None,
        PageSize: int | None = None,
        ExportSourceType: str | None = None,
        JobStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_import_jobs(
        self,
        *,
        ImportDestinationType: str | None = None,
        NextToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_multi_region_endpoints(
        self,
        *,
        NextToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_recommendations(
        self,
        *,
        Filter: dict[str, str] | None = None,
        NextToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_reputation_entities(
        self,
        *,
        Filter: dict[str, str] | None = None,
        NextToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resource_tenants(
        self,
        *,
        ResourceArn: str,
        PageSize: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_suppressed_destinations(
        self,
        *,
        TenantName: str | None = None,
        Reasons: list[str] | None = None,
        StartDate: datetime.datetime | str | None = None,
        EndDate: datetime.datetime | str | None = None,
        NextToken: str | None = None,
        PageSize: int | None = None,
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
    def list_tenant_resources(
        self,
        *,
        TenantName: str,
        Filter: dict[str, str] | None = None,
        PageSize: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tenants(
        self,
        *,
        Filter: dict[str, str] | None = None,
        NextToken: str | None = None,
        PageSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_account_dedicated_ip_warmup_attributes(
        self,
        *,
        AutoWarmupEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_account_delivery_attributes(
        self,
        *,
        SharedPoolDeliveryMode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_account_details(
        self,
        *,
        MailType: str,
        WebsiteURL: str,
        ContactLanguage: str | None = None,
        UseCaseDescription: str | None = None,
        AdditionalContactEmailAddresses: list[str] | None = None,
        ProductionAccessEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_account_pricing_attributes(
        self,
        *,
        Plan: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_account_sending_attributes(
        self,
        *,
        SendingEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_account_suppression_attributes(
        self,
        *,
        SuppressedReasons: list[str] | None = None,
        ValidationAttributes: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_account_vdm_attributes(
        self,
        *,
        VdmAttributes: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_configuration_set_archiving_options(
        self,
        *,
        ConfigurationSetName: str,
        ArchiveArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_configuration_set_delivery_options(
        self,
        *,
        ConfigurationSetName: str,
        TlsPolicy: str | None = None,
        SendingPoolName: str | None = None,
        MaxDeliverySeconds: int | None = None,
        SharedPoolDeliveryMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_configuration_set_reputation_options(
        self,
        *,
        ConfigurationSetName: str,
        ReputationMetricsEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_configuration_set_sending_options(
        self,
        *,
        ConfigurationSetName: str,
        SendingEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_configuration_set_suppression_options(
        self,
        *,
        ConfigurationSetName: str,
        SuppressionScope: str | None = None,
        SuppressedReasons: list[str] | None = None,
        ValidationOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_configuration_set_tracking_options(
        self,
        *,
        ConfigurationSetName: str,
        CustomRedirectDomain: str | None = None,
        HttpsPolicy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_configuration_set_vdm_options(
        self,
        *,
        ConfigurationSetName: str,
        VdmOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_dedicated_ip_in_pool(
        self,
        *,
        Ip: str,
        DestinationPoolName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_dedicated_ip_pool_scaling_attributes(
        self,
        *,
        PoolName: str,
        ScalingMode: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_dedicated_ip_warmup_attributes(
        self,
        *,
        Ip: str,
        WarmupPercentage: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_deliverability_dashboard_option(
        self,
        *,
        DashboardEnabled: bool,
        SubscribedDomains: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_email_identity_configuration_set_attributes(
        self,
        *,
        EmailIdentity: str,
        ConfigurationSetName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_email_identity_dkim_attributes(
        self,
        *,
        EmailIdentity: str,
        SigningEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_email_identity_dkim_signing_attributes(
        self,
        *,
        EmailIdentity: str,
        SigningAttributesOrigin: str,
        SigningAttributes: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_email_identity_feedback_attributes(
        self,
        *,
        EmailIdentity: str,
        EmailForwardingEnabled: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_email_identity_mail_from_attributes(
        self,
        *,
        EmailIdentity: str,
        MailFromDomain: str | None = None,
        BehaviorOnMxFailure: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_suppressed_destination(
        self,
        *,
        EmailAddress: str,
        Reason: str,
        TenantName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_tenant_suppression_attributes(
        self,
        *,
        TenantName: str,
        SuppressedReasons: list[str] | None = None,
        SuppressionScope: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_bulk_email(
        self,
        *,
        DefaultContent: dict[str, Any],
        BulkEmailEntries: list[dict[str, Any]],
        FromEmailAddress: str | None = None,
        FromEmailAddressIdentityArn: str | None = None,
        ReplyToAddresses: list[str] | None = None,
        FeedbackForwardingEmailAddress: str | None = None,
        FeedbackForwardingEmailAddressIdentityArn: str | None = None,
        DefaultEmailTags: list[dict[str, Any]] | None = None,
        ConfigurationSetName: str | None = None,
        EndpointId: str | None = None,
        TenantName: str | None = None,
        ConfigurationOverrides: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_custom_verification_email(
        self,
        *,
        EmailAddress: str,
        TemplateName: str,
        ConfigurationSetName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_email(
        self,
        *,
        Content: dict[str, Any],
        FromEmailAddress: str | None = None,
        FromEmailAddressIdentityArn: str | None = None,
        Destination: dict[str, Any] | None = None,
        ReplyToAddresses: list[str] | None = None,
        FeedbackForwardingEmailAddress: str | None = None,
        FeedbackForwardingEmailAddressIdentityArn: str | None = None,
        EmailTags: list[dict[str, Any]] | None = None,
        ConfigurationSetName: str | None = None,
        EndpointId: str | None = None,
        TenantName: str | None = None,
        ListManagementOptions: dict[str, Any] | None = None,
        ConfigurationOverrides: dict[str, Any] | None = None,
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
    def test_render_email_template(
        self,
        *,
        TemplateName: str,
        TemplateData: str,
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
    def update_configuration_set(
        self,
        *,
        ConfigurationSetName: str,
        MessageSecurityOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_configuration_set_event_destination(
        self,
        *,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_contact(
        self,
        *,
        ContactListName: str,
        EmailAddress: str,
        TopicPreferences: list[dict[str, Any]] | None = None,
        UnsubscribeAll: bool | None = None,
        AttributesData: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_contact_list(
        self,
        *,
        ContactListName: str,
        Topics: list[dict[str, Any]] | None = None,
        Description: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_custom_verification_email_template(
        self,
        *,
        TemplateName: str,
        FromEmailAddress: str,
        TemplateSubject: str,
        TemplateContent: str,
        SuccessRedirectionURL: str,
        FailureRedirectionURL: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_email_identity_policy(
        self,
        *,
        EmailIdentity: str,
        PolicyName: str,
        Policy: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_email_template(
        self,
        *,
        TemplateName: str,
        TemplateContent: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_reputation_entity_customer_managed_status(
        self,
        *,
        ReputationEntityType: str,
        ReputationEntityReference: str,
        SendingStatus: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_reputation_entity_policy(
        self,
        *,
        ReputationEntityType: str,
        ReputationEntityReference: str,
        ReputationEntityPolicy: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
