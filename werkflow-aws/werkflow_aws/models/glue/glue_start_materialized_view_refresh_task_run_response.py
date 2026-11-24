from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlueStartMaterializedViewRefreshTaskRunResponse(BaseModel):
    MaterializedViewRefreshTaskRunId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
