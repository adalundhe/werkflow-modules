from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactTagModel(BaseModel):
    key: StrictStr | None = None
    value: StrictStr | None = None
