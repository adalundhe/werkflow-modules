from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_set_column_id_mapping import QuickSightDataSetColumnIdMapping


class QuickSightTransformOperationSource(BaseModel):
    TransformOperationId: StrictStr | None = None
    ColumnIdMappings: list[QuickSightDataSetColumnIdMapping] | None = None
