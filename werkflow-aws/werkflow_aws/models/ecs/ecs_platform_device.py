from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ECSPlatformDevice(BaseModel):
    id: StrictStr
    type: Literal['GPU', 'NEURON_DEVICE']
