from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchDescribeDryRunProgressRequest(BaseModel):
    DomainName: StrictStr
    DryRunId: StrictStr | None = None
    LoadDryRunConfig: StrictBool | None = None
