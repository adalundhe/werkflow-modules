from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeAlgorithmImage(BaseModel):
    name: StrictStr | None = None
    dockerURI: StrictStr | None = None
