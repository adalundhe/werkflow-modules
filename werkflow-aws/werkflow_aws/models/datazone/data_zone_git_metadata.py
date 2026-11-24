from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DataZoneGitMetadata(BaseModel):
    connectionId: StrictStr | None = None
    repository: StrictStr | None = None
    branch: StrictStr | None = None
    commitHash: StrictStr | None = None
    fileName: StrictStr | None = None
    committedAt: datetime.datetime | StrictStr | None = None
    commitMessage: StrictStr | None = None
