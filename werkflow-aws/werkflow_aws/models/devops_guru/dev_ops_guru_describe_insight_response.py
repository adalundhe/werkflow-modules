from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dev_ops_guru_proactive_insight import DevOpsGuruProactiveInsight
from .dev_ops_guru_reactive_insight import DevOpsGuruReactiveInsight


class DevOpsGuruDescribeInsightResponse(BaseModel):
    ProactiveInsight: DevOpsGuruProactiveInsight | None = None
    ReactiveInsight: DevOpsGuruReactiveInsight | None = None
    ResponseMetadata: dict[str, Any] | None = None
