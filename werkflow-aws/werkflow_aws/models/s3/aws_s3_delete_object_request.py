from pydantic import (
    BaseModel,
    StrictStr,
    StrictBool
)


class AWSS3DeleteObjectRequest(BaseModel):
    Bucket: StrictStr
    Key: StrictStr
    MFA: StrictStr | None = None
    VersionId: StrictStr | None = None
    BypassGovernanceRetention: StrictBool | None = None
    ExpectedBucketOwner: StrictStr | None = None

