from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDescribeTermsRequest(BaseModel):
    TermsId: StrictStr
    UserPoolId: StrictStr
