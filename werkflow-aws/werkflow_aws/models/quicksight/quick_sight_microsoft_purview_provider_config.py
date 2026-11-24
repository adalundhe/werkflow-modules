from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_label_action_mapping import QuickSightLabelActionMapping
from .quick_sight_microsoft_purview_credentials import QuickSightMicrosoftPurviewCredentials


class QuickSightMicrosoftPurviewProviderConfig(BaseModel):
    Credentials: QuickSightMicrosoftPurviewCredentials | None = None
    LabelActionMappings: list[QuickSightLabelActionMapping] | None = None
    UnmappedAction: StrictStr | None = None
