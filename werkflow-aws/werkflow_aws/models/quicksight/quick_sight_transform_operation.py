from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_cast_column_type_operation import QuickSightCastColumnTypeOperation
from .quick_sight_create_columns_operation import QuickSightCreateColumnsOperation
from .quick_sight_filter_operation import QuickSightFilterOperation
from .quick_sight_override_dataset_parameter_operation import QuickSightOverrideDatasetParameterOperation
from .quick_sight_project_operation import QuickSightProjectOperation
from .quick_sight_rename_column_operation import QuickSightRenameColumnOperation
from .quick_sight_tag_column_operation import QuickSightTagColumnOperation
from .quick_sight_untag_column_operation import QuickSightUntagColumnOperation


class QuickSightTransformOperation(BaseModel):
    ProjectOperation: QuickSightProjectOperation | None = None
    FilterOperation: QuickSightFilterOperation | None = None
    CreateColumnsOperation: QuickSightCreateColumnsOperation | None = None
    RenameColumnOperation: QuickSightRenameColumnOperation | None = None
    CastColumnTypeOperation: QuickSightCastColumnTypeOperation | None = None
    TagColumnOperation: QuickSightTagColumnOperation | None = None
    UntagColumnOperation: QuickSightUntagColumnOperation | None = None
    OverrideDatasetParameterOperation: QuickSightOverrideDatasetParameterOperation | None = None
