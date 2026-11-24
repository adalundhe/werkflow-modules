from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AmplifyProductionBranch(BaseModel):
    lastDeployTime: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    thumbnailUrl: StrictStr | None = None
    branchName: StrictStr | None = None
