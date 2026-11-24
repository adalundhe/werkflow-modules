from __future__ import annotations
from pydantic import BaseModel
from .connect_evaluation_automation_rule_category import ConnectEvaluationAutomationRuleCategory


class ConnectEvaluationContactLensAnswerAnalysisDetails(BaseModel):
    MatchedRuleCategories: list[ConnectEvaluationAutomationRuleCategory] | None = None
