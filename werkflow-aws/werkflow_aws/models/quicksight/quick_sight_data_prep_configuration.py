from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_destination_table import QuickSightDestinationTable
from .quick_sight_source_table import QuickSightSourceTable
from .quick_sight_transform_step import QuickSightTransformStep


class QuickSightDataPrepConfiguration(BaseModel):
    SourceTableMap: dict[StrictStr, QuickSightSourceTable] | None = None
    TransformStepMap: dict[StrictStr, QuickSightTransformStep] | None = None
    DestinationTableMap: dict[StrictStr, QuickSightDestinationTable] | None = None
