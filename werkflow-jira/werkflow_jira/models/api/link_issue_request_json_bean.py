from __future__ import annotations
from pydantic import BaseModel
from .comment import Comment
from .issue_link_type import IssueLinkType
from .linked_issue import LinkedIssue


class LinkIssueRequestJsonBean(BaseModel):
    comment: Comment | None = None
    inwardIssue: LinkedIssue | None = None
    outwardIssue: LinkedIssue | None = None
    type: IssueLinkType | None = None
