from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class GlueGetSchemaResponse(BaseModel):
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
    CreatedTime: StrictStr | None = None
    UpdatedTime: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
