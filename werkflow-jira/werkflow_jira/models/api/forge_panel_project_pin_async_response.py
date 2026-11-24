from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ForgePanelProjectPinAsyncResponse(BaseModel):
    taskId: StrictStr | None = None
