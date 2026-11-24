from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .athena_table_metadata import AthenaTableMetadata


class AthenaGetTableMetadataResponse(BaseModel):
    TableMetadata: AthenaTableMetadata | None = None
    ResponseMetadata: dict[str, Any] | None = None
