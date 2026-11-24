from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .document_db_tag import DocumentDBTag


class DocumentDBCreateDBSubnetGroupRequest(BaseModel):
    DBSubnetGroupName: StrictStr
    DBSubnetGroupDescription: StrictStr
    SubnetIds: list[StrictStr]
    Tags: list[DocumentDBTag] | None = None
