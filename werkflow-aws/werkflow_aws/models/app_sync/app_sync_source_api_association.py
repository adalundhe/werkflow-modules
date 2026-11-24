from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .app_sync_source_api_association_config import AppSyncSourceApiAssociationConfig


class AppSyncSourceApiAssociation(BaseModel):
    associationId: StrictStr | None = None
    associationArn: StrictStr | None = None
    sourceApiId: StrictStr | None = None
    sourceApiArn: StrictStr | None = None
    mergedApiArn: StrictStr | None = None
    mergedApiId: StrictStr | None = None
    description: StrictStr | None = None
    sourceApiAssociationConfig: AppSyncSourceApiAssociationConfig | None = None
    sourceApiAssociationStatus: StrictStr | None = None
    sourceApiAssociationStatusDetail: StrictStr | None = None
    lastSuccessfulMergeDate: datetime.datetime | StrictStr | None = None
