from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class BackupListScanJobsRequest(BaseModel):
    ByAccountId: StrictStr | None = None
    ByBackupVaultName: StrictStr | None = None
    ByCompleteAfter: datetime.datetime | StrictStr | None = None
    ByCompleteBefore: datetime.datetime | StrictStr | None = None
    ByMalwareScanner: Literal['GUARDDUTY'] | None = None
    ByRecoveryPointArn: StrictStr | None = None
    ByResourceArn: StrictStr | None = None
    ByResourceType: Literal['EBS', 'EC2', 'S3'] | None = None
    ByScanResultStatus: Literal['NO_THREATS_FOUND', 'THREATS_FOUND', 'UNKNOWN'] | None = None
    ByState: Literal['CANCELED', 'COMPLETED', 'COMPLETED_WITH_ISSUES', 'CREATED', 'FAILED', 'RUNNING'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
