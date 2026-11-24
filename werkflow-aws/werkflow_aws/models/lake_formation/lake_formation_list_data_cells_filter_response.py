from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lake_formation_data_cells_filter import LakeFormationDataCellsFilter


class LakeFormationListDataCellsFilterResponse(BaseModel):
    DataCellsFilters: list[LakeFormationDataCellsFilter] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
