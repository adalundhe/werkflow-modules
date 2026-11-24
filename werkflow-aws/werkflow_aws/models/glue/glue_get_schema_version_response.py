from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class GlueGetSchemaVersionResponse(BaseModel):
    SchemaVersionId: StrictStr | None = None
    SchemaDefinition: StrictStr | None = None
    DataFormat: StrictStr | None = None
    SchemaArn: StrictStr | None = None
    VersionNumber: StrictInt | None = None
    Status: StrictStr | None = None
    CreatedTime: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
