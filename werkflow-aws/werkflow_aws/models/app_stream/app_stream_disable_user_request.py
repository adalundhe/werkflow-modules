from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AppStreamDisableUserRequest(BaseModel):
    UserName: StrictStr
    AuthenticationType: Literal['API', 'SAML', 'USERPOOL', 'AWS_AD']
