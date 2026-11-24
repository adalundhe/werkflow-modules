from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LakeFormationWorkUnitRange(BaseModel):
    WorkUnitIdMax: StrictInt | None = None
    WorkUnitIdMin: StrictInt | None = None
    WorkUnitToken: StrictStr | None = None
