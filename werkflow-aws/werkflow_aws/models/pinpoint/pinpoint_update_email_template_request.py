from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .pinpoint_email_template_request import PinpointEmailTemplateRequest


class PinpointUpdateEmailTemplateRequest(BaseModel):
    EmailTemplateRequest: PinpointEmailTemplateRequest
    TemplateName: StrictStr
    CreateNewVersion: StrictBool | None = None
    Version: StrictStr | None = None
