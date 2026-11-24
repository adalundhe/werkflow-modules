from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_column_group import QuickSightColumnGroup
from .quick_sight_column_level_permission_rule import QuickSightColumnLevelPermissionRule
from .quick_sight_data_prep_configuration import QuickSightDataPrepConfiguration
from .quick_sight_data_set_usage_configuration import QuickSightDataSetUsageConfiguration
from .quick_sight_dataset_parameter import QuickSightDatasetParameter
from .quick_sight_field_folder import QuickSightFieldFolder
from .quick_sight_logical_table import QuickSightLogicalTable
from .quick_sight_performance_configuration import QuickSightPerformanceConfiguration
from .quick_sight_physical_table import QuickSightPhysicalTable
from .quick_sight_row_level_permission_data_set import QuickSightRowLevelPermissionDataSet
from .quick_sight_row_level_permission_tag_configuration import QuickSightRowLevelPermissionTagConfiguration
from .quick_sight_semantic_model_configuration import QuickSightSemanticModelConfiguration
from .quick_sight_unmaterialized_calculated_column import QuickSightUnmaterializedCalculatedColumn


class QuickSightUpdateDataSetRequest(BaseModel):
    AwsAccountId: StrictStr
    DataSetId: StrictStr
    Name: StrictStr
    PhysicalTableMap: dict[StrictStr, QuickSightPhysicalTable]
    ImportMode: Literal['SPICE', 'DIRECT_QUERY']
    LogicalTableMap: dict[StrictStr, QuickSightLogicalTable] | None = None
    ColumnGroups: list[QuickSightColumnGroup] | None = None
    FieldFolders: dict[StrictStr, QuickSightFieldFolder] | None = None
    RowLevelPermissionDataSet: QuickSightRowLevelPermissionDataSet | None = None
    RowLevelPermissionTagConfiguration: QuickSightRowLevelPermissionTagConfiguration | None = None
    ColumnLevelPermissionRules: list[QuickSightColumnLevelPermissionRule] | None = None
    DataSetUsageConfiguration: QuickSightDataSetUsageConfiguration | None = None
    DatasetParameters: list[QuickSightDatasetParameter] | None = None
    PerformanceConfiguration: QuickSightPerformanceConfiguration | None = None
    DataPrepConfiguration: QuickSightDataPrepConfiguration | None = None
    SemanticModelConfiguration: QuickSightSemanticModelConfiguration | None = None
    UnmaterializedCalculatedColumns: list[QuickSightUnmaterializedCalculatedColumn] | None = None
