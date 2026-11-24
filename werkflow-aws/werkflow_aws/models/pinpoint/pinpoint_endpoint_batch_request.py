from __future__ import annotations
from pydantic import BaseModel
from .pinpoint_endpoint_batch_item import PinpointEndpointBatchItem


class PinpointEndpointBatchRequest(BaseModel):
    Item: list[PinpointEndpointBatchItem]
