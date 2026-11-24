from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ConfigServiceCustomPolicyDetails(BaseModel):
    PolicyRuntime: StrictStr | None = None
    PolicyText: StrictStr | None = None
    EnableDebugLogDelivery: StrictBool | None = None
