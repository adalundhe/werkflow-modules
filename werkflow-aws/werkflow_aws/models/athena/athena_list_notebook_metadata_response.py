from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .athena_notebook_metadata import AthenaNotebookMetadata


class AthenaListNotebookMetadataResponse(BaseModel):
    NextToken: StrictStr | None = None
    NotebookMetadataList: list[AthenaNotebookMetadata] | None = None
    ResponseMetadata: dict[str, Any] | None = None
