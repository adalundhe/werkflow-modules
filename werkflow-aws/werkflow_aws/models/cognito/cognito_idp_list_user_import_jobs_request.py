from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPListUserImportJobsRequest(BaseModel):
    UserPoolId: StrictStr
    MaxResults: StrictInt
    PaginationToken: StrictStr | None = None
