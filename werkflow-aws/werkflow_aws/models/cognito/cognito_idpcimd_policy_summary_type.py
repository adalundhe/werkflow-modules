from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPCIMDPolicySummaryType(BaseModel):
    CIMDPolicyId: StrictStr | None = None
    ClientId: StrictStr | None = None
    PolicyName: StrictStr | None = None
    CacheDuration: StrictInt | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    LastModifiedDate: datetime.datetime | StrictStr | None = None
