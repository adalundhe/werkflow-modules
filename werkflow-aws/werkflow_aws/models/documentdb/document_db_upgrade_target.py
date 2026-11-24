from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DocumentDBUpgradeTarget(BaseModel):
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    Description: StrictStr | None = None
    AutoUpgrade: StrictBool | None = None
    IsMajorVersionUpgrade: StrictBool | None = None
