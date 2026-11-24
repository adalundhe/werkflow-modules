from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_hsm_hsm import CloudHSMHsm


class CloudHSMCreateHsmResponse(BaseModel):
    Hsm: CloudHSMHsm | None = None
    ResponseMetadata: dict[str, Any] | None = None
