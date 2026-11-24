from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from typing import Any


class MSKClusterV2(BaseModel):
    ActiveOperationArn: StrictStr | None = None
    ClusterType: StrictStr | None = None
    ClusterArn: StrictStr | None = None
    ClusterName: StrictStr | None = None
    CreationTime: datetime.datetime | None = None
    CurrentVersion: StrictStr | None = None
    State: StrictStr | None = None
    StateInfo: dict[str, Any] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    Provisioned: dict[str, Any] | None = None
    Serverless: dict[str, Any] | None = None
