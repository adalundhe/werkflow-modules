from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .io_t_http_url_destination_properties import IoTHttpUrlDestinationProperties
from .io_t_influx_db_destination_properties import IoTInfluxDBDestinationProperties
from .io_t_vpc_destination_properties import IoTVpcDestinationProperties


class IoTTopicRuleDestination(BaseModel):
    arn: StrictStr | None = None
    status: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    statusReason: StrictStr | None = None
    httpUrlProperties: IoTHttpUrlDestinationProperties | None = None
    vpcProperties: IoTVpcDestinationProperties | None = None
    influxDBProperties: IoTInfluxDBDestinationProperties | None = None
