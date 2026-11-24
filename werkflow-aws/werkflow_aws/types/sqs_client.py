from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class SQSClient(ABC):

    @abstractmethod
    def list_queues(
        self,
        *,
        QueueNamePrefix: str | None = None,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_queue_url(
        self,
        *,
        QueueName: str,
        QueueOwnerAWSAccountId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_queue_attributes(
        self,
        *,
        QueueUrl: str,
        AttributeNames: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_queue_attributes(
        self,
        *,
        QueueUrl: str,
        Attributes: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_queue(
        self,
        *,
        QueueName: str,
        Attributes: dict[str, str] | None = None,
        tags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_queue(
        self,
        *,
        QueueUrl: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def purge_queue(
        self,
        *,
        QueueUrl: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_dead_letter_source_queues(
        self,
        *,
        QueueUrl: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_message(
        self,
        *,
        QueueUrl: str,
        MessageBody: str,
        DelaySeconds: int | None = None,
        MessageAttributes: dict[str, dict[str, Any]] | None = None,
        MessageSystemAttributes: dict[str, dict[str, Any]] | None = None,
        MessageDeduplicationId: str | None = None,
        MessageGroupId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_message_batch(
        self,
        *,
        QueueUrl: str,
        Entries: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def receive_message(
        self,
        *,
        QueueUrl: str,
        AttributeNames: list[str] | None = None,
        MessageSystemAttributeNames: list[str] | None = None,
        MessageAttributeNames: list[str] | None = None,
        MaxNumberOfMessages: int | None = None,
        VisibilityTimeout: int | None = None,
        WaitTimeSeconds: int | None = None,
        ReceiveRequestAttemptId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_message(
        self,
        *,
        QueueUrl: str,
        ReceiptHandle: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_message_batch(
        self,
        *,
        QueueUrl: str,
        Entries: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def change_message_visibility(
        self,
        *,
        QueueUrl: str,
        ReceiptHandle: str,
        VisibilityTimeout: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def change_message_visibility_batch(
        self,
        *,
        QueueUrl: str,
        Entries: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_queue_tags(
        self,
        *,
        QueueUrl: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_queue(
        self,
        *,
        QueueUrl: str,
        Tags: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_queue(
        self,
        *,
        QueueUrl: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_permission(
        self,
        *,
        QueueUrl: str,
        Label: str,
        AWSAccountIds: list[str],
        Actions: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_message_move_task(
        self,
        *,
        TaskHandle: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_message_move_tasks(
        self,
        *,
        SourceArn: str,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_permission(
        self,
        *,
        QueueUrl: str,
        Label: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_message_move_task(
        self,
        *,
        SourceArn: str,
        DestinationArn: str | None = None,
        MaxNumberOfMessagesPerSecond: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
