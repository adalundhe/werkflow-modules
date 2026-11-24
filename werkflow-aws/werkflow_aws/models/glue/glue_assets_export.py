from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueAssetsExport(BaseModel):
    S3TablesExport: StrictStr | None = None
