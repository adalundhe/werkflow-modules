from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_usd import SageMakerUSD


class SageMakerPublicWorkforceTaskPrice(BaseModel):
    AmountInUsd: SageMakerUSD | None = None
