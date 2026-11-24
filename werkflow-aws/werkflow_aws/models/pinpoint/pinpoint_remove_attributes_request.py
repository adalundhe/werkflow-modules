from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_update_attributes_request import PinpointUpdateAttributesRequest


class PinpointRemoveAttributesRequest(BaseModel):
    ApplicationId: StrictStr
    AttributeType: StrictStr
    UpdateAttributesRequest: PinpointUpdateAttributesRequest
