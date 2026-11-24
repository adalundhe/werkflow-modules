from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_agent_version import SageMakerAgentVersion
from .sage_maker_device_stats import SageMakerDeviceStats
from .sage_maker_edge_model_stat import SageMakerEdgeModelStat
from .sage_maker_edge_output_config import SageMakerEdgeOutputConfig


class SageMakerGetDeviceFleetReportResponse(BaseModel):
    DeviceFleetArn: StrictStr | None = None
    DeviceFleetName: StrictStr | None = None
    OutputConfig: SageMakerEdgeOutputConfig | None = None
    Description: StrictStr | None = None
    ReportGenerated: datetime.datetime | StrictStr | None = None
    DeviceStats: SageMakerDeviceStats | None = None
    AgentVersions: list[SageMakerAgentVersion] | None = None
    ModelStats: list[SageMakerEdgeModelStat] | None = None
    ResponseMetadata: dict[str, Any] | None = None
