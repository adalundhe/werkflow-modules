from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneDBClusterOptionGroupStatus(BaseModel):
    DBClusterOptionGroupName: StrictStr | None = None
    Status: StrictStr | None = None
