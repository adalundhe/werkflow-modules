from __future__ import annotations
from pydantic import BaseModel
from .io_t_retry_criteria import IoTRetryCriteria


class IoTJobExecutionsRetryConfig(BaseModel):
    criteriaList: list[IoTRetryCriteria] | None = None
