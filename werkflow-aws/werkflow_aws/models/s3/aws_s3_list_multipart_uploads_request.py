from pydantic import (
    StrictStr,
    StrictInt
)

from werkflow_aws.models.base import AWSBoto3Base


class AWSs3ListMultipartUploadsRequest(AWSBoto3Base):
    Bucket: StrictStr
    Delimiter: StrictStr | None=None
    EncodingType: StrictStr | None=None
    KeyMarker: StrictStr | None=None
    MaxUploads: StrictInt | None=None
    Prefix: StrictStr | None=None
    UploadIdMarker: StrictStr | None=None
    ExpectedBucketOwner: StrictStr | None=None
    RequestPayer: StrictStr | None = None
