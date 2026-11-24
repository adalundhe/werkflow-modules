from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_amazon_q_settings import SageMakerAmazonQSettings
from .sage_maker_docker_settings import SageMakerDockerSettings
from .sage_maker_r_studio_server_pro_domain_settings import SageMakerRStudioServerProDomainSettings
from .sage_maker_trusted_identity_propagation_settings import SageMakerTrustedIdentityPropagationSettings
from .sage_maker_unified_studio_settings import SageMakerUnifiedStudioSettings


class SageMakerDomainSettings(BaseModel):
    SecurityGroupIds: list[StrictStr] | None = None
    RStudioServerProDomainSettings: SageMakerRStudioServerProDomainSettings | None = None
    ExecutionRoleIdentityConfig: StrictStr | None = None
    TrustedIdentityPropagationSettings: SageMakerTrustedIdentityPropagationSettings | None = None
    DockerSettings: SageMakerDockerSettings | None = None
    AmazonQSettings: SageMakerAmazonQSettings | None = None
    UnifiedStudioSettings: SageMakerUnifiedStudioSettings | None = None
    IpAddressType: StrictStr | None = None
