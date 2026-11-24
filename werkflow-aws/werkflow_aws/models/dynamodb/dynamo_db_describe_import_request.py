from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBDescribeImportRequest(BaseModel):
    ImportArn: StrictStr
