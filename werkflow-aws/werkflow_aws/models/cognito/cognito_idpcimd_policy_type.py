from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPCIMDPolicyType(BaseModel):
    UserPoolId: StrictStr | None = None
    CIMDPolicyId: StrictStr | None = None
    ClientId: StrictStr | None = None
    PolicyName: StrictStr | None = None
    CacheDuration: StrictInt | None = None
    URLPatterns: list[StrictStr] | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    LastModifiedDate: datetime.datetime | StrictStr | None = None
