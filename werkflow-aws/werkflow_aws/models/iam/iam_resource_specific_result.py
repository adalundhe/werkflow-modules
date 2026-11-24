from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .iam_permissions_boundary_decision_detail import IAMPermissionsBoundaryDecisionDetail
from .iam_statement import IAMStatement


class IAMResourceSpecificResult(BaseModel):
    EvalResourceName: StrictStr | None = None
    EvalResourceDecision: StrictStr | None = None
    MatchedStatements: list[IAMStatement] | None = None
    MissingContextValues: list[StrictStr] | None = None
    EvalDecisionDetails: dict[StrictStr, StrictStr] | None = None
    PermissionsBoundaryDecisionDetail: IAMPermissionsBoundaryDecisionDetail | None = None
