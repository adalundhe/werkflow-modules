from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CodeCatalystListSourceRepositoryBranchesItem(BaseModel):
    ref: StrictStr | None = None
    name: StrictStr | None = None
    lastUpdatedTime: datetime.datetime | StrictStr | None = None
    headCommitId: StrictStr | None = None
