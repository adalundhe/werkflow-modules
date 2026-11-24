from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_item_error import GlueItemError
from .glue_iterable_form_item import GlueIterableFormItem


class GlueBatchGetIterableFormsResponse(BaseModel):
    Items: list[GlueIterableFormItem] | None = None
    Errors: list[GlueItemError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
