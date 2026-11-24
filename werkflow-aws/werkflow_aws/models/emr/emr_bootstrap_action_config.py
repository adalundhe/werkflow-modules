from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_script_bootstrap_action_config import EMRScriptBootstrapActionConfig


class EMRBootstrapActionConfig(BaseModel):
    Name: StrictStr | None = None
    ScriptBootstrapAction: EMRScriptBootstrapActionConfig | None = None
