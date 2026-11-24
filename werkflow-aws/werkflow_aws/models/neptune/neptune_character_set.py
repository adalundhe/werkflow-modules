from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneCharacterSet(BaseModel):
    CharacterSetName: StrictStr | None = None
    CharacterSetDescription: StrictStr | None = None
