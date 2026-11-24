from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBListTagsOfResourceRequest(BaseModel):
    ResourceArn: StrictStr
    NextToken: StrictStr | None = None
