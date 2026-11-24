from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_registered_user_console_feature_configurations import QuickSightRegisteredUserConsoleFeatureConfigurations


class QuickSightRegisteredUserQuickSightConsoleEmbeddingConfiguration(BaseModel):
    InitialPath: StrictStr | None = None
    FeatureConfigurations: QuickSightRegisteredUserConsoleFeatureConfigurations | None = None
