from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lake_formation_opt_ins_info import LakeFormationOptInsInfo


class LakeFormationListLakeFormationOptInsResponse(BaseModel):
    LakeFormationOptInsInfoList: list[LakeFormationOptInsInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
