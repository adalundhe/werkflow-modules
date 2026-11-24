from __future__ import annotations

from typing import Dict, List, Literal

from pydantic import BaseModel, StrictStr, model_validator

from werkflow_jira.models.requests.jira.content.marks import JiraContentMark

from .jira_inline_attrs import (
    EmojiAttrs,
    HardBreakAttrs,
    InlineCardAttrs,
    MentionAttrs,
)

MarkType = Literal[
    "backgroundColor",
    "border",
    "code",
    "em",
    "link",
    "strong",
    "subsup",
    "textColor",
    "underline",
]


class JiraInlineBlock(BaseModel):
    text: StrictStr | None = None
    type: Literal[
        "emoji",
        "hardBreak",
        "inlineCard",
        "mention",
        "text",
        "mediaInline",
    ] = "text"
    marks: List[JiraContentMark] | None = None
    attrs: EmojiAttrs | HardBreakAttrs | InlineCardAttrs | MentionAttrs | None = None

    @model_validator(mode="after")
    def validate_text_block(self) -> JiraInlineBlock:
        if self.type != "text":
            assert self.marks is None, "Marks may only be used with a Text node."

        if self.marks:
            incompatible_mark_types: Dict[MarkType, List[MarkType]] = {
                "backgroundColor": ["code"],
                "textColor": ["code", "link"],
                "code": [
                    "backgroundColor",
                    "border",
                    "em",
                    "strong",
                    "subsup",
                    "textColor",
                    "underline",
                ],
            }

            for mark in self.marks:
                if incompatible_types := incompatible_mark_types.get(mark.type):
                    self.check_marks_compatible(mark.type, incompatible_types)

        return self

    def check_marks_compatible(
        self,
        mark_type: MarkType,
        incompatible_types: List[MarkType],
    ) -> None:
        if not self.marks:
            return

        matching_marks = len([mark for mark in self.marks if mark.type == mark_type])
        if matching_marks == 0:
            return

        for incompatible_type in incompatible_types:
            incompatible_marks = len(
                [mark for mark in self.marks if mark.type == incompatible_type]
            )

            assert (
                incompatible_marks == 0
            ), f"Cannot use Mark type {mark_type} with Mark type {incompatible_type}"
