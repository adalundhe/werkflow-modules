from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockHumanWorkflowConfig(BaseModel):
    flowDefinitionArn: StrictStr | None = None
    instructions: StrictStr | None = None
