from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueKeySchemaElement(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
