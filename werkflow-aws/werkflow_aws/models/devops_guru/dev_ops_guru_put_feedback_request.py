from __future__ import annotations
from pydantic import BaseModel
from .dev_ops_guru_insight_feedback import DevOpsGuruInsightFeedback


class DevOpsGuruPutFeedbackRequest(BaseModel):
    InsightFeedback: DevOpsGuruInsightFeedback | None = None
