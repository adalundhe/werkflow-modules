from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueUpsertRedshiftTargetOptions(BaseModel):
    TableLocation: StrictStr | None = None
    ConnectionName: StrictStr | None = None
    UpsertKeys: list[StrictStr] | None = None
