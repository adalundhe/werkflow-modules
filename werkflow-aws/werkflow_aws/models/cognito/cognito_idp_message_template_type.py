from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPMessageTemplateType(BaseModel):
    SMSMessage: StrictStr | None = None
    EmailMessage: StrictStr | None = None
    EmailSubject: StrictStr | None = None
