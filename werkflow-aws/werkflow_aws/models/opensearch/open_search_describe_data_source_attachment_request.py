from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDescribeDataSourceAttachmentRequest(BaseModel):
    id: StrictStr
    dataSourceArn: StrictStr
