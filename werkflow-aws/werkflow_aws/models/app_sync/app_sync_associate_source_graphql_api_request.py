from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_sync_source_api_association_config import AppSyncSourceApiAssociationConfig


class AppSyncAssociateSourceGraphqlApiRequest(BaseModel):
    mergedApiIdentifier: StrictStr
    sourceApiIdentifier: StrictStr
    description: StrictStr | None = None
    sourceApiAssociationConfig: AppSyncSourceApiAssociationConfig | None = None
