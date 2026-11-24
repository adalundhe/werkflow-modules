from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_setup_execution_details import LightsailSetupExecutionDetails
from .lightsail_setup_history_resource import LightsailSetupHistoryResource
from .lightsail_setup_request import LightsailSetupRequest


class LightsailSetupHistory(BaseModel):
    operationId: StrictStr | None = None
    request: LightsailSetupRequest | None = None
    resource: LightsailSetupHistoryResource | None = None
    executionDetails: list[LightsailSetupExecutionDetails] | None = None
    status: StrictStr | None = None
