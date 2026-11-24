from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_status_report_model import Route53StatusReportModel


class Route53HealthCheckObservationModel(BaseModel):
    Region: StrictStr | None = None
    IPAddress: StrictStr | None = None
    StatusReport: Route53StatusReportModel | None = None
