from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESGetEmailTemplateRequest(BaseModel):
    TemplateName: StrictStr
