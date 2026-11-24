from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .athena_table_metadata import AthenaTableMetadata


class AthenaListTableMetadataResponse(BaseModel):
    TableMetadataList: list[AthenaTableMetadata] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
