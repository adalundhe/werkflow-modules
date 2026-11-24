from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_email_template_response import PinpointEmailTemplateResponse


class PinpointGetEmailTemplateResponse(BaseModel):
    EmailTemplateResponse: PinpointEmailTemplateResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
