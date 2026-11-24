from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_anonymous_user_dashboard_feature_configurations import QuickSightAnonymousUserDashboardFeatureConfigurations


class QuickSightAnonymousUserDashboardEmbeddingConfiguration(BaseModel):
    InitialDashboardId: StrictStr
    EnabledFeatures: list[Literal['SHARED_VIEW']] | None = None
    DisabledFeatures: list[Literal['SHARED_VIEW']] | None = None
    FeatureConfigurations: QuickSightAnonymousUserDashboardFeatureConfigurations | None = None
