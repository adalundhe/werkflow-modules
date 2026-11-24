from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .pinpoint_in_app_template_request import PinpointInAppTemplateRequest


class PinpointUpdateInAppTemplateRequest(BaseModel):
    InAppTemplateRequest: PinpointInAppTemplateRequest
    TemplateName: StrictStr
    CreateNewVersion: StrictBool | None = None
    Version: StrictStr | None = None
