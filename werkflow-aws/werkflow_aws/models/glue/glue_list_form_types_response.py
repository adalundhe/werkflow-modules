from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_form_type_item import GlueFormTypeItem


class GlueListFormTypesResponse(BaseModel):
    Items: list[GlueFormTypeItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
