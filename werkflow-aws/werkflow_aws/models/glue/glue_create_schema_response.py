from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class GlueCreateSchemaResponse(BaseModel):
    RegistryName: StrictStr | None = None
    RegistryArn: StrictStr | None = None
    SchemaName: StrictStr | None = None
    SchemaArn: StrictStr | None = None
    Description: StrictStr | None = None
    DataFormat: StrictStr | None = None
    Compatibility: StrictStr | None = None
    SchemaCheckpoint: StrictInt | None = None
    LatestSchemaVersion: StrictInt | None = None
    NextSchemaVersion: StrictInt | None = None
    SchemaStatus: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    SchemaVersionId: StrictStr | None = None
    SchemaVersionStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
