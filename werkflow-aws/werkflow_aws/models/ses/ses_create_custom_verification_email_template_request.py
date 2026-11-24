from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_tag import SESTag


class SESCreateCustomVerificationEmailTemplateRequest(BaseModel):
    TemplateName: StrictStr
    FromEmailAddress: StrictStr
    TemplateSubject: StrictStr
    TemplateContent: StrictStr
    SuccessRedirectionURL: StrictStr
    FailureRedirectionURL: StrictStr
    Tags: list[SESTag] | None = None
