from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_gateway_operation_error import ECSGatewayOperationError


class ECSGatewayResourceFailure(BaseModel):
    arn: StrictStr | None = None
    errors: list[ECSGatewayOperationError] | None = None
