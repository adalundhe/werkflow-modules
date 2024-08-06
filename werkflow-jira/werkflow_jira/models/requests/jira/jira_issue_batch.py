from pydantic import BaseModel, conlist

from .jira_issue import JiraIssue


class JiraIssueBatch(BaseModel):
    issueUpdates: conlist(JiraIssue, min_length=1, max_length=50)
