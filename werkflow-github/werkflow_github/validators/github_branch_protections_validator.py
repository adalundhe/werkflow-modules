from typing import List, Optional

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr


class Check(BaseModel):
    context: StrictStr
    app_id: StrictInt


class DismissalRestrictions(BaseModel):
    users: List[StrictStr] = Field(default_factory=list)
    teams: List[StrictStr] = Field(default_factory=list)
    apps: List[StrictStr] = Field(default_factory=list)


class BypassPullRequestAllowances(BaseModel):
    users: List[StrictStr] = Field(default_factory=list)
    teams: List[StrictStr] = Field(default_factory=list)
    apps: List[StrictStr] = Field(default_factory=list)


class Restrictions(BaseModel):
    users: List[StrictStr] = Field(default_factory=list)
    teams: List[StrictStr] = Field(default_factory=list)
    apps: List[StrictStr] = Field(default_factory=list)


class RequiredPullRequestReviews(BaseModel):
    dismissal_restrictions: Optional[DismissalRestrictions] = None
    dismiss_stale_reviews: Optional[StrictBool] = None
    require_code_owner_reviews: StrictBool
    required_approving_review_count: StrictInt
    require_last_push_approval: StrictBool
    bypass_pull_request_allowances: Optional[BypassPullRequestAllowances] = None


class RequiredStatusChecks(BaseModel):
    strict: StrictBool
    contexts: List[StrictStr] = Field(default_factory=list)
    checks: List[Check] = Field(default_factory=list)


class GithubBranchProtections(BaseModel):
    required_status_checks: Optional[RequiredStatusChecks] = None
    enforce_admins: StrictBool
    required_pull_request_reviews: RequiredPullRequestReviews
    restrictions: Optional[Restrictions] = None
    required_linear_history: StrictBool
    allow_force_pushes: Optional[StrictBool] = None
    allow_deletions: StrictBool
    block_creations: StrictBool
    required_conversation_resolution: StrictBool
    lock_branch: StrictBool
    allow_fork_syncing: StrictBool
