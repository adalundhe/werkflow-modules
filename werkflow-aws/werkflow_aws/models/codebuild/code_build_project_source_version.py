from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildProjectSourceVersion(BaseModel):
    sourceIdentifier: StrictStr | None = None
    sourceVersion: StrictStr | None = None
