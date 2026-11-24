from __future__ import annotations
from pydantic import BaseModel
from .io_t_aws_job_abort_criteria import IoTAwsJobAbortCriteria


class IoTAwsJobAbortConfig(BaseModel):
    abortCriteriaList: list[IoTAwsJobAbortCriteria]
