from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubStatelessCustomPublishMetricActionDimension(BaseModel):
    Value: StrictStr | None = None
