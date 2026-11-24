from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DynamoDBStreamSpecificationModel(BaseModel):
    StreamEnabled: StrictBool | None = None
    StreamViewType: StrictStr | None = None
