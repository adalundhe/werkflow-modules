from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_template_alias import QuickSightTemplateAlias


class QuickSightDescribeTemplateAliasResponse(BaseModel):
    TemplateAlias: QuickSightTemplateAlias | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
