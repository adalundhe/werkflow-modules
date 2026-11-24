from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchCognitoOptions(BaseModel):
    Enabled: StrictBool | None = None
    UserPoolId: StrictStr | None = None
    IdentityPoolId: StrictStr | None = None
    RoleArn: StrictStr | None = None
