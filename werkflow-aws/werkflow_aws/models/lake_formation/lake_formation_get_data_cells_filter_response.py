from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lake_formation_data_cells_filter import LakeFormationDataCellsFilter


class LakeFormationGetDataCellsFilterResponse(BaseModel):
    DataCellsFilter: LakeFormationDataCellsFilter | None = None
    ResponseMetadata: dict[str, Any] | None = None
