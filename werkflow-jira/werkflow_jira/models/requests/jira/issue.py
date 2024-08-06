import datetime
from typing import List

from pydantic import BaseModel, StrictStr

from .content import JiraTopLevelBlock


class Issue(BaseModel):
    summary: StrictStr
    issue_type: StrictStr
    description: JiraTopLevelBlock
    priority: StrictStr
    reporter: StrictStr
    project: StrictStr
    assignee: StrictStr | None = None
    labels: List[StrictStr] | None = None
    due_date: datetime.datetime
    parent_issue: StrictStr | None = None

    class Config:
        arbitrary_types_allowed=True