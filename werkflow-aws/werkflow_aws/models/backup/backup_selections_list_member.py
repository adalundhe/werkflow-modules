from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BackupSelectionsListMember(BaseModel):
    SelectionId: StrictStr | None = None
    SelectionName: StrictStr | None = None
    BackupPlanId: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    CreatorRequestId: StrictStr | None = None
    IamRoleArn: StrictStr | None = None
