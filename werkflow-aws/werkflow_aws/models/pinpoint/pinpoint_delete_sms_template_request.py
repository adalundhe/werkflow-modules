from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointDeleteSmsTemplateRequest(BaseModel):
    TemplateName: StrictStr
    Version: StrictStr | None = None
