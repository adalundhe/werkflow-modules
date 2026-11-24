from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_alias_routing_configuration import LambdaAliasRoutingConfiguration


class LambdaCreateAliasRequest(BaseModel):
    FunctionName: StrictStr
    Name: StrictStr
    FunctionVersion: StrictStr
    Description: StrictStr | None = None
    RoutingConfig: LambdaAliasRoutingConfiguration | None = None
