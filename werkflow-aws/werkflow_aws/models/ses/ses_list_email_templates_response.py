from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_email_template_metadata import SESEmailTemplateMetadata


class SESListEmailTemplatesResponse(BaseModel):
    TemplatesMetadata: list[SESEmailTemplateMetadata] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
