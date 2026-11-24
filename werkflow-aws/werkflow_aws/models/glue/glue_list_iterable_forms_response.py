from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_iterable_form_list_item import GlueIterableFormListItem


class GlueListIterableFormsResponse(BaseModel):
    Items: list[GlueIterableFormListItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
