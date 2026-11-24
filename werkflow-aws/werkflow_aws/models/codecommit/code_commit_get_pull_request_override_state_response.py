from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class CodeCommitGetPullRequestOverrideStateResponse(BaseModel):
    overridden: StrictBool | None = None
    overrider: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
