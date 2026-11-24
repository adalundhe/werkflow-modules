from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockSelectiveContentGuarding(BaseModel):
    system: StrictStr | None = None
    messages: StrictStr | None = None
