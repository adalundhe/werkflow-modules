from pydantic import BaseModel, StrictStr, StrictInt, StrictBool
from typing import Optional, List


class Check(BaseModel):
    context: StrictStr
    app_jd: StrictInt


class DismissalRestrictions(BaseModel):
    users: List[StrictStr]=[]
    teams: List[StrictStr]=[]
    apps: List[StrictStr]=[]


class BypassPullRequestAllowances(BaseModel):
    users: List[StrictStr]=[]
    teams: List[StrictStr]=[]
    apps: List[StrictStr]=[]


class Restrictions(BaseModel):
    users: List[StrictStr]=[]
    teams: List[StrictStr]=[]
    apps: List[StrictStr]=[]


class RequiredPullRequestReviews(BaseModel):
    dismissal_restrictions: Optional[DismissalRestrictions]
    require_code_owner_reviews: StrictBool
    required_approving_review_count: StrictInt
    require_last_push_approval: StrictBool
    bypass_pull_request_allowances: Optional[BypassPullRequestAllowances]


class RequiredStatusChecks(BaseModel):
    strict: StrictBool
    contexts: List[StrictStr]=[]
    checks: List[Check]=[]


class GithubBranchProtections(BaseModel):
    required_status_checks: Optional[RequiredStatusChecks]
    enforce_admins: StrictBool
    required_pull_request_reviews: RequiredPullRequestReviews
    restrictions: Optional[Restrictions]
    required_linear_history: StrictBool
    allow_deletions: StrictBool
    block_creations: StrictBool
    required_conversation_resolution: StrictBool
    lock_branch: StrictBool
    allow_fork_syncing: StrictBool

