from pydantic import (
    StrictStr
)
from werkflow_aws.models.base import AWSBoto3Base


class AWSs3Tag(AWSBoto3Base):
    key: StrictStr
    value: StrictStr