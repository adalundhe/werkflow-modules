from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dev_ops_guru_proactive_anomaly import DevOpsGuruProactiveAnomaly
from .dev_ops_guru_reactive_anomaly import DevOpsGuruReactiveAnomaly


class DevOpsGuruDescribeAnomalyResponse(BaseModel):
    ProactiveAnomaly: DevOpsGuruProactiveAnomaly | None = None
    ReactiveAnomaly: DevOpsGuruReactiveAnomaly | None = None
    ResponseMetadata: dict[str, Any] | None = None
