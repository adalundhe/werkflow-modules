from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceDescribeEventTopicsRequest(BaseModel):
    DirectoryId: StrictStr | None = None
    TopicNames: list[StrictStr] | None = None
