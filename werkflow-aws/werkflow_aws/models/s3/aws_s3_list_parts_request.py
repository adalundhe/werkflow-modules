from pydantic import (
    StrictStr,
    StrictInt
)
from werkflow_aws.models.base import AWSBoto3Base


class AWSs3ListPartsRequest(AWSBoto3Base):
    Bucket: StrictStr
    Key: StrictStr
    MaxParts: StrictInt | None=None
    PartNumberMarker: StrictInt | None=None
    UploadId: StrictStr
    RequestPayer: StrictStr | None=None
    ExpectedBucketOwner: StrictStr | None=None
    SSECustomerAlgorithm: StrictStr | None=None
    SSECustomerKey: StrictStr | None=None
