from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointDeleteEmailTemplateRequest(BaseModel):
    TemplateName: StrictStr
    Version: StrictStr | None = None
