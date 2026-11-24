from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailLoadBalancerTlsPolicy(BaseModel):
    name: StrictStr | None = None
    isDefault: StrictBool | None = None
    description: StrictStr | None = None
    protocols: list[StrictStr] | None = None
    ciphers: list[StrictStr] | None = None
