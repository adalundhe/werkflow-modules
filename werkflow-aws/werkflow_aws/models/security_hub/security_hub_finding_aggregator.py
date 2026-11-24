from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubFindingAggregator(BaseModel):
    FindingAggregatorArn: StrictStr | None = None
