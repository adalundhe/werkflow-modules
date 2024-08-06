from typing import Any, Dict, List

from pydantic import AnyHttpUrl, BaseModel, EmailStr, StrictBool, StrictInt, StrictStr


class JiraProjectInsight(BaseModel):
    lastIssueUpdatetime: StrictStr
    totalIssueCount: StrictInt


class JiraProjectCategory(BaseModel):
    description: StrictStr
    id: StrictStr
    name: StrictStr
    self: AnyHttpUrl


class JiraProject(BaseModel):
    assigneeType: StrictStr
    avatarUrl: Dict[StrictStr, StrictStr] | None = None
    components: List[Dict[StrictStr, Any]] | None = None
    description: StrictStr
    email: EmailStr | None = None
    id: StrictStr
    name: StrictStr
    insight: JiraProjectInsight | None = None
    issueTypes: List[Dict[StrictStr, Any]] | None = None
    key: StrictStr
    lead: Dict[StrictStr, Any] | None = None
    projectCategory: JiraProjectCategory | None = None
    priorerties: Dict[StrictStr, Any] | None = None
    roles: Dict[StrictStr, Any] | None = None
    self: AnyHttpUrl
    simplified: StrictBool
    style: StrictStr
    url: AnyHttpUrl | None = None
    versions: List[Any] | None = None
