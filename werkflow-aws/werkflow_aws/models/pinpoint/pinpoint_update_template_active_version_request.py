from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_template_active_version_request import PinpointTemplateActiveVersionRequest


class PinpointUpdateTemplateActiveVersionRequest(BaseModel):
    TemplateActiveVersionRequest: PinpointTemplateActiveVersionRequest
    TemplateName: StrictStr
    TemplateType: StrictStr
