from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_elastic_gpu_health import EC2ElasticGpuHealth
from .ec2_tag_model import EC2TagModel


class EC2ElasticGpus(BaseModel):
    ElasticGpuId: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    ElasticGpuType: StrictStr | None = None
    ElasticGpuHealth: EC2ElasticGpuHealth | None = None
    ElasticGpuState: StrictStr | None = None
    InstanceId: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
