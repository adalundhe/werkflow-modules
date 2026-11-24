from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .issue_type_screen_scheme import IssueTypeScreenScheme


class IssueTypeScreenSchemesProjects(BaseModel):
    issueTypeScreenScheme: IssueTypeScreenScheme | None = None
    projectIds: list[StrictStr] | None = None
