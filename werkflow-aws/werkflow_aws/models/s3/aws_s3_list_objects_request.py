from pydantic import (
    BaseModel,
    StrictBool,
    StrictStr,
    StrictInt,
)


class AWSS3ListObjectsRequest(BaseModel):
    Bucket: StrictStr
    Delimiter: StrictStr | None = None
    EncodingType: StrictStr | None = None
    MaxKeys: StrictInt | None = None
    Prefix: StrictStr | None = None
    ContinuationToken: StrictStr | None = None
    FetchOwner: StrictBool | None = None
    StartAfter: StrictStr | None = None
    ExpectedBucketOwner: StrictStr | None = None
    OptionalObjectAttributes: list[StrictStr] | None = None