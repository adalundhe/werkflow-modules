from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lake_formation_work_unit_range import LakeFormationWorkUnitRange


class LakeFormationGetWorkUnitsResponse(BaseModel):
    NextToken: StrictStr | None = None
    QueryId: StrictStr | None = None
    WorkUnitRanges: list[LakeFormationWorkUnitRange] | None = None
    ResponseMetadata: dict[str, Any] | None = None
