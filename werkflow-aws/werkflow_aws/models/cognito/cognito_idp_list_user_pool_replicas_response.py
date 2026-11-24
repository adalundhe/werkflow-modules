from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_user_pool_replica_type import CognitoIDPUserPoolReplicaType


class CognitoIDPListUserPoolReplicasResponse(BaseModel):
    UserPoolReplicas: list[CognitoIDPUserPoolReplicaType] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
