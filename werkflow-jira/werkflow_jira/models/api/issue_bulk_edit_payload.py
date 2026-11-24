from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .jira_issue_fields import JiraIssueFields


class IssueBulkEditPayload(BaseModel):
    editedFieldsInput: JiraIssueFields | None = None
    selectedActions: list[StrictStr] | None = None
    selectedIssueIdsOrKeys: list[StrictStr] | None = None
    sendBulkNotification: StrictBool | None = None
