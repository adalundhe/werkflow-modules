from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_custom_action_filter_operation import QuickSightCustomActionFilterOperation
from .quick_sight_custom_action_navigation_operation import QuickSightCustomActionNavigationOperation
from .quick_sight_custom_action_set_parameters_operation import QuickSightCustomActionSetParametersOperation
from .quick_sight_custom_action_url_operation import QuickSightCustomActionURLOperation


class QuickSightVisualCustomActionOperation(BaseModel):
    FilterOperation: QuickSightCustomActionFilterOperation | None = None
    NavigationOperation: QuickSightCustomActionNavigationOperation | None = None
    URLOperation: QuickSightCustomActionURLOperation | None = None
    SetParametersOperation: QuickSightCustomActionSetParametersOperation | None = None
