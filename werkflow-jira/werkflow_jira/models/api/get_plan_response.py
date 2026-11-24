from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .get_cross_project_release_response import GetCrossProjectReleaseResponse
from .get_custom_field_response import GetCustomFieldResponse
from .get_exclusion_rules_response import GetExclusionRulesResponse
from .get_issue_source_response import GetIssueSourceResponse
from .get_permission_response import GetPermissionResponse
from .get_scheduling_response import GetSchedulingResponse


class GetPlanResponse(BaseModel):
    crossProjectReleases: list[GetCrossProjectReleaseResponse] | None = None
    customFields: list[GetCustomFieldResponse] | None = None
    exclusionRules: GetExclusionRulesResponse | None = None
    id: StrictInt | None = None
    issueSources: list[GetIssueSourceResponse] | None = None
    lastSaved: StrictStr | None = None
    leadAccountId: StrictStr | None = None
    name: StrictStr | None = None
    permissions: list[GetPermissionResponse] | None = None
    scheduling: GetSchedulingResponse | None = None
    status: StrictStr | None = None
