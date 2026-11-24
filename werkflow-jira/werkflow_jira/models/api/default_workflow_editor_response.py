from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DefaultWorkflowEditorResponse(BaseModel):
    value: StrictStr | None = None
