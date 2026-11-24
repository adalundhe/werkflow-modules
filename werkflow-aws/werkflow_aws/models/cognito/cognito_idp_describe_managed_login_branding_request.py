from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CognitoIDPDescribeManagedLoginBrandingRequest(BaseModel):
    UserPoolId: StrictStr
    ManagedLoginBrandingId: StrictStr
    ReturnMergedResources: StrictBool | None = None
