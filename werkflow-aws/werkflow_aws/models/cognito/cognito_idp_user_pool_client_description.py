from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPUserPoolClientDescription(BaseModel):
    ClientId: StrictStr | None = None
    UserPoolId: StrictStr | None = None
    ClientName: StrictStr | None = None
