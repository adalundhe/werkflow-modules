from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessInstructionCollection(BaseModel):
    responseLength: StrictStr | None = None
    targetAudience: StrictStr | None = None
    perspective: StrictStr | None = None
    outputStyle: StrictStr | None = None
    identity: StrictStr | None = None
    tone: StrictStr | None = None
    customInstructions: StrictStr | None = None
    examples: StrictStr | None = None
