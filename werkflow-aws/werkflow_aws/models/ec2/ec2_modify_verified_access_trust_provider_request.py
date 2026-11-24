from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_modify_verified_access_native_application_oidc_options import EC2ModifyVerifiedAccessNativeApplicationOidcOptions
from .ec2_modify_verified_access_trust_provider_device_options import EC2ModifyVerifiedAccessTrustProviderDeviceOptions
from .ec2_modify_verified_access_trust_provider_oidc_options import EC2ModifyVerifiedAccessTrustProviderOidcOptions
from .ec2_verified_access_sse_specification_request import EC2VerifiedAccessSseSpecificationRequest


class EC2ModifyVerifiedAccessTrustProviderRequest(BaseModel):
    VerifiedAccessTrustProviderId: StrictStr
    OidcOptions: EC2ModifyVerifiedAccessTrustProviderOidcOptions | None = None
    DeviceOptions: EC2ModifyVerifiedAccessTrustProviderDeviceOptions | None = None
    Description: StrictStr | None = None
    DryRun: StrictBool | None = None
    ClientToken: StrictStr | None = None
    SseSpecification: EC2VerifiedAccessSseSpecificationRequest | None = None
    NativeApplicationOidcOptions: EC2ModifyVerifiedAccessNativeApplicationOidcOptions | None = None
