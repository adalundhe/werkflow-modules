from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class AmplifyStartJobRequest(BaseModel):
    appId: StrictStr
    branchName: StrictStr
    jobType: Literal['RELEASE', 'RETRY', 'MANUAL', 'WEB_HOOK']
    jobId: StrictStr | None = None
    jobReason: StrictStr | None = None
    commitId: StrictStr | None = None
    commitMessage: StrictStr | None = None
    commitTime: datetime.datetime | StrictStr | None = None
