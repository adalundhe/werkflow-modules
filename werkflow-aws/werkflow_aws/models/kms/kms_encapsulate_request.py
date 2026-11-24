from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class KMSEncapsulateRequest(BaseModel):
    KeyId: StrictStr
    EncapsulationAlgorithm: Literal['ML_KEM']
    GrantTokens: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
