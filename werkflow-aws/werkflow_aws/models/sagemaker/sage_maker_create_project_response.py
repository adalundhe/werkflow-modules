from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerCreateProjectResponse(BaseModel):
    ProjectArn: StrictStr | None = None
    ProjectId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
