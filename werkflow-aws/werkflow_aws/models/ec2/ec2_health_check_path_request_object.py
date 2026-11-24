from __future__ import annotations
from pydantic import BaseModel
from .ec2_health_check_path_destination_request_object import EC2HealthCheckPathDestinationRequestObject
from .ec2_health_check_path_source_request_object import EC2HealthCheckPathSourceRequestObject


class EC2HealthCheckPathRequestObject(BaseModel):
    Source: EC2HealthCheckPathSourceRequestObject | None = None
    Destinations: list[EC2HealthCheckPathDestinationRequestObject] | None = None
