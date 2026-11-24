from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class VersionRelatedWork(BaseModel):
    category: StrictStr | None = None
    issueId: StrictInt | None = None
    relatedWorkId: StrictStr | None = None
    title: StrictStr | None = None
    url: StrictStr | None = None
