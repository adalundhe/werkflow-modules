from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .document_db_tag import DocumentDBTag


class DocumentDBCopyDBClusterParameterGroupRequest(BaseModel):
    SourceDBClusterParameterGroupIdentifier: StrictStr
    TargetDBClusterParameterGroupIdentifier: StrictStr
    TargetDBClusterParameterGroupDescription: StrictStr
    Tags: list[DocumentDBTag] | None = None
