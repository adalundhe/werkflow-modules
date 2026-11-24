from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_shared_view_configurations import QuickSightSharedViewConfigurations


class QuickSightAnonymousUserDashboardFeatureConfigurations(BaseModel):
    SharedView: QuickSightSharedViewConfigurations | None = None
