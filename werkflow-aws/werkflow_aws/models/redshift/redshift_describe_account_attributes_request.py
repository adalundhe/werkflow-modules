from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDescribeAccountAttributesRequest(BaseModel):
    AttributeNames: list[StrictStr] | None = None
