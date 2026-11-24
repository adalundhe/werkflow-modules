from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetCloudFormationStackRecordsRequest(BaseModel):
    pageToken: StrictStr | None = None
