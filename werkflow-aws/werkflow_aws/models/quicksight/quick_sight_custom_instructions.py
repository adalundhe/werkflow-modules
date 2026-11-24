from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightCustomInstructions(BaseModel):
    CustomInstructionsString: StrictStr | None = None
