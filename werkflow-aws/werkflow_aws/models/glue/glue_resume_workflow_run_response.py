from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlueResumeWorkflowRunResponse(BaseModel):
    RunId: StrictStr | None = None
    NodeIds: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
