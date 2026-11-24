from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitReactionValueFormats(BaseModel):
    emoji: StrictStr | None = None
    shortCode: StrictStr | None = None
    unicode: StrictStr | None = None
