from __future__ import annotations

import datetime
from typing import Annotated, Any, Dict, List, Literal

from pydantic import (
    BaseModel,
    Field,
    StrictStr,
    field_serializer,
)

from .content import JiraChildBlock, JiraInlineBlock, JiraTopLevelBlock


class JiraIssueDescription(BaseModel):
    content: Annotated[
        List[JiraTopLevelBlock | JiraInlineBlock | JiraChildBlock],
        Field(min_length=1),
    ]
    type: Literal["doc"] = "doc"
    version: Literal[1] = 1


class JiraIssueAssignee(BaseModel):
    id: StrictStr


class JiraIssueParent(BaseModel):
    key: StrictStr


class JiraIssuePriority(BaseModel):
    id: StrictStr


class JiraIssueReporter(BaseModel):
    id: StrictStr


class JiraIssueProject(BaseModel):
    id: StrictStr


class JiraIssueType(BaseModel):
    id: StrictStr


class JiraIssueFields(BaseModel):
    assignee: JiraIssueAssignee | None = None
    description: JiraIssueDescription
    issuetype: JiraIssueType
    duedate: datetime.date | datetime.datetime | StrictStr | None = None
    labels: List[StrictStr] | None = None
    parent: JiraIssueParent | None = None
    priority: JiraIssuePriority | None = None
    project: JiraIssueProject
    reporter: JiraIssueReporter | None = None
    summary: StrictStr

    @field_serializer("duedate")
    def serialize_duedate(
        self,
        value: datetime.date | datetime.datetime | str | None,
    ) -> str | None:
        if value is None:
            return None
        if isinstance(value, datetime.datetime):
            return value.date().isoformat()
        if isinstance(value, datetime.date):
            return value.isoformat()
        return value


class JiraIssue(BaseModel):
    fields: JiraIssueFields
    update: Dict[StrictStr, Any] = Field(default_factory=dict)
