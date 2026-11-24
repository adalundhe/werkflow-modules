from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .comprehend_update_data_security_config import ComprehendUpdateDataSecurityConfig


class ComprehendUpdateFlywheelRequest(BaseModel):
    FlywheelArn: StrictStr
    ActiveModelArn: StrictStr | None = None
    DataAccessRoleArn: StrictStr | None = None
    DataSecurityConfig: ComprehendUpdateDataSecurityConfig | None = None
