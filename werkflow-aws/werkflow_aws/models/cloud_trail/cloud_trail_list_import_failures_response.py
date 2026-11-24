from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_trail_import_failure_list_item import CloudTrailImportFailureListItem


class CloudTrailListImportFailuresResponse(BaseModel):
    Failures: list[CloudTrailImportFailureListItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
