from __future__ import annotations

from typing import List, Literal

from pydantic import (
    BaseModel,
    conlist,
)

from werkflow_jira.models.requests.jira.content.child import JiraChildBlock
from werkflow_jira.models.requests.jira.content.inline import JiraInlineBlock
from werkflow_jira.models.requests.jira.content.marks import JiraContentMark

from .jira_top_level_attrs import (
    HeadingAttrs,
    MediaSingleAttrs,
    OrderedListAttrs,
    PanelAttrs,
    ParagraphAttrs,
    TableAttrs,
)


class JiraTopLevelBlock(BaseModel):
    content: conlist(JiraChildBlock | JiraInlineBlock, min_length=1) | None = None
    type: Literal[
        "blockquote",
        "bulletList",
        "codeBlock",
        "heading",
        "mediaGroup",
        "mediaSingle",
        "orderedList",
        "panel",
        "paragraph",
        "rule",
        "table",
        "multiBodiedExtension",
    ] = "paragraph"
    attrs: (
        HeadingAttrs
        | MediaSingleAttrs
        | OrderedListAttrs
        | PanelAttrs
        | ParagraphAttrs
        | TableAttrs
        | None
    ) = None
    marks: List[JiraContentMark] | None = None
