from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPListUsersRequest(BaseModel):
    UserPoolId: StrictStr
    AttributesToGet: list[StrictStr] | None = None
    Limit: StrictInt | None = None
    PaginationToken: StrictStr | None = None
    Filter: StrictStr | None = None
