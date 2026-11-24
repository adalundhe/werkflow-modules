from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jira_rich_text_input import JiraRichTextInput


class JiraRichTextField(BaseModel):
    fieldId: StrictStr | None = None
    richText: JiraRichTextInput | None = None
