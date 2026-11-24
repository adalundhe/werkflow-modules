from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dynamo_db_enable_kinesis_streaming_configuration import DynamoDBEnableKinesisStreamingConfiguration


class DynamoDBDisableKinesisStreamingDestinationResponse(BaseModel):
    TableName: StrictStr | None = None
    StreamArn: StrictStr | None = None
    DestinationStatus: StrictStr | None = None
    EnableKinesisStreamingConfiguration: DynamoDBEnableKinesisStreamingConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
