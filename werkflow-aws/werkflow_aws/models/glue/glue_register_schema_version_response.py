from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class GlueRegisterSchemaVersionResponse(BaseModel):
    SchemaVersionId: StrictStr | None = None
    VersionNumber: StrictInt | None = None
    Status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
