from werkflow_aws.models.eum import (
    EndUserMessagingAssociateOriginationIdentityRequest,
    EndUserMessagingAssociateOriginationIdentityResponse,
    EndUserMessagingAssociateProtectConfigurationRequest,
    EndUserMessagingAssociateProtectConfigurationResponse,
    EndUserMessagingCarrierLookupRequest,
    EndUserMessagingCarrierLookupResponse,
    EndUserMessagingCreateConfigurationSetRequest,
    EndUserMessagingCreateConfigurationSetResponse,
    EndUserMessagingCreateEventDestinationRequest,
    EndUserMessagingCreateEventDestinationResponse,
    EndUserMessagingCreateNotifyConfigurationRequest,
    EndUserMessagingCreateNotifyConfigurationResponse,
    EndUserMessagingCreateOptOutListRequest,
    EndUserMessagingCreateOptOutListResponse,
    EndUserMessagingCreatePoolRequest,
    EndUserMessagingCreatePoolResponse,
    EndUserMessagingCreateProtectConfigurationRequest,
    EndUserMessagingCreateProtectConfigurationResponse,
    EndUserMessagingCreateRcsAgentRequest,
    EndUserMessagingCreateRcsAgentResponse,
    EndUserMessagingCreateRegistrationAssociationRequest,
    EndUserMessagingCreateRegistrationAssociationResponse,
    EndUserMessagingCreateRegistrationAttachmentRequest,
    EndUserMessagingCreateRegistrationAttachmentResponse,
    EndUserMessagingCreateRegistrationRequest,
    EndUserMessagingCreateRegistrationResponse,
    EndUserMessagingCreateRegistrationVersionRequest,
    EndUserMessagingCreateRegistrationVersionResponse,
    EndUserMessagingCreateVerifiedDestinationNumberRequest,
    EndUserMessagingCreateVerifiedDestinationNumberResponse,
    EndUserMessagingDeleteAccountDefaultProtectConfigurationRequest,
    EndUserMessagingDeleteAccountDefaultProtectConfigurationResponse,
    EndUserMessagingDeleteConfigurationSetRequest,
    EndUserMessagingDeleteConfigurationSetResponse,
    EndUserMessagingDeleteDefaultMessageTypeRequest,
    EndUserMessagingDeleteDefaultMessageTypeResponse,
    EndUserMessagingDeleteDefaultSenderIdRequest,
    EndUserMessagingDeleteDefaultSenderIdResponse,
    EndUserMessagingDeleteEventDestinationRequest,
    EndUserMessagingDeleteEventDestinationResponse,
    EndUserMessagingDeleteKeywordRequest,
    EndUserMessagingDeleteKeywordResponse,
    EndUserMessagingDeleteMediaMessageSpendLimitOverrideRequest,
    EndUserMessagingDeleteMediaMessageSpendLimitOverrideResponse,
    EndUserMessagingDeleteNotifyConfigurationRequest,
    EndUserMessagingDeleteNotifyConfigurationResponse,
    EndUserMessagingDeleteNotifyMessageSpendLimitOverrideRequest,
    EndUserMessagingDeleteNotifyMessageSpendLimitOverrideResponse,
    EndUserMessagingDeleteOptOutListRequest,
    EndUserMessagingDeleteOptOutListResponse,
    EndUserMessagingDeleteOptedOutNumberRequest,
    EndUserMessagingDeleteOptedOutNumberResponse,
    EndUserMessagingDeletePoolRequest,
    EndUserMessagingDeletePoolResponse,
    EndUserMessagingDeleteProtectConfigurationRequest,
    EndUserMessagingDeleteProtectConfigurationResponse,
    EndUserMessagingDeleteProtectConfigurationRuleSetNumberOverrideRequest,
    EndUserMessagingDeleteProtectConfigurationRuleSetNumberOverrideResponse,
    EndUserMessagingDeleteRcsAgentRequest,
    EndUserMessagingDeleteRcsAgentResponse,
    EndUserMessagingDeleteRcsMessageSpendLimitOverrideRequest,
    EndUserMessagingDeleteRcsMessageSpendLimitOverrideResponse,
    EndUserMessagingDeleteRegistrationAttachmentRequest,
    EndUserMessagingDeleteRegistrationAttachmentResponse,
    EndUserMessagingDeleteRegistrationFieldValueRequest,
    EndUserMessagingDeleteRegistrationFieldValueResponse,
    EndUserMessagingDeleteRegistrationRequest,
    EndUserMessagingDeleteRegistrationResponse,
    EndUserMessagingDeleteResourcePolicyRequest,
    EndUserMessagingDeleteResourcePolicyResponse,
    EndUserMessagingDeleteTextMessageSpendLimitOverrideRequest,
    EndUserMessagingDeleteTextMessageSpendLimitOverrideResponse,
    EndUserMessagingDeleteVerifiedDestinationNumberRequest,
    EndUserMessagingDeleteVerifiedDestinationNumberResponse,
    EndUserMessagingDeleteVoiceMessageSpendLimitOverrideRequest,
    EndUserMessagingDeleteVoiceMessageSpendLimitOverrideResponse,
    EndUserMessagingDescribeAccountAttributesRequest,
    EndUserMessagingDescribeAccountAttributesResponse,
    EndUserMessagingDescribeAccountLimitsRequest,
    EndUserMessagingDescribeAccountLimitsResponse,
    EndUserMessagingDescribeConfigurationSetsRequest,
    EndUserMessagingDescribeConfigurationSetsResponse,
    EndUserMessagingDescribeKeywordsRequest,
    EndUserMessagingDescribeKeywordsResponse,
    EndUserMessagingDescribeNotifyConfigurationsRequest,
    EndUserMessagingDescribeNotifyConfigurationsResponse,
    EndUserMessagingDescribeNotifyTemplatesRequest,
    EndUserMessagingDescribeNotifyTemplatesResponse,
    EndUserMessagingDescribeOptOutListsRequest,
    EndUserMessagingDescribeOptOutListsResponse,
    EndUserMessagingDescribeOptedOutNumbersRequest,
    EndUserMessagingDescribeOptedOutNumbersResponse,
    EndUserMessagingDescribePhoneNumbersRequest,
    EndUserMessagingDescribePhoneNumbersResponse,
    EndUserMessagingDescribePoolsRequest,
    EndUserMessagingDescribePoolsResponse,
    EndUserMessagingDescribeProtectConfigurationsRequest,
    EndUserMessagingDescribeProtectConfigurationsResponse,
    EndUserMessagingDescribeRcsAgentCountryLaunchStatusRequest,
    EndUserMessagingDescribeRcsAgentCountryLaunchStatusResponse,
    EndUserMessagingDescribeRcsAgentsRequest,
    EndUserMessagingDescribeRcsAgentsResponse,
    EndUserMessagingDescribeRegistrationAttachmentsRequest,
    EndUserMessagingDescribeRegistrationAttachmentsResponse,
    EndUserMessagingDescribeRegistrationFieldDefinitionsRequest,
    EndUserMessagingDescribeRegistrationFieldDefinitionsResponse,
    EndUserMessagingDescribeRegistrationFieldValuesRequest,
    EndUserMessagingDescribeRegistrationFieldValuesResponse,
    EndUserMessagingDescribeRegistrationSectionDefinitionsRequest,
    EndUserMessagingDescribeRegistrationSectionDefinitionsResponse,
    EndUserMessagingDescribeRegistrationTypeDefinitionsRequest,
    EndUserMessagingDescribeRegistrationTypeDefinitionsResponse,
    EndUserMessagingDescribeRegistrationVersionsRequest,
    EndUserMessagingDescribeRegistrationVersionsResponse,
    EndUserMessagingDescribeRegistrationsRequest,
    EndUserMessagingDescribeRegistrationsResponse,
    EndUserMessagingDescribeSenderIdsRequest,
    EndUserMessagingDescribeSenderIdsResponse,
    EndUserMessagingDescribeSpendLimitsRequest,
    EndUserMessagingDescribeSpendLimitsResponse,
    EndUserMessagingDescribeVerifiedDestinationNumbersRequest,
    EndUserMessagingDescribeVerifiedDestinationNumbersResponse,
    EndUserMessagingDisassociateOriginationIdentityRequest,
    EndUserMessagingDisassociateOriginationIdentityResponse,
    EndUserMessagingDisassociateProtectConfigurationRequest,
    EndUserMessagingDisassociateProtectConfigurationResponse,
    EndUserMessagingDiscardRegistrationVersionRequest,
    EndUserMessagingDiscardRegistrationVersionResponse,
    EndUserMessagingGetProtectConfigurationCountryRuleSetRequest,
    EndUserMessagingGetProtectConfigurationCountryRuleSetResponse,
    EndUserMessagingGetResourcePolicyRequest,
    EndUserMessagingGetResourcePolicyResponse,
    EndUserMessagingListAvailablePhoneNumbersRequest,
    EndUserMessagingListAvailablePhoneNumbersResponse,
    EndUserMessagingListNotifyCountriesRequest,
    EndUserMessagingListNotifyCountriesResponse,
    EndUserMessagingListPoolOriginationIdentitiesRequest,
    EndUserMessagingListPoolOriginationIdentitiesResponse,
    EndUserMessagingListProtectConfigurationRuleSetNumberOverridesRequest,
    EndUserMessagingListProtectConfigurationRuleSetNumberOverridesResponse,
    EndUserMessagingListRegistrationAssociationsRequest,
    EndUserMessagingListRegistrationAssociationsResponse,
    EndUserMessagingListTagsForResourceRequest,
    EndUserMessagingListTagsForResourceResponse,
    EndUserMessagingPutKeywordRequest,
    EndUserMessagingPutKeywordResponse,
    EndUserMessagingPutMessageFeedbackRequest,
    EndUserMessagingPutMessageFeedbackResponse,
    EndUserMessagingPutOptedOutNumberRequest,
    EndUserMessagingPutOptedOutNumberResponse,
    EndUserMessagingPutProtectConfigurationRuleSetNumberOverrideRequest,
    EndUserMessagingPutProtectConfigurationRuleSetNumberOverrideResponse,
    EndUserMessagingPutRegistrationFieldValueRequest,
    EndUserMessagingPutRegistrationFieldValueResponse,
    EndUserMessagingPutResourcePolicyRequest,
    EndUserMessagingPutResourcePolicyResponse,
    EndUserMessagingReleasePhoneNumberRequest,
    EndUserMessagingReleasePhoneNumberResponse,
    EndUserMessagingReleaseSenderIdRequest,
    EndUserMessagingReleaseSenderIdResponse,
    EndUserMessagingRequestPhoneNumberRequest,
    EndUserMessagingRequestPhoneNumberResponse,
    EndUserMessagingRequestSenderIdRequest,
    EndUserMessagingRequestSenderIdResponse,
    EndUserMessagingSendDestinationNumberVerificationCodeRequest,
    EndUserMessagingSendDestinationNumberVerificationCodeResponse,
    EndUserMessagingSendMediaMessageRequest,
    EndUserMessagingSendMediaMessageResponse,
    EndUserMessagingSendNotifyTextMessageRequest,
    EndUserMessagingSendNotifyTextMessageResponse,
    EndUserMessagingSendNotifyVoiceMessageRequest,
    EndUserMessagingSendNotifyVoiceMessageResponse,
    EndUserMessagingSendRcsMessageRequest,
    EndUserMessagingSendRcsMessageResponse,
    EndUserMessagingSendTextMessageRequest,
    EndUserMessagingSendTextMessageResponse,
    EndUserMessagingSendVoiceMessageRequest,
    EndUserMessagingSendVoiceMessageResponse,
    EndUserMessagingSetAccountDefaultProtectConfigurationRequest,
    EndUserMessagingSetAccountDefaultProtectConfigurationResponse,
    EndUserMessagingSetDefaultMessageFeedbackEnabledRequest,
    EndUserMessagingSetDefaultMessageFeedbackEnabledResponse,
    EndUserMessagingSetDefaultMessageTypeRequest,
    EndUserMessagingSetDefaultMessageTypeResponse,
    EndUserMessagingSetDefaultSenderIdRequest,
    EndUserMessagingSetDefaultSenderIdResponse,
    EndUserMessagingSetMediaMessageSpendLimitOverrideRequest,
    EndUserMessagingSetMediaMessageSpendLimitOverrideResponse,
    EndUserMessagingSetNotifyMessageSpendLimitOverrideRequest,
    EndUserMessagingSetNotifyMessageSpendLimitOverrideResponse,
    EndUserMessagingSetRcsMessageSpendLimitOverrideRequest,
    EndUserMessagingSetRcsMessageSpendLimitOverrideResponse,
    EndUserMessagingSetTextMessageSpendLimitOverrideRequest,
    EndUserMessagingSetTextMessageSpendLimitOverrideResponse,
    EndUserMessagingSetVoiceMessageSpendLimitOverrideRequest,
    EndUserMessagingSetVoiceMessageSpendLimitOverrideResponse,
    EndUserMessagingSubmitRegistrationVersionRequest,
    EndUserMessagingSubmitRegistrationVersionResponse,
    EndUserMessagingTagResourceRequest,
    EndUserMessagingTagResourceResponse,
    EndUserMessagingUntagResourceRequest,
    EndUserMessagingUntagResourceResponse,
    EndUserMessagingUpdateEventDestinationRequest,
    EndUserMessagingUpdateEventDestinationResponse,
    EndUserMessagingUpdateNotifyConfigurationRequest,
    EndUserMessagingUpdateNotifyConfigurationResponse,
    EndUserMessagingUpdatePhoneNumberRequest,
    EndUserMessagingUpdatePhoneNumberResponse,
    EndUserMessagingUpdatePoolRequest,
    EndUserMessagingUpdatePoolResponse,
    EndUserMessagingUpdateProtectConfigurationCountryRuleSetRequest,
    EndUserMessagingUpdateProtectConfigurationCountryRuleSetResponse,
    EndUserMessagingUpdateProtectConfigurationRequest,
    EndUserMessagingUpdateProtectConfigurationResponse,
    EndUserMessagingUpdateRcsAgentRequest,
    EndUserMessagingUpdateRcsAgentResponse,
    EndUserMessagingUpdateSenderIdRequest,
    EndUserMessagingUpdateSenderIdResponse,
    EndUserMessagingVerifyDestinationNumberRequest,
    EndUserMessagingVerifyDestinationNumberResponse,
)
from werkflow_aws.types.eum_client import EndUserMessagingClient
from .base import AWSBaseService


