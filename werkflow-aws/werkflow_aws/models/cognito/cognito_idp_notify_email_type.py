from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPNotifyEmailType(BaseModel):
    Subject: StrictStr | None = None
    HtmlBody: StrictStr | None = None
    TextBody: StrictStr | None = None
