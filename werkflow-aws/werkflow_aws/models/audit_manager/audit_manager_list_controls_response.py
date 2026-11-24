from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .audit_manager_control_metadata import AuditManagerControlMetadata


class AuditManagerListControlsResponse(BaseModel):
    controlMetadataList: list[AuditManagerControlMetadata] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
