from __future__ import annotations
from pydantic import BaseModel
from .connect_sign_in_distribution import ConnectSignInDistribution


class ConnectSignInConfig(BaseModel):
    Distributions: list[ConnectSignInDistribution] | None = None
