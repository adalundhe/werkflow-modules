from werkflow_aws.models.sqs import (
    SQSChangeMessageVisibilityBatchRequest,
    SQSChangeMessageVisibilityBatchResponse,
    SQSChangeMessageVisibilityRequest,
    SQSChangeMessageVisibilityResponse,
    SQSCreateQueueRequest,
    SQSCreateQueueResponse,
    SQSDeleteMessageBatchRequest,
    SQSDeleteMessageBatchResponse,
    SQSDeleteMessageRequest,
    SQSDeleteMessageResponse,
    SQSDeleteQueueRequest,
    SQSDeleteQueueResponse,
    SQSGetQueueAttributesRequest,
    SQSGetQueueAttributesResponse,
    SQSGetQueueUrlRequest,
    SQSGetQueueUrlResponse,
    SQSListDeadLetterSourceQueuesRequest,
    SQSListDeadLetterSourceQueuesResponse,
    SQSListQueueTagsRequest,
    SQSListQueueTagsResponse,
    SQSListQueuesRequest,
    SQSListQueuesResponse,
    SQSPurgeQueueRequest,
    SQSPurgeQueueResponse,
    SQSReceiveMessageRequest,
    SQSReceiveMessageResponse,
    SQSSendMessageBatchRequest,
    SQSSendMessageBatchResponse,
    SQSSendMessageRequest,
    SQSSendMessageResponse,
    SQSSetQueueAttributesRequest,
    SQSSetQueueAttributesResponse,
    SQSTagQueueRequest,
    SQSTagQueueResponse,
    SQSUntagQueueRequest,
    SQSUntagQueueResponse,
)
from werkflow_aws.services.base import AWSBaseService
from werkflow_aws.types.sqs_client import SQSClient
from werkflow_aws.models.sqs import (
    SQSAddPermissionRequest,
    SQSAddPermissionResponse,
    SQSCancelMessageMoveTaskRequest,
    SQSCancelMessageMoveTaskResponse,
    SQSListMessageMoveTasksRequest,
    SQSListMessageMoveTasksResponse,
    SQSRemovePermissionRequest,
    SQSRemovePermissionResponse,
    SQSStartMessageMoveTaskRequest,
    SQSStartMessageMoveTaskResponse,
)


