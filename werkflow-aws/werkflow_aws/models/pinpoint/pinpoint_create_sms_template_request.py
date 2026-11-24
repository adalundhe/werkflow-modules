from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_sms_template_request import PinpointSMSTemplateRequest


class PinpointCreateSmsTemplateRequest(BaseModel):
    SMSTemplateRequest: PinpointSMSTemplateRequest
    TemplateName: StrictStr
