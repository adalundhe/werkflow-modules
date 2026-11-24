from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dms_schema_conversion_request import DMSSchemaConversionRequest


class DMSCancelMetadataModelConversionResponse(BaseModel):
    Request: DMSSchemaConversionRequest | None = None
    ResponseMetadata: dict[str, Any] | None = None
