from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontConnectionGroupAssociationFilter(BaseModel):
    AnycastIpListId: StrictStr | None = None
