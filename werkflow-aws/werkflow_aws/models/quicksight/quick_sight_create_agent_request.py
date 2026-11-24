from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_custom_prompt_input import QuickSightCustomPromptInput


class QuickSightCreateAgentRequest(BaseModel):
    AwsAccountId: StrictStr
    AgentId: StrictStr
    Name: StrictStr
    Spaces: list[StrictStr] | None = None
    ActionConnectors: list[StrictStr] | None = None
    Description: StrictStr | None = None
    IconId: StrictStr | None = None
    StarterPrompts: list[StrictStr] | None = None
    WelcomeMessage: StrictStr | None = None
    AgentLifecycle: Literal['PREVIEW', 'PUBLISHED'] | None = None
    CustomPromptInput: QuickSightCustomPromptInput | None = None
