from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_tag import SESTag


class SESGetCustomVerificationEmailTemplateResponse(BaseModel):
    TemplateName: StrictStr | None = None
    FromEmailAddress: StrictStr | None = None
    TemplateSubject: StrictStr | None = None
    TemplateContent: StrictStr | None = None
    Tags: list[SESTag] | None = None
    SuccessRedirectionURL: StrictStr | None = None
    FailureRedirectionURL: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
