from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_elastic_load_balancing_model import EKSElasticLoadBalancingModel


class EKSKubernetesNetworkConfigResponseModel(BaseModel):
    serviceIpv4Cidr: StrictStr | None = None
    serviceIpv6Cidr: StrictStr | None = None
    ipFamily: StrictStr | None = None
    elasticLoadBalancing: EKSElasticLoadBalancingModel | None = None
