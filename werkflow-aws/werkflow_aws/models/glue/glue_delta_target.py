from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueDeltaTarget(BaseModel):
    DeltaTables: list[StrictStr] | None = None
    ConnectionName: StrictStr | None = None
    WriteManifest: StrictBool | None = None
    CreateNativeDeltaTable: StrictBool | None = None
