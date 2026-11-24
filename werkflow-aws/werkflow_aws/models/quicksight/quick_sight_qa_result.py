from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_dashboard_visual_result import QuickSightDashboardVisualResult
from .quick_sight_generated_answer_result import QuickSightGeneratedAnswerResult


class QuickSightQAResult(BaseModel):
    ResultType: StrictStr | None = None
    DashboardVisual: QuickSightDashboardVisualResult | None = None
    GeneratedAnswer: QuickSightGeneratedAnswerResult | None = None
