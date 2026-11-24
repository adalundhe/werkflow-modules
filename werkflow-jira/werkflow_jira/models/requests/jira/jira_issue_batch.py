from typing import Annotated, List

from pydantic import BaseModel, Field

from .jira_issue import JiraIssue


class JiraIssueBatch(BaseModel):
    issueUpdates: Annotated[List[JiraIssue], Field(min_length=1, max_length=50)]
