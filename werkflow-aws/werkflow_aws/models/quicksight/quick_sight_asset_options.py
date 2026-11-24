from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_visual_custom_action_defaults import QuickSightVisualCustomActionDefaults
from .quick_sight_visual_messages import QuickSightVisualMessages


class QuickSightAssetOptions(BaseModel):
    Timezone: StrictStr | None = None
    WeekStart: StrictStr | None = None
    QBusinessInsightsStatus: StrictStr | None = None
    ExcludedDataSetArns: list[StrictStr] | None = None
    CustomActionDefaults: QuickSightVisualCustomActionDefaults | None = None
    VisualMessages: QuickSightVisualMessages | None = None
