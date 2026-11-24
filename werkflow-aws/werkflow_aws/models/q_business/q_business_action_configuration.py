from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_action_filter_configuration import QBusinessActionFilterConfiguration


class QBusinessActionConfiguration(BaseModel):
    action: StrictStr | None = None
    filterConfiguration: QBusinessActionFilterConfiguration | None = None
