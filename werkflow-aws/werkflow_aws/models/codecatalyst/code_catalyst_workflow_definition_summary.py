from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystWorkflowDefinitionSummary(BaseModel):
    path: StrictStr | None = None
