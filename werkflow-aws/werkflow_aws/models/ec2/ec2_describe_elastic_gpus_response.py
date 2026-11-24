from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_elastic_gpus import EC2ElasticGpus


class EC2DescribeElasticGpusResponse(BaseModel):
    ElasticGpuSet: list[EC2ElasticGpus] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
