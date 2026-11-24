from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class EC2CreateNetworkingFlexCostAllocationPolicyResponse(BaseModel):
    FcaPolicyId: StrictStr | None = None
    FcaPolicyArn: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    ExpectedEffectiveAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
