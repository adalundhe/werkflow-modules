from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_endpoint_message_result import PinpointEndpointMessageResult
from .pinpoint_message_result import PinpointMessageResult


class PinpointMessageResponse(BaseModel):
    ApplicationId: StrictStr | None = None
    EndpointResult: dict[StrictStr, PinpointEndpointMessageResult] | None = None
    RequestId: StrictStr | None = None
    Result: dict[StrictStr, PinpointMessageResult] | None = None
