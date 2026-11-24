from werkflow_aws.models.ses import (
    SESAssociateEmailIdentityCertificateRequest,
    SESAssociateEmailIdentityCertificateResponse,
    SESBatchGetMetricDataRequest,
    SESBatchGetMetricDataResponse,
    SESCancelExportJobRequest,
    SESCancelExportJobResponse,
    SESCreateConfigurationSetEventDestinationRequest,
    SESCreateConfigurationSetEventDestinationResponse,
    SESCreateConfigurationSetRequest,
    SESCreateConfigurationSetResponse,
    SESCreateContactListRequest,
    SESCreateContactListResponse,
    SESCreateContactRequest,
    SESCreateContactResponse,
    SESCreateCustomVerificationEmailTemplateRequest,
    SESCreateCustomVerificationEmailTemplateResponse,
    SESCreateDedicatedIpPoolRequest,
    SESCreateDedicatedIpPoolResponse,
    SESCreateDeliverabilityTestReportRequest,
    SESCreateDeliverabilityTestReportResponse,
    SESCreateEmailIdentityPolicyRequest,
    SESCreateEmailIdentityPolicyResponse,
    SESCreateEmailIdentityRequest,
    SESCreateEmailIdentityResponse,
    SESCreateEmailTemplateRequest,
    SESCreateEmailTemplateResponse,
    SESCreateExportJobRequest,
    SESCreateExportJobResponse,
    SESCreateImportJobRequest,
    SESCreateImportJobResponse,
    SESCreateMultiRegionEndpointRequest,
    SESCreateMultiRegionEndpointResponse,
    SESCreateTenantRequest,
    SESCreateTenantResourceAssociationRequest,
    SESCreateTenantResourceAssociationResponse,
    SESCreateTenantResponse,
    SESDeleteConfigurationSetEventDestinationRequest,
    SESDeleteConfigurationSetEventDestinationResponse,
    SESDeleteConfigurationSetRequest,
    SESDeleteConfigurationSetResponse,
    SESDeleteContactListRequest,
    SESDeleteContactListResponse,
    SESDeleteContactRequest,
    SESDeleteContactResponse,
    SESDeleteCustomVerificationEmailTemplateRequest,
    SESDeleteCustomVerificationEmailTemplateResponse,
    SESDeleteDedicatedIpPoolRequest,
    SESDeleteDedicatedIpPoolResponse,
    SESDeleteEmailIdentityPolicyRequest,
    SESDeleteEmailIdentityPolicyResponse,
    SESDeleteEmailIdentityRequest,
    SESDeleteEmailIdentityResponse,
    SESDeleteEmailTemplateRequest,
    SESDeleteEmailTemplateResponse,
    SESDeleteMultiRegionEndpointRequest,
    SESDeleteMultiRegionEndpointResponse,
    SESDeleteSuppressedDestinationRequest,
    SESDeleteSuppressedDestinationResponse,
    SESDeleteTenantRequest,
    SESDeleteTenantResourceAssociationRequest,
    SESDeleteTenantResourceAssociationResponse,
    SESDeleteTenantResponse,
    SESDisassociateEmailIdentityCertificateRequest,
    SESDisassociateEmailIdentityCertificateResponse,
    SESGetAccountRequest,
    SESGetAccountResponse,
    SESGetBlacklistReportsRequest,
    SESGetBlacklistReportsResponse,
    SESGetConfigurationSetEventDestinationsRequest,
    SESGetConfigurationSetEventDestinationsResponse,
    SESGetConfigurationSetRequest,
    SESGetConfigurationSetResponse,
    SESGetContactListRequest,
    SESGetContactListResponse,
    SESGetContactRequest,
    SESGetContactResponse,
    SESGetCustomVerificationEmailTemplateRequest,
    SESGetCustomVerificationEmailTemplateResponse,
    SESGetDedicatedIpPoolRequest,
    SESGetDedicatedIpPoolResponse,
    SESGetDedicatedIpRequest,
    SESGetDedicatedIpResponse,
    SESGetDedicatedIpsRequest,
    SESGetDedicatedIpsResponse,
    SESGetDeliverabilityDashboardOptionsRequest,
    SESGetDeliverabilityDashboardOptionsResponse,
    SESGetDeliverabilityTestReportRequest,
    SESGetDeliverabilityTestReportResponse,
    SESGetDomainDeliverabilityCampaignRequest,
    SESGetDomainDeliverabilityCampaignResponse,
    SESGetDomainStatisticsReportRequest,
    SESGetDomainStatisticsReportResponse,
    SESGetEmailAddressInsightsRequest,
    SESGetEmailAddressInsightsResponse,
    SESGetEmailIdentityPoliciesRequest,
    SESGetEmailIdentityPoliciesResponse,
    SESGetEmailIdentityRequest,
    SESGetEmailIdentityResponse,
    SESGetEmailTemplateRequest,
    SESGetEmailTemplateResponse,
    SESGetExportJobRequest,
    SESGetExportJobResponse,
    SESGetImportJobRequest,
    SESGetImportJobResponse,
    SESGetMessageInsightsRequest,
    SESGetMessageInsightsResponse,
    SESGetMultiRegionEndpointRequest,
    SESGetMultiRegionEndpointResponse,
    SESGetReputationEntityRequest,
    SESGetReputationEntityResponse,
    SESGetSuppressedDestinationRequest,
    SESGetSuppressedDestinationResponse,
    SESGetTenantRequest,
    SESGetTenantResponse,
    SESListConfigurationSetsRequest,
    SESListConfigurationSetsResponse,
    SESListContactListsRequest,
    SESListContactListsResponse,
    SESListContactsRequest,
    SESListContactsResponse,
    SESListCustomVerificationEmailTemplatesRequest,
    SESListCustomVerificationEmailTemplatesResponse,
    SESListDedicatedIpPoolsRequest,
    SESListDedicatedIpPoolsResponse,
    SESListDeliverabilityTestReportsRequest,
    SESListDeliverabilityTestReportsResponse,
    SESListDomainDeliverabilityCampaignsRequest,
    SESListDomainDeliverabilityCampaignsResponse,
    SESListEmailIdentitiesRequest,
    SESListEmailIdentitiesResponse,
    SESListEmailIdentityCertificatesRequest,
    SESListEmailIdentityCertificatesResponse,
    SESListEmailTemplatesRequest,
    SESListEmailTemplatesResponse,
    SESListExportJobsRequest,
    SESListExportJobsResponse,
    SESListImportJobsRequest,
    SESListImportJobsResponse,
    SESListMultiRegionEndpointsRequest,
    SESListMultiRegionEndpointsResponse,
    SESListRecommendationsRequest,
    SESListRecommendationsResponse,
    SESListReputationEntitiesRequest,
    SESListReputationEntitiesResponse,
    SESListResourceTenantsRequest,
    SESListResourceTenantsResponse,
    SESListSuppressedDestinationsRequest,
    SESListSuppressedDestinationsResponse,
    SESListTagsForResourceRequest,
    SESListTagsForResourceResponse,
    SESListTenantResourcesRequest,
    SESListTenantResourcesResponse,
    SESListTenantsRequest,
    SESListTenantsResponse,
    SESPutAccountDedicatedIpWarmupAttributesRequest,
    SESPutAccountDedicatedIpWarmupAttributesResponse,
    SESPutAccountDeliveryAttributesRequest,
    SESPutAccountDeliveryAttributesResponse,
    SESPutAccountDetailsRequest,
    SESPutAccountDetailsResponse,
    SESPutAccountPricingAttributesRequest,
    SESPutAccountPricingAttributesResponse,
    SESPutAccountSendingAttributesRequest,
    SESPutAccountSendingAttributesResponse,
    SESPutAccountSuppressionAttributesRequest,
    SESPutAccountSuppressionAttributesResponse,
    SESPutAccountVdmAttributesRequest,
    SESPutAccountVdmAttributesResponse,
    SESPutConfigurationSetArchivingOptionsRequest,
    SESPutConfigurationSetArchivingOptionsResponse,
    SESPutConfigurationSetDeliveryOptionsRequest,
    SESPutConfigurationSetDeliveryOptionsResponse,
    SESPutConfigurationSetReputationOptionsRequest,
    SESPutConfigurationSetReputationOptionsResponse,
    SESPutConfigurationSetSendingOptionsRequest,
    SESPutConfigurationSetSendingOptionsResponse,
    SESPutConfigurationSetSuppressionOptionsRequest,
    SESPutConfigurationSetSuppressionOptionsResponse,
    SESPutConfigurationSetTrackingOptionsRequest,
    SESPutConfigurationSetTrackingOptionsResponse,
    SESPutConfigurationSetVdmOptionsRequest,
    SESPutConfigurationSetVdmOptionsResponse,
    SESPutDedicatedIpInPoolRequest,
    SESPutDedicatedIpInPoolResponse,
    SESPutDedicatedIpPoolScalingAttributesRequest,
    SESPutDedicatedIpPoolScalingAttributesResponse,
    SESPutDedicatedIpWarmupAttributesRequest,
    SESPutDedicatedIpWarmupAttributesResponse,
    SESPutDeliverabilityDashboardOptionRequest,
    SESPutDeliverabilityDashboardOptionResponse,
    SESPutEmailIdentityConfigurationSetAttributesRequest,
    SESPutEmailIdentityConfigurationSetAttributesResponse,
    SESPutEmailIdentityDkimAttributesRequest,
    SESPutEmailIdentityDkimAttributesResponse,
    SESPutEmailIdentityDkimSigningAttributesRequest,
    SESPutEmailIdentityDkimSigningAttributesResponse,
    SESPutEmailIdentityFeedbackAttributesRequest,
    SESPutEmailIdentityFeedbackAttributesResponse,
    SESPutEmailIdentityMailFromAttributesRequest,
    SESPutEmailIdentityMailFromAttributesResponse,
    SESPutSuppressedDestinationRequest,
    SESPutSuppressedDestinationResponse,
    SESPutTenantSuppressionAttributesRequest,
    SESPutTenantSuppressionAttributesResponse,
    SESSendBulkEmailRequest,
    SESSendBulkEmailResponse,
    SESSendCustomVerificationEmailRequest,
    SESSendCustomVerificationEmailResponse,
    SESSendEmailRequest,
    SESSendEmailResponse,
    SESTagResourceRequest,
    SESTagResourceResponse,
    SESTestRenderEmailTemplateRequest,
    SESTestRenderEmailTemplateResponse,
    SESUntagResourceRequest,
    SESUntagResourceResponse,
    SESUpdateConfigurationSetEventDestinationRequest,
    SESUpdateConfigurationSetEventDestinationResponse,
    SESUpdateConfigurationSetRequest,
    SESUpdateConfigurationSetResponse,
    SESUpdateContactListRequest,
    SESUpdateContactListResponse,
    SESUpdateContactRequest,
    SESUpdateContactResponse,
    SESUpdateCustomVerificationEmailTemplateRequest,
    SESUpdateCustomVerificationEmailTemplateResponse,
    SESUpdateEmailIdentityPolicyRequest,
    SESUpdateEmailIdentityPolicyResponse,
    SESUpdateEmailTemplateRequest,
    SESUpdateEmailTemplateResponse,
    SESUpdateReputationEntityCustomerManagedStatusRequest,
    SESUpdateReputationEntityCustomerManagedStatusResponse,
    SESUpdateReputationEntityPolicyRequest,
    SESUpdateReputationEntityPolicyResponse,
)
from werkflow_aws.types.ses_client import SESClient
from .base import AWSBaseService


