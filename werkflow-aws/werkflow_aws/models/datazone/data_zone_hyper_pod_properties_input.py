from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneHyperPodPropertiesInput(BaseModel):
    clusterName: StrictStr
