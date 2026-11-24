from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPListUserPoolClientsRequest(BaseModel):
    UserPoolId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    ClientType: Literal['REGULAR', 'DCR'] | None = None
