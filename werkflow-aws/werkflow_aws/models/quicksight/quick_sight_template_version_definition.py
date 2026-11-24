from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_analysis_defaults import QuickSightAnalysisDefaults
from .quick_sight_asset_options import QuickSightAssetOptions
from .quick_sight_calculated_field import QuickSightCalculatedField
from .quick_sight_column_configuration import QuickSightColumnConfiguration
from .quick_sight_data_set_configuration import QuickSightDataSetConfiguration
from .quick_sight_filter_group import QuickSightFilterGroup
from .quick_sight_parameter_declaration import QuickSightParameterDeclaration
from .quick_sight_query_execution_options import QuickSightQueryExecutionOptions
from .quick_sight_sheet_definition import QuickSightSheetDefinition
from .quick_sight_static_file import QuickSightStaticFile
from .quick_sight_tooltip_sheet_definition import QuickSightTooltipSheetDefinition
from .quick_sight_topic_configuration import QuickSightTopicConfiguration


class QuickSightTemplateVersionDefinition(BaseModel):
    DataSetConfigurations: list[QuickSightDataSetConfiguration] | None = None
    TopicConfigurations: list[QuickSightTopicConfiguration] | None = None
    Sheets: list[QuickSightSheetDefinition] | None = None
    TooltipSheets: list[QuickSightTooltipSheetDefinition] | None = None
    CalculatedFields: list[QuickSightCalculatedField] | None = None
    ParameterDeclarations: list[QuickSightParameterDeclaration] | None = None
    FilterGroups: list[QuickSightFilterGroup] | None = None
    ColumnConfigurations: list[QuickSightColumnConfiguration] | None = None
    AnalysisDefaults: QuickSightAnalysisDefaults | None = None
    Options: QuickSightAssetOptions | None = None
    QueryExecutionOptions: QuickSightQueryExecutionOptions | None = None
    StaticFiles: list[QuickSightStaticFile] | None = None
