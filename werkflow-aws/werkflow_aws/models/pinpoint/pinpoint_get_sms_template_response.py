from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_sms_template_response import PinpointSMSTemplateResponse


class PinpointGetSmsTemplateResponse(BaseModel):
    SMSTemplateResponse: PinpointSMSTemplateResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
