from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class KinesisMinimumThroughputBillingCommitmentInput(BaseModel):
    Status: Literal['ENABLED', 'DISABLED']
