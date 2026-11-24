from __future__ import annotations
from pydantic import BaseModel
from .io_t_abort_criteria import IoTAbortCriteria


class IoTAbortConfig(BaseModel):
    criteriaList: list[IoTAbortCriteria] | None = None
