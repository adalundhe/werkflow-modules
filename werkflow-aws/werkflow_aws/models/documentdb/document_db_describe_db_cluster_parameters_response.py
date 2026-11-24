from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .document_db_parameter import DocumentDBParameter


class DocumentDBDescribeDBClusterParametersResponse(BaseModel):
    Parameters: list[DocumentDBParameter] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
