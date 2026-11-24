from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_built_in_slot_type_summary import LexBuiltInSlotTypeSummary


class LexListBuiltInSlotTypesResponse(BaseModel):
    builtInSlotTypeSummaries: list[LexBuiltInSlotTypeSummary] | None = None
    nextToken: StrictStr | None = None
    localeId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
