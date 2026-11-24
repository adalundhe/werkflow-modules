from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .firehose_delivery_stream_description import FirehoseDeliveryStreamDescription


class FirehoseDescribeDeliveryStreamResponse(BaseModel):
    DeliveryStreamDescription: FirehoseDeliveryStreamDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
