from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .device_farm_unique_problem import DeviceFarmUniqueProblem


class DeviceFarmListUniqueProblemsResponse(BaseModel):
    uniqueProblems: dict[StrictStr, list[DeviceFarmUniqueProblem]] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
