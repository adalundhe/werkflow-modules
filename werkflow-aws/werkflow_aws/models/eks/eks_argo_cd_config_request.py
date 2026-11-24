from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_argo_cd_aws_idc_config_request import EKSArgoCdAwsIdcConfigRequest
from .eks_argo_cd_network_access_config_request import EKSArgoCdNetworkAccessConfigRequest
from .eks_argo_cd_role_mapping import EKSArgoCdRoleMapping


class EKSArgoCdConfigRequest(BaseModel):
    awsIdc: EKSArgoCdAwsIdcConfigRequest
    namespace: StrictStr | None = None
    rbacRoleMappings: list[EKSArgoCdRoleMapping] | None = None
    networkAccess: EKSArgoCdNetworkAccessConfigRequest | None = None
    endpointPrefix: StrictStr | None = None
