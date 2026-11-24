from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesDescribeAccountModificationsRequest(BaseModel):
    NextToken: StrictStr | None = None
