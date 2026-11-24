from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class BedrockGuardrailTopic(BaseModel):
    name: StrictStr | None = None
    definition: StrictStr | None = None
    examples: list[StrictStr] | None = None
    type: StrictStr | None = None
    inputAction: StrictStr | None = None
    outputAction: StrictStr | None = None
    inputEnabled: StrictBool | None = None
    outputEnabled: StrictBool | None = None
