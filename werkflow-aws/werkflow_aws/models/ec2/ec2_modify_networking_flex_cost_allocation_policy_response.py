from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class EC2ModifyNetworkingFlexCostAllocationPolicyResponse(BaseModel):
    FcaPolicyId: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    Version: StrictInt | None = None
    VersionExpectedEffectiveAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
