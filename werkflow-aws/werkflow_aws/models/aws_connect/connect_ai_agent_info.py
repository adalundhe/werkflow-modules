from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ConnectAiAgentInfo(BaseModel):
    AiUseCase: StrictStr | None = None
    AiAgentVersionId: StrictStr | None = None
    AiAgentEscalated: StrictBool | None = None
