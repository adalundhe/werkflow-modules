from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .document_dbdb_cluster_parameter_group import DocumentDBDBClusterParameterGroup


class DocumentDBDescribeDBClusterParameterGroupsResponse(BaseModel):
    Marker: StrictStr | None = None
    DBClusterParameterGroups: list[DocumentDBDBClusterParameterGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None
