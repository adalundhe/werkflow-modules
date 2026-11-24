from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_glossary_term_item import GlueGlossaryTermItem


class GlueListGlossaryTermsResponse(BaseModel):
    Items: list[GlueGlossaryTermItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
