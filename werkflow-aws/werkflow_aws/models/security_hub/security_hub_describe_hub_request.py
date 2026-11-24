from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubDescribeHubRequest(BaseModel):
    HubArn: StrictStr | None = None
