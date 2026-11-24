from werkflow_aws.models.sns import (
    SNSAddPermissionRequest,
    SNSAddPermissionResponse,
    SNSCheckIfPhoneNumberIsOptedOutRequest,
    SNSCheckIfPhoneNumberIsOptedOutResponse,
    SNSConfirmSubscriptionRequest,
    SNSConfirmSubscriptionResponse,
    SNSCreatePlatformApplicationRequest,
    SNSCreatePlatformApplicationResponse,
    SNSCreatePlatformEndpointRequest,
    SNSCreatePlatformEndpointResponse,
    SNSCreateSMSSandboxPhoneNumberRequest,
    SNSCreateSMSSandboxPhoneNumberResponse,
    SNSCreateTopicRequest,
    SNSCreateTopicResponse,
    SNSDeleteEndpointRequest,
    SNSDeleteEndpointResponse,
    SNSDeletePlatformApplicationRequest,
    SNSDeletePlatformApplicationResponse,
    SNSDeleteSMSSandboxPhoneNumberRequest,
    SNSDeleteSMSSandboxPhoneNumberResponse,
    SNSDeleteTopicRequest,
    SNSDeleteTopicResponse,
    SNSGetDataProtectionPolicyRequest,
    SNSGetDataProtectionPolicyResponse,
    SNSGetEndpointAttributesRequest,
    SNSGetEndpointAttributesResponse,
    SNSGetPlatformApplicationAttributesRequest,
    SNSGetPlatformApplicationAttributesResponse,
    SNSGetSMSAttributesRequest,
    SNSGetSMSAttributesResponse,
    SNSGetSMSSandboxAccountStatusRequest,
    SNSGetSMSSandboxAccountStatusResponse,
    SNSGetSubscriptionAttributesRequest,
    SNSGetSubscriptionAttributesResponse,
    SNSGetTopicAttributesRequest,
    SNSGetTopicAttributesResponse,
    SNSListEndpointsByPlatformApplicationRequest,
    SNSListEndpointsByPlatformApplicationResponse,
    SNSListOriginationNumbersRequest,
    SNSListOriginationNumbersResponse,
    SNSListPhoneNumbersOptedOutRequest,
    SNSListPhoneNumbersOptedOutResponse,
    SNSListPlatformApplicationsRequest,
    SNSListPlatformApplicationsResponse,
    SNSListSMSSandboxPhoneNumbersRequest,
    SNSListSMSSandboxPhoneNumbersResponse,
    SNSListSubscriptionsByTopicRequest,
    SNSListSubscriptionsByTopicResponse,
    SNSListSubscriptionsRequest,
    SNSListSubscriptionsResponse,
    SNSListTagsForResourceRequest,
    SNSListTagsForResourceResponse,
    SNSListTopicsRequest,
    SNSListTopicsResponse,
    SNSOptInPhoneNumberRequest,
    SNSOptInPhoneNumberResponse,
    SNSPublishBatchRequest,
    SNSPublishBatchResponse,
    SNSPublishRequest,
    SNSPublishResponse,
    SNSPutDataProtectionPolicyRequest,
    SNSPutDataProtectionPolicyResponse,
    SNSRemovePermissionRequest,
    SNSRemovePermissionResponse,
    SNSSetEndpointAttributesRequest,
    SNSSetEndpointAttributesResponse,
    SNSSetPlatformApplicationAttributesRequest,
    SNSSetPlatformApplicationAttributesResponse,
    SNSSetSMSAttributesRequest,
    SNSSetSMSAttributesResponse,
    SNSSetSubscriptionAttributesRequest,
    SNSSetSubscriptionAttributesResponse,
    SNSSetTopicAttributesRequest,
    SNSSetTopicAttributesResponse,
    SNSSubscribeRequest,
    SNSSubscribeResponse,
    SNSTagResourceRequest,
    SNSTagResourceResponse,
    SNSUnsubscribeRequest,
    SNSUnsubscribeResponse,
    SNSUntagResourceRequest,
    SNSUntagResourceResponse,
    SNSVerifySMSSandboxPhoneNumberRequest,
    SNSVerifySMSSandboxPhoneNumberResponse,
)
from werkflow_aws.types.sns_client import SNSClient
from .base import AWSBaseService


