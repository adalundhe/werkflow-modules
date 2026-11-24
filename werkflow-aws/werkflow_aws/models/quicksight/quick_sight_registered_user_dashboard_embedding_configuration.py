from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_registered_user_dashboard_feature_configurations import QuickSightRegisteredUserDashboardFeatureConfigurations


class QuickSightRegisteredUserDashboardEmbeddingConfiguration(BaseModel):
    InitialDashboardId: StrictStr
    FeatureConfigurations: QuickSightRegisteredUserDashboardFeatureConfigurations | None = None
