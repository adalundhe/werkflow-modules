from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESUpdateCustomVerificationEmailTemplateRequest(BaseModel):
    TemplateName: StrictStr
    FromEmailAddress: StrictStr
    TemplateSubject: StrictStr
    TemplateContent: StrictStr
    SuccessRedirectionURL: StrictStr
    FailureRedirectionURL: StrictStr