class AWSSNS(AWSBaseService[SNSClient]):
    service_name = 'sns'
    boto3_service_name = 'sns'

    def __init__(self) -> None:
        super().__init__(service_name='sns', boto3_service_name='sns')

    async def add_permission(
        self,
        request: SNSAddPermissionRequest,
    ) -> SNSAddPermissionResponse:
        client = self._require_client()
        return await self._execute(client.add_permission, request, SNSAddPermissionResponse)

    async def check_if_phone_number_is_opted_out(
        self,
        request: SNSCheckIfPhoneNumberIsOptedOutRequest,
    ) -> SNSCheckIfPhoneNumberIsOptedOutResponse:
        client = self._require_client()
        return await self._execute(client.check_if_phone_number_is_opted_out, request, SNSCheckIfPhoneNumberIsOptedOutResponse)

    async def confirm_subscription(
        self,
        request: SNSConfirmSubscriptionRequest,
    ) -> SNSConfirmSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.confirm_subscription, request, SNSConfirmSubscriptionResponse)

    async def create_platform_application(
        self,
        request: SNSCreatePlatformApplicationRequest,
    ) -> SNSCreatePlatformApplicationResponse:
        client = self._require_client()
        return await self._execute(client.create_platform_application, request, SNSCreatePlatformApplicationResponse)

    async def create_platform_endpoint(
        self,
        request: SNSCreatePlatformEndpointRequest,
    ) -> SNSCreatePlatformEndpointResponse:
        client = self._require_client()
        return await self._execute(client.create_platform_endpoint, request, SNSCreatePlatformEndpointResponse)

    async def create_sms_sandbox_phone_number(
        self,
        request: SNSCreateSMSSandboxPhoneNumberRequest,
    ) -> SNSCreateSMSSandboxPhoneNumberResponse:
        client = self._require_client()
        return await self._execute(client.create_sms_sandbox_phone_number, request, SNSCreateSMSSandboxPhoneNumberResponse)

    async def create_topic(
        self,
        request: SNSCreateTopicRequest,
    ) -> SNSCreateTopicResponse:
        client = self._require_client()
        return await self._execute(client.create_topic, request, SNSCreateTopicResponse)

    async def delete_endpoint(
        self,
        request: SNSDeleteEndpointRequest,
    ) -> SNSDeleteEndpointResponse:
        client = self._require_client()
        return await self._execute(client.delete_endpoint, request, SNSDeleteEndpointResponse)

    async def delete_platform_application(
        self,
        request: SNSDeletePlatformApplicationRequest,
    ) -> SNSDeletePlatformApplicationResponse:
        client = self._require_client()
        return await self._execute(client.delete_platform_application, request, SNSDeletePlatformApplicationResponse)

    async def delete_sms_sandbox_phone_number(
        self,
        request: SNSDeleteSMSSandboxPhoneNumberRequest,
    ) -> SNSDeleteSMSSandboxPhoneNumberResponse:
        client = self._require_client()
        return await self._execute(client.delete_sms_sandbox_phone_number, request, SNSDeleteSMSSandboxPhoneNumberResponse)

    async def delete_topic(
        self,
        request: SNSDeleteTopicRequest,
    ) -> SNSDeleteTopicResponse:
        client = self._require_client()
        return await self._execute(client.delete_topic, request, SNSDeleteTopicResponse)

    async def get_data_protection_policy(
        self,
        request: SNSGetDataProtectionPolicyRequest,
    ) -> SNSGetDataProtectionPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_data_protection_policy, request, SNSGetDataProtectionPolicyResponse)

    async def get_endpoint_attributes(
        self,
        request: SNSGetEndpointAttributesRequest,
    ) -> SNSGetEndpointAttributesResponse:
        client = self._require_client()
        return await self._execute(client.get_endpoint_attributes, request, SNSGetEndpointAttributesResponse)

    async def get_platform_application_attributes(
        self,
        request: SNSGetPlatformApplicationAttributesRequest,
    ) -> SNSGetPlatformApplicationAttributesResponse:
        client = self._require_client()
        return await self._execute(client.get_platform_application_attributes, request, SNSGetPlatformApplicationAttributesResponse)

    async def get_sms_attributes(
        self,
        request: SNSGetSMSAttributesRequest | None = None,
    ) -> SNSGetSMSAttributesResponse:
        client = self._require_client()
        return await self._execute(client.get_sms_attributes, request, SNSGetSMSAttributesResponse)

    async def get_sms_sandbox_account_status(
        self,
        request: SNSGetSMSSandboxAccountStatusRequest | None = None,
    ) -> SNSGetSMSSandboxAccountStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_sms_sandbox_account_status, request, SNSGetSMSSandboxAccountStatusResponse)

    async def get_subscription_attributes(
        self,
        request: SNSGetSubscriptionAttributesRequest,
    ) -> SNSGetSubscriptionAttributesResponse:
        client = self._require_client()
        return await self._execute(client.get_subscription_attributes, request, SNSGetSubscriptionAttributesResponse)

    async def get_topic_attributes(
        self,
        request: SNSGetTopicAttributesRequest,
    ) -> SNSGetTopicAttributesResponse:
        client = self._require_client()
        return await self._execute(client.get_topic_attributes, request, SNSGetTopicAttributesResponse)

    async def list_endpoints_by_platform_application(
        self,
        request: SNSListEndpointsByPlatformApplicationRequest,
    ) -> SNSListEndpointsByPlatformApplicationResponse:
        client = self._require_client()
        return await self._execute(client.list_endpoints_by_platform_application, request, SNSListEndpointsByPlatformApplicationResponse)

    async def list_endpoints_by_platform_application_paginated(
        self,
        request: SNSListEndpointsByPlatformApplicationRequest,
    ) -> list[SNSListEndpointsByPlatformApplicationResponse]:
        return await self._paginate('list_endpoints_by_platform_application', request, SNSListEndpointsByPlatformApplicationResponse)

    async def list_origination_numbers(
        self,
        request: SNSListOriginationNumbersRequest | None = None,
    ) -> SNSListOriginationNumbersResponse:
        client = self._require_client()
        return await self._execute(client.list_origination_numbers, request, SNSListOriginationNumbersResponse)

    async def list_origination_numbers_paginated(
        self,
        request: SNSListOriginationNumbersRequest | None = None,
    ) -> list[SNSListOriginationNumbersResponse]:
        return await self._paginate('list_origination_numbers', request, SNSListOriginationNumbersResponse)

    async def list_phone_numbers_opted_out(
        self,
        request: SNSListPhoneNumbersOptedOutRequest | None = None,
    ) -> SNSListPhoneNumbersOptedOutResponse:
        client = self._require_client()
        return await self._execute(client.list_phone_numbers_opted_out, request, SNSListPhoneNumbersOptedOutResponse)

    async def list_phone_numbers_opted_out_paginated(
        self,
        request: SNSListPhoneNumbersOptedOutRequest | None = None,
    ) -> list[SNSListPhoneNumbersOptedOutResponse]:
        return await self._paginate('list_phone_numbers_opted_out', request, SNSListPhoneNumbersOptedOutResponse)

    async def list_platform_applications(
        self,
        request: SNSListPlatformApplicationsRequest | None = None,
    ) -> SNSListPlatformApplicationsResponse:
        client = self._require_client()
        return await self._execute(client.list_platform_applications, request, SNSListPlatformApplicationsResponse)

    async def list_platform_applications_paginated(
        self,
        request: SNSListPlatformApplicationsRequest | None = None,
    ) -> list[SNSListPlatformApplicationsResponse]:
        return await self._paginate('list_platform_applications', request, SNSListPlatformApplicationsResponse)

    async def list_sms_sandbox_phone_numbers(
        self,
        request: SNSListSMSSandboxPhoneNumbersRequest | None = None,
    ) -> SNSListSMSSandboxPhoneNumbersResponse:
        client = self._require_client()
        return await self._execute(client.list_sms_sandbox_phone_numbers, request, SNSListSMSSandboxPhoneNumbersResponse)

    async def list_sms_sandbox_phone_numbers_paginated(
        self,
        request: SNSListSMSSandboxPhoneNumbersRequest | None = None,
    ) -> list[SNSListSMSSandboxPhoneNumbersResponse]:
        return await self._paginate('list_sms_sandbox_phone_numbers', request, SNSListSMSSandboxPhoneNumbersResponse)

    async def list_subscriptions(
        self,
        request: SNSListSubscriptionsRequest | None = None,
    ) -> SNSListSubscriptionsResponse:
        client = self._require_client()
        return await self._execute(client.list_subscriptions, request, SNSListSubscriptionsResponse)

    async def list_subscriptions_paginated(
        self,
        request: SNSListSubscriptionsRequest | None = None,
    ) -> list[SNSListSubscriptionsResponse]:
        return await self._paginate('list_subscriptions', request, SNSListSubscriptionsResponse)

    async def list_subscriptions_by_topic(
        self,
        request: SNSListSubscriptionsByTopicRequest,
    ) -> SNSListSubscriptionsByTopicResponse:
        client = self._require_client()
        return await self._execute(client.list_subscriptions_by_topic, request, SNSListSubscriptionsByTopicResponse)

    async def list_subscriptions_by_topic_paginated(
        self,
        request: SNSListSubscriptionsByTopicRequest,
    ) -> list[SNSListSubscriptionsByTopicResponse]:
        return await self._paginate('list_subscriptions_by_topic', request, SNSListSubscriptionsByTopicResponse)

    async def list_tags_for_resource(
        self,
        request: SNSListTagsForResourceRequest,
    ) -> SNSListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, SNSListTagsForResourceResponse)

    async def list_topics(
        self,
        request: SNSListTopicsRequest | None = None,
    ) -> SNSListTopicsResponse:
        client = self._require_client()
        return await self._execute(client.list_topics, request, SNSListTopicsResponse)

    async def list_topics_paginated(
        self,
        request: SNSListTopicsRequest | None = None,
    ) -> list[SNSListTopicsResponse]:
        return await self._paginate('list_topics', request, SNSListTopicsResponse)

    async def opt_in_phone_number(
        self,
        request: SNSOptInPhoneNumberRequest,
    ) -> SNSOptInPhoneNumberResponse:
        client = self._require_client()
        return await self._execute(client.opt_in_phone_number, request, SNSOptInPhoneNumberResponse)

    async def publish(
        self,
        request: SNSPublishRequest,
    ) -> SNSPublishResponse:
        client = self._require_client()
        return await self._execute(client.publish, request, SNSPublishResponse)

    async def publish_batch(
        self,
        request: SNSPublishBatchRequest,
    ) -> SNSPublishBatchResponse:
        client = self._require_client()
        return await self._execute(client.publish_batch, request, SNSPublishBatchResponse)

    async def put_data_protection_policy(
        self,
        request: SNSPutDataProtectionPolicyRequest,
    ) -> SNSPutDataProtectionPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_data_protection_policy, request, SNSPutDataProtectionPolicyResponse)

    async def remove_permission(
        self,
        request: SNSRemovePermissionRequest,
    ) -> SNSRemovePermissionResponse:
        client = self._require_client()
        return await self._execute(client.remove_permission, request, SNSRemovePermissionResponse)

    async def set_endpoint_attributes(
        self,
        request: SNSSetEndpointAttributesRequest,
    ) -> SNSSetEndpointAttributesResponse:
        client = self._require_client()
        return await self._execute(client.set_endpoint_attributes, request, SNSSetEndpointAttributesResponse)

    async def set_platform_application_attributes(
        self,
        request: SNSSetPlatformApplicationAttributesRequest,
    ) -> SNSSetPlatformApplicationAttributesResponse:
        client = self._require_client()
        return await self._execute(client.set_platform_application_attributes, request, SNSSetPlatformApplicationAttributesResponse)

    async def set_sms_attributes(
        self,
        request: SNSSetSMSAttributesRequest,
    ) -> SNSSetSMSAttributesResponse:
        client = self._require_client()
        return await self._execute(client.set_sms_attributes, request, SNSSetSMSAttributesResponse)

    async def set_subscription_attributes(
        self,
        request: SNSSetSubscriptionAttributesRequest,
    ) -> SNSSetSubscriptionAttributesResponse:
        client = self._require_client()
        return await self._execute(client.set_subscription_attributes, request, SNSSetSubscriptionAttributesResponse)

    async def set_topic_attributes(
        self,
        request: SNSSetTopicAttributesRequest,
    ) -> SNSSetTopicAttributesResponse:
        client = self._require_client()
        return await self._execute(client.set_topic_attributes, request, SNSSetTopicAttributesResponse)

    async def subscribe(
        self,
        request: SNSSubscribeRequest,
    ) -> SNSSubscribeResponse:
        client = self._require_client()
        return await self._execute(client.subscribe, request, SNSSubscribeResponse)

    async def tag_resource(
        self,
        request: SNSTagResourceRequest,
    ) -> SNSTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, SNSTagResourceResponse)

    async def unsubscribe(
        self,
        request: SNSUnsubscribeRequest,
    ) -> SNSUnsubscribeResponse:
        client = self._require_client()
        return await self._execute(client.unsubscribe, request, SNSUnsubscribeResponse)

    async def untag_resource(
        self,
        request: SNSUntagResourceRequest,
    ) -> SNSUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, SNSUntagResourceResponse)

    async def verify_sms_sandbox_phone_number(
        self,
        request: SNSVerifySMSSandboxPhoneNumberRequest,
    ) -> SNSVerifySMSSandboxPhoneNumberResponse:
        client = self._require_client()
        return await self._execute(client.verify_sms_sandbox_phone_number, request, SNSVerifySMSSandboxPhoneNumberResponse)