class AWSSES(AWSBaseService[SESClient]):
    service_name = 'ses'
    boto3_service_name = 'sesv2'

    def __init__(self) -> None:
        super().__init__(service_name='ses', boto3_service_name='sesv2')

    async def associate_email_identity_certificate(
        self,
        request: SESAssociateEmailIdentityCertificateRequest,
    ) -> SESAssociateEmailIdentityCertificateResponse:
        client = self._require_client()
        return await self._execute(client.associate_email_identity_certificate, request, SESAssociateEmailIdentityCertificateResponse)

    async def batch_get_metric_data(
        self,
        request: SESBatchGetMetricDataRequest,
    ) -> SESBatchGetMetricDataResponse:
        client = self._require_client()
        return await self._execute(client.batch_get_metric_data, request, SESBatchGetMetricDataResponse)

    async def cancel_export_job(
        self,
        request: SESCancelExportJobRequest,
    ) -> SESCancelExportJobResponse:
        client = self._require_client()
        return await self._execute(client.cancel_export_job, request, SESCancelExportJobResponse)

    async def create_configuration_set(
        self,
        request: SESCreateConfigurationSetRequest,
    ) -> SESCreateConfigurationSetResponse:
        client = self._require_client()
        return await self._execute(client.create_configuration_set, request, SESCreateConfigurationSetResponse)

    async def create_configuration_set_event_destination(
        self,
        request: SESCreateConfigurationSetEventDestinationRequest,
    ) -> SESCreateConfigurationSetEventDestinationResponse:
        client = self._require_client()
        return await self._execute(client.create_configuration_set_event_destination, request, SESCreateConfigurationSetEventDestinationResponse)

    async def create_contact(
        self,
        request: SESCreateContactRequest,
    ) -> SESCreateContactResponse:
        client = self._require_client()
        return await self._execute(client.create_contact, request, SESCreateContactResponse)

    async def create_contact_list(
        self,
        request: SESCreateContactListRequest,
    ) -> SESCreateContactListResponse:
        client = self._require_client()
        return await self._execute(client.create_contact_list, request, SESCreateContactListResponse)

    async def create_custom_verification_email_template(
        self,
        request: SESCreateCustomVerificationEmailTemplateRequest,
    ) -> SESCreateCustomVerificationEmailTemplateResponse:
        client = self._require_client()
        return await self._execute(client.create_custom_verification_email_template, request, SESCreateCustomVerificationEmailTemplateResponse)

    async def create_dedicated_ip_pool(
        self,
        request: SESCreateDedicatedIpPoolRequest,
    ) -> SESCreateDedicatedIpPoolResponse:
        client = self._require_client()
        return await self._execute(client.create_dedicated_ip_pool, request, SESCreateDedicatedIpPoolResponse)

    async def create_deliverability_test_report(
        self,
        request: SESCreateDeliverabilityTestReportRequest,
    ) -> SESCreateDeliverabilityTestReportResponse:
        client = self._require_client()
        return await self._execute(client.create_deliverability_test_report, request, SESCreateDeliverabilityTestReportResponse)

    async def create_email_identity(
        self,
        request: SESCreateEmailIdentityRequest,
    ) -> SESCreateEmailIdentityResponse:
        client = self._require_client()
        return await self._execute(client.create_email_identity, request, SESCreateEmailIdentityResponse)

    async def create_email_identity_policy(
        self,
        request: SESCreateEmailIdentityPolicyRequest,
    ) -> SESCreateEmailIdentityPolicyResponse:
        client = self._require_client()
        return await self._execute(client.create_email_identity_policy, request, SESCreateEmailIdentityPolicyResponse)

    async def create_email_template(
        self,
        request: SESCreateEmailTemplateRequest,
    ) -> SESCreateEmailTemplateResponse:
        client = self._require_client()
        return await self._execute(client.create_email_template, request, SESCreateEmailTemplateResponse)

    async def create_export_job(
        self,
        request: SESCreateExportJobRequest,
    ) -> SESCreateExportJobResponse:
        client = self._require_client()
        return await self._execute(client.create_export_job, request, SESCreateExportJobResponse)

    async def create_import_job(
        self,
        request: SESCreateImportJobRequest,
    ) -> SESCreateImportJobResponse:
        client = self._require_client()
        return await self._execute(client.create_import_job, request, SESCreateImportJobResponse)

    async def create_multi_region_endpoint(
        self,
        request: SESCreateMultiRegionEndpointRequest,
    ) -> SESCreateMultiRegionEndpointResponse:
        client = self._require_client()
        return await self._execute(client.create_multi_region_endpoint, request, SESCreateMultiRegionEndpointResponse)

    async def create_tenant(
        self,
        request: SESCreateTenantRequest,
    ) -> SESCreateTenantResponse:
        client = self._require_client()
        return await self._execute(client.create_tenant, request, SESCreateTenantResponse)

    async def create_tenant_resource_association(
        self,
        request: SESCreateTenantResourceAssociationRequest,
    ) -> SESCreateTenantResourceAssociationResponse:
        client = self._require_client()
        return await self._execute(client.create_tenant_resource_association, request, SESCreateTenantResourceAssociationResponse)

    async def delete_configuration_set(
        self,
        request: SESDeleteConfigurationSetRequest,
    ) -> SESDeleteConfigurationSetResponse:
        client = self._require_client()
        return await self._execute(client.delete_configuration_set, request, SESDeleteConfigurationSetResponse)

    async def delete_configuration_set_event_destination(
        self,
        request: SESDeleteConfigurationSetEventDestinationRequest,
    ) -> SESDeleteConfigurationSetEventDestinationResponse:
        client = self._require_client()
        return await self._execute(client.delete_configuration_set_event_destination, request, SESDeleteConfigurationSetEventDestinationResponse)

    async def delete_contact(
        self,
        request: SESDeleteContactRequest,
    ) -> SESDeleteContactResponse:
        client = self._require_client()
        return await self._execute(client.delete_contact, request, SESDeleteContactResponse)

    async def delete_contact_list(
        self,
        request: SESDeleteContactListRequest,
    ) -> SESDeleteContactListResponse:
        client = self._require_client()
        return await self._execute(client.delete_contact_list, request, SESDeleteContactListResponse)

    async def delete_custom_verification_email_template(
        self,
        request: SESDeleteCustomVerificationEmailTemplateRequest,
    ) -> SESDeleteCustomVerificationEmailTemplateResponse:
        client = self._require_client()
        return await self._execute(client.delete_custom_verification_email_template, request, SESDeleteCustomVerificationEmailTemplateResponse)

    async def delete_dedicated_ip_pool(
        self,
        request: SESDeleteDedicatedIpPoolRequest,
    ) -> SESDeleteDedicatedIpPoolResponse:
        client = self._require_client()
        return await self._execute(client.delete_dedicated_ip_pool, request, SESDeleteDedicatedIpPoolResponse)

    async def delete_email_identity(
        self,
        request: SESDeleteEmailIdentityRequest,
    ) -> SESDeleteEmailIdentityResponse:
        client = self._require_client()
        return await self._execute(client.delete_email_identity, request, SESDeleteEmailIdentityResponse)

    async def delete_email_identity_policy(
        self,
        request: SESDeleteEmailIdentityPolicyRequest,
    ) -> SESDeleteEmailIdentityPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_email_identity_policy, request, SESDeleteEmailIdentityPolicyResponse)

    async def delete_email_template(
        self,
        request: SESDeleteEmailTemplateRequest,
    ) -> SESDeleteEmailTemplateResponse:
        client = self._require_client()
        return await self._execute(client.delete_email_template, request, SESDeleteEmailTemplateResponse)

    async def delete_multi_region_endpoint(
        self,
        request: SESDeleteMultiRegionEndpointRequest,
    ) -> SESDeleteMultiRegionEndpointResponse:
        client = self._require_client()
        return await self._execute(client.delete_multi_region_endpoint, request, SESDeleteMultiRegionEndpointResponse)

    async def delete_suppressed_destination(
        self,
        request: SESDeleteSuppressedDestinationRequest,
    ) -> SESDeleteSuppressedDestinationResponse:
        client = self._require_client()
        return await self._execute(client.delete_suppressed_destination, request, SESDeleteSuppressedDestinationResponse)

    async def delete_tenant(
        self,
        request: SESDeleteTenantRequest,
    ) -> SESDeleteTenantResponse:
        client = self._require_client()
        return await self._execute(client.delete_tenant, request, SESDeleteTenantResponse)

    async def delete_tenant_resource_association(
        self,
        request: SESDeleteTenantResourceAssociationRequest,
    ) -> SESDeleteTenantResourceAssociationResponse:
        client = self._require_client()
        return await self._execute(client.delete_tenant_resource_association, request, SESDeleteTenantResourceAssociationResponse)

    async def disassociate_email_identity_certificate(
        self,
        request: SESDisassociateEmailIdentityCertificateRequest,
    ) -> SESDisassociateEmailIdentityCertificateResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_email_identity_certificate, request, SESDisassociateEmailIdentityCertificateResponse)

    async def get_account(
        self,
        request: SESGetAccountRequest | None = None,
    ) -> SESGetAccountResponse:
        client = self._require_client()
        return await self._execute(client.get_account, request, SESGetAccountResponse)

    async def get_blacklist_reports(
        self,
        request: SESGetBlacklistReportsRequest,
    ) -> SESGetBlacklistReportsResponse:
        client = self._require_client()
        return await self._execute(client.get_blacklist_reports, request, SESGetBlacklistReportsResponse)

    async def get_configuration_set(
        self,
        request: SESGetConfigurationSetRequest,
    ) -> SESGetConfigurationSetResponse:
        client = self._require_client()
        return await self._execute(client.get_configuration_set, request, SESGetConfigurationSetResponse)

    async def get_configuration_set_event_destinations(
        self,
        request: SESGetConfigurationSetEventDestinationsRequest,
    ) -> SESGetConfigurationSetEventDestinationsResponse:
        client = self._require_client()
        return await self._execute(client.get_configuration_set_event_destinations, request, SESGetConfigurationSetEventDestinationsResponse)

    async def get_contact(
        self,
        request: SESGetContactRequest,
    ) -> SESGetContactResponse:
        client = self._require_client()
        return await self._execute(client.get_contact, request, SESGetContactResponse)

    async def get_contact_list(
        self,
        request: SESGetContactListRequest,
    ) -> SESGetContactListResponse:
        client = self._require_client()
        return await self._execute(client.get_contact_list, request, SESGetContactListResponse)

    async def get_custom_verification_email_template(
        self,
        request: SESGetCustomVerificationEmailTemplateRequest,
    ) -> SESGetCustomVerificationEmailTemplateResponse:
        client = self._require_client()
        return await self._execute(client.get_custom_verification_email_template, request, SESGetCustomVerificationEmailTemplateResponse)

    async def get_dedicated_ip(
        self,
        request: SESGetDedicatedIpRequest,
    ) -> SESGetDedicatedIpResponse:
        client = self._require_client()
        return await self._execute(client.get_dedicated_ip, request, SESGetDedicatedIpResponse)

    async def get_dedicated_ip_pool(
        self,
        request: SESGetDedicatedIpPoolRequest,
    ) -> SESGetDedicatedIpPoolResponse:
        client = self._require_client()
        return await self._execute(client.get_dedicated_ip_pool, request, SESGetDedicatedIpPoolResponse)

    async def get_dedicated_ips(
        self,
        request: SESGetDedicatedIpsRequest | None = None,
    ) -> SESGetDedicatedIpsResponse:
        client = self._require_client()
        return await self._execute(client.get_dedicated_ips, request, SESGetDedicatedIpsResponse)

    async def get_deliverability_dashboard_options(
        self,
        request: SESGetDeliverabilityDashboardOptionsRequest | None = None,
    ) -> SESGetDeliverabilityDashboardOptionsResponse:
        client = self._require_client()
        return await self._execute(client.get_deliverability_dashboard_options, request, SESGetDeliverabilityDashboardOptionsResponse)

    async def get_deliverability_test_report(
        self,
        request: SESGetDeliverabilityTestReportRequest,
    ) -> SESGetDeliverabilityTestReportResponse:
        client = self._require_client()
        return await self._execute(client.get_deliverability_test_report, request, SESGetDeliverabilityTestReportResponse)

    async def get_domain_deliverability_campaign(
        self,
        request: SESGetDomainDeliverabilityCampaignRequest,
    ) -> SESGetDomainDeliverabilityCampaignResponse:
        client = self._require_client()
        return await self._execute(client.get_domain_deliverability_campaign, request, SESGetDomainDeliverabilityCampaignResponse)

    async def get_domain_statistics_report(
        self,
        request: SESGetDomainStatisticsReportRequest,
    ) -> SESGetDomainStatisticsReportResponse:
        client = self._require_client()
        return await self._execute(client.get_domain_statistics_report, request, SESGetDomainStatisticsReportResponse)

    async def get_email_address_insights(
        self,
        request: SESGetEmailAddressInsightsRequest,
    ) -> SESGetEmailAddressInsightsResponse:
        client = self._require_client()
        return await self._execute(client.get_email_address_insights, request, SESGetEmailAddressInsightsResponse)

    async def get_email_identity(
        self,
        request: SESGetEmailIdentityRequest,
    ) -> SESGetEmailIdentityResponse:
        client = self._require_client()
        return await self._execute(client.get_email_identity, request, SESGetEmailIdentityResponse)

    async def get_email_identity_policies(
        self,
        request: SESGetEmailIdentityPoliciesRequest,
    ) -> SESGetEmailIdentityPoliciesResponse:
        client = self._require_client()
        return await self._execute(client.get_email_identity_policies, request, SESGetEmailIdentityPoliciesResponse)

    async def get_email_template(
        self,
        request: SESGetEmailTemplateRequest,
    ) -> SESGetEmailTemplateResponse:
        client = self._require_client()
        return await self._execute(client.get_email_template, request, SESGetEmailTemplateResponse)

    async def get_export_job(
        self,
        request: SESGetExportJobRequest,
    ) -> SESGetExportJobResponse:
        client = self._require_client()
        return await self._execute(client.get_export_job, request, SESGetExportJobResponse)

    async def get_import_job(
        self,
        request: SESGetImportJobRequest,
    ) -> SESGetImportJobResponse:
        client = self._require_client()
        return await self._execute(client.get_import_job, request, SESGetImportJobResponse)

    async def get_message_insights(
        self,
        request: SESGetMessageInsightsRequest,
    ) -> SESGetMessageInsightsResponse:
        client = self._require_client()
        return await self._execute(client.get_message_insights, request, SESGetMessageInsightsResponse)

    async def get_multi_region_endpoint(
        self,
        request: SESGetMultiRegionEndpointRequest,
    ) -> SESGetMultiRegionEndpointResponse:
        client = self._require_client()
        return await self._execute(client.get_multi_region_endpoint, request, SESGetMultiRegionEndpointResponse)

    async def get_reputation_entity(
        self,
        request: SESGetReputationEntityRequest,
    ) -> SESGetReputationEntityResponse:
        client = self._require_client()
        return await self._execute(client.get_reputation_entity, request, SESGetReputationEntityResponse)

    async def get_suppressed_destination(
        self,
        request: SESGetSuppressedDestinationRequest,
    ) -> SESGetSuppressedDestinationResponse:
        client = self._require_client()
        return await self._execute(client.get_suppressed_destination, request, SESGetSuppressedDestinationResponse)

    async def get_tenant(
        self,
        request: SESGetTenantRequest,
    ) -> SESGetTenantResponse:
        client = self._require_client()
        return await self._execute(client.get_tenant, request, SESGetTenantResponse)

    async def list_configuration_sets(
        self,
        request: SESListConfigurationSetsRequest | None = None,
    ) -> SESListConfigurationSetsResponse:
        client = self._require_client()
        return await self._execute(client.list_configuration_sets, request, SESListConfigurationSetsResponse)

    async def list_contact_lists(
        self,
        request: SESListContactListsRequest | None = None,
    ) -> SESListContactListsResponse:
        client = self._require_client()
        return await self._execute(client.list_contact_lists, request, SESListContactListsResponse)

    async def list_contacts(
        self,
        request: SESListContactsRequest,
    ) -> SESListContactsResponse:
        client = self._require_client()
        return await self._execute(client.list_contacts, request, SESListContactsResponse)

    async def list_custom_verification_email_templates(
        self,
        request: SESListCustomVerificationEmailTemplatesRequest | None = None,
    ) -> SESListCustomVerificationEmailTemplatesResponse:
        client = self._require_client()
        return await self._execute(client.list_custom_verification_email_templates, request, SESListCustomVerificationEmailTemplatesResponse)

    async def list_dedicated_ip_pools(
        self,
        request: SESListDedicatedIpPoolsRequest | None = None,
    ) -> SESListDedicatedIpPoolsResponse:
        client = self._require_client()
        return await self._execute(client.list_dedicated_ip_pools, request, SESListDedicatedIpPoolsResponse)

    async def list_deliverability_test_reports(
        self,
        request: SESListDeliverabilityTestReportsRequest | None = None,
    ) -> SESListDeliverabilityTestReportsResponse:
        client = self._require_client()
        return await self._execute(client.list_deliverability_test_reports, request, SESListDeliverabilityTestReportsResponse)

    async def list_domain_deliverability_campaigns(
        self,
        request: SESListDomainDeliverabilityCampaignsRequest,
    ) -> SESListDomainDeliverabilityCampaignsResponse:
        client = self._require_client()
        return await self._execute(client.list_domain_deliverability_campaigns, request, SESListDomainDeliverabilityCampaignsResponse)

    async def list_email_identities(
        self,
        request: SESListEmailIdentitiesRequest | None = None,
    ) -> SESListEmailIdentitiesResponse:
        client = self._require_client()
        return await self._execute(client.list_email_identities, request, SESListEmailIdentitiesResponse)

    async def list_email_identity_certificates(
        self,
        request: SESListEmailIdentityCertificatesRequest,
    ) -> SESListEmailIdentityCertificatesResponse:
        client = self._require_client()
        return await self._execute(client.list_email_identity_certificates, request, SESListEmailIdentityCertificatesResponse)

    async def list_email_identity_certificates_paginated(
        self,
        request: SESListEmailIdentityCertificatesRequest,
    ) -> list[SESListEmailIdentityCertificatesResponse]:
        return await self._paginate('list_email_identity_certificates', request, SESListEmailIdentityCertificatesResponse)

    async def list_email_templates(
        self,
        request: SESListEmailTemplatesRequest | None = None,
    ) -> SESListEmailTemplatesResponse:
        client = self._require_client()
        return await self._execute(client.list_email_templates, request, SESListEmailTemplatesResponse)

    async def list_export_jobs(
        self,
        request: SESListExportJobsRequest | None = None,
    ) -> SESListExportJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_export_jobs, request, SESListExportJobsResponse)

    async def list_import_jobs(
        self,
        request: SESListImportJobsRequest | None = None,
    ) -> SESListImportJobsResponse:
        client = self._require_client()
        return await self._execute(client.list_import_jobs, request, SESListImportJobsResponse)

    async def list_multi_region_endpoints(
        self,
        request: SESListMultiRegionEndpointsRequest | None = None,
    ) -> SESListMultiRegionEndpointsResponse:
        client = self._require_client()
        return await self._execute(client.list_multi_region_endpoints, request, SESListMultiRegionEndpointsResponse)

    async def list_multi_region_endpoints_paginated(
        self,
        request: SESListMultiRegionEndpointsRequest | None = None,
    ) -> list[SESListMultiRegionEndpointsResponse]:
        return await self._paginate('list_multi_region_endpoints', request, SESListMultiRegionEndpointsResponse)

    async def list_recommendations(
        self,
        request: SESListRecommendationsRequest | None = None,
    ) -> SESListRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.list_recommendations, request, SESListRecommendationsResponse)

    async def list_reputation_entities(
        self,
        request: SESListReputationEntitiesRequest | None = None,
    ) -> SESListReputationEntitiesResponse:
        client = self._require_client()
        return await self._execute(client.list_reputation_entities, request, SESListReputationEntitiesResponse)

    async def list_reputation_entities_paginated(
        self,
        request: SESListReputationEntitiesRequest | None = None,
    ) -> list[SESListReputationEntitiesResponse]:
        return await self._paginate('list_reputation_entities', request, SESListReputationEntitiesResponse)

    async def list_resource_tenants(
        self,
        request: SESListResourceTenantsRequest,
    ) -> SESListResourceTenantsResponse:
        client = self._require_client()
        return await self._execute(client.list_resource_tenants, request, SESListResourceTenantsResponse)

    async def list_resource_tenants_paginated(
        self,
        request: SESListResourceTenantsRequest,
    ) -> list[SESListResourceTenantsResponse]:
        return await self._paginate('list_resource_tenants', request, SESListResourceTenantsResponse)

    async def list_suppressed_destinations(
        self,
        request: SESListSuppressedDestinationsRequest | None = None,
    ) -> SESListSuppressedDestinationsResponse:
        client = self._require_client()
        return await self._execute(client.list_suppressed_destinations, request, SESListSuppressedDestinationsResponse)

    async def list_tags_for_resource(
        self,
        request: SESListTagsForResourceRequest,
    ) -> SESListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, SESListTagsForResourceResponse)

    async def list_tenant_resources(
        self,
        request: SESListTenantResourcesRequest,
    ) -> SESListTenantResourcesResponse:
        client = self._require_client()
        return await self._execute(client.list_tenant_resources, request, SESListTenantResourcesResponse)

    async def list_tenant_resources_paginated(
        self,
        request: SESListTenantResourcesRequest,
    ) -> list[SESListTenantResourcesResponse]:
        return await self._paginate('list_tenant_resources', request, SESListTenantResourcesResponse)

    async def list_tenants(
        self,
        request: SESListTenantsRequest | None = None,
    ) -> SESListTenantsResponse:
        client = self._require_client()
        return await self._execute(client.list_tenants, request, SESListTenantsResponse)

    async def list_tenants_paginated(
        self,
        request: SESListTenantsRequest | None = None,
    ) -> list[SESListTenantsResponse]:
        return await self._paginate('list_tenants', request, SESListTenantsResponse)

    async def put_account_dedicated_ip_warmup_attributes(
        self,
        request: SESPutAccountDedicatedIpWarmupAttributesRequest | None = None,
    ) -> SESPutAccountDedicatedIpWarmupAttributesResponse:
        client = self._require_client()
        return await self._execute(client.put_account_dedicated_ip_warmup_attributes, request, SESPutAccountDedicatedIpWarmupAttributesResponse)

    async def put_account_delivery_attributes(
        self,
        request: SESPutAccountDeliveryAttributesRequest,
    ) -> SESPutAccountDeliveryAttributesResponse:
        client = self._require_client()
        return await self._execute(client.put_account_delivery_attributes, request, SESPutAccountDeliveryAttributesResponse)

    async def put_account_details(
        self,
        request: SESPutAccountDetailsRequest,
    ) -> SESPutAccountDetailsResponse:
        client = self._require_client()
        return await self._execute(client.put_account_details, request, SESPutAccountDetailsResponse)

    async def put_account_pricing_attributes(
        self,
        request: SESPutAccountPricingAttributesRequest,
    ) -> SESPutAccountPricingAttributesResponse:
        client = self._require_client()
        return await self._execute(client.put_account_pricing_attributes, request, SESPutAccountPricingAttributesResponse)

    async def put_account_sending_attributes(
        self,
        request: SESPutAccountSendingAttributesRequest | None = None,
    ) -> SESPutAccountSendingAttributesResponse:
        client = self._require_client()
        return await self._execute(client.put_account_sending_attributes, request, SESPutAccountSendingAttributesResponse)

    async def put_account_suppression_attributes(
        self,
        request: SESPutAccountSuppressionAttributesRequest | None = None,
    ) -> SESPutAccountSuppressionAttributesResponse:
        client = self._require_client()
        return await self._execute(client.put_account_suppression_attributes, request, SESPutAccountSuppressionAttributesResponse)

    async def put_account_vdm_attributes(
        self,
        request: SESPutAccountVdmAttributesRequest,
    ) -> SESPutAccountVdmAttributesResponse:
        client = self._require_client()
        return await self._execute(client.put_account_vdm_attributes, request, SESPutAccountVdmAttributesResponse)

    async def put_configuration_set_archiving_options(
        self,
        request: SESPutConfigurationSetArchivingOptionsRequest,
    ) -> SESPutConfigurationSetArchivingOptionsResponse:
        client = self._require_client()
        return await self._execute(client.put_configuration_set_archiving_options, request, SESPutConfigurationSetArchivingOptionsResponse)

    async def put_configuration_set_delivery_options(
        self,
        request: SESPutConfigurationSetDeliveryOptionsRequest,
    ) -> SESPutConfigurationSetDeliveryOptionsResponse:
        client = self._require_client()
        return await self._execute(client.put_configuration_set_delivery_options, request, SESPutConfigurationSetDeliveryOptionsResponse)

    async def put_configuration_set_reputation_options(
        self,
        request: SESPutConfigurationSetReputationOptionsRequest,
    ) -> SESPutConfigurationSetReputationOptionsResponse:
        client = self._require_client()
        return await self._execute(client.put_configuration_set_reputation_options, request, SESPutConfigurationSetReputationOptionsResponse)

    async def put_configuration_set_sending_options(
        self,
        request: SESPutConfigurationSetSendingOptionsRequest,
    ) -> SESPutConfigurationSetSendingOptionsResponse:
        client = self._require_client()
        return await self._execute(client.put_configuration_set_sending_options, request, SESPutConfigurationSetSendingOptionsResponse)

    async def put_configuration_set_suppression_options(
        self,
        request: SESPutConfigurationSetSuppressionOptionsRequest,
    ) -> SESPutConfigurationSetSuppressionOptionsResponse:
        client = self._require_client()
        return await self._execute(client.put_configuration_set_suppression_options, request, SESPutConfigurationSetSuppressionOptionsResponse)

    async def put_configuration_set_tracking_options(
        self,
        request: SESPutConfigurationSetTrackingOptionsRequest,
    ) -> SESPutConfigurationSetTrackingOptionsResponse:
        client = self._require_client()
        return await self._execute(client.put_configuration_set_tracking_options, request, SESPutConfigurationSetTrackingOptionsResponse)

    async def put_configuration_set_vdm_options(
        self,
        request: SESPutConfigurationSetVdmOptionsRequest,
    ) -> SESPutConfigurationSetVdmOptionsResponse:
        client = self._require_client()
        return await self._execute(client.put_configuration_set_vdm_options, request, SESPutConfigurationSetVdmOptionsResponse)

    async def put_dedicated_ip_in_pool(
        self,
        request: SESPutDedicatedIpInPoolRequest,
    ) -> SESPutDedicatedIpInPoolResponse:
        client = self._require_client()
        return await self._execute(client.put_dedicated_ip_in_pool, request, SESPutDedicatedIpInPoolResponse)

    async def put_dedicated_ip_pool_scaling_attributes(
        self,
        request: SESPutDedicatedIpPoolScalingAttributesRequest,
    ) -> SESPutDedicatedIpPoolScalingAttributesResponse:
        client = self._require_client()
        return await self._execute(client.put_dedicated_ip_pool_scaling_attributes, request, SESPutDedicatedIpPoolScalingAttributesResponse)

    async def put_dedicated_ip_warmup_attributes(
        self,
        request: SESPutDedicatedIpWarmupAttributesRequest,
    ) -> SESPutDedicatedIpWarmupAttributesResponse:
        client = self._require_client()
        return await self._execute(client.put_dedicated_ip_warmup_attributes, request, SESPutDedicatedIpWarmupAttributesResponse)

    async def put_deliverability_dashboard_option(
        self,
        request: SESPutDeliverabilityDashboardOptionRequest,
    ) -> SESPutDeliverabilityDashboardOptionResponse:
        client = self._require_client()
        return await self._execute(client.put_deliverability_dashboard_option, request, SESPutDeliverabilityDashboardOptionResponse)

    async def put_email_identity_configuration_set_attributes(
        self,
        request: SESPutEmailIdentityConfigurationSetAttributesRequest,
    ) -> SESPutEmailIdentityConfigurationSetAttributesResponse:
        client = self._require_client()
        return await self._execute(client.put_email_identity_configuration_set_attributes, request, SESPutEmailIdentityConfigurationSetAttributesResponse)

    async def put_email_identity_dkim_attributes(
        self,
        request: SESPutEmailIdentityDkimAttributesRequest,
    ) -> SESPutEmailIdentityDkimAttributesResponse:
        client = self._require_client()
        return await self._execute(client.put_email_identity_dkim_attributes, request, SESPutEmailIdentityDkimAttributesResponse)

    async def put_email_identity_dkim_signing_attributes(
        self,
        request: SESPutEmailIdentityDkimSigningAttributesRequest,
    ) -> SESPutEmailIdentityDkimSigningAttributesResponse:
        client = self._require_client()
        return await self._execute(client.put_email_identity_dkim_signing_attributes, request, SESPutEmailIdentityDkimSigningAttributesResponse)

    async def put_email_identity_feedback_attributes(
        self,
        request: SESPutEmailIdentityFeedbackAttributesRequest,
    ) -> SESPutEmailIdentityFeedbackAttributesResponse:
        client = self._require_client()
        return await self._execute(client.put_email_identity_feedback_attributes, request, SESPutEmailIdentityFeedbackAttributesResponse)

    async def put_email_identity_mail_from_attributes(
        self,
        request: SESPutEmailIdentityMailFromAttributesRequest,
    ) -> SESPutEmailIdentityMailFromAttributesResponse:
        client = self._require_client()
        return await self._execute(client.put_email_identity_mail_from_attributes, request, SESPutEmailIdentityMailFromAttributesResponse)

    async def put_suppressed_destination(
        self,
        request: SESPutSuppressedDestinationRequest,
    ) -> SESPutSuppressedDestinationResponse:
        client = self._require_client()
        return await self._execute(client.put_suppressed_destination, request, SESPutSuppressedDestinationResponse)

    async def put_tenant_suppression_attributes(
        self,
        request: SESPutTenantSuppressionAttributesRequest,
    ) -> SESPutTenantSuppressionAttributesResponse:
        client = self._require_client()
        return await self._execute(client.put_tenant_suppression_attributes, request, SESPutTenantSuppressionAttributesResponse)

    async def send_bulk_email(
        self,
        request: SESSendBulkEmailRequest,
    ) -> SESSendBulkEmailResponse:
        client = self._require_client()
        return await self._execute(client.send_bulk_email, request, SESSendBulkEmailResponse)

    async def send_custom_verification_email(
        self,
        request: SESSendCustomVerificationEmailRequest,
    ) -> SESSendCustomVerificationEmailResponse:
        client = self._require_client()
        return await self._execute(client.send_custom_verification_email, request, SESSendCustomVerificationEmailResponse)

    async def send_email(
        self,
        request: SESSendEmailRequest,
    ) -> SESSendEmailResponse:
        client = self._require_client()
        return await self._execute(client.send_email, request, SESSendEmailResponse)

    async def tag_resource(
        self,
        request: SESTagResourceRequest,
    ) -> SESTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, SESTagResourceResponse)

    async def test_render_email_template(
        self,
        request: SESTestRenderEmailTemplateRequest,
    ) -> SESTestRenderEmailTemplateResponse:
        client = self._require_client()
        return await self._execute(client.test_render_email_template, request, SESTestRenderEmailTemplateResponse)

    async def untag_resource(
        self,
        request: SESUntagResourceRequest,
    ) -> SESUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, SESUntagResourceResponse)

    async def update_configuration_set(
        self,
        request: SESUpdateConfigurationSetRequest,
    ) -> SESUpdateConfigurationSetResponse:
        client = self._require_client()
        return await self._execute(client.update_configuration_set, request, SESUpdateConfigurationSetResponse)

    async def update_configuration_set_event_destination(
        self,
        request: SESUpdateConfigurationSetEventDestinationRequest,
    ) -> SESUpdateConfigurationSetEventDestinationResponse:
        client = self._require_client()
        return await self._execute(client.update_configuration_set_event_destination, request, SESUpdateConfigurationSetEventDestinationResponse)

    async def update_contact(
        self,
        request: SESUpdateContactRequest,
    ) -> SESUpdateContactResponse:
        client = self._require_client()
        return await self._execute(client.update_contact, request, SESUpdateContactResponse)

    async def update_contact_list(
        self,
        request: SESUpdateContactListRequest,
    ) -> SESUpdateContactListResponse:
        client = self._require_client()
        return await self._execute(client.update_contact_list, request, SESUpdateContactListResponse)

    async def update_custom_verification_email_template(
        self,
        request: SESUpdateCustomVerificationEmailTemplateRequest,
    ) -> SESUpdateCustomVerificationEmailTemplateResponse:
        client = self._require_client()
        return await self._execute(client.update_custom_verification_email_template, request, SESUpdateCustomVerificationEmailTemplateResponse)

    async def update_email_identity_policy(
        self,
        request: SESUpdateEmailIdentityPolicyRequest,
    ) -> SESUpdateEmailIdentityPolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_email_identity_policy, request, SESUpdateEmailIdentityPolicyResponse)

    async def update_email_template(
        self,
        request: SESUpdateEmailTemplateRequest,
    ) -> SESUpdateEmailTemplateResponse:
        client = self._require_client()
        return await self._execute(client.update_email_template, request, SESUpdateEmailTemplateResponse)

    async def update_reputation_entity_customer_managed_status(
        self,
        request: SESUpdateReputationEntityCustomerManagedStatusRequest,
    ) -> SESUpdateReputationEntityCustomerManagedStatusResponse:
        client = self._require_client()
        return await self._execute(client.update_reputation_entity_customer_managed_status, request, SESUpdateReputationEntityCustomerManagedStatusResponse)

    async def update_reputation_entity_policy(
        self,
        request: SESUpdateReputationEntityPolicyRequest,
    ) -> SESUpdateReputationEntityPolicyResponse:
        client = self._require_client()
        return await self._execute(client.update_reputation_entity_policy, request, SESUpdateReputationEntityPolicyResponse)
