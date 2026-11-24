from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .firehose_http_endpoint_common_attribute import FirehoseHttpEndpointCommonAttribute


class FirehoseHttpEndpointRequestConfiguration(BaseModel):
    ContentEncoding: StrictStr | None = None
    CommonAttributes: list[FirehoseHttpEndpointCommonAttribute] | None = None
