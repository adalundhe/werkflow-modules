from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .emr_step import EMRStep


class EMRDescribeStepResponse(BaseModel):
    Step: EMRStep | None = None
    ResponseMetadata: dict[str, Any] | None = None
