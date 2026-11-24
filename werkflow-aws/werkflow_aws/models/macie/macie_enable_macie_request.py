from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class MacieEnableMacieRequest(BaseModel):
    clientToken: StrictStr | None = None
    findingPublishingFrequency: Literal['FIFTEEN_MINUTES', 'ONE_HOUR', 'SIX_HOURS'] | None = None
    status: Literal['PAUSED', 'ENABLED'] | None = None
