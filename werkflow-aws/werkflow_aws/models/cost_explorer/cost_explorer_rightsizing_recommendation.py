from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_current_instance import CostExplorerCurrentInstance
from .cost_explorer_modify_recommendation_detail import CostExplorerModifyRecommendationDetail
from .cost_explorer_terminate_recommendation_detail import CostExplorerTerminateRecommendationDetail


class CostExplorerRightsizingRecommendation(BaseModel):
    AccountId: StrictStr | None = None
    CurrentInstance: CostExplorerCurrentInstance | None = None
    RightsizingType: StrictStr | None = None
    ModifyRecommendationDetail: CostExplorerModifyRecommendationDetail | None = None
    TerminateRecommendationDetail: CostExplorerTerminateRecommendationDetail | None = None
    FindingReasonCodes: list[StrictStr] | None = None
