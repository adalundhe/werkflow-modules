from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBDescribeExportRequest(BaseModel):
    ExportArn: StrictStr
