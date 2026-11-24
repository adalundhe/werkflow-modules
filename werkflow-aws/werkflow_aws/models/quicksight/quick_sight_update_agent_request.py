from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_custom_prompt_input import QuickSightCustomPromptInput


class QuickSightUpdateAgentRequest(BaseModel):
    AgentId: StrictStr
    AwsAccountId: StrictStr
    Name: StrictStr
    Description: StrictStr | None = None
    IconId: StrictStr | None = None
    StarterPrompts: list[StrictStr] | None = None
    WelcomeMessage: StrictStr | None = None
    CustomPromptInput: QuickSightCustomPromptInput | None = None
    SpacesToAdd: list[StrictStr] | None = None
    SpacesToRemove: list[StrictStr] | None = None
    ActionConnectorsToAdd: list[StrictStr] | None = None
    ActionConnectorsToRemove: list[StrictStr] | None = None
