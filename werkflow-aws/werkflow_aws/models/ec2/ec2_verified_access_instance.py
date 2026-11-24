from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_model import EC2TagModel
from .ec2_verified_access_instance_custom_sub_domain import EC2VerifiedAccessInstanceCustomSubDomain
from .ec2_verified_access_trust_provider_condensed import EC2VerifiedAccessTrustProviderCondensed


class EC2VerifiedAccessInstance(BaseModel):
    VerifiedAccessInstanceId: StrictStr | None = None
    Description: StrictStr | None = None
    VerifiedAccessTrustProviders: list[EC2VerifiedAccessTrustProviderCondensed] | None = None
    CreationTime: StrictStr | None = None
    LastUpdatedTime: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    FipsEnabled: StrictBool | None = None
    CidrEndpointsCustomSubDomain: EC2VerifiedAccessInstanceCustomSubDomain | None = None
