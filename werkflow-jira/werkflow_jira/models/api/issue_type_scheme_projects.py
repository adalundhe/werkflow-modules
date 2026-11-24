from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .issue_type_scheme import IssueTypeScheme


class IssueTypeSchemeProjects(BaseModel):
    issueTypeScheme: IssueTypeScheme | None = None
    projectIds: list[StrictStr] | None = None
