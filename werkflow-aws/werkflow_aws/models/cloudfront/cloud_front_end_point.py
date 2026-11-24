from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_kinesis_stream_config import CloudFrontKinesisStreamConfig


class CloudFrontEndPoint(BaseModel):
    StreamType: StrictStr | None = None
    KinesisStreamConfig: CloudFrontKinesisStreamConfig | None = None
