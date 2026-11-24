from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPInboundFederationLambdaType(BaseModel):
    LambdaVersion: StrictStr | None = None
    LambdaArn: StrictStr | None = None