class AWSEndUserMessaging(AWSBaseService[EndUserMessagingClient]):
    service_name = 'eum'
    boto3_service_name = 'pinpoint-sms-voice-v2'

    def __init__(self) -> None:
        super().__init__(service_name='eum', boto3_service_name='pinpoint-sms-voice-v2')

    async def associate_origination_identity(
        self,
        request: EndUserMessagingAssociateOriginationIdentityRequest,
    ) -> EndUserMessagingAssociateOriginationIdentityResponse:
        client = self._require_client()
        return await self._execute(client.associate_origination_identity, request, EndUserMessagingAssociateOriginationIdentityResponse)

    async def associate_protect_configuration(
        self,
        request: EndUserMessagingAssociateProtectConfigurationRequest,
    ) -> EndUserMessagingAssociateProtectConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.associate_protect_configuration, request, EndUserMessagingAssociateProtectConfigurationResponse)

    async def carrier_lookup(
        self,
        request: EndUserMessagingCarrierLookupRequest,
    ) -> EndUserMessagingCarrierLookupResponse:
        client = self._require_client()
        return await self._execute(client.carrier_lookup, request, EndUserMessagingCarrierLookupResponse)

    async def create_configuration_set(
        self,
        request: EndUserMessagingCreateConfigurationSetRequest,
    ) -> EndUserMessagingCreateConfigurationSetResponse:
        client = self._require_client()
        return await self._execute(client.create_configuration_set, request, EndUserMessagingCreateConfigurationSetResponse)

    async def create_event_destination(
        self,
        request: EndUserMessagingCreateEventDestinationRequest,
    ) -> EndUserMessagingCreateEventDestinationResponse:
        client = self._require_client()
        return await self._execute(client.create_event_destination, request, EndUserMessagingCreateEventDestinationResponse)

    async def create_notify_configuration(
        self,
        request: EndUserMessagingCreateNotifyConfigurationRequest,
    ) -> EndUserMessagingCreateNotifyConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_notify_configuration, request, EndUserMessagingCreateNotifyConfigurationResponse)

    async def create_opt_out_list(
        self,
        request: EndUserMessagingCreateOptOutListRequest,
    ) -> EndUserMessagingCreateOptOutListResponse:
        client = self._require_client()
        return await self._execute(client.create_opt_out_list, request, EndUserMessagingCreateOptOutListResponse)

    async def create_pool(
        self,
        request: EndUserMessagingCreatePoolRequest,
    ) -> EndUserMessagingCreatePoolResponse:
        client = self._require_client()
        return await self._execute(client.create_pool, request, EndUserMessagingCreatePoolResponse)

    async def create_protect_configuration(
        self,
        request: EndUserMessagingCreateProtectConfigurationRequest | None = None,
    ) -> EndUserMessagingCreateProtectConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_protect_configuration, request, EndUserMessagingCreateProtectConfigurationResponse)

    async def create_rcs_agent(
        self,
        request: EndUserMessagingCreateRcsAgentRequest | None = None,
    ) -> EndUserMessagingCreateRcsAgentResponse:
        client = self._require_client()
        return await self._execute(client.create_rcs_agent, request, EndUserMessagingCreateRcsAgentResponse)

    async def create_registration(
        self,
        request: EndUserMessagingCreateRegistrationRequest,
    ) -> EndUserMessagingCreateRegistrationResponse:
        client = self._require_client()
        return await self._execute(client.create_registration, request, EndUserMessagingCreateRegistrationResponse)

    async def create_registration_association(
        self,
        request: EndUserMessagingCreateRegistrationAssociationRequest,
    ) -> EndUserMessagingCreateRegistrationAssociationResponse:
        client = self._require_client()
        return await self._execute(client.create_registration_association, request, EndUserMessagingCreateRegistrationAssociationResponse)

    async def create_registration_attachment(
        self,
        request: EndUserMessagingCreateRegistrationAttachmentRequest | None = None,
    ) -> EndUserMessagingCreateRegistrationAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.create_registration_attachment, request, EndUserMessagingCreateRegistrationAttachmentResponse)

    async def create_registration_version(
        self,
        request: EndUserMessagingCreateRegistrationVersionRequest,
    ) -> EndUserMessagingCreateRegistrationVersionResponse:
        client = self._require_client()
        return await self._execute(client.create_registration_version, request, EndUserMessagingCreateRegistrationVersionResponse)

    async def create_verified_destination_number(
        self,
        request: EndUserMessagingCreateVerifiedDestinationNumberRequest,
    ) -> EndUserMessagingCreateVerifiedDestinationNumberResponse:
        client = self._require_client()
        return await self._execute(client.create_verified_destination_number, request, EndUserMessagingCreateVerifiedDestinationNumberResponse)

    async def delete_account_default_protect_configuration(
        self,
        request: EndUserMessagingDeleteAccountDefaultProtectConfigurationRequest | None = None,
    ) -> EndUserMessagingDeleteAccountDefaultProtectConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_account_default_protect_configuration, request, EndUserMessagingDeleteAccountDefaultProtectConfigurationResponse)

    async def delete_configuration_set(
        self,
        request: EndUserMessagingDeleteConfigurationSetRequest,
    ) -> EndUserMessagingDeleteConfigurationSetResponse:
        client = self._require_client()
        return await self._execute(client.delete_configuration_set, request, EndUserMessagingDeleteConfigurationSetResponse)

    async def delete_default_message_type(
        self,
        request: EndUserMessagingDeleteDefaultMessageTypeRequest,
    ) -> EndUserMessagingDeleteDefaultMessageTypeResponse:
        client = self._require_client()
        return await self._execute(client.delete_default_message_type, request, EndUserMessagingDeleteDefaultMessageTypeResponse)

    async def delete_default_sender_id(
        self,
        request: EndUserMessagingDeleteDefaultSenderIdRequest,
    ) -> EndUserMessagingDeleteDefaultSenderIdResponse:
        client = self._require_client()
        return await self._execute(client.delete_default_sender_id, request, EndUserMessagingDeleteDefaultSenderIdResponse)

    async def delete_event_destination(
        self,
        request: EndUserMessagingDeleteEventDestinationRequest,
    ) -> EndUserMessagingDeleteEventDestinationResponse:
        client = self._require_client()
        return await self._execute(client.delete_event_destination, request, EndUserMessagingDeleteEventDestinationResponse)

    async def delete_keyword(
        self,
        request: EndUserMessagingDeleteKeywordRequest,
    ) -> EndUserMessagingDeleteKeywordResponse:
        client = self._require_client()
        return await self._execute(client.delete_keyword, request, EndUserMessagingDeleteKeywordResponse)

    async def delete_media_message_spend_limit_override(
        self,
        request: EndUserMessagingDeleteMediaMessageSpendLimitOverrideRequest | None = None,
    ) -> EndUserMessagingDeleteMediaMessageSpendLimitOverrideResponse:
        client = self._require_client()
        return await self._execute(client.delete_media_message_spend_limit_override, request, EndUserMessagingDeleteMediaMessageSpendLimitOverrideResponse)

    async def delete_notify_configuration(
        self,
        request: EndUserMessagingDeleteNotifyConfigurationRequest,
    ) -> EndUserMessagingDeleteNotifyConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_notify_configuration, request, EndUserMessagingDeleteNotifyConfigurationResponse)

    async def delete_notify_message_spend_limit_override(
        self,
        request: EndUserMessagingDeleteNotifyMessageSpendLimitOverrideRequest | None = None,
    ) -> EndUserMessagingDeleteNotifyMessageSpendLimitOverrideResponse:
        client = self._require_client()
        return await self._execute(client.delete_notify_message_spend_limit_override, request, EndUserMessagingDeleteNotifyMessageSpendLimitOverrideResponse)

    async def delete_opt_out_list(
        self,
        request: EndUserMessagingDeleteOptOutListRequest,
    ) -> EndUserMessagingDeleteOptOutListResponse:
        client = self._require_client()
        return await self._execute(client.delete_opt_out_list, request, EndUserMessagingDeleteOptOutListResponse)

    async def delete_opted_out_number(
        self,
        request: EndUserMessagingDeleteOptedOutNumberRequest,
    ) -> EndUserMessagingDeleteOptedOutNumberResponse:
        client = self._require_client()
        return await self._execute(client.delete_opted_out_number, request, EndUserMessagingDeleteOptedOutNumberResponse)

    async def delete_pool(
        self,
        request: EndUserMessagingDeletePoolRequest,
    ) -> EndUserMessagingDeletePoolResponse:
        client = self._require_client()
        return await self._execute(client.delete_pool, request, EndUserMessagingDeletePoolResponse)

    async def delete_protect_configuration(
        self,
        request: EndUserMessagingDeleteProtectConfigurationRequest,
    ) -> EndUserMessagingDeleteProtectConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_protect_configuration, request, EndUserMessagingDeleteProtectConfigurationResponse)

    async def delete_protect_configuration_rule_set_number_override(
        self,
        request: EndUserMessagingDeleteProtectConfigurationRuleSetNumberOverrideRequest,
    ) -> EndUserMessagingDeleteProtectConfigurationRuleSetNumberOverrideResponse:
        client = self._require_client()
        return await self._execute(client.delete_protect_configuration_rule_set_number_override, request, EndUserMessagingDeleteProtectConfigurationRuleSetNumberOverrideResponse)

    async def delete_rcs_agent(
        self,
        request: EndUserMessagingDeleteRcsAgentRequest,
    ) -> EndUserMessagingDeleteRcsAgentResponse:
        client = self._require_client()
        return await self._execute(client.delete_rcs_agent, request, EndUserMessagingDeleteRcsAgentResponse)

    async def delete_rcs_message_spend_limit_override(
        self,
        request: EndUserMessagingDeleteRcsMessageSpendLimitOverrideRequest | None = None,
    ) -> EndUserMessagingDeleteRcsMessageSpendLimitOverrideResponse:
        client = self._require_client()
        return await self._execute(client.delete_rcs_message_spend_limit_override, request, EndUserMessagingDeleteRcsMessageSpendLimitOverrideResponse)

    async def delete_registration(
        self,
        request: EndUserMessagingDeleteRegistrationRequest,
    ) -> EndUserMessagingDeleteRegistrationResponse:
        client = self._require_client()
        return await self._execute(client.delete_registration, request, EndUserMessagingDeleteRegistrationResponse)

    async def delete_registration_attachment(
        self,
        request: EndUserMessagingDeleteRegistrationAttachmentRequest,
    ) -> EndUserMessagingDeleteRegistrationAttachmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_registration_attachment, request, EndUserMessagingDeleteRegistrationAttachmentResponse)

    async def delete_registration_field_value(
        self,
        request: EndUserMessagingDeleteRegistrationFieldValueRequest,
    ) -> EndUserMessagingDeleteRegistrationFieldValueResponse:
        client = self._require_client()
        return await self._execute(client.delete_registration_field_value, request, EndUserMessagingDeleteRegistrationFieldValueResponse)

    async def delete_resource_policy(
        self,
        request: EndUserMessagingDeleteResourcePolicyRequest,
    ) -> EndUserMessagingDeleteResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_resource_policy, request, EndUserMessagingDeleteResourcePolicyResponse)

    async def delete_text_message_spend_limit_override(
        self,
        request: EndUserMessagingDeleteTextMessageSpendLimitOverrideRequest | None = None,
    ) -> EndUserMessagingDeleteTextMessageSpendLimitOverrideResponse:
        client = self._require_client()
        return await self._execute(client.delete_text_message_spend_limit_override, request, EndUserMessagingDeleteTextMessageSpendLimitOverrideResponse)

    async def delete_verified_destination_number(
        self,
        request: EndUserMessagingDeleteVerifiedDestinationNumberRequest,
    ) -> EndUserMessagingDeleteVerifiedDestinationNumberResponse:
        client = self._require_client()
        return await self._execute(client.delete_verified_destination_number, request, EndUserMessagingDeleteVerifiedDestinationNumberResponse)

    async def delete_voice_message_spend_limit_override(
        self,
        request: EndUserMessagingDeleteVoiceMessageSpendLimitOverrideRequest | None = None,
    ) -> EndUserMessagingDeleteVoiceMessageSpendLimitOverrideResponse:
        client = self._require_client()
        return await self._execute(client.delete_voice_message_spend_limit_override, request, EndUserMessagingDeleteVoiceMessageSpendLimitOverrideResponse)

    async def describe_account_attributes(
        self,
        request: EndUserMessagingDescribeAccountAttributesRequest | None = None,
    ) -> EndUserMessagingDescribeAccountAttributesResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_attributes, request, EndUserMessagingDescribeAccountAttributesResponse)

    async def describe_account_attributes_paginated(
        self,
        request: EndUserMessagingDescribeAccountAttributesRequest | None = None,
    ) -> list[EndUserMessagingDescribeAccountAttributesResponse]:
        return await self._paginate('describe_account_attributes', request, EndUserMessagingDescribeAccountAttributesResponse)

    async def describe_account_limits(
        self,
        request: EndUserMessagingDescribeAccountLimitsRequest | None = None,
    ) -> EndUserMessagingDescribeAccountLimitsResponse:
        client = self._require_client()
        return await self._execute(client.describe_account_limits, request, EndUserMessagingDescribeAccountLimitsResponse)

    async def describe_account_limits_paginated(
        self,
        request: EndUserMessagingDescribeAccountLimitsRequest | None = None,
    ) -> list[EndUserMessagingDescribeAccountLimitsResponse]:
        return await self._paginate('describe_account_limits', request, EndUserMessagingDescribeAccountLimitsResponse)

    async def describe_configuration_sets(
        self,
        request: EndUserMessagingDescribeConfigurationSetsRequest | None = None,
    ) -> EndUserMessagingDescribeConfigurationSetsResponse:
        client = self._require_client()
        return await self._execute(client.describe_configuration_sets, request, EndUserMessagingDescribeConfigurationSetsResponse)

    async def describe_configuration_sets_paginated(
        self,
        request: EndUserMessagingDescribeConfigurationSetsRequest | None = None,
    ) -> list[EndUserMessagingDescribeConfigurationSetsResponse]:
        return await self._paginate('describe_configuration_sets', request, EndUserMessagingDescribeConfigurationSetsResponse)

    async def describe_keywords(
        self,
        request: EndUserMessagingDescribeKeywordsRequest,
    ) -> EndUserMessagingDescribeKeywordsResponse:
        client = self._require_client()
        return await self._execute(client.describe_keywords, request, EndUserMessagingDescribeKeywordsResponse)

    async def describe_keywords_paginated(
        self,
        request: EndUserMessagingDescribeKeywordsRequest,
    ) -> list[EndUserMessagingDescribeKeywordsResponse]:
        return await self._paginate('describe_keywords', request, EndUserMessagingDescribeKeywordsResponse)

    async def describe_notify_configurations(
        self,
        request: EndUserMessagingDescribeNotifyConfigurationsRequest | None = None,
    ) -> EndUserMessagingDescribeNotifyConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_notify_configurations, request, EndUserMessagingDescribeNotifyConfigurationsResponse)

    async def describe_notify_configurations_paginated(
        self,
        request: EndUserMessagingDescribeNotifyConfigurationsRequest | None = None,
    ) -> list[EndUserMessagingDescribeNotifyConfigurationsResponse]:
        return await self._paginate('describe_notify_configurations', request, EndUserMessagingDescribeNotifyConfigurationsResponse)

    async def describe_notify_templates(
        self,
        request: EndUserMessagingDescribeNotifyTemplatesRequest | None = None,
    ) -> EndUserMessagingDescribeNotifyTemplatesResponse:
        client = self._require_client()
        return await self._execute(client.describe_notify_templates, request, EndUserMessagingDescribeNotifyTemplatesResponse)

    async def describe_notify_templates_paginated(
        self,
        request: EndUserMessagingDescribeNotifyTemplatesRequest | None = None,
    ) -> list[EndUserMessagingDescribeNotifyTemplatesResponse]:
        return await self._paginate('describe_notify_templates', request, EndUserMessagingDescribeNotifyTemplatesResponse)

    async def describe_opt_out_lists(
        self,
        request: EndUserMessagingDescribeOptOutListsRequest | None = None,
    ) -> EndUserMessagingDescribeOptOutListsResponse:
        client = self._require_client()
        return await self._execute(client.describe_opt_out_lists, request, EndUserMessagingDescribeOptOutListsResponse)

    async def describe_opt_out_lists_paginated(
        self,
        request: EndUserMessagingDescribeOptOutListsRequest | None = None,
    ) -> list[EndUserMessagingDescribeOptOutListsResponse]:
        return await self._paginate('describe_opt_out_lists', request, EndUserMessagingDescribeOptOutListsResponse)

    async def describe_opted_out_numbers(
        self,
        request: EndUserMessagingDescribeOptedOutNumbersRequest,
    ) -> EndUserMessagingDescribeOptedOutNumbersResponse:
        client = self._require_client()
        return await self._execute(client.describe_opted_out_numbers, request, EndUserMessagingDescribeOptedOutNumbersResponse)

    async def describe_opted_out_numbers_paginated(
        self,
        request: EndUserMessagingDescribeOptedOutNumbersRequest,
    ) -> list[EndUserMessagingDescribeOptedOutNumbersResponse]:
        return await self._paginate('describe_opted_out_numbers', request, EndUserMessagingDescribeOptedOutNumbersResponse)

    async def describe_phone_numbers(
        self,
        request: EndUserMessagingDescribePhoneNumbersRequest | None = None,
    ) -> EndUserMessagingDescribePhoneNumbersResponse:
        client = self._require_client()
        return await self._execute(client.describe_phone_numbers, request, EndUserMessagingDescribePhoneNumbersResponse)

    async def describe_phone_numbers_paginated(
        self,
        request: EndUserMessagingDescribePhoneNumbersRequest | None = None,
    ) -> list[EndUserMessagingDescribePhoneNumbersResponse]:
        return await self._paginate('describe_phone_numbers', request, EndUserMessagingDescribePhoneNumbersResponse)

    async def describe_pools(
        self,
        request: EndUserMessagingDescribePoolsRequest | None = None,
    ) -> EndUserMessagingDescribePoolsResponse:
        client = self._require_client()
        return await self._execute(client.describe_pools, request, EndUserMessagingDescribePoolsResponse)

    async def describe_pools_paginated(
        self,
        request: EndUserMessagingDescribePoolsRequest | None = None,
    ) -> list[EndUserMessagingDescribePoolsResponse]:
        return await self._paginate('describe_pools', request, EndUserMessagingDescribePoolsResponse)

    async def describe_protect_configurations(
        self,
        request: EndUserMessagingDescribeProtectConfigurationsRequest | None = None,
    ) -> EndUserMessagingDescribeProtectConfigurationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_protect_configurations, request, EndUserMessagingDescribeProtectConfigurationsResponse)

    async def describe_protect_configurations_paginated(
        self,
        request: EndUserMessagingDescribeProtectConfigurationsRequest | None = None,
    ) -> list[EndUserMessagingDescribeProtectConfigurationsResponse]:
        return await self._paginate('describe_protect_configurations', request, EndUserMessagingDescribeProtectConfigurationsResponse)

    async def describe_rcs_agent_country_launch_status(
        self,
        request: EndUserMessagingDescribeRcsAgentCountryLaunchStatusRequest,
    ) -> EndUserMessagingDescribeRcsAgentCountryLaunchStatusResponse:
        client = self._require_client()
        return await self._execute(client.describe_rcs_agent_country_launch_status, request, EndUserMessagingDescribeRcsAgentCountryLaunchStatusResponse)

    async def describe_rcs_agent_country_launch_status_paginated(
        self,
        request: EndUserMessagingDescribeRcsAgentCountryLaunchStatusRequest,
    ) -> list[EndUserMessagingDescribeRcsAgentCountryLaunchStatusResponse]:
        return await self._paginate('describe_rcs_agent_country_launch_status', request, EndUserMessagingDescribeRcsAgentCountryLaunchStatusResponse)

    async def describe_rcs_agents(
        self,
        request: EndUserMessagingDescribeRcsAgentsRequest | None = None,
    ) -> EndUserMessagingDescribeRcsAgentsResponse:
        client = self._require_client()
        return await self._execute(client.describe_rcs_agents, request, EndUserMessagingDescribeRcsAgentsResponse)

    async def describe_rcs_agents_paginated(
        self,
        request: EndUserMessagingDescribeRcsAgentsRequest | None = None,
    ) -> list[EndUserMessagingDescribeRcsAgentsResponse]:
        return await self._paginate('describe_rcs_agents', request, EndUserMessagingDescribeRcsAgentsResponse)

    async def describe_registration_attachments(
        self,
        request: EndUserMessagingDescribeRegistrationAttachmentsRequest | None = None,
    ) -> EndUserMessagingDescribeRegistrationAttachmentsResponse:
        client = self._require_client()
        return await self._execute(client.describe_registration_attachments, request, EndUserMessagingDescribeRegistrationAttachmentsResponse)

    async def describe_registration_attachments_paginated(
        self,
        request: EndUserMessagingDescribeRegistrationAttachmentsRequest | None = None,
    ) -> list[EndUserMessagingDescribeRegistrationAttachmentsResponse]:
        return await self._paginate('describe_registration_attachments', request, EndUserMessagingDescribeRegistrationAttachmentsResponse)

    async def describe_registration_field_definitions(
        self,
        request: EndUserMessagingDescribeRegistrationFieldDefinitionsRequest,
    ) -> EndUserMessagingDescribeRegistrationFieldDefinitionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_registration_field_definitions, request, EndUserMessagingDescribeRegistrationFieldDefinitionsResponse)

    async def describe_registration_field_definitions_paginated(
        self,
        request: EndUserMessagingDescribeRegistrationFieldDefinitionsRequest,
    ) -> list[EndUserMessagingDescribeRegistrationFieldDefinitionsResponse]:
        return await self._paginate('describe_registration_field_definitions', request, EndUserMessagingDescribeRegistrationFieldDefinitionsResponse)

    async def describe_registration_field_values(
        self,
        request: EndUserMessagingDescribeRegistrationFieldValuesRequest,
    ) -> EndUserMessagingDescribeRegistrationFieldValuesResponse:
        client = self._require_client()
        return await self._execute(client.describe_registration_field_values, request, EndUserMessagingDescribeRegistrationFieldValuesResponse)

    async def describe_registration_field_values_paginated(
        self,
        request: EndUserMessagingDescribeRegistrationFieldValuesRequest,
    ) -> list[EndUserMessagingDescribeRegistrationFieldValuesResponse]:
        return await self._paginate('describe_registration_field_values', request, EndUserMessagingDescribeRegistrationFieldValuesResponse)

    async def describe_registration_section_definitions(
        self,
        request: EndUserMessagingDescribeRegistrationSectionDefinitionsRequest,
    ) -> EndUserMessagingDescribeRegistrationSectionDefinitionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_registration_section_definitions, request, EndUserMessagingDescribeRegistrationSectionDefinitionsResponse)

    async def describe_registration_section_definitions_paginated(
        self,
        request: EndUserMessagingDescribeRegistrationSectionDefinitionsRequest,
    ) -> list[EndUserMessagingDescribeRegistrationSectionDefinitionsResponse]:
        return await self._paginate('describe_registration_section_definitions', request, EndUserMessagingDescribeRegistrationSectionDefinitionsResponse)

    async def describe_registration_type_definitions(
        self,
        request: EndUserMessagingDescribeRegistrationTypeDefinitionsRequest | None = None,
    ) -> EndUserMessagingDescribeRegistrationTypeDefinitionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_registration_type_definitions, request, EndUserMessagingDescribeRegistrationTypeDefinitionsResponse)

    async def describe_registration_type_definitions_paginated(
        self,
        request: EndUserMessagingDescribeRegistrationTypeDefinitionsRequest | None = None,
    ) -> list[EndUserMessagingDescribeRegistrationTypeDefinitionsResponse]:
        return await self._paginate('describe_registration_type_definitions', request, EndUserMessagingDescribeRegistrationTypeDefinitionsResponse)

    async def describe_registration_versions(
        self,
        request: EndUserMessagingDescribeRegistrationVersionsRequest,
    ) -> EndUserMessagingDescribeRegistrationVersionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_registration_versions, request, EndUserMessagingDescribeRegistrationVersionsResponse)

    async def describe_registration_versions_paginated(
        self,
        request: EndUserMessagingDescribeRegistrationVersionsRequest,
    ) -> list[EndUserMessagingDescribeRegistrationVersionsResponse]:
        return await self._paginate('describe_registration_versions', request, EndUserMessagingDescribeRegistrationVersionsResponse)

    async def describe_registrations(
        self,
        request: EndUserMessagingDescribeRegistrationsRequest | None = None,
    ) -> EndUserMessagingDescribeRegistrationsResponse:
        client = self._require_client()
        return await self._execute(client.describe_registrations, request, EndUserMessagingDescribeRegistrationsResponse)

    async def describe_registrations_paginated(
        self,
        request: EndUserMessagingDescribeRegistrationsRequest | None = None,
    ) -> list[EndUserMessagingDescribeRegistrationsResponse]:
        return await self._paginate('describe_registrations', request, EndUserMessagingDescribeRegistrationsResponse)

    async def describe_sender_ids(
        self,
        request: EndUserMessagingDescribeSenderIdsRequest | None = None,
    ) -> EndUserMessagingDescribeSenderIdsResponse:
        client = self._require_client()
        return await self._execute(client.describe_sender_ids, request, EndUserMessagingDescribeSenderIdsResponse)

    async def describe_sender_ids_paginated(
        self,
        request: EndUserMessagingDescribeSenderIdsRequest | None = None,
    ) -> list[EndUserMessagingDescribeSenderIdsResponse]:
        return await self._paginate('describe_sender_ids', request, EndUserMessagingDescribeSenderIdsResponse)

    async def describe_spend_limits(
        self,
        request: EndUserMessagingDescribeSpendLimitsRequest | None = None,
    ) -> EndUserMessagingDescribeSpendLimitsResponse:
        client = self._require_client()
        return await self._execute(client.describe_spend_limits, request, EndUserMessagingDescribeSpendLimitsResponse)

    async def describe_spend_limits_paginated(
        self,
        request: EndUserMessagingDescribeSpendLimitsRequest | None = None,
    ) -> list[EndUserMessagingDescribeSpendLimitsResponse]:
        return await self._paginate('describe_spend_limits', request, EndUserMessagingDescribeSpendLimitsResponse)

    async def describe_verified_destination_numbers(
        self,
        request: EndUserMessagingDescribeVerifiedDestinationNumbersRequest | None = None,
    ) -> EndUserMessagingDescribeVerifiedDestinationNumbersResponse:
        client = self._require_client()
        return await self._execute(client.describe_verified_destination_numbers, request, EndUserMessagingDescribeVerifiedDestinationNumbersResponse)

    async def describe_verified_destination_numbers_paginated(
        self,
        request: EndUserMessagingDescribeVerifiedDestinationNumbersRequest | None = None,
    ) -> list[EndUserMessagingDescribeVerifiedDestinationNumbersResponse]:
        return await self._paginate('describe_verified_destination_numbers', request, EndUserMessagingDescribeVerifiedDestinationNumbersResponse)

    async def disassociate_origination_identity(
        self,
        request: EndUserMessagingDisassociateOriginationIdentityRequest,
    ) -> EndUserMessagingDisassociateOriginationIdentityResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_origination_identity, request, EndUserMessagingDisassociateOriginationIdentityResponse)

    async def disassociate_protect_configuration(
        self,
        request: EndUserMessagingDisassociateProtectConfigurationRequest,
    ) -> EndUserMessagingDisassociateProtectConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_protect_configuration, request, EndUserMessagingDisassociateProtectConfigurationResponse)

    async def discard_registration_version(
        self,
        request: EndUserMessagingDiscardRegistrationVersionRequest,
    ) -> EndUserMessagingDiscardRegistrationVersionResponse:
        client = self._require_client()
        return await self._execute(client.discard_registration_version, request, EndUserMessagingDiscardRegistrationVersionResponse)

    async def get_protect_configuration_country_rule_set(
        self,
        request: EndUserMessagingGetProtectConfigurationCountryRuleSetRequest,
    ) -> EndUserMessagingGetProtectConfigurationCountryRuleSetResponse:
        client = self._require_client()
        return await self._execute(client.get_protect_configuration_country_rule_set, request, EndUserMessagingGetProtectConfigurationCountryRuleSetResponse)

    async def get_resource_policy(
        self,
        request: EndUserMessagingGetResourcePolicyRequest,
    ) -> EndUserMessagingGetResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_policy, request, EndUserMessagingGetResourcePolicyResponse)

    async def list_available_phone_numbers(
        self,
        request: EndUserMessagingListAvailablePhoneNumbersRequest,
    ) -> EndUserMessagingListAvailablePhoneNumbersResponse:
        client = self._require_client()
        return await self._execute(client.list_available_phone_numbers, request, EndUserMessagingListAvailablePhoneNumbersResponse)

    async def list_available_phone_numbers_paginated(
        self,
        request: EndUserMessagingListAvailablePhoneNumbersRequest,
    ) -> list[EndUserMessagingListAvailablePhoneNumbersResponse]:
        return await self._paginate('list_available_phone_numbers', request, EndUserMessagingListAvailablePhoneNumbersResponse)

    async def list_notify_countries(
        self,
        request: EndUserMessagingListNotifyCountriesRequest | None = None,
    ) -> EndUserMessagingListNotifyCountriesResponse:
        client = self._require_client()
        return await self._execute(client.list_notify_countries, request, EndUserMessagingListNotifyCountriesResponse)

    async def list_notify_countries_paginated(
        self,
        request: EndUserMessagingListNotifyCountriesRequest | None = None,
    ) -> list[EndUserMessagingListNotifyCountriesResponse]:
        return await self._paginate('list_notify_countries', request, EndUserMessagingListNotifyCountriesResponse)

    async def list_pool_origination_identities(
        self,
        request: EndUserMessagingListPoolOriginationIdentitiesRequest,
    ) -> EndUserMessagingListPoolOriginationIdentitiesResponse:
        client = self._require_client()
        return await self._execute(client.list_pool_origination_identities, request, EndUserMessagingListPoolOriginationIdentitiesResponse)

    async def list_pool_origination_identities_paginated(
        self,
        request: EndUserMessagingListPoolOriginationIdentitiesRequest,
    ) -> list[EndUserMessagingListPoolOriginationIdentitiesResponse]:
        return await self._paginate('list_pool_origination_identities', request, EndUserMessagingListPoolOriginationIdentitiesResponse)

    async def list_protect_configuration_rule_set_number_overrides(
        self,
        request: EndUserMessagingListProtectConfigurationRuleSetNumberOverridesRequest,
    ) -> EndUserMessagingListProtectConfigurationRuleSetNumberOverridesResponse:
        client = self._require_client()
        return await self._execute(client.list_protect_configuration_rule_set_number_overrides, request, EndUserMessagingListProtectConfigurationRuleSetNumberOverridesResponse)

    async def list_protect_configuration_rule_set_number_overrides_paginated(
        self,
        request: EndUserMessagingListProtectConfigurationRuleSetNumberOverridesRequest,
    ) -> list[EndUserMessagingListProtectConfigurationRuleSetNumberOverridesResponse]:
        return await self._paginate('list_protect_configuration_rule_set_number_overrides', request, EndUserMessagingListProtectConfigurationRuleSetNumberOverridesResponse)

    async def list_registration_associations(
        self,
        request: EndUserMessagingListRegistrationAssociationsRequest,
    ) -> EndUserMessagingListRegistrationAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.list_registration_associations, request, EndUserMessagingListRegistrationAssociationsResponse)

    async def list_registration_associations_paginated(
        self,
        request: EndUserMessagingListRegistrationAssociationsRequest,
    ) -> list[EndUserMessagingListRegistrationAssociationsResponse]:
        return await self._paginate('list_registration_associations', request, EndUserMessagingListRegistrationAssociationsResponse)

    async def list_tags_for_resource(
        self,
        request: EndUserMessagingListTagsForResourceRequest,
    ) -> EndUserMessagingListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, EndUserMessagingListTagsForResourceResponse)

    async def put_keyword(
        self,
        request: EndUserMessagingPutKeywordRequest,
    ) -> EndUserMessagingPutKeywordResponse:
        client = self._require_client()
        return await self._execute(client.put_keyword, request, EndUserMessagingPutKeywordResponse)

    async def put_message_feedback(
        self,
        request: EndUserMessagingPutMessageFeedbackRequest,
    ) -> EndUserMessagingPutMessageFeedbackResponse:
        client = self._require_client()
        return await self._execute(client.put_message_feedback, request, EndUserMessagingPutMessageFeedbackResponse)

    async def put_opted_out_number(
        self,
        request: EndUserMessagingPutOptedOutNumberRequest,
    ) -> EndUserMessagingPutOptedOutNumberResponse:
        client = self._require_client()
        return await self._execute(client.put_opted_out_number, request, EndUserMessagingPutOptedOutNumberResponse)

    async def put_protect_configuration_rule_set_number_override(
        self,
        request: EndUserMessagingPutProtectConfigurationRuleSetNumberOverrideRequest,
    ) -> EndUserMessagingPutProtectConfigurationRuleSetNumberOverrideResponse:
        client = self._require_client()
        return await self._execute(client.put_protect_configuration_rule_set_number_override, request, EndUserMessagingPutProtectConfigurationRuleSetNumberOverrideResponse)

    async def put_registration_field_value(
        self,
        request: EndUserMessagingPutRegistrationFieldValueRequest,
    ) -> EndUserMessagingPutRegistrationFieldValueResponse:
        client = self._require_client()
        return await self._execute(client.put_registration_field_value, request, EndUserMessagingPutRegistrationFieldValueResponse)

    async def put_resource_policy(
        self,
        request: EndUserMessagingPutResourcePolicyRequest,
    ) -> EndUserMessagingPutResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_resource_policy, request, EndUserMessagingPutResourcePolicyResponse)

    async def release_phone_number(
        self,
        request: EndUserMessagingReleasePhoneNumberRequest,
    ) -> EndUserMessagingReleasePhoneNumberResponse:
        client = self._require_client()
        return await self._execute(client.release_phone_number, request, EndUserMessagingReleasePhoneNumberResponse)

    async def release_sender_id(
        self,
        request: EndUserMessagingReleaseSenderIdRequest,
    ) -> EndUserMessagingReleaseSenderIdResponse:
        client = self._require_client()
        return await self._execute(client.release_sender_id, request, EndUserMessagingReleaseSenderIdResponse)

    async def request_phone_number(
        self,
        request: EndUserMessagingRequestPhoneNumberRequest,
    ) -> EndUserMessagingRequestPhoneNumberResponse:
        client = self._require_client()
        return await self._execute(client.request_phone_number, request, EndUserMessagingRequestPhoneNumberResponse)

    async def request_sender_id(
        self,
        request: EndUserMessagingRequestSenderIdRequest,
    ) -> EndUserMessagingRequestSenderIdResponse:
        client = self._require_client()
        return await self._execute(client.request_sender_id, request, EndUserMessagingRequestSenderIdResponse)

    async def send_destination_number_verification_code(
        self,
        request: EndUserMessagingSendDestinationNumberVerificationCodeRequest,
    ) -> EndUserMessagingSendDestinationNumberVerificationCodeResponse:
        client = self._require_client()
        return await self._execute(client.send_destination_number_verification_code, request, EndUserMessagingSendDestinationNumberVerificationCodeResponse)

    async def send_media_message(
        self,
        request: EndUserMessagingSendMediaMessageRequest,
    ) -> EndUserMessagingSendMediaMessageResponse:
        client = self._require_client()
        return await self._execute(client.send_media_message, request, EndUserMessagingSendMediaMessageResponse)

    async def send_notify_text_message(
        self,
        request: EndUserMessagingSendNotifyTextMessageRequest,
    ) -> EndUserMessagingSendNotifyTextMessageResponse:
        client = self._require_client()
        return await self._execute(client.send_notify_text_message, request, EndUserMessagingSendNotifyTextMessageResponse)

    async def send_notify_voice_message(
        self,
        request: EndUserMessagingSendNotifyVoiceMessageRequest,
    ) -> EndUserMessagingSendNotifyVoiceMessageResponse:
        client = self._require_client()
        return await self._execute(client.send_notify_voice_message, request, EndUserMessagingSendNotifyVoiceMessageResponse)

    async def send_rcs_message(
        self,
        request: EndUserMessagingSendRcsMessageRequest,
    ) -> EndUserMessagingSendRcsMessageResponse:
        client = self._require_client()
        return await self._execute(client.send_rcs_message, request, EndUserMessagingSendRcsMessageResponse)

    async def send_text_message(
        self,
        request: EndUserMessagingSendTextMessageRequest,
    ) -> EndUserMessagingSendTextMessageResponse:
        client = self._require_client()
        return await self._execute(client.send_text_message, request, EndUserMessagingSendTextMessageResponse)

    async def send_voice_message(
        self,
        request: EndUserMessagingSendVoiceMessageRequest,
    ) -> EndUserMessagingSendVoiceMessageResponse:
        client = self._require_client()
        return await self._execute(client.send_voice_message, request, EndUserMessagingSendVoiceMessageResponse)

    async def set_account_default_protect_configuration(
        self,
        request: EndUserMessagingSetAccountDefaultProtectConfigurationRequest,
    ) -> EndUserMessagingSetAccountDefaultProtectConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.set_account_default_protect_configuration, request, EndUserMessagingSetAccountDefaultProtectConfigurationResponse)

    async def set_default_message_feedback_enabled(
        self,
        request: EndUserMessagingSetDefaultMessageFeedbackEnabledRequest,
    ) -> EndUserMessagingSetDefaultMessageFeedbackEnabledResponse:
        client = self._require_client()
        return await self._execute(client.set_default_message_feedback_enabled, request, EndUserMessagingSetDefaultMessageFeedbackEnabledResponse)

    async def set_default_message_type(
        self,
        request: EndUserMessagingSetDefaultMessageTypeRequest,
    ) -> EndUserMessagingSetDefaultMessageTypeResponse:
        client = self._require_client()
        return await self._execute(client.set_default_message_type, request, EndUserMessagingSetDefaultMessageTypeResponse)

    async def set_default_sender_id(
        self,
        request: EndUserMessagingSetDefaultSenderIdRequest,
    ) -> EndUserMessagingSetDefaultSenderIdResponse:
        client = self._require_client()
        return await self._execute(client.set_default_sender_id, request, EndUserMessagingSetDefaultSenderIdResponse)

    async def set_media_message_spend_limit_override(
        self,
        request: EndUserMessagingSetMediaMessageSpendLimitOverrideRequest,
    ) -> EndUserMessagingSetMediaMessageSpendLimitOverrideResponse:
        client = self._require_client()
        return await self._execute(client.set_media_message_spend_limit_override, request, EndUserMessagingSetMediaMessageSpendLimitOverrideResponse)

    async def set_notify_message_spend_limit_override(
        self,
        request: EndUserMessagingSetNotifyMessageSpendLimitOverrideRequest,
    ) -> EndUserMessagingSetNotifyMessageSpendLimitOverrideResponse:
        client = self._require_client()
        return await self._execute(client.set_notify_message_spend_limit_override, request, EndUserMessagingSetNotifyMessageSpendLimitOverrideResponse)

    async def set_rcs_message_spend_limit_override(
        self,
        request: EndUserMessagingSetRcsMessageSpendLimitOverrideRequest,
    ) -> EndUserMessagingSetRcsMessageSpendLimitOverrideResponse:
        client = self._require_client()
        return await self._execute(client.set_rcs_message_spend_limit_override, request, EndUserMessagingSetRcsMessageSpendLimitOverrideResponse)

    async def set_text_message_spend_limit_override(
        self,
        request: EndUserMessagingSetTextMessageSpendLimitOverrideRequest,
    ) -> EndUserMessagingSetTextMessageSpendLimitOverrideResponse:
        client = self._require_client()
        return await self._execute(client.set_text_message_spend_limit_override, request, EndUserMessagingSetTextMessageSpendLimitOverrideResponse)

    async def set_voice_message_spend_limit_override(
        self,
        request: EndUserMessagingSetVoiceMessageSpendLimitOverrideRequest,
    ) -> EndUserMessagingSetVoiceMessageSpendLimitOverrideResponse:
        client = self._require_client()
        return await self._execute(client.set_voice_message_spend_limit_override, request, EndUserMessagingSetVoiceMessageSpendLimitOverrideResponse)

    async def submit_registration_version(
        self,
        request: EndUserMessagingSubmitRegistrationVersionRequest,
    ) -> EndUserMessagingSubmitRegistrationVersionResponse:
        client = self._require_client()
        return await self._execute(client.submit_registration_version, request, EndUserMessagingSubmitRegistrationVersionResponse)

    async def tag_resource(
        self,
        request: EndUserMessagingTagResourceRequest,
    ) -> EndUserMessagingTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, EndUserMessagingTagResourceResponse)

    async def untag_resource(
        self,
        request: EndUserMessagingUntagResourceRequest,
    ) -> EndUserMessagingUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, EndUserMessagingUntagResourceResponse)

    async def update_event_destination(
        self,
        request: EndUserMessagingUpdateEventDestinationRequest,
    ) -> EndUserMessagingUpdateEventDestinationResponse:
        client = self._require_client()
        return await self._execute(client.update_event_destination, request, EndUserMessagingUpdateEventDestinationResponse)

    async def update_notify_configuration(
        self,
        request: EndUserMessagingUpdateNotifyConfigurationRequest,
    ) -> EndUserMessagingUpdateNotifyConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_notify_configuration, request, EndUserMessagingUpdateNotifyConfigurationResponse)

    async def update_phone_number(
        self,
        request: EndUserMessagingUpdatePhoneNumberRequest,
    ) -> EndUserMessagingUpdatePhoneNumberResponse:
        client = self._require_client()
        return await self._execute(client.update_phone_number, request, EndUserMessagingUpdatePhoneNumberResponse)

    async def update_pool(
        self,
        request: EndUserMessagingUpdatePoolRequest,
    ) -> EndUserMessagingUpdatePoolResponse:
        client = self._require_client()
        return await self._execute(client.update_pool, request, EndUserMessagingUpdatePoolResponse)

    async def update_protect_configuration(
        self,
        request: EndUserMessagingUpdateProtectConfigurationRequest,
    ) -> EndUserMessagingUpdateProtectConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_protect_configuration, request, EndUserMessagingUpdateProtectConfigurationResponse)

    async def update_protect_configuration_country_rule_set(
        self,
        request: EndUserMessagingUpdateProtectConfigurationCountryRuleSetRequest,
    ) -> EndUserMessagingUpdateProtectConfigurationCountryRuleSetResponse:
        client = self._require_client()
        return await self._execute(client.update_protect_configuration_country_rule_set, request, EndUserMessagingUpdateProtectConfigurationCountryRuleSetResponse)

    async def update_rcs_agent(
        self,
        request: EndUserMessagingUpdateRcsAgentRequest,
    ) -> EndUserMessagingUpdateRcsAgentResponse:
        client = self._require_client()
        return await self._execute(client.update_rcs_agent, request, EndUserMessagingUpdateRcsAgentResponse)

    async def update_sender_id(
        self,
        request: EndUserMessagingUpdateSenderIdRequest,
    ) -> EndUserMessagingUpdateSenderIdResponse:
        client = self._require_client()
        return await self._execute(client.update_sender_id, request, EndUserMessagingUpdateSenderIdResponse)

    async def verify_destination_number(
        self,
        request: EndUserMessagingVerifyDestinationNumberRequest,
    ) -> EndUserMessagingVerifyDestinationNumberResponse:
        client = self._require_client()
        return await self._execute(client.verify_destination_number, request, EndUserMessagingVerifyDestinationNumberResponse)
