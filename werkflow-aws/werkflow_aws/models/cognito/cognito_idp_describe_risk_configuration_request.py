from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDescribeRiskConfigurationRequest(BaseModel):
    UserPoolId: StrictStr
    ClientId: StrictStr | None = None
