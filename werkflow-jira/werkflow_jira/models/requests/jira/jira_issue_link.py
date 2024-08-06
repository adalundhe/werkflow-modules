from typing import Dict

from pydantic import BaseModel, StrictStr

from .jira_issue import JiraIssueDescription


class JiraIssueLinkComment(BaseModel):
    body: JiraIssueDescription
    visibility: Dict[StrictStr, StrictStr] | None = None


class JiraIssueLinkKey(BaseModel):
    key: StrictStr


class JiraIssueLinkRefType(BaseModel):
    name: StrictStr


class JiraIssueLink(BaseModel):
    comment: JiraIssueLinkComment
    inwardIssue: JiraIssueLinkKey
    outwardIssue: JiraIssueLinkKey
    type: JiraIssueLinkRefType
