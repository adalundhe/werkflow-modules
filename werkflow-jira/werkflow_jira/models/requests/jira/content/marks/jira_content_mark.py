from __future__ import annotations

from typing import Dict, Literal, Union

from pydantic import BaseModel, model_validator

from .jira_content_mark_attrs import (
    BackgroundColorMarkAttrs,
    LinkMarkAttrs,
    SubSupMarkAttrs,
    TextColorAttrs,
)


class JiraContentMark(BaseModel):
    type: Literal[
        "backgroundColor",
        "border",
        "code",
        "em",
        "link",
        "strong",
        "subsup",
        "textColor",
        "underline",
    ] = "strong"
    attrs: (
        BackgroundColorMarkAttrs
        | LinkMarkAttrs
        | SubSupMarkAttrs
        | TextColorAttrs
        | None
    ) = None

    @model_validator(mode="after")
    def validate_mark(self) -> JiraContentMark:
        attrs_types: Dict[
            str,
            type[
                Union[
                    BackgroundColorMarkAttrs,
                    LinkMarkAttrs,
                    SubSupMarkAttrs,
                    TextColorAttrs,
                ]
            ],
        ] = {
            "backgroundColor": BackgroundColorMarkAttrs,
            "link": LinkMarkAttrs,
            "subsup": SubSupMarkAttrs,
            "textColor": TextColorAttrs,
        }

        if mark_attrs_type := attrs_types.get(self.type):
            assert isinstance(
                self.attrs, mark_attrs_type
            ), f"Mark of type {self.type} requires attrs of type {mark_attrs_type.__name__}"

        return self
