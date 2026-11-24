from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .macie_finding import MacieFinding


class MacieGetFindingsResponse(BaseModel):
    findings: list[MacieFinding] | None = None
    ResponseMetadata: dict[str, Any] | None = None
