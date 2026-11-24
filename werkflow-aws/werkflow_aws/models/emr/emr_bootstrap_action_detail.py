from __future__ import annotations
from pydantic import BaseModel
from .emr_bootstrap_action_config import EMRBootstrapActionConfig


class EMRBootstrapActionDetail(BaseModel):
    BootstrapActionConfig: EMRBootstrapActionConfig | None = None
