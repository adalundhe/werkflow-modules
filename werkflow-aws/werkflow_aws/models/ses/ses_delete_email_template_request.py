from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESDeleteEmailTemplateRequest(BaseModel):
    TemplateName: StrictStr
