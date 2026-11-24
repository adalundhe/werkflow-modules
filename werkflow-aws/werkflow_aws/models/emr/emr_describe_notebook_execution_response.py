from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .emr_notebook_execution import EMRNotebookExecution


class EMRDescribeNotebookExecutionResponse(BaseModel):
    NotebookExecution: EMRNotebookExecution | None = None
    ResponseMetadata: dict[str, Any] | None = None
