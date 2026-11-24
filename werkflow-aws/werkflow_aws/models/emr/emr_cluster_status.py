from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_cluster_state_change_reason import EMRClusterStateChangeReason
from .emr_cluster_timeline import EMRClusterTimeline
from .emr_error_detail import EMRErrorDetail


class EMRClusterStatus(BaseModel):
    State: StrictStr | None = None
    StateChangeReason: EMRClusterStateChangeReason | None = None
    Timeline: EMRClusterTimeline | None = None
    ErrorDetails: list[EMRErrorDetail] | None = None
