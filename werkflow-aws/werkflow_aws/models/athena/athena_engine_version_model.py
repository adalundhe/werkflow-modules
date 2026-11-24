from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaEngineVersionModel(BaseModel):
    SelectedEngineVersion: StrictStr | None = None
    EffectiveEngineVersion: StrictStr | None = None
