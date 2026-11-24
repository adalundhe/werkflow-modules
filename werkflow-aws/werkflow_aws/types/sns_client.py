from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class SNSClient(ABC):

    @abstractmethod
    def add_permission(
        self,
        *,
        TopicArn: str,
        Label: str,
        AWSAccountId: list[str],
        ActionName: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def check_if_phone_number_is_opted_out(
        self,
        *,
        phoneNumber: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def confirm_subscription(
        self,
        *,
        TopicArn: str,
        Token: str,
        AuthenticateOnUnsubscribe: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_platform_application(
        self,
        *,
        Name: str,
        Platform: str,
        Attributes: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_platform_endpoint(
        self,
        *,
        PlatformApplicationArn: str,
        Token: str,
        CustomUserData: str | None = None,
        Attributes: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_sms_sandbox_phone_number(
        self,
        *,
        PhoneNumber: str,
        LanguageCode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_topic(
        self,
        *,
        Name: str,
        Attributes: dict[str, str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        DataProtectionPolicy: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_endpoint(
        self,
        *,
        EndpointArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_platform_application(
        self,
        *,
        PlatformApplicationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_sms_sandbox_phone_number(
        self,
        *,
        PhoneNumber: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_topic(
        self,
        *,
        TopicArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_data_protection_policy(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_endpoint_attributes(
        self,
        *,
        EndpointArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_platform_application_attributes(
        self,
        *,
        PlatformApplicationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_sms_attributes(
        self,
        *,
        attributes: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_sms_sandbox_account_status(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_subscription_attributes(
        self,
        *,
        SubscriptionArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_topic_attributes(
        self,
        *,
        TopicArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_endpoints_by_platform_application(
        self,
        *,
        PlatformApplicationArn: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_origination_numbers(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_phone_numbers_opted_out(
        self,
        *,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_platform_applications(
        self,
        *,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_sms_sandbox_phone_numbers(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_subscriptions(
        self,
        *,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_subscriptions_by_topic(
        self,
        *,
        TopicArn: str,
        NextToken: str | None = None,
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
    def list_topics(
        self,
        *,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def opt_in_phone_number(
        self,
        *,
        phoneNumber: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def publish(
        self,
        *,
        Message: str,
        TopicArn: str | None = None,
        TargetArn: str | None = None,
        PhoneNumber: str | None = None,
        Subject: str | None = None,
        MessageStructure: str | None = None,
        MessageAttributes: dict[str, dict[str, Any]] | None = None,
        MessageDeduplicationId: str | None = None,
        MessageGroupId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def publish_batch(
        self,
        *,
        TopicArn: str,
        PublishBatchRequestEntries: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_data_protection_policy(
        self,
        *,
        ResourceArn: str,
        DataProtectionPolicy: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_permission(
        self,
        *,
        TopicArn: str,
        Label: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_endpoint_attributes(
        self,
        *,
        EndpointArn: str,
        Attributes: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_platform_application_attributes(
        self,
        *,
        PlatformApplicationArn: str,
        Attributes: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_sms_attributes(
        self,
        *,
        attributes: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_subscription_attributes(
        self,
        *,
        SubscriptionArn: str,
        AttributeName: str,
        AttributeValue: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_topic_attributes(
        self,
        *,
        TopicArn: str,
        AttributeName: str,
        AttributeValue: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def subscribe(
        self,
        *,
        TopicArn: str,
        Protocol: str,
        Endpoint: str | None = None,
        Attributes: dict[str, str] | None = None,
        ReturnSubscriptionArn: bool | None = None,
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
    def unsubscribe(
        self,
        *,
        SubscriptionArn: str,
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
    def verify_sms_sandbox_phone_number(
        self,
        *,
        PhoneNumber: str,
        OneTimePassword: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
