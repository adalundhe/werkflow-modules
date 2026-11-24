from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rdsdb_subnet_group_model import RDSDBSubnetGroupModel


class RDSCreateDBSubnetGroupResponse(BaseModel):
    DBSubnetGroup: RDSDBSubnetGroupModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
