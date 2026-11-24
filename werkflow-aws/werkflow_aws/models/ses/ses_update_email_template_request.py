from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_email_template_content import SESEmailTemplateContent


class SESUpdateEmailTemplateRequest(BaseModel):
    TemplateName: StrictStr
    TemplateContent: SESEmailTemplateContent
