from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class WorkSpacesDescribeApplicationAssociationsRequest(BaseModel):
    ApplicationId: StrictStr
    AssociatedResourceTypes: list[Literal['WORKSPACE', 'BUNDLE', 'IMAGE']]
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
