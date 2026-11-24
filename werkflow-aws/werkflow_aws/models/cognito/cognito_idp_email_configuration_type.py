from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPEmailConfigurationType(BaseModel):
    SourceArn: StrictStr | None = None
    ReplyToEmailAddress: StrictStr | None = None
    EmailSendingAccount: StrictStr | None = None
    From: StrictStr | None = None
    ConfigurationSet: StrictStr | None = None
