from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueS3TablesExportState(BaseModel):
    Status: StrictStr | None = None
