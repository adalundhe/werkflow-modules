from __future__ import annotations

from typing import List, Literal

from pydantic import (
    BaseModel,
    StrictStr,
    model_validator,
)

from werkflow_jira.models.requests.jira.content.marks import JiraContentMark

from .jira_inline_attrs import (
    EmojirAttrs,
    HardBreakAttrs,
    InlineCardAttrs,
    MentionAttrs,
)


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
    attrs: EmojirAttrs | HardBreakAttrs | InlineCardAttrs | MentionAttrs | None = None

    @model_validator(mode="after")
    def validate_text_block(self):
        if self.type != "text":
            assert self.marks is None, "Marks may only be used with a Text node."

        if self.marks:
            incompatible_mark_types = {
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
                    self.check_marks_compatible(mark, incompatible_types)

        return self

    def check_marks_compatible(
        self,
        mark_type: Literal[
            "backgroundColor",
            "border",
            "code",
            "em",
            "link",
            "strong",
            "subsup",
            "textColor",
            "underline",
        ],
        incompatible_types: List[
            Literal[
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
        ],
    ):
        matching_marks = len([mark for mark in self.marks if mark == mark_type])

        for incompatible_type in incompatible_types:
            incompatible_marks = len(
                [mark for mark in self.marks if mark.type == incompatible_type]
            )

            assert (
                matching_marks >= 0 and incompatible_marks == 0
            ), f"Cannot use Mark type {mark_type} with Mark type {incompatible_type}"
