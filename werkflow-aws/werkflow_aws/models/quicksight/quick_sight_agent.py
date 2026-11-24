from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_custom_prompt_interface import QuickSightCustomPromptInterface


class QuickSightAgent(BaseModel):
    Spaces: list[StrictStr] | None = None
    ActionConnectors: list[StrictStr] | None = None
    Description: StrictStr | None = None
    IconId: StrictStr | None = None
    Name: StrictStr | None = None
    StarterPrompts: list[StrictStr] | None = None
    WelcomeMessage: StrictStr | None = None
    Arn: StrictStr | None = None
    AgentId: StrictStr | None = None
    AgentLifecycle: StrictStr | None = None
    AgentStatus: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    Creator: StrictStr | None = None
    CustomPromptInterface: QuickSightCustomPromptInterface | None = None
    ErrorMessage: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
