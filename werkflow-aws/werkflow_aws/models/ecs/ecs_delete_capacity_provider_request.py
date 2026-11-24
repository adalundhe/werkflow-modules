from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSDeleteCapacityProviderRequest(BaseModel):
    capacityProvider: StrictStr
    cluster: StrictStr | None = None
