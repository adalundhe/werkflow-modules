from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitObjectTypes(BaseModel):
    source: StrictStr | None = None
    destination: StrictStr | None = None
    base: StrictStr | None = None
