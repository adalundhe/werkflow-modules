from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDBClusterOptionGroupStatus(BaseModel):
    DBClusterOptionGroupName: StrictStr | None = None
    Status: StrictStr | None = None
