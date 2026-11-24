from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueJdbcTarget(BaseModel):
    ConnectionName: StrictStr | None = None
    Path: StrictStr | None = None
    Exclusions: list[StrictStr] | None = None
    EnableAdditionalMetadata: list[StrictStr] | None = None
