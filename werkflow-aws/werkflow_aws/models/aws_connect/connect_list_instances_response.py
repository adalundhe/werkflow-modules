from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_instance_summary import ConnectInstanceSummary


class ConnectListInstancesResponse(BaseModel):
    InstanceSummaryList: list[ConnectInstanceSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
