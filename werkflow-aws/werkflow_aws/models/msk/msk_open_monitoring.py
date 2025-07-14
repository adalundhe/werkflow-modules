from pydantic import BaseModel
from .msk_prometheus import MSKPrometheus


class MSKOpenMonitoring(BaseModel):
    Prometheus: MSKPrometheus