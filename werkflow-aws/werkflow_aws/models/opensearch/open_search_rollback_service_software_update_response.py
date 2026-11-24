from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_rollback_service_software_options import OpenSearchRollbackServiceSoftwareOptions


class OpenSearchRollbackServiceSoftwareUpdateResponse(BaseModel):
    RollbackServiceSoftwareOptions: OpenSearchRollbackServiceSoftwareOptions | None = None
    ResponseMetadata: dict[str, Any] | None = None
