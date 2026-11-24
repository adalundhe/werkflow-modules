from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .x_ray_sampling_rate_boost import XRaySamplingRateBoost


class XRaySamplingRule(BaseModel):
    RuleName: StrictStr | None = None
    RuleARN: StrictStr | None = None
    ResourceARN: StrictStr | None = None
    Priority: StrictInt | None = None
    FixedRate: StrictFloat | StrictInt | None = None
    ReservoirSize: StrictInt | None = None
    ServiceName: StrictStr | None = None
    ServiceType: StrictStr | None = None
    Host: StrictStr | None = None
    HTTPMethod: StrictStr | None = None
    URLPath: StrictStr | None = None
    Version: StrictInt | None = None
    Attributes: dict[StrictStr, StrictStr] | None = None
    SamplingRateBoost: XRaySamplingRateBoost | None = None
