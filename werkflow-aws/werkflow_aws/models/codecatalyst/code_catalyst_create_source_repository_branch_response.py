from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeCatalystCreateSourceRepositoryBranchResponse(BaseModel):
    ref: StrictStr | None = None
    name: StrictStr | None = None
    lastUpdatedTime: datetime.datetime | StrictStr | None = None
    headCommitId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
