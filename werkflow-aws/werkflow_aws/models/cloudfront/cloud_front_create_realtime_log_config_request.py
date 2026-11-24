from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_end_point import CloudFrontEndPoint


class CloudFrontCreateRealtimeLogConfigRequest(BaseModel):
    EndPoints: list[CloudFrontEndPoint]
    Fields: list[StrictStr]
    Name: StrictStr
    SamplingRate: StrictInt
