from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lake_formation_tagged_table import LakeFormationTaggedTable


class LakeFormationSearchTablesByLFTagsResponse(BaseModel):
    NextToken: StrictStr | None = None
    TableList: list[LakeFormationTaggedTable] | None = None
    ResponseMetadata: dict[str, Any] | None = None
