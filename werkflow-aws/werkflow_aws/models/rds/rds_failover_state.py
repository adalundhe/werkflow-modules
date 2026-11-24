from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RDSFailoverState(BaseModel):
    Status: StrictStr | None = None
    FromDbClusterArn: StrictStr | None = None
    ToDbClusterArn: StrictStr | None = None
    IsDataLossAllowed: StrictBool | None = None
