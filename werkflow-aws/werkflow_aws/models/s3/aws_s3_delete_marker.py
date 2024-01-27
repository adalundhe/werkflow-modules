import datetime
from pydantic import (
    BaseModel,
    StrictStr,
    StrictBool
)
from werkflow_aws.models.base import AWSBoto3Base
from typing import Dict, Literal


class AWSs3DeleteMarker(AWSBoto3Base):
    Owner: Dict[
        Literal[
            'DisplayName',
            'ID'
        ],
        StrictStr
    ]
    Key: StrictStr
    VersionId: StrictStr
    IsLatest: StrictBool
    LastModified: datetime.datetime