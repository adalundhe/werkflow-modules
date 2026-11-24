from __future__ import annotations
from pydantic import BaseModel
from .ec2_cloud_watch_log_options_specification import EC2CloudWatchLogOptionsSpecification


class EC2VpnTunnelLogOptionsSpecification(BaseModel):
    CloudWatchLogOptions: EC2CloudWatchLogOptionsSpecification | None = None
