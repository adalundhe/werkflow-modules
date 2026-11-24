from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .emr_instance_resize_policy import EMRInstanceResizePolicy


class EMRShrinkPolicy(BaseModel):
    DecommissionTimeout: StrictInt | None = None
    InstanceResizePolicy: EMRInstanceResizePolicy | None = None
