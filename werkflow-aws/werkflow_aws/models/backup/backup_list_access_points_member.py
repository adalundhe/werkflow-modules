from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BackupListAccessPointsMember(BaseModel):
    AccessPointArn: StrictStr | None = None
    AccessPointMetadata: dict[StrictStr, StrictStr] | None = None
    BackupVaultArn: StrictStr | None = None
    BackupVaultName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Name: StrictStr | None = None
    RecoveryPointArn: StrictStr | None = None
    ResourceArn: StrictStr | None = None
    ResourceType: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
