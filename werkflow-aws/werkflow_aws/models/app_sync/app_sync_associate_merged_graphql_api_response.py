from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_sync_source_api_association import AppSyncSourceApiAssociation


class AppSyncAssociateMergedGraphqlApiResponse(BaseModel):
    sourceApiAssociation: AppSyncSourceApiAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
