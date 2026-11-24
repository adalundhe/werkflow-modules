from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_sheet_element_configuration_overrides import QuickSightSheetElementConfigurationOverrides


class QuickSightSheetElementRenderingRule(BaseModel):
    Expression: StrictStr | None = None
    ConfigurationOverrides: QuickSightSheetElementConfigurationOverrides | None = None
