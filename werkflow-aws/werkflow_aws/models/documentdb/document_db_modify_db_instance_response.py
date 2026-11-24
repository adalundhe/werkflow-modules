from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .document_dbdb_instance import DocumentDBDBInstance


class DocumentDBModifyDBInstanceResponse(BaseModel):
    DBInstance: DocumentDBDBInstance | None = None
    ResponseMetadata: dict[str, Any] | None = None
