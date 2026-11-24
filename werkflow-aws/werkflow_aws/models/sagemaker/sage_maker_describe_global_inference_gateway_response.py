from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_global_inference_gateway_routing import SageMakerGlobalInferenceGatewayRouting


class SageMakerDescribeGlobalInferenceGatewayResponse(BaseModel):
    Arn: StrictStr | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    ExecutionRoleArn: StrictStr | None = None
    Status: StrictStr | None = None
    EndpointUrl: StrictStr | None = None
    VpcEndpointServiceName: StrictStr | None = None
    Routing: SageMakerGlobalInferenceGatewayRouting | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
