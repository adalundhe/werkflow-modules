from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class MSKCreateVpcConnectionResponse(BaseModel):
    VpcConnectionArn: StrictStr | None = None
    State: StrictStr | None = None
    Authentication: StrictStr | None = None
    VpcId: StrictStr | None = None
    ClientSubnets: list[StrictStr] | None = None
    SecurityGroups: list[StrictStr] | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
