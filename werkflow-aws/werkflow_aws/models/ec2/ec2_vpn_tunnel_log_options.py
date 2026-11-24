from __future__ import annotations
from pydantic import BaseModel
from .ec2_cloud_watch_log_options import EC2CloudWatchLogOptions


class EC2VpnTunnelLogOptions(BaseModel):
    CloudWatchLogOptions: EC2CloudWatchLogOptions | None = None
