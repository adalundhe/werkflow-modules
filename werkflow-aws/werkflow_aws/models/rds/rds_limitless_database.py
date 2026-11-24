from __future__ import annotations
from pydantic import BaseModel, StrictFloat
from .rds_limitless_database_status import RDSLimitlessDatabaseStatus


class RDSLimitlessDatabase(BaseModel):
    Status: RDSLimitlessDatabaseStatus | None = None
    MinRequiredACU: StrictFloat | None = None
