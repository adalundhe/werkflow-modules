import datetime
from pydantic import (
    StrictBool,
    StrictStr,
    StrictInt
)

from typing import Optional, Dict, Union, Literal
from werkflow_aws.models.base import AWSBoto3Options
from werkflow_aws.models.parsing import (
    convert_key_to_boto3_arg,
    convert_key_to_boto3_arg_upper_matching,
    key_contains_patterns
)


class AWSs3PutObjectOptions(AWSBoto3Options):
    acl: Union[
            Optional[Literal['private']],
            Optional[Literal['public-read']],
            Optional[Literal['public-read-write']],
            Optional[Literal['authenticated-read']],
            Optional[Literal['aws-exec-read']],
            Optional[Literal['bucket-owner-read']],
            Optional[Literal['bucket-owner-full-control']]
    ]=None
    cache_control: Optional[str]=None
    content_disposition: Optional[str]=None
    content_encoding: Optional[str]=None
    content_language: Optional[str]=None
    content_length: Optional[int]=None
    content_md5: Optional[str]=None
    content_type: Optional[str]=None
    checksum_algorithm: Union[
        Optional[Literal['CRC32']],
        Optional[Literal['CRC32C']],
        Optional[Literal['SHA1']],
        Optional[Literal['SHA256']]
    ]=None
    checksum_crc32: Optional[str]=None
    checksum_crc32c: Optional[str]=None
    checksum_sha1: Optional[str]=None
    checksum_sha256: Optional[str]=None
    expires: Optional[datetime.datetime]=None
    grant_full_control: Optional[str]=None
    grant_read: Optional[str]=None
    grant_read_acp: Optional[str]=None
    grant_write_acp: Optional[str]=None
    metadata: Optional[Dict[str, str]]=None
    server_side_encryption: Union[
        Optional[Literal['AES256']],
        Optional[Literal['aws:kms']],
        Optional[Literal['aws:kms:dsse']]
    ]=None
    storage_class: Union[
        Optional[Literal['STANDARD']],
        Optional[Literal['REDUCED_REDUNDANCY']],
        Optional[Literal['STANDARD_IA']],
        Optional[Literal['ONEZONE_IA']],
        Optional[Literal['INTELLIGENT_TIERING']],
        Optional[Literal['GLACIER']],
        Optional[Literal['DEEP_ARCHIVE']],
        Optional[Literal['OUTPOSTS']],
        Optional[Literal['GLACIER_IR']],
        Optional[Literal['SNOW']]
    ]=None
    website_redirection_location: Optional[str]=None
    sse_customer_algorithm: Optional[str]=None
    sse_customer_key: Optional[str]=None
    sse_kms_id: Optional[str]=None
    sse_kms_encryption_context: Optional[str]=None
    bucket_key_enabled: Optional[bool]=None
    tagging: Optional[str]=None
    object_lock_mode: Union[
        Optional[Literal['GOVERNANCE']],
        Optional[Literal['COMPLIANCE']]
    ]=None
    object_lock_retain_until_date: Optional[datetime.datetime]=None
    object_lock_legal_hold_status: Union[
        Optional[Literal['ON']],
        Optional[Literal['OFF']]
    ]=None
    expected_bucket_owner: Optional[str]=None

    def to_options(self):

        options = self._filtered_options_to_dict()

        uppercased_options = {
            convert_key_to_boto3_arg_upper_matching(
                key,
                [
                    'md5', 
                    'crc32',
                    'crc32c',
                    'sha1',
                    'sha256',
                    'acp',
                    'sse',
                    'kms'
                ]
            ): value  for key, value in options.items() if key_contains_patterns(
                key,
                [
                    'content_md5',
                    'checksum_crc32',
                    'checksum_crc32c',
                    'checksum_sha1',
                    'checksum_sha256',
                    'grant_read_acp',
                    'grant_write_acp',
                    'sse_customer_algorithm',
                    'sse_customer_key',
                    'sse_kms_id',
                    'sse_kms_encryption_context'
                ]
            )
        }

        parsed_options = {
            convert_key_to_boto3_arg(
                key
            ): value for key, value in options.items() if key not in uppercased_options
        }

        parsed_options.update(uppercased_options)

        return uppercased_options