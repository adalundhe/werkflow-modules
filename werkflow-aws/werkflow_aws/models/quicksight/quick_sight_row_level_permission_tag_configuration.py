from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_row_level_permission_tag_rule import QuickSightRowLevelPermissionTagRule


class QuickSightRowLevelPermissionTagConfiguration(BaseModel):
    Status: StrictStr | None = None
    TagRules: list[QuickSightRowLevelPermissionTagRule] | None = None
    TagRuleConfigurations: list[list[StrictStr]] | None = None
