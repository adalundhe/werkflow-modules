from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubPhysicalResourceId(BaseModel):
    awsAccountId: StrictStr | None = None
    awsRegion: StrictStr | None = None
    identifier: StrictStr | None = None
    type: StrictStr | None = None
