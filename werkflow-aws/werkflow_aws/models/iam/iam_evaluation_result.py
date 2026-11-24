from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .iam_organizations_decision_detail import IAMOrganizationsDecisionDetail
from .iam_permissions_boundary_decision_detail import IAMPermissionsBoundaryDecisionDetail
from .iam_resource_specific_result import IAMResourceSpecificResult
from .iam_statement import IAMStatement


class IAMEvaluationResult(BaseModel):
    EvalActionName: StrictStr | None = None
    EvalResourceName: StrictStr | None = None
    EvalDecision: StrictStr | None = None
    MatchedStatements: list[IAMStatement] | None = None
    MissingContextValues: list[StrictStr] | None = None
    OrganizationsDecisionDetail: IAMOrganizationsDecisionDetail | None = None
    PermissionsBoundaryDecisionDetail: IAMPermissionsBoundaryDecisionDetail | None = None
    EvalDecisionDetails: dict[StrictStr, StrictStr] | None = None
    ResourceSpecificResults: list[IAMResourceSpecificResult] | None = None
