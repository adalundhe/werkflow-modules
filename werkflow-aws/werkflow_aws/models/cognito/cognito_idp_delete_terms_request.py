from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDeleteTermsRequest(BaseModel):
    TermsId: StrictStr
    UserPoolId: StrictStr
