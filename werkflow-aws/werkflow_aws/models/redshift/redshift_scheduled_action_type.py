from __future__ import annotations
from pydantic import BaseModel
from .redshift_pause_cluster_message import RedshiftPauseClusterMessage
from .redshift_resize_cluster_message import RedshiftResizeClusterMessage
from .redshift_resume_cluster_message import RedshiftResumeClusterMessage


class RedshiftScheduledActionType(BaseModel):
    ResizeCluster: RedshiftResizeClusterMessage | None = None
    PauseCluster: RedshiftPauseClusterMessage | None = None
    ResumeCluster: RedshiftResumeClusterMessage | None = None
