from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDescribeTermsByClientRequest(BaseModel):
    ClientId: StrictStr
    UserPoolId: StrictStr
    TermsName: StrictStr
