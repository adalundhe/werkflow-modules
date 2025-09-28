from pydantic import (
    BaseModel,
    StrictStr
)



class AWSS3DeleteBucketRequest(BaseModel):
    Bucket: StrictStr
    ExpectedBucketOwner: StrictStr | None = None

