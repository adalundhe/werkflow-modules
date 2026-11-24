from __future__ import annotations
from pydantic import BaseModel
from .lake_formation_data_cells_filter import LakeFormationDataCellsFilter


class LakeFormationUpdateDataCellsFilterRequest(BaseModel):
    TableData: LakeFormationDataCellsFilter
