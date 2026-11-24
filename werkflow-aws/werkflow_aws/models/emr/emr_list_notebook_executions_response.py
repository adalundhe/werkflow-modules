from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .emr_notebook_execution_summary import EMRNotebookExecutionSummary


class EMRListNotebookExecutionsResponse(BaseModel):
    NotebookExecutions: list[EMRNotebookExecutionSummary] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
