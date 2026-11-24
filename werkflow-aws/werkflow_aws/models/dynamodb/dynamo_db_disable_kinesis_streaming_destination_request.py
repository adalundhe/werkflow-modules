from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_enable_kinesis_streaming_configuration import DynamoDBEnableKinesisStreamingConfiguration


class DynamoDBDisableKinesisStreamingDestinationRequest(BaseModel):
    TableName: StrictStr
    StreamArn: StrictStr
    EnableKinesisStreamingConfiguration: DynamoDBEnableKinesisStreamingConfiguration | None = None
