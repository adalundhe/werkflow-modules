from pydantic import (
    StrictStr,
    StrictInt
)
from werkflow_aws.models.base import AWSBoto3Base
from typing import Dict, Any, Optional


class AWSs3GeneratePresignedURLOptions(AWSBoto3Base):
    params: Optional[Dict[StrictStr, Any]]=None
    expires_in: Optional[StrictInt]=None
    http_method: Optional[StrictStr]=None