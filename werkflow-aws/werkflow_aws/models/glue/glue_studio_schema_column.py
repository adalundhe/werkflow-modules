from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueStudioSchemaColumn(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    GlueStudioType: StrictStr | None = None
