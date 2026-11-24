from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class MSKProvisionedThroughput(BaseModel):
    Enabled: StrictBool | None = None
    VolumeThroughput: StrictInt | None = None
