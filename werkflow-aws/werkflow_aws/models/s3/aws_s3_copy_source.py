from pydantic import (
    StrictStr
)
from werkflow_aws.models.base import AWSBoto3Base


class AWSs3CopySource(AWSBoto3Base):
    Bucket: StrictStr
    Key: StrictStr
    VersionId: StrictStr