from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetSmsTemplateRequest(BaseModel):
    TemplateName: StrictStr
    Version: StrictStr | None = None
