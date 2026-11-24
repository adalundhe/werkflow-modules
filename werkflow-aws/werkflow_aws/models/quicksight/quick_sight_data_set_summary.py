from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .quick_sight_row_level_permission_data_set import QuickSightRowLevelPermissionDataSet


class QuickSightDataSetSummary(BaseModel):
    Arn: StrictStr | None = None
    DataSetId: StrictStr | None = None
    Name: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    ImportMode: StrictStr | None = None
    RowLevelPermissionDataSet: QuickSightRowLevelPermissionDataSet | None = None
    RowLevelPermissionDataSetMap: dict[StrictStr, QuickSightRowLevelPermissionDataSet] | None = None
    RowLevelPermissionTagConfigurationApplied: StrictBool | None = None
    ColumnLevelPermissionRulesApplied: StrictBool | None = None
    UseAs: StrictStr | None = None
