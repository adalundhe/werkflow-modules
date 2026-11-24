from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .create_cross_project_release_request import CreateCrossProjectReleaseRequest
from .create_custom_field_request import CreateCustomFieldRequest
from .create_exclusion_rules_request import CreateExclusionRulesRequest
from .create_issue_source_request import CreateIssueSourceRequest
from .create_permission_request import CreatePermissionRequest
from .create_scheduling_request import CreateSchedulingRequest


class CreatePlanRequest(BaseModel):
    crossProjectReleases: list[CreateCrossProjectReleaseRequest] | None = None
    customFields: list[CreateCustomFieldRequest] | None = None
    exclusionRules: CreateExclusionRulesRequest | None = None
    issueSources: list[CreateIssueSourceRequest] | None = None
    leadAccountId: StrictStr | None = None
    name: StrictStr | None = None
    permissions: list[CreatePermissionRequest] | None = None
    scheduling: CreateSchedulingRequest | None = None
