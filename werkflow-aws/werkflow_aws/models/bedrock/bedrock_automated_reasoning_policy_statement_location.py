from __future__ import annotations
from pydantic import BaseModel, StrictInt


class BedrockAutomatedReasoningPolicyStatementLocation(BaseModel):
    lines: list[StrictInt] | None = None
