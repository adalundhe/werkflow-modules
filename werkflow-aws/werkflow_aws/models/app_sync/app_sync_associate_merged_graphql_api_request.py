from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_sync_source_api_association_config import AppSyncSourceApiAssociationConfig


class AppSyncAssociateMergedGraphqlApiRequest(BaseModel):
    sourceApiIdentifier: StrictStr
    mergedApiIdentifier: StrictStr
    description: StrictStr | None = None
    sourceApiAssociationConfig: AppSyncSourceApiAssociationConfig | None = None
