from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_in_app_template_request import PinpointInAppTemplateRequest


class PinpointCreateInAppTemplateRequest(BaseModel):
    InAppTemplateRequest: PinpointInAppTemplateRequest
    TemplateName: StrictStr
