from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_in_app_template_response import PinpointInAppTemplateResponse


class PinpointGetInAppTemplateResponse(BaseModel):
    InAppTemplateResponse: PinpointInAppTemplateResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
