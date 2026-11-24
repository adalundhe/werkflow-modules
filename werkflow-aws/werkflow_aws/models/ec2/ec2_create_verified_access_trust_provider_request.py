from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_create_verified_access_native_application_oidc_options import EC2CreateVerifiedAccessNativeApplicationOidcOptions
from .ec2_create_verified_access_trust_provider_device_options import EC2CreateVerifiedAccessTrustProviderDeviceOptions
from .ec2_create_verified_access_trust_provider_oidc_options import EC2CreateVerifiedAccessTrustProviderOidcOptions
from .ec2_tag_specification_model import EC2TagSpecificationModel
from .ec2_verified_access_sse_specification_request import EC2VerifiedAccessSseSpecificationRequest


class EC2CreateVerifiedAccessTrustProviderRequest(BaseModel):
    TrustProviderType: Literal['user', 'device']
    PolicyReferenceName: StrictStr
    UserTrustProviderType: Literal['iam-identity-center', 'oidc'] | None = None
    DeviceTrustProviderType: Literal['jamf', 'crowdstrike', 'jumpcloud'] | None = None
    OidcOptions: EC2CreateVerifiedAccessTrustProviderOidcOptions | None = None
    DeviceOptions: EC2CreateVerifiedAccessTrustProviderDeviceOptions | None = None
    Description: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
    SseSpecification: EC2VerifiedAccessSseSpecificationRequest | None = None
    NativeApplicationOidcOptions: EC2CreateVerifiedAccessNativeApplicationOidcOptions | None = None
