from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .neptune_db_subnet_group import NeptuneDBSubnetGroup


class NeptuneModifyDBSubnetGroupResponse(BaseModel):
    DBSubnetGroup: NeptuneDBSubnetGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
