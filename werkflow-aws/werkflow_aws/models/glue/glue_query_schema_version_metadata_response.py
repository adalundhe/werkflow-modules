from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_metadata_info import GlueMetadataInfo


class GlueQuerySchemaVersionMetadataResponse(BaseModel):
    MetadataInfoMap: dict[StrictStr, GlueMetadataInfo] | None = None
    SchemaVersionId: StrictStr | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
