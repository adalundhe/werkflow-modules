from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class BackupListRecoveryPointsByResourceRequest(BaseModel):
    ResourceArn: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    ManagedByAWSBackupOnly: StrictBool | None = None
