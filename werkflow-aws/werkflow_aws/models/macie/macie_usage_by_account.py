from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .macie_service_limit import MacieServiceLimit


class MacieUsageByAccount(BaseModel):
    currency: StrictStr | None = None
    estimatedCost: StrictStr | None = None
    serviceLimit: MacieServiceLimit | None = None
    type: StrictStr | None = None
