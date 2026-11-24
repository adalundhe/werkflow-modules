from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class BedrockRuntimeReasoningContentBlockDelta(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    text: StrictStr | None = None
    redactedContent: StrictBytes | Any | None = None
    signature: StrictStr | None = None
