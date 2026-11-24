from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AuditManagerControlComment(BaseModel):
    authorName: StrictStr | None = None
    commentBody: StrictStr | None = None
    postedDate: datetime.datetime | StrictStr | None = None
