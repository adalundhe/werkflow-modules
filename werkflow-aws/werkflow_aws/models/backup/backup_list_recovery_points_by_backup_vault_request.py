from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class BackupListRecoveryPointsByBackupVaultRequest(BaseModel):
    BackupVaultName: StrictStr
    BackupVaultAccountId: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    ByResourceArn: StrictStr | None = None
    ByResourceType: StrictStr | None = None
    ByBackupPlanId: StrictStr | None = None
    ByCreatedBefore: datetime.datetime | StrictStr | None = None
    ByCreatedAfter: datetime.datetime | StrictStr | None = None
    ByParentRecoveryPointArn: StrictStr | None = None
