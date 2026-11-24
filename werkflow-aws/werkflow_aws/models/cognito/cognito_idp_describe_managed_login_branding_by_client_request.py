from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CognitoIDPDescribeManagedLoginBrandingByClientRequest(BaseModel):
    UserPoolId: StrictStr
    ClientId: StrictStr
    ReturnMergedResources: StrictBool | None = None
