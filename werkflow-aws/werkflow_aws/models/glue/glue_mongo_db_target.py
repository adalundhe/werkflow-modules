from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueMongoDBTarget(BaseModel):
    ConnectionName: StrictStr | None = None
    Path: StrictStr | None = None
    ScanAll: StrictBool | None = None
