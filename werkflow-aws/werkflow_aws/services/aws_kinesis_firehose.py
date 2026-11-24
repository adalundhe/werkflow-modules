from werkflow_aws.models.kinesis_firehose import (
    FirehoseCreateDeliveryStreamRequest,
    FirehoseCreateDeliveryStreamResponse,
    FirehoseDeleteDeliveryStreamRequest,
    FirehoseDeleteDeliveryStreamResponse,
    FirehoseDescribeDeliveryStreamRequest,
    FirehoseDescribeDeliveryStreamResponse,
    FirehoseListDeliveryStreamsRequest,
    FirehoseListDeliveryStreamsResponse,
    FirehoseListTagsForDeliveryStreamRequest,
    FirehoseListTagsForDeliveryStreamResponse,
    FirehosePutRecordBatchRequest,
    FirehosePutRecordBatchResponse,
    FirehosePutRecordRequest,
    FirehosePutRecordResponse,
    FirehoseStartDeliveryStreamEncryptionRequest,
    FirehoseStartDeliveryStreamEncryptionResponse,
    FirehoseStopDeliveryStreamEncryptionRequest,
    FirehoseStopDeliveryStreamEncryptionResponse,
    FirehoseTagDeliveryStreamRequest,
    FirehoseTagDeliveryStreamResponse,
    FirehoseUntagDeliveryStreamRequest,
    FirehoseUntagDeliveryStreamResponse,
    FirehoseUpdateDestinationRequest,
    FirehoseUpdateDestinationResponse,
)
from werkflow_aws.types.kinesis_firehose_client import FirehoseClient
from .base import AWSBaseService


class AWSFirehose(AWSBaseService[FirehoseClient]):
    service_name = 'kinesis-firehose'
    boto3_service_name = 'firehose'

    def __init__(self) -> None:
        super().__init__(service_name='kinesis-firehose', boto3_service_name='firehose')

    async def create_delivery_stream(
        self,
        request: FirehoseCreateDeliveryStreamRequest,
    ) -> FirehoseCreateDeliveryStreamResponse:
        client = self._require_client()
        return await self._execute(client.create_delivery_stream, request, FirehoseCreateDeliveryStreamResponse)

    async def delete_delivery_stream(
        self,
        request: FirehoseDeleteDeliveryStreamRequest,
    ) -> FirehoseDeleteDeliveryStreamResponse:
        client = self._require_client()
        return await self._execute(client.delete_delivery_stream, request, FirehoseDeleteDeliveryStreamResponse)

    async def describe_delivery_stream(
        self,
        request: FirehoseDescribeDeliveryStreamRequest,
    ) -> FirehoseDescribeDeliveryStreamResponse:
        client = self._require_client()
        return await self._execute(client.describe_delivery_stream, request, FirehoseDescribeDeliveryStreamResponse)

    async def list_delivery_streams(
        self,
        request: FirehoseListDeliveryStreamsRequest | None = None,
    ) -> FirehoseListDeliveryStreamsResponse:
        client = self._require_client()
        return await self._execute(client.list_delivery_streams, request, FirehoseListDeliveryStreamsResponse)

    async def list_tags_for_delivery_stream(
        self,
        request: FirehoseListTagsForDeliveryStreamRequest,
    ) -> FirehoseListTagsForDeliveryStreamResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_delivery_stream, request, FirehoseListTagsForDeliveryStreamResponse)

    async def put_record(
        self,
        request: FirehosePutRecordRequest,
    ) -> FirehosePutRecordResponse:
        client = self._require_client()
        return await self._execute(client.put_record, request, FirehosePutRecordResponse)

    async def put_record_batch(
        self,
        request: FirehosePutRecordBatchRequest,
    ) -> FirehosePutRecordBatchResponse:
        client = self._require_client()
        return await self._execute(client.put_record_batch, request, FirehosePutRecordBatchResponse)

    async def start_delivery_stream_encryption(
        self,
        request: FirehoseStartDeliveryStreamEncryptionRequest,
    ) -> FirehoseStartDeliveryStreamEncryptionResponse:
        client = self._require_client()
        return await self._execute(client.start_delivery_stream_encryption, request, FirehoseStartDeliveryStreamEncryptionResponse)

    async def stop_delivery_stream_encryption(
        self,
        request: FirehoseStopDeliveryStreamEncryptionRequest,
    ) -> FirehoseStopDeliveryStreamEncryptionResponse:
        client = self._require_client()
        return await self._execute(client.stop_delivery_stream_encryption, request, FirehoseStopDeliveryStreamEncryptionResponse)

    async def tag_delivery_stream(
        self,
        request: FirehoseTagDeliveryStreamRequest,
    ) -> FirehoseTagDeliveryStreamResponse:
        client = self._require_client()
        return await self._execute(client.tag_delivery_stream, request, FirehoseTagDeliveryStreamResponse)

    async def untag_delivery_stream(
        self,
        request: FirehoseUntagDeliveryStreamRequest,
    ) -> FirehoseUntagDeliveryStreamResponse:
        client = self._require_client()
        return await self._execute(client.untag_delivery_stream, request, FirehoseUntagDeliveryStreamResponse)

    async def update_destination(
        self,
        request: FirehoseUpdateDestinationRequest,
    ) -> FirehoseUpdateDestinationResponse:
        client = self._require_client()
        return await self._execute(client.update_destination, request, FirehoseUpdateDestinationResponse)
