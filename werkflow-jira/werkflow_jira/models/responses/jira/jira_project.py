from typing import Any, Dict, List

from pydantic import (
    AliasChoices,
    AnyHttpUrl,
    BaseModel,
    Field,
    StrictBool,
    StrictInt,
    StrictStr,
)


class JiraProjectInsight(BaseModel):
    lastIssueUpdateTime: StrictStr | None = Field(
        default=None,
        validation_alias=AliasChoices("lastIssueUpdateTime", "lastIssueUpdatetime"),
    )
    totalIssueCount: StrictInt


class JiraProjectCategory(BaseModel):
    description: StrictStr | None = None
    id: StrictStr
    name: StrictStr
    self: AnyHttpUrl


class JiraProject(BaseModel):
    assigneeType: StrictStr | None = None
    avatarUrls: Dict[StrictStr, StrictStr] | None = Field(
        default=None,
        validation_alias=AliasChoices("avatarUrls", "avatarUrl"),
    )
    components: List[Dict[StrictStr, Any]] | None = None
    description: StrictStr | None = None
    email: StrictStr | None = None
    id: StrictStr
    name: StrictStr
    insight: JiraProjectInsight | None = None
    issueTypes: List[Dict[StrictStr, Any]] | None = None
    key: StrictStr
    lead: Dict[StrictStr, Any] | None = None
    projectCategory: JiraProjectCategory | None = None
    properties: Dict[StrictStr, Any] | None = Field(
        default=None,
        validation_alias=AliasChoices("properties", "priorerties"),
    )
    roles: Dict[StrictStr, Any] | None = None
    self: AnyHttpUrl
    simplified: StrictBool | None = None
    style: StrictStr | None = None
    url: AnyHttpUrl | None = None
    versions: List[Any] | None = None
