from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .directory_service_schema_extension_info import DirectoryServiceSchemaExtensionInfo


class DirectoryServiceListSchemaExtensionsResponse(BaseModel):
    SchemaExtensionsInfo: list[DirectoryServiceSchemaExtensionInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
