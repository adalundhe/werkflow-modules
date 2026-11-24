from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CognitoIDPCreateTermsRequest(BaseModel):
    UserPoolId: StrictStr
    ClientId: StrictStr
    TermsName: StrictStr
    TermsSource: Literal['LINK']
    Enforcement: Literal['NONE']
    Links: dict[StrictStr, StrictStr] | None = None
