from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerClusterOrchestratorEksConfig(BaseModel):
    ClusterArn: StrictStr | None = None