class AWSSQS(AWSBaseService[SQSClient]):
    service_name = 'SQS'
    boto3_service_name = 'sqs'

    async def list_queues(
        self,
        request: SQSListQueuesRequest | None = None,
    ) -> SQSListQueuesResponse:
        client = self._require_client()
        return await self._execute(
            client.list_queues,
            request,
            SQSListQueuesResponse,
        )

    async def list_queues_paginated(
        self,
        request: SQSListQueuesRequest | None = None,
    ) -> list[SQSListQueuesResponse]:
        self._require_client()
        return await self._paginate(
            'list_queues',
            request,
            SQSListQueuesResponse,
        )

    async def get_queue_url(
        self,
        request: SQSGetQueueUrlRequest,
    ) -> SQSGetQueueUrlResponse:
        client = self._require_client()
        return await self._execute(
            client.get_queue_url,
            request,
            SQSGetQueueUrlResponse,
        )

    async def get_queue_attributes(
        self,
        request: SQSGetQueueAttributesRequest,
    ) -> SQSGetQueueAttributesResponse:
        client = self._require_client()
        return await self._execute(
            client.get_queue_attributes,
            request,
            SQSGetQueueAttributesResponse,
        )

    async def set_queue_attributes(
        self,
        request: SQSSetQueueAttributesRequest,
    ) -> SQSSetQueueAttributesResponse:
        client = self._require_client()
        return await self._execute(
            client.set_queue_attributes,
            request,
            SQSSetQueueAttributesResponse,
        )

    async def create_queue(
        self,
        request: SQSCreateQueueRequest,
    ) -> SQSCreateQueueResponse:
        client = self._require_client()
        return await self._execute(
            client.create_queue,
            request,
            SQSCreateQueueResponse,
        )

    async def delete_queue(
        self,
        request: SQSDeleteQueueRequest,
    ) -> SQSDeleteQueueResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_queue,
            request,
            SQSDeleteQueueResponse,
        )

    async def purge_queue(
        self,
        request: SQSPurgeQueueRequest,
    ) -> SQSPurgeQueueResponse:
        client = self._require_client()
        return await self._execute(
            client.purge_queue,
            request,
            SQSPurgeQueueResponse,
        )

    async def list_dead_letter_source_queues(
        self,
        request: SQSListDeadLetterSourceQueuesRequest,
    ) -> SQSListDeadLetterSourceQueuesResponse:
        client = self._require_client()
        return await self._execute(
            client.list_dead_letter_source_queues,
            request,
            SQSListDeadLetterSourceQueuesResponse,
        )

    async def list_dead_letter_source_queues_paginated(
        self,
        request: SQSListDeadLetterSourceQueuesRequest,
    ) -> list[SQSListDeadLetterSourceQueuesResponse]:
        self._require_client()
        return await self._paginate(
            'list_dead_letter_source_queues',
            request,
            SQSListDeadLetterSourceQueuesResponse,
        )

    async def send_message(
        self,
        request: SQSSendMessageRequest,
    ) -> SQSSendMessageResponse:
        client = self._require_client()
        return await self._execute(
            client.send_message,
            request,
            SQSSendMessageResponse,
        )

    async def send_message_batch(
        self,
        request: SQSSendMessageBatchRequest,
    ) -> SQSSendMessageBatchResponse:
        client = self._require_client()
        return await self._execute(
            client.send_message_batch,
            request,
            SQSSendMessageBatchResponse,
        )

    async def receive_message(
        self,
        request: SQSReceiveMessageRequest,
    ) -> SQSReceiveMessageResponse:
        client = self._require_client()
        return await self._execute(
            client.receive_message,
            request,
            SQSReceiveMessageResponse,
        )

    async def delete_message(
        self,
        request: SQSDeleteMessageRequest,
    ) -> SQSDeleteMessageResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_message,
            request,
            SQSDeleteMessageResponse,
        )

    async def delete_message_batch(
        self,
        request: SQSDeleteMessageBatchRequest,
    ) -> SQSDeleteMessageBatchResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_message_batch,
            request,
            SQSDeleteMessageBatchResponse,
        )

    async def change_message_visibility(
        self,
        request: SQSChangeMessageVisibilityRequest,
    ) -> SQSChangeMessageVisibilityResponse:
        client = self._require_client()
        return await self._execute(
            client.change_message_visibility,
            request,
            SQSChangeMessageVisibilityResponse,
        )

    async def change_message_visibility_batch(
        self,
        request: SQSChangeMessageVisibilityBatchRequest,
    ) -> SQSChangeMessageVisibilityBatchResponse:
        client = self._require_client()
        return await self._execute(
            client.change_message_visibility_batch,
            request,
            SQSChangeMessageVisibilityBatchResponse,
        )

    async def list_queue_tags(
        self,
        request: SQSListQueueTagsRequest,
    ) -> SQSListQueueTagsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_queue_tags,
            request,
            SQSListQueueTagsResponse,
        )

    async def tag_queue(
        self,
        request: SQSTagQueueRequest,
    ) -> SQSTagQueueResponse:
        client = self._require_client()
        return await self._execute(
            client.tag_queue,
            request,
            SQSTagQueueResponse,
        )

    async def untag_queue(
        self,
        request: SQSUntagQueueRequest,
    ) -> SQSUntagQueueResponse:
        client = self._require_client()
        return await self._execute(
            client.untag_queue,
            request,
            SQSUntagQueueResponse,
        )

    async def add_permission(
        self,
        request: SQSAddPermissionRequest,
    ) -> SQSAddPermissionResponse:
        client = self._require_client()
        return await self._execute(client.add_permission, request, SQSAddPermissionResponse)

    async def cancel_message_move_task(
        self,
        request: SQSCancelMessageMoveTaskRequest,
    ) -> SQSCancelMessageMoveTaskResponse:
        client = self._require_client()
        return await self._execute(client.cancel_message_move_task, request, SQSCancelMessageMoveTaskResponse)

    async def list_message_move_tasks(
        self,
        request: SQSListMessageMoveTasksRequest,
    ) -> SQSListMessageMoveTasksResponse:
        client = self._require_client()
        return await self._execute(client.list_message_move_tasks, request, SQSListMessageMoveTasksResponse)

    async def remove_permission(
        self,
        request: SQSRemovePermissionRequest,
    ) -> SQSRemovePermissionResponse:
        client = self._require_client()
        return await self._execute(client.remove_permission, request, SQSRemovePermissionResponse)

    async def start_message_move_task(
        self,
        request: SQSStartMessageMoveTaskRequest,
    ) -> SQSStartMessageMoveTaskResponse:
        client = self._require_client()
        return await self._execute(client.start_message_move_task, request, SQSStartMessageMoveTaskResponse)

