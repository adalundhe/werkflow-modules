from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_table_cell_image_sizing_configuration import QuickSightTableCellImageSizingConfiguration


class QuickSightTableFieldImageConfiguration(BaseModel):
    SizingOptions: QuickSightTableCellImageSizingConfiguration | None = None
