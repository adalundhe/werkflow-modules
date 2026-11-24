from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSListPlatformApplicationsRequest(BaseModel):
    NextToken: StrictStr | None = None
