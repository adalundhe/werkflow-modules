from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_glossary_item import GlueGlossaryItem


class GlueListGlossariesResponse(BaseModel):
    Items: list[GlueGlossaryItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
