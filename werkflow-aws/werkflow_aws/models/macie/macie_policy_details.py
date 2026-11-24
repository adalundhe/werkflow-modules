from __future__ import annotations
from pydantic import BaseModel
from .macie_finding_action import MacieFindingAction
from .macie_finding_actor import MacieFindingActor


class MaciePolicyDetails(BaseModel):
    action: MacieFindingAction | None = None
    actor: MacieFindingActor | None = None
