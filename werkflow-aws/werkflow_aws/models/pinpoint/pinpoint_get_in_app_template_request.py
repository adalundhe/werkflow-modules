from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetInAppTemplateRequest(BaseModel):
    TemplateName: StrictStr
    Version: StrictStr | None = None
