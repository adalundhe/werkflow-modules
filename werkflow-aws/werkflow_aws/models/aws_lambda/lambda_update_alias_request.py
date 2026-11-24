from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_alias_routing_configuration import LambdaAliasRoutingConfiguration


class LambdaUpdateAliasRequest(BaseModel):
    FunctionName: StrictStr
    Name: StrictStr
    FunctionVersion: StrictStr | None = None
    Description: StrictStr | None = None
    RoutingConfig: LambdaAliasRoutingConfiguration | None = None
    RevisionId: StrictStr | None = None
