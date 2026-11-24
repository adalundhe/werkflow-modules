from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_row_level_permission_data_set import QuickSightRowLevelPermissionDataSet
from .quick_sight_row_level_permission_tag_configuration import QuickSightRowLevelPermissionTagConfiguration


class QuickSightRowLevelPermissionConfiguration(BaseModel):
    TagConfiguration: QuickSightRowLevelPermissionTagConfiguration | None = None
    RowLevelPermissionDataSet: QuickSightRowLevelPermissionDataSet | None = None
