from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ServiceCatalogLastSync(BaseModel):
    LastSyncTime: datetime.datetime | StrictStr | None = None
    LastSyncStatus: StrictStr | None = None
    LastSyncStatusMessage: StrictStr | None = None
    LastSuccessfulSyncTime: datetime.datetime | StrictStr | None = None
    LastSuccessfulSyncProvisioningArtifactId: StrictStr | None = None
