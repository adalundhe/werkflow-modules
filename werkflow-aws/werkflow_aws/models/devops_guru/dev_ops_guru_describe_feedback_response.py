from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dev_ops_guru_insight_feedback import DevOpsGuruInsightFeedback


class DevOpsGuruDescribeFeedbackResponse(BaseModel):
    InsightFeedback: DevOpsGuruInsightFeedback | None = None
    ResponseMetadata: dict[str, Any] | None = None
