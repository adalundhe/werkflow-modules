from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_endpoint_message_result import PinpointEndpointMessageResult


class PinpointSendUsersMessageResponse(BaseModel):
    ApplicationId: StrictStr | None = None
    RequestId: StrictStr | None = None
    Result: dict[StrictStr, dict[StrictStr, PinpointEndpointMessageResult]] | None = None
