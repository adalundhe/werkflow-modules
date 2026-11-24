from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESGetCustomVerificationEmailTemplateRequest(BaseModel):
    TemplateName: StrictStr
