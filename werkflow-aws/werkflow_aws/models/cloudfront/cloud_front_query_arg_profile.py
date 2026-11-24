from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontQueryArgProfile(BaseModel):
    QueryArg: StrictStr | None = None
    ProfileId: StrictStr | None = None
