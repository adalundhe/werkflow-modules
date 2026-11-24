from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ProjectFeatureState(BaseModel):
    state: StrictStr | None = None
