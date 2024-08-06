from __future__ import annotations

from typing import List, Literal

from pydantic import BaseModel, conlist

from werkflow_jira.models.requests.jira.content.inline import JiraInlineBlock
from werkflow_jira.models.requests.jira.content.marks.jira_content_mark import (
    JiraContentMark,
)

from .jira_child_attrs import MediaAttrs, TableCellAttrs, TableHeaderAttrs


class JiraChildBlock(BaseModel):
    content: conlist(JiraChildBlock | JiraInlineBlock, min_length=1)
    attrs: MediaAttrs | TableCellAttrs | TableHeaderAttrs | None = None
    type: Literal[
        "paragraph",
        "listItem",
        "media",
        "tableCell",
        "tableHeader",
        "tableRow",
        "extensionFrame",
    ] = "paragraph"
    marks: List[JiraContentMark] | None = None
