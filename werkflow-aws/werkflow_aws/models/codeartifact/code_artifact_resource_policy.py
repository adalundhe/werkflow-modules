from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactResourcePolicy(BaseModel):
    resourceArn: StrictStr | None = None
    revision: StrictStr | None = None
    document: StrictStr | None = None
