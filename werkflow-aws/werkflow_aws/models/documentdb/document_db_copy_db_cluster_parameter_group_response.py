from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .document_dbdb_cluster_parameter_group import DocumentDBDBClusterParameterGroup


class DocumentDBCopyDBClusterParameterGroupResponse(BaseModel):
    DBClusterParameterGroup: DocumentDBDBClusterParameterGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
