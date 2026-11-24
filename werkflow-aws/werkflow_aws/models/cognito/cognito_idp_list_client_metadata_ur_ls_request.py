from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPListClientMetadataURLsRequest(BaseModel):
    UserPoolId: StrictStr
    CIMDPolicyId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
