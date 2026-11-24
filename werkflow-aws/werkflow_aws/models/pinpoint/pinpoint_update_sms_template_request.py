from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .pinpoint_sms_template_request import PinpointSMSTemplateRequest


class PinpointUpdateSmsTemplateRequest(BaseModel):
    SMSTemplateRequest: PinpointSMSTemplateRequest
    TemplateName: StrictStr
    CreateNewVersion: StrictBool | None = None
    Version: StrictStr | None = None
