from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaProvisionedPollerConfigModel(BaseModel):
    MinimumPollers: StrictInt | None = None
    MaximumPollers: StrictInt | None = None
    PollerGroupName: StrictStr | None = None
