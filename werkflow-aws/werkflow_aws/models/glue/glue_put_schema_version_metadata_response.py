from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class GluePutSchemaVersionMetadataResponse(BaseModel):
    SchemaArn: StrictStr | None = None
    SchemaName: StrictStr | None = None
    RegistryName: StrictStr | None = None
    LatestVersion: StrictBool | None = None
    VersionNumber: StrictInt | None = None
    SchemaVersionId: StrictStr | None = None
    MetadataKey: StrictStr | None = None
    MetadataValue: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
