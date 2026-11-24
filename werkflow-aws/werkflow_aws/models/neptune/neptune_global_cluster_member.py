from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class NeptuneGlobalClusterMember(BaseModel):
    DBClusterArn: StrictStr | None = None
    Readers: list[StrictStr] | None = None
    IsWriter: StrictBool | None = None
