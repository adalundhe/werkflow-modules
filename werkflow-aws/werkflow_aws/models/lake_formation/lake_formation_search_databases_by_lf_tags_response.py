from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lake_formation_tagged_database import LakeFormationTaggedDatabase


class LakeFormationSearchDatabasesByLFTagsResponse(BaseModel):
    NextToken: StrictStr | None = None
    DatabaseList: list[LakeFormationTaggedDatabase] | None = None
    ResponseMetadata: dict[str, Any] | None = None
