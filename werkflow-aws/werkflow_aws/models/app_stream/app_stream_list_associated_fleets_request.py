from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamListAssociatedFleetsRequest(BaseModel):
    StackName: StrictStr
    NextToken: StrictStr | None = None
