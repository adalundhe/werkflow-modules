from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DefaultWorkflow(BaseModel):
    updateDraftIfNeeded: StrictBool | None = None
    workflow: StrictStr | None = None
