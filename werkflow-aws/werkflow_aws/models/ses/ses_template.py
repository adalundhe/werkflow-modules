from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_attachment import SESAttachment
from .ses_email_template_content import SESEmailTemplateContent
from .ses_message_header import SESMessageHeader


class SESTemplate(BaseModel):
    TemplateName: StrictStr | None = None
    TemplateArn: StrictStr | None = None
    TemplateContent: SESEmailTemplateContent | None = None
    TemplateData: StrictStr | None = None
    Headers: list[SESMessageHeader] | None = None
    Attachments: list[SESAttachment] | None = None
