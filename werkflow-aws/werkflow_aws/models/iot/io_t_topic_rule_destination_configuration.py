from __future__ import annotations
from pydantic import BaseModel
from .io_t_http_url_destination_configuration import IoTHttpUrlDestinationConfiguration
from .io_t_influx_db_destination_configuration import IoTInfluxDBDestinationConfiguration
from .io_t_vpc_destination_configuration import IoTVpcDestinationConfiguration


class IoTTopicRuleDestinationConfiguration(BaseModel):
    httpUrlConfiguration: IoTHttpUrlDestinationConfiguration | None = None
    vpcConfiguration: IoTVpcDestinationConfiguration | None = None
    influxDBConfiguration: IoTInfluxDBDestinationConfiguration | None = None
