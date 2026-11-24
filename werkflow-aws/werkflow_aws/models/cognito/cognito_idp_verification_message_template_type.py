from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPVerificationMessageTemplateType(BaseModel):
    SmsMessage: StrictStr | None = None
    EmailMessage: StrictStr | None = None
    EmailSubject: StrictStr | None = None
    EmailMessageByLink: StrictStr | None = None
    EmailSubjectByLink: StrictStr | None = None
    DefaultEmailOption: StrictStr | None = None
