from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightCustomPromptInputParameters(BaseModel):
    ResponseLength: StrictStr | None = None
    OutputStyle: StrictStr | None = None
    Identity: StrictStr | None = None
    Tone: StrictStr | None = None
    CustomInstructions: StrictStr | None = None
