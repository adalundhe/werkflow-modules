from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_context_attribute import RDSContextAttribute
from .rds_issue_details import RDSIssueDetails
from .rds_recommended_action_parameter import RDSRecommendedActionParameter


class RDSRecommendedAction(BaseModel):
    ActionId: StrictStr | None = None
    Title: StrictStr | None = None
    Description: StrictStr | None = None
    Operation: StrictStr | None = None
    Parameters: list[RDSRecommendedActionParameter] | None = None
    ApplyModes: list[StrictStr] | None = None
    Status: StrictStr | None = None
    IssueDetails: RDSIssueDetails | None = None
    ContextAttributes: list[RDSContextAttribute] | None = None
