from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesDescribeWorkspaceBundlesRequest(BaseModel):
    BundleIds: list[StrictStr] | None = None
    Owner: StrictStr | None = None
    NextToken: StrictStr | None = None
