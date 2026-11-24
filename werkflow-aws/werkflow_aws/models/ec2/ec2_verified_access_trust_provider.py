from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_device_options import EC2DeviceOptions
from .ec2_native_application_oidc_options import EC2NativeApplicationOidcOptions
from .ec2_oidc_options import EC2OidcOptions
from .ec2_tag_model import EC2TagModel
from .ec2_verified_access_sse_specification_response import EC2VerifiedAccessSseSpecificationResponse


class EC2VerifiedAccessTrustProvider(BaseModel):
    VerifiedAccessTrustProviderId: StrictStr | None = None
    Description: StrictStr | None = None
    TrustProviderType: StrictStr | None = None
    UserTrustProviderType: StrictStr | None = None
    DeviceTrustProviderType: StrictStr | None = None
    OidcOptions: EC2OidcOptions | None = None
    DeviceOptions: EC2DeviceOptions | None = None
    PolicyReferenceName: StrictStr | None = None
    CreationTime: StrictStr | None = None
    LastUpdatedTime: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    SseSpecification: EC2VerifiedAccessSseSpecificationResponse | None = None
    NativeApplicationOidcOptions: EC2NativeApplicationOidcOptions | None = None
