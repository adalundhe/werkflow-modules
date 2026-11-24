from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .document_dbdb_subnet_group import DocumentDBDBSubnetGroup


class DocumentDBDescribeDBSubnetGroupsResponse(BaseModel):
    Marker: StrictStr | None = None
    DBSubnetGroups: list[DocumentDBDBSubnetGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None
