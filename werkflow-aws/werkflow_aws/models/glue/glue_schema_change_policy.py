from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueSchemaChangePolicy(BaseModel):
    UpdateBehavior: StrictStr | None = None
    DeleteBehavior: StrictStr | None = None
