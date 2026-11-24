from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .io_t_http_url_destination_summary import IoTHttpUrlDestinationSummary
from .io_t_influx_db_destination_summary import IoTInfluxDBDestinationSummary
from .io_t_vpc_destination_summary import IoTVpcDestinationSummary


class IoTTopicRuleDestinationSummary(BaseModel):
    arn: StrictStr | None = None
    status: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    statusReason: StrictStr | None = None
    httpUrlSummary: IoTHttpUrlDestinationSummary | None = None
    vpcDestinationSummary: IoTVpcDestinationSummary | None = None
    influxDBSummary: IoTInfluxDBDestinationSummary | None = None
