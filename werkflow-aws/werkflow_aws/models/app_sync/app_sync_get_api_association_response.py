from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_sync_api_association import AppSyncApiAssociation


class AppSyncGetApiAssociationResponse(BaseModel):
    apiAssociation: AppSyncApiAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
