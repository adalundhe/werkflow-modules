from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .athena_notebook_session_summary import AthenaNotebookSessionSummary


class AthenaListNotebookSessionsResponse(BaseModel):
    NotebookSessionsList: list[AthenaNotebookSessionSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
