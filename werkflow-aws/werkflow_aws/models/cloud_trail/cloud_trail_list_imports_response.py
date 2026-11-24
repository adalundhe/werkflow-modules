from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_trail_imports_list_item import CloudTrailImportsListItem


class CloudTrailListImportsResponse(BaseModel):
    Imports: list[CloudTrailImportsListItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
