from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .athena_notebook_metadata import AthenaNotebookMetadata


class AthenaGetNotebookMetadataResponse(BaseModel):
    NotebookMetadata: AthenaNotebookMetadata | None = None
    ResponseMetadata: dict[str, Any] | None = None
