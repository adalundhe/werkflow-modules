from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_template_create_message_body import PinpointTemplateCreateMessageBody


class PinpointCreateInAppTemplateResponse(BaseModel):
    TemplateCreateMessageBody: PinpointTemplateCreateMessageBody | None = None
    ResponseMetadata: dict[str, Any] | None = None
