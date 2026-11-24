from __future__ import annotations
from pydantic import BaseModel
from .ec2_health_check_path_destination_response_object import EC2HealthCheckPathDestinationResponseObject
from .ec2_health_check_path_source_response_object import EC2HealthCheckPathSourceResponseObject


class EC2HealthCheckPathResponseObject(BaseModel):
    Source: EC2HealthCheckPathSourceResponseObject | None = None
    Destinations: list[EC2HealthCheckPathDestinationResponseObject] | None = None
