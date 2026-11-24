from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_elastic_load_balancing import EKSElasticLoadBalancing
from .eks_ip_family import EKSIpFamily


class EKSKubernetesNetworkConfigRequest(BaseModel):
    serviceIpv4Cidr: StrictStr | None = None
    ipFamily: EKSIpFamily | None = None
    elasticLoadBalancing: EKSElasticLoadBalancing | None = None
