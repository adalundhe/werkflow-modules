from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_custom_verification_email_template_metadata import SESCustomVerificationEmailTemplateMetadata


class SESListCustomVerificationEmailTemplatesResponse(BaseModel):
    CustomVerificationEmailTemplates: list[SESCustomVerificationEmailTemplateMetadata] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
