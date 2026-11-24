from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_failed_to_update_association import QuickSightFailedToUpdateAssociation


class QuickSightUpdateAgentResponse(BaseModel):
    Arn: StrictStr | None = None
    AgentId: StrictStr | None = None
    AgentStatus: StrictStr | None = None
    FailedToAddSpaces: list[QuickSightFailedToUpdateAssociation] | None = None
    FailedToRemoveSpaces: list[QuickSightFailedToUpdateAssociation] | None = None
    FailedToAddActionConnectors: list[QuickSightFailedToUpdateAssociation] | None = None
    FailedToRemoveActionConnectors: list[QuickSightFailedToUpdateAssociation] | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
