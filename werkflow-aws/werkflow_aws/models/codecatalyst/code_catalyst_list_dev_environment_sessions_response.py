from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_catalyst_dev_environment_session_summary import CodeCatalystDevEnvironmentSessionSummary


class CodeCatalystListDevEnvironmentSessionsResponse(BaseModel):
    items: list[CodeCatalystDevEnvironmentSessionSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
