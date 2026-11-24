from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_email_template_request import PinpointEmailTemplateRequest


class PinpointCreateEmailTemplateRequest(BaseModel):
    EmailTemplateRequest: PinpointEmailTemplateRequest
    TemplateName: StrictStr
