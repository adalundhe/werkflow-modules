from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_template_alias import QuickSightTemplateAlias


class QuickSightListTemplateAliasesResponse(BaseModel):
    TemplateAliasList: list[QuickSightTemplateAlias] | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
