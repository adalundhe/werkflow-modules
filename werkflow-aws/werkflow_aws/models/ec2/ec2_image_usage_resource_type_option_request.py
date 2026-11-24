from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ImageUsageResourceTypeOptionRequest(BaseModel):
    OptionName: StrictStr | None = None
    OptionValues: list[StrictStr] | None = None
