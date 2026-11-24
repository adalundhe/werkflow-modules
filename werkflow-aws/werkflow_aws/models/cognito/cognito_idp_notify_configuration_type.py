from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_notify_email_type import CognitoIDPNotifyEmailType


class CognitoIDPNotifyConfigurationType(BaseModel):
    From: StrictStr | None = None
    ReplyTo: StrictStr | None = None
    SourceArn: StrictStr | None = None
    BlockEmail: CognitoIDPNotifyEmailType | None = None
    NoActionEmail: CognitoIDPNotifyEmailType | None = None
    MfaEmail: CognitoIDPNotifyEmailType | None = None
