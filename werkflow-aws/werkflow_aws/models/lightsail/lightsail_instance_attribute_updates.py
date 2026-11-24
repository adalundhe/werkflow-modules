from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailInstanceAttributeUpdates(BaseModel):
    bundleId: StrictStr | None = None
