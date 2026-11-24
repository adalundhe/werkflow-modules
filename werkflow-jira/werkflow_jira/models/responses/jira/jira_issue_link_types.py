from typing import Annotated, List

from pydantic import BaseModel, Field

from .jira_issue_link_type import JiraIssueLinkType


class JiraIssueLinkTypes(BaseModel):
    issueLinkTypes: Annotated[List[JiraIssueLinkType], Field(min_length=1)]
