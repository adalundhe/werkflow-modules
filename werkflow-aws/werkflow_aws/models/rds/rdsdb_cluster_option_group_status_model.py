from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDBClusterOptionGroupStatusModel(BaseModel):
    DBClusterOptionGroupName: StrictStr | None = None
    Status: StrictStr | None = None
