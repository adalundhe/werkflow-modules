from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerClusterSlurmConfigDetails(BaseModel):
    NodeType: StrictStr | None = None
    PartitionNames: list[StrictStr] | None = None
