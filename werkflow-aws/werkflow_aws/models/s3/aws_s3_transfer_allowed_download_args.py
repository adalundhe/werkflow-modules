from typing import Any, Literal, Optional
from pydantic import StrictStr
from werkflow_aws.models.base import AWSBoto3Base
from werkflow_aws.models.parsing import (
    convert_key_to_boto3_arg,
    convert_key_to_boto3_arg_upper_matching,
)

_UPPER_PATTERNS = ['md5', 'crc32', 'crc32c', 'sha1', 'sha256', 'acp', 'sse', 'kms']
_SPECIAL_KEYS = {
    'sse_customer_algorithm',
    'sse_customer_key',
    'sse_customer_key_md5',
}


class AWSs3TransferAllowedDownloadArgs(AWSBoto3Base):
    checksum_mode: Optional[Literal['ENABLED', 'DISABLED']] = None
    version_id: Optional[StrictStr] = None
    sse_customer_algorithm: Optional[StrictStr] = None
    sse_customer_key: Optional[StrictStr] = None
    sse_customer_key_md5: Optional[StrictStr] = None
    request_payer: Optional[Literal['requester']] = None
    expected_bucket_owner: Optional[StrictStr] = None

    def to_data(self) -> dict[str, Any]:
        options = self._filtered_options_to_dict()
        parsed: dict[str, Any] = {}
        for key, value in options.items():
            if key in _SPECIAL_KEYS:
                boto_key = convert_key_to_boto3_arg_upper_matching(key, _UPPER_PATTERNS)
            else:
                boto_key = convert_key_to_boto3_arg(key)
            parsed[boto_key] = value
        return parsed

    to_options = to_data
