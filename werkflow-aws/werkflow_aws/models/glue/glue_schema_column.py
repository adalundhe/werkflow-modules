from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueSchemaColumn(BaseModel):
    Name: StrictStr | None = None
    DataType: StrictStr | None = None
