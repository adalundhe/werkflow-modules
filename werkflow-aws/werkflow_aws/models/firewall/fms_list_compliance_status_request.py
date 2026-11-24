from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FMSListComplianceStatusRequest(BaseModel):
    PolicyId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
