from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_catalyst_dev_environment_summary import CodeCatalystDevEnvironmentSummary


class CodeCatalystListDevEnvironmentsResponse(BaseModel):
    items: list[CodeCatalystDevEnvironmentSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
