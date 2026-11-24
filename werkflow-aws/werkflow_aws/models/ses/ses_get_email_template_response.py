from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_email_template_content import SESEmailTemplateContent
from .ses_tag import SESTag


class SESGetEmailTemplateResponse(BaseModel):
    TemplateName: StrictStr | None = None
    TemplateContent: SESEmailTemplateContent | None = None
    Tags: list[SESTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
