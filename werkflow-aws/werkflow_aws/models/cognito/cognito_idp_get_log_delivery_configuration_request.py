from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPGetLogDeliveryConfigurationRequest(BaseModel):
    UserPoolId: StrictStr
