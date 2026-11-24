from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from .issue_update_details import IssueUpdateDetails


class IssuesUpdateBean(BaseModel):
    model_config = ConfigDict(extra="allow")

    issueUpdates: list[IssueUpdateDetails] | None = None
