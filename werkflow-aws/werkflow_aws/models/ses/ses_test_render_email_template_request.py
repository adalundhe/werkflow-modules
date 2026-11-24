from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESTestRenderEmailTemplateRequest(BaseModel):
    TemplateName: StrictStr
    TemplateData: StrictStr
