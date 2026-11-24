from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CognitoIDPUpdateTermsRequest(BaseModel):
    TermsId: StrictStr
    UserPoolId: StrictStr
    TermsName: StrictStr | None = None
    TermsSource: Literal['LINK'] | None = None
    Enforcement: Literal['NONE'] | None = None
    Links: dict[StrictStr, StrictStr] | None = None
