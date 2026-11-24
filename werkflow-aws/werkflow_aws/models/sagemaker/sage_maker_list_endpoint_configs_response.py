from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_endpoint_config_summary import SageMakerEndpointConfigSummary


class SageMakerListEndpointConfigsResponse(BaseModel):
    EndpointConfigs: list[SageMakerEndpointConfigSummary] | None = None
    NextToken: StrictStr | None = None
