from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .directory_service_update_info_entry import DirectoryServiceUpdateInfoEntry


class DirectoryServiceDescribeUpdateDirectoryResponse(BaseModel):
    UpdateActivities: list[DirectoryServiceUpdateInfoEntry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
