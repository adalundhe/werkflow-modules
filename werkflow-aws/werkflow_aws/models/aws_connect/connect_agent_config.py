from __future__ import annotations
from pydantic import BaseModel
from .connect_distribution import ConnectDistribution


class ConnectAgentConfig(BaseModel):
    Distributions: list[ConnectDistribution] | None = None
