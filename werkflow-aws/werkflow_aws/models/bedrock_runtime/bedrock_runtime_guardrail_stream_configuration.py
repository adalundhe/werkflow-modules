from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class BedrockRuntimeGuardrailStreamConfiguration(BaseModel):
    guardrailIdentifier: StrictStr | None = None
    guardrailVersion: StrictStr | None = None
    trace: Literal['enabled', 'disabled', 'enabled_full'] | None = None
    streamProcessingMode: Literal['sync', 'async'] | None = None
