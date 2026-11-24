from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudFormationDescribePublisherResponse(BaseModel):
    PublisherId: StrictStr | None = None
    PublisherStatus: StrictStr | None = None
    IdentityProvider: StrictStr | None = None
    PublisherProfile: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
