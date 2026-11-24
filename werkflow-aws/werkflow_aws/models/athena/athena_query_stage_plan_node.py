from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaQueryStagePlanNode(BaseModel):
    Name: StrictStr | None = None
    Identifier: StrictStr | None = None
    Children: list[AthenaQueryStagePlanNode] | None = None
    RemoteSources: list[StrictStr] | None = None
