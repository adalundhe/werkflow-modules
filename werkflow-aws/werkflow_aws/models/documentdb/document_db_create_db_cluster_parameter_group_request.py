from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .document_db_tag import DocumentDBTag


class DocumentDBCreateDBClusterParameterGroupRequest(BaseModel):
    DBClusterParameterGroupName: StrictStr
    DBParameterGroupFamily: StrictStr
    Description: StrictStr
    Tags: list[DocumentDBTag] | None = None
