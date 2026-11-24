from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessAppliedCreatorModeConfiguration(BaseModel):
    creatorModeControl: StrictStr | None = None
