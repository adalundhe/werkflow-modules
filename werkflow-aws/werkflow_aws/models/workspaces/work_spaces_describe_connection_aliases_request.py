from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class WorkSpacesDescribeConnectionAliasesRequest(BaseModel):
    AliasIds: list[StrictStr] | None = None
    ResourceId: StrictStr | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
