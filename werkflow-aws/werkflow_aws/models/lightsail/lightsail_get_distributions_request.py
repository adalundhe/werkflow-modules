from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetDistributionsRequest(BaseModel):
    distributionName: StrictStr | None = None
    pageToken: StrictStr | None = None
