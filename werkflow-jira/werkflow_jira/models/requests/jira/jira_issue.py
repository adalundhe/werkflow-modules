from __future__ import annotations

import datetime
from typing import Any, Dict, List, Literal

from pydantic import (
    BaseModel,
    FutureDate,
    StrictStr,
    conlist,
)

from .content import JiraChildBlock, JiraInlineBlock, JiraTopLevelBlock


class JiraIssueDescription(BaseModel):
    content: conlist(
        JiraTopLevelBlock | JiraInlineBlock | JiraChildBlock,
        min_length=1,
    )
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
    assignee: JiraIssueAssignee
    description: JiraIssueDescription
    issuetype: JiraIssueType
    duedate: FutureDate | None = None
    labels: List[StrictStr] | None = None
    parent: JiraIssueParent | None = None
    priority: JiraIssuePriority | None = None
    project: JiraIssueProject
    reporter: JiraIssueReporter
    summary: StrictStr


class JiraIssue(BaseModel):
    fields: JiraIssueFields
    update: Dict[StrictStr, Any] = {}


JiraIssueDict = Dict[
    Literal[
        "summary",
        "issue_type",
        "description",
        "priority",
        "reporter",
        "project",
        "assignee",
        "labels",
        "due_date",
        "parent_issue",
    ],
    str | list[str] | datetime.datetime | list[JiraTopLevelBlock],
]
