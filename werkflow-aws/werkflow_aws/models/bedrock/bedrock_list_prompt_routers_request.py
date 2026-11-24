from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class BedrockListPromptRoutersRequest(BaseModel):
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    type: Literal['custom', 'default'] | None = None
