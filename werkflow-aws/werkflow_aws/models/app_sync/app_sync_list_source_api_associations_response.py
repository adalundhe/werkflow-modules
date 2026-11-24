from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_sync_source_api_association_summary import AppSyncSourceApiAssociationSummary


class AppSyncListSourceApiAssociationsResponse(BaseModel):
    sourceApiAssociationSummaries: list[AppSyncSourceApiAssociationSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
