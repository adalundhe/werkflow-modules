from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamGetExportImageTaskRequest(BaseModel):
    TaskId: StrictStr | None = None
