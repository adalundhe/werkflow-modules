from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_search_index_field_status import CloudSearchIndexFieldStatus


class CloudSearchDefineIndexFieldResponse(BaseModel):
    IndexField: CloudSearchIndexFieldStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
