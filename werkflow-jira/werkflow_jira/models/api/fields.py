from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .issue_type_details import IssueTypeDetails
from .priority import Priority
from .status_details import StatusDetails
from .time_tracking_details import TimeTrackingDetails
from .user_details import UserDetails


class Fields(BaseModel):
    assignee: UserDetails | None = None
    issueType: IssueTypeDetails | None = None
    issuetype: IssueTypeDetails | None = None
    priority: Priority | None = None
    status: StatusDetails | None = None
    summary: StrictStr | None = None
    timetracking: TimeTrackingDetails | None = None
