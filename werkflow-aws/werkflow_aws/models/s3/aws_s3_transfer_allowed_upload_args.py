import datetime
from typing import Any, Dict, Literal, Optional
from pydantic import StrictStr
from werkflow_aws.models.base import AWSBoto3Base
from werkflow_aws.models.parsing import (
    convert_key_to_boto3_arg,
    convert_key_to_boto3_arg_upper_matching,
)

_UPPER_PATTERNS = ['acl', 'md5', 'crc32', 'crc32c', 'sha1', 'sha256', 'acp', 'sse', 'kms']
_SPECIAL_KEYS = {
    'acl',
    'content_md5',
    'checksum_crc32',
    'checksum_crc32c',
    'checksum_sha1',
    'checksum_sha256',
    'grant_read_acp',
    'grant_write_acp',
    'sse_customer_algorithm',
    'sse_customer_key',
    'sse_kms_key_id',
    'sse_kms_encryption_context',
}


class AWSs3TransferAllowedUploadArgs(AWSBoto3Base):
    acl: Optional[
        Literal[
            'private',
            'public-read',
            'public-read-write',
            'authenticated-read',
            'aws-exec-read',
            'bucket-owner-read',
            'bucket-owner-full-control',
        ]
    ] = None
    cache_control: Optional[StrictStr] = None
    content_disposition: Optional[StrictStr] = None
    content_encoding: Optional[StrictStr] = None
    content_language: Optional[StrictStr] = None
    content_length: Optional[int] = None
    content_md5: Optional[StrictStr] = None
    content_type: Optional[StrictStr] = None
    checksum_algorithm: Optional[Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256']] = None
    checksum_crc32: Optional[StrictStr] = None
    checksum_crc32c: Optional[StrictStr] = None
    checksum_sha1: Optional[StrictStr] = None
    checksum_sha256: Optional[StrictStr] = None
    expires: Optional[datetime.datetime] = None
    grant_full_control: Optional[StrictStr] = None
    grant_read: Optional[StrictStr] = None
    grant_read_acp: Optional[StrictStr] = None
    grant_write_acp: Optional[StrictStr] = None
    metadata: Optional[Dict[str, str]] = None
    server_side_encryption: Optional[Literal['AES256', 'aws:kms', 'aws:kms:dsse']] = None
    storage_class: Optional[
        Literal[
            'STANDARD',
            'REDUCED_REDUNDANCY',
            'STANDARD_IA',
            'ONEZONE_IA',
            'INTELLIGENT_TIERING',
            'GLACIER',
            'OUTPOSTS',
            'GLACIER_IR',
            'SNOW',
        ]
    ] = None
    website_redirect_location: Optional[StrictStr] = None
    sse_customer_algorithm: Optional[StrictStr] = None
    sse_customer_key: Optional[StrictStr] = None
    sse_kms_key_id: Optional[StrictStr] = None
    sse_kms_encryption_context: Optional[StrictStr] = None
    bucket_key_enabled: Optional[bool] = None
    tagging: Optional[StrictStr] = None
    object_lock_mode: Optional[Literal['GOVERNANCE', 'COMPLIANCE']] = None
    object_lock_retain_until_date: Optional[datetime.datetime] = None
    object_lock_legal_hold_status: Optional[Literal['ON', 'OFF']] = None
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
