from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .compute_optimizer_metric_source import ComputeOptimizerMetricSource


class ComputeOptimizerLicenseConfiguration(BaseModel):
    numberOfCores: StrictInt | None = None
    instanceType: StrictStr | None = None
    operatingSystem: StrictStr | None = None
    licenseEdition: StrictStr | None = None
    licenseName: StrictStr | None = None
    licenseModel: StrictStr | None = None
    licenseVersion: StrictStr | None = None
    metricsSource: list[ComputeOptimizerMetricSource] | None = None
