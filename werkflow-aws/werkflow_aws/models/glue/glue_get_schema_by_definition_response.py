from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlueGetSchemaByDefinitionResponse(BaseModel):
    SchemaVersionId: StrictStr | None = None
    SchemaArn: StrictStr | None = None
    DataFormat: StrictStr | None = None
    Status: StrictStr | None = None
    CreatedTime: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
