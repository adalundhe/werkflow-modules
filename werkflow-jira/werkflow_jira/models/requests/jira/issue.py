import datetime
from typing import List

from pydantic import BaseModel, ConfigDict, StrictStr

from .content import JiraTopLevelBlock


class Issue(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    summary: StrictStr
    issue_type: StrictStr
    description: List[JiraTopLevelBlock]
    priority: StrictStr
    reporter: StrictStr | None = None
    project: StrictStr
    assignee: StrictStr | None = None
    labels: List[StrictStr] | None = None
    due_date: datetime.datetime | datetime.date | None = None
    parent_issue: StrictStr | None = None
