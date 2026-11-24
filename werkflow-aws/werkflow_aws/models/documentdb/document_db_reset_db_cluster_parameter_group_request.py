from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .document_db_parameter import DocumentDBParameter


class DocumentDBResetDBClusterParameterGroupRequest(BaseModel):
    DBClusterParameterGroupName: StrictStr
    ResetAllParameters: StrictBool | None = None
    Parameters: list[DocumentDBParameter] | None = None
