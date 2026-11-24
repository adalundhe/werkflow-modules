from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dynamo_db_update_kinesis_streaming_configuration import DynamoDBUpdateKinesisStreamingConfiguration


class DynamoDBUpdateKinesisStreamingDestinationResponse(BaseModel):
    TableName: StrictStr | None = None
    StreamArn: StrictStr | None = None
    DestinationStatus: StrictStr | None = None
    UpdateKinesisStreamingConfiguration: DynamoDBUpdateKinesisStreamingConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
