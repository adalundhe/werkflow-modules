from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_attributes_resource import PinpointAttributesResource


class PinpointRemoveAttributesResponse(BaseModel):
    AttributesResource: PinpointAttributesResource | None = None
    ResponseMetadata: dict[str, Any] | None = None
