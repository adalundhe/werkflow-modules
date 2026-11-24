from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_aggregate_operation import QuickSightAggregateOperation
from .quick_sight_append_operation import QuickSightAppendOperation
from .quick_sight_cast_column_types_operation import QuickSightCastColumnTypesOperation
from .quick_sight_create_columns_operation import QuickSightCreateColumnsOperation
from .quick_sight_filters_operation import QuickSightFiltersOperation
from .quick_sight_import_table_operation import QuickSightImportTableOperation
from .quick_sight_join_operation import QuickSightJoinOperation
from .quick_sight_pivot_operation import QuickSightPivotOperation
from .quick_sight_project_operation import QuickSightProjectOperation
from .quick_sight_rename_columns_operation import QuickSightRenameColumnsOperation
from .quick_sight_unpivot_operation import QuickSightUnpivotOperation


class QuickSightTransformStep(BaseModel):
    ImportTableStep: QuickSightImportTableOperation | None = None
    ProjectStep: QuickSightProjectOperation | None = None
    FiltersStep: QuickSightFiltersOperation | None = None
    CreateColumnsStep: QuickSightCreateColumnsOperation | None = None
    RenameColumnsStep: QuickSightRenameColumnsOperation | None = None
    CastColumnTypesStep: QuickSightCastColumnTypesOperation | None = None
    JoinStep: QuickSightJoinOperation | None = None
    AggregateStep: QuickSightAggregateOperation | None = None
    PivotStep: QuickSightPivotOperation | None = None
    UnpivotStep: QuickSightUnpivotOperation | None = None
    AppendStep: QuickSightAppendOperation | None = None
