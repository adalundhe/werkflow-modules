from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .document_dbdb_subnet_group import DocumentDBDBSubnetGroup


class DocumentDBCreateDBSubnetGroupResponse(BaseModel):
    DBSubnetGroup: DocumentDBDBSubnetGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
