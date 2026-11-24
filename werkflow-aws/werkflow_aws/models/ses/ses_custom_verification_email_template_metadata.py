from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESCustomVerificationEmailTemplateMetadata(BaseModel):
    TemplateName: StrictStr | None = None
    FromEmailAddress: StrictStr | None = None
    TemplateSubject: StrictStr | None = None
    SuccessRedirectionURL: StrictStr | None = None
    FailureRedirectionURL: StrictStr | None = None
