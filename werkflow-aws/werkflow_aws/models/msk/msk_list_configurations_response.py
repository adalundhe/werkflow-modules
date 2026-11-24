from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_configuration import MSKConfiguration


class MSKListConfigurationsResponse(BaseModel):
    Configurations: list[MSKConfiguration] | None = None
    NextToken: StrictStr | None = None
