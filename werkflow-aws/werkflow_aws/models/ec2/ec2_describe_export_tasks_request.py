from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeExportTasksRequest(BaseModel):
    Filters: list[EC2FilterModel] | None = None
    ExportTaskIds: list[StrictStr] | None = None
