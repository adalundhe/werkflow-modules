from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildEnvironmentImage(BaseModel):
    name: StrictStr | None = None
    description: StrictStr | None = None
    versions: list[StrictStr] | None = None
