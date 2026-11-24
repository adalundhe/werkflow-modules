from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2CognitoConfig(BaseModel):
    AppClientId: StrictStr | None = None
    UserPoolArn: StrictStr | None = None
    UserPoolDomain: StrictStr | None = None
