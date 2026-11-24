from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationDescribePublisherRequest(BaseModel):
    PublisherId: StrictStr | None = None
