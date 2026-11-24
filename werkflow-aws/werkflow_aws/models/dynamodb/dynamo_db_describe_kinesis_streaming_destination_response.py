from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dynamo_db_kinesis_data_stream_destination import DynamoDBKinesisDataStreamDestination


class DynamoDBDescribeKinesisStreamingDestinationResponse(BaseModel):
    TableName: StrictStr | None = None
    KinesisDataStreamDestinations: list[DynamoDBKinesisDataStreamDestination] | None = None
    ResponseMetadata: dict[str, Any] | None = None
