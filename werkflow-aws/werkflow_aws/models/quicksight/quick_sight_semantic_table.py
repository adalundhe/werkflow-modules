from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_row_level_permission_configuration import QuickSightRowLevelPermissionConfiguration
from .quick_sight_table_semantic_metadata import QuickSightTableSemanticMetadata


class QuickSightSemanticTable(BaseModel):
    Alias: StrictStr | None = None
    DestinationTableId: StrictStr | None = None
    RowLevelPermissionConfiguration: QuickSightRowLevelPermissionConfiguration | None = None
    SemanticMetadata: QuickSightTableSemanticMetadata | None = None
