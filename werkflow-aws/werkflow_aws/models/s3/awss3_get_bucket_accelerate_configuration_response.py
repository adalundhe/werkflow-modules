from __future__ import annotations
from typing import Any, Literal
from pydantic import BaseModel


class AWSS3GetBucketAccelerateConfigurationResponse(BaseModel):
    Status: Literal['Enabled', 'Suspended'] | None = None
    RequestCharged: Literal['requester'] | None = None
    ResponseMetadata: dict[str, Any] | None = None
