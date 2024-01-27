from pydantic import (
    StrictStr,
    StrictInt,
    constr
)
from typing import Dict, List, Any, Optional, Literal
from werkflow_aws.models.base import AWSBoto3Base


class AWSs3GeneratePresignedPostOptions(AWSBoto3Base):
    fields: Optional[
        Dict[str, Any]
    ]=None
    conditions: List[
        Dict[
            Literal[
                'acl',
                'content-length-range',
                'Cache-Control',
                'Content-Type',
                'Content-Disposition',
                'Content-Encoding',
                'Expires',
                'success_action_redirect',
                'redirect',
                'success_action_status',
            ] | constr(pattern=r'^(x-amz-meta-)(.*)'),
            StrictStr | StrictInt
        ] | List[
            Literal[
                'acl',
                'content-length-range',
                'Cache-Control',
                'Content-Type',
                'Content-Disposition',
                'Content-Encoding',
                'Expires',
                'success_action_redirect',
                'redirect',
                'success_action_status',
            ] | constr(pattern=r'^(x-amz-meta-)(.*)') |
            StrictStr | StrictInt
        ]
    ]