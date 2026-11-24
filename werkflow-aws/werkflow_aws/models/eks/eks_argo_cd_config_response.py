from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_argo_cd_aws_idc_config_response import EKSArgoCdAwsIdcConfigResponse
from .eks_argo_cd_network_access_config_response import EKSArgoCdNetworkAccessConfigResponse
from .eks_argo_cd_role_mapping import EKSArgoCdRoleMapping


class EKSArgoCdConfigResponse(BaseModel):
    namespace: StrictStr | None = None
    awsIdc: EKSArgoCdAwsIdcConfigResponse | None = None
    rbacRoleMappings: list[EKSArgoCdRoleMapping] | None = None
    networkAccess: EKSArgoCdNetworkAccessConfigResponse | None = None
    serverUrl: StrictStr | None = None
    endpointPrefix: StrictStr | None = None
