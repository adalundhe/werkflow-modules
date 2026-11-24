from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ExportArchivedIssuesTaskProgressResponse(BaseModel):
    fileUrl: StrictStr | None = None
    payload: StrictStr | None = None
    progress: StrictInt | None = None
    status: StrictStr | None = None
    submittedTime: StrictStr | None = None
    taskId: StrictStr | None = None
