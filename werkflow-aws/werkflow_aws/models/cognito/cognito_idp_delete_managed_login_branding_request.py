from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPDeleteManagedLoginBrandingRequest(BaseModel):
    ManagedLoginBrandingId: StrictStr
    UserPoolId: StrictStr
