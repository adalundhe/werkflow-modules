from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BackupTieringConfigurationsListMember(BaseModel):
    TieringConfigurationArn: StrictStr | None = None
    TieringConfigurationName: StrictStr | None = None
    BackupVaultName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
