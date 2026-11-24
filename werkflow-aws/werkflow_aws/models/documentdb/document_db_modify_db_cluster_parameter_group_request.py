from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .document_db_parameter import DocumentDBParameter


class DocumentDBModifyDBClusterParameterGroupRequest(BaseModel):
    DBClusterParameterGroupName: StrictStr
    Parameters: list[DocumentDBParameter]
