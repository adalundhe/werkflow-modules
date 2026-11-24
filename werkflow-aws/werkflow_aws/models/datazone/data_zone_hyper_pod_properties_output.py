from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneHyperPodPropertiesOutput(BaseModel):
    clusterName: StrictStr | None = None
    clusterArn: StrictStr | None = None
    orchestrator: StrictStr | None = None
