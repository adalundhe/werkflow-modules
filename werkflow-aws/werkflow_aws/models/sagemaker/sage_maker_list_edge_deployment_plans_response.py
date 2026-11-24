from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_edge_deployment_plan_summary import SageMakerEdgeDeploymentPlanSummary


class SageMakerListEdgeDeploymentPlansResponse(BaseModel):
    EdgeDeploymentPlanSummaries: list[SageMakerEdgeDeploymentPlanSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
