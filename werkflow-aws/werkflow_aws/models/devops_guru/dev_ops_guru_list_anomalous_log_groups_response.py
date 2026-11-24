from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_anomalous_log_group import DevOpsGuruAnomalousLogGroup


class DevOpsGuruListAnomalousLogGroupsResponse(BaseModel):
    InsightId: StrictStr | None = None
    AnomalousLogGroups: list[DevOpsGuruAnomalousLogGroup] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
