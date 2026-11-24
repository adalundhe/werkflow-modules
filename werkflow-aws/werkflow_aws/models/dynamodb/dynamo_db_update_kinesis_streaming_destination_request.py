from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_update_kinesis_streaming_configuration import DynamoDBUpdateKinesisStreamingConfiguration


class DynamoDBUpdateKinesisStreamingDestinationRequest(BaseModel):
    TableName: StrictStr
    StreamArn: StrictStr
    UpdateKinesisStreamingConfiguration: DynamoDBUpdateKinesisStreamingConfiguration | None = None
