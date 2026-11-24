from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystWorkflowDefinition(BaseModel):
    path: StrictStr | None = None
