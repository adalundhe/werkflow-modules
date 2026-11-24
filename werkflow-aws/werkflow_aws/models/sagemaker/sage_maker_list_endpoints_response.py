from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_endpoint_summary import SageMakerEndpointSummary


class SageMakerListEndpointsResponse(BaseModel):
    Endpoints: list[SageMakerEndpointSummary] | None = None
    NextToken: StrictStr | None = None
