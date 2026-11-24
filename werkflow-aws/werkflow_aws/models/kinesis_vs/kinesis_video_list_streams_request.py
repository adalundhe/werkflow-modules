from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_video_stream_name_condition import KinesisVideoStreamNameCondition


class KinesisVideoListStreamsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    StreamNameCondition: KinesisVideoStreamNameCondition | None = None
