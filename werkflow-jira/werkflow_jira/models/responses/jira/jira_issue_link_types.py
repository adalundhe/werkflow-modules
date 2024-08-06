from pydantic import BaseModel, conlist

from .jira_issue_link_type import JiraIssueLinkType


class JiraIssueLinkTypes(BaseModel):
    issueLinkTypes: conlist(JiraIssueLinkType, min_length=1)
