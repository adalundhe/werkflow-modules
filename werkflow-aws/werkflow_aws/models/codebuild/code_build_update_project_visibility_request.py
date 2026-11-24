from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodeBuildUpdateProjectVisibilityRequest(BaseModel):
    projectArn: StrictStr
    projectVisibility: Literal['PUBLIC_READ', 'PRIVATE']
    resourceAccessRole: StrictStr | None = None
