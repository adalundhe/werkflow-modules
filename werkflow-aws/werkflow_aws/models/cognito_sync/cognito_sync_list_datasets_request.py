from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoSyncListDatasetsRequest(BaseModel):
    IdentityPoolId: StrictStr
    IdentityId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
