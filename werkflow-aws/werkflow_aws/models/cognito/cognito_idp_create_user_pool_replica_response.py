from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idp_user_pool_replica_type import CognitoIDPUserPoolReplicaType


class CognitoIDPCreateUserPoolReplicaResponse(BaseModel):
    UserPoolReplica: CognitoIDPUserPoolReplicaType | None = None
    ResponseMetadata: dict[str, Any] | None = None
