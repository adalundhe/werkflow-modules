from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CodeBuildProjectBadge(BaseModel):
    badgeEnabled: StrictBool | None = None
    badgeRequestUrl: StrictStr | None = None
