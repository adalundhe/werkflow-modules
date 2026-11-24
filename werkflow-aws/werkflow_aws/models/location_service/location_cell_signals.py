from __future__ import annotations
from pydantic import BaseModel
from .location_lte_cell_details import LocationLteCellDetails


class LocationCellSignals(BaseModel):
    LteCellDetails: list[LocationLteCellDetails]
