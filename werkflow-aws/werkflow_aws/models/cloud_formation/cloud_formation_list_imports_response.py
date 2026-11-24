from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudFormationListImportsResponse(BaseModel):
    Imports: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
