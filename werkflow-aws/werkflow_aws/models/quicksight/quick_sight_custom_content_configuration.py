from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions


class QuickSightCustomContentConfiguration(BaseModel):
    ContentUrl: StrictStr | None = None
    ContentType: StrictStr | None = None
    ImageScaling: StrictStr | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
