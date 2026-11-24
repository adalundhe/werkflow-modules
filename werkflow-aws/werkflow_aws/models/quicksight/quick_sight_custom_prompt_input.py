from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_custom_prompt_input_parameters import QuickSightCustomPromptInputParameters
from .quick_sight_custom_prompt_profile import QuickSightCustomPromptProfile


class QuickSightCustomPromptInput(BaseModel):
    ExistingPrompt: QuickSightCustomPromptProfile | None = None
    NewPrompt: QuickSightCustomPromptInputParameters | None = None
