from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlueDeleteSchemaResponse(BaseModel):
    SchemaArn: StrictStr | None = None
    SchemaName: StrictStr | None = None
    Status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
