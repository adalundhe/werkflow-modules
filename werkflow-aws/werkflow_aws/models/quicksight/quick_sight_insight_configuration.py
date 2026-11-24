from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_computation import QuickSightComputation
from .quick_sight_custom_narrative_options import QuickSightCustomNarrativeOptions
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions


class QuickSightInsightConfiguration(BaseModel):
    Computations: list[QuickSightComputation] | None = None
    CustomNarrative: QuickSightCustomNarrativeOptions | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
