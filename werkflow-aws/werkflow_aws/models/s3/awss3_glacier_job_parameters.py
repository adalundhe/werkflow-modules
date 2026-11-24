from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class AWSS3GlacierJobParameters(BaseModel):
    Tier: Literal['Standard', 'Bulk', 'Expedited']
