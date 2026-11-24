from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CostExplorerRedshiftInstanceDetails(BaseModel):
    Family: StrictStr | None = None
    NodeType: StrictStr | None = None
    Region: StrictStr | None = None
    CurrentGeneration: StrictBool | None = None
    SizeFlexEligible: StrictBool | None = None
