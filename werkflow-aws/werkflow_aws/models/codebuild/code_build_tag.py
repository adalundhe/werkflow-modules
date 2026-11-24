from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildTag(BaseModel):
    key: StrictStr | None = None
    value: StrictStr | None = None
