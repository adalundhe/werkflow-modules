from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_endpoint_batch_request import PinpointEndpointBatchRequest


class PinpointUpdateEndpointsBatchRequest(BaseModel):
    ApplicationId: StrictStr
    EndpointBatchRequest: PinpointEndpointBatchRequest
