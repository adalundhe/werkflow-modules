from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDeploymentStrategyOptions(BaseModel):
    DeploymentStrategy: StrictStr | None = None
