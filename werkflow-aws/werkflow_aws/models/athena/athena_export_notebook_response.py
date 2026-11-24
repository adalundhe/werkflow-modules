from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .athena_notebook_metadata import AthenaNotebookMetadata


class AthenaExportNotebookResponse(BaseModel):
    NotebookMetadata: AthenaNotebookMetadata | None = None
    Payload: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
