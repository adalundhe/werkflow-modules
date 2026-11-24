from __future__ import annotations
from typing import Any, Literal
from pydantic import BaseModel


class AWSS3GetBucketRequestPaymentResponse(BaseModel):
    Payer: Literal['Requester', 'BucketOwner'] | None = None
    ResponseMetadata: dict[str, Any] | None = None
