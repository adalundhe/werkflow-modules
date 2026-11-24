from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ConnectAiAgentSearchCriteria(BaseModel):
    Id: StrictStr | None = None
    VersionNumber: StrictInt | None = None
    AiAgentEscalated: StrictBool | None = None
    AiUseCase: Literal['AgentAssistance', 'SelfService'] | None = None
