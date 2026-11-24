from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SageMakerClusterSlurmConfig(BaseModel):
    NodeType: Literal['Controller', 'Login', 'Compute']
    PartitionNames: list[StrictStr] | None = None
