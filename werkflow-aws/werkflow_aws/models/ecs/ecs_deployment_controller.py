from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSDeploymentController(BaseModel):
    type: StrictStr | None = None
