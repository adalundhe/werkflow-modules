from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AppStreamCreateUserRequest(BaseModel):
    UserName: StrictStr
    AuthenticationType: Literal['API', 'SAML', 'USERPOOL', 'AWS_AD']
    MessageAction: Literal['SUPPRESS', 'RESEND'] | None = None
    FirstName: StrictStr | None = None
    LastName: StrictStr | None = None
