from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .io_t_authorizer_description import IoTAuthorizerDescription


class IoTDescribeDefaultAuthorizerResponse(BaseModel):
    authorizerDescription: IoTAuthorizerDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
