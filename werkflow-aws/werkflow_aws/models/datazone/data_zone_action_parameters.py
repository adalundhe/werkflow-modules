from __future__ import annotations
from pydantic import BaseModel
from .data_zone_aws_console_link_parameters import DataZoneAwsConsoleLinkParameters


class DataZoneActionParameters(BaseModel):
    awsConsoleLink: DataZoneAwsConsoleLinkParameters | None = None
