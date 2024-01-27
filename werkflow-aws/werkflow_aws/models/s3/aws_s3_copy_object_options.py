import datetime
from pydantic import (
    StrictStr,
    StrictBool
)
from typing import Literal, Optional, Dict
from werkflow_aws.models.base import AWSBoto3Base
from werkflow_aws.models.parsing import (
    convert_key_to_boto3_arg, 
    convert_key_to_boto3_arg_upper_matching,
    key_contains_patterns
)


class AWSs3CopyObjectOptions(AWSBoto3Base):
    acl: Optional[
        Literal[
            'private',
            'public-read',
            'public-read-write',
            'authenticated-read',
            'aws-exec-read',
            'bucket-owner-read',
            'bucket-owner-full-control'
        ]
    ]=None
    cache_control: Optional[StrictStr]=None
    checksum_algorithm: Optional[
        Literal[
            'CRC32',
            'CRC32C',
            'SHA1',
            'SHA256'
        ]
    ]=None
    content_disposition: Optional[StrictStr]=None
    content_encoding: Optional[StrictStr]=None
    content_language: Optional[StrictStr]=None
    content_type: Optional[StrictStr]=None
    copy_source_if_match: Optional[StrictStr]=None
    copy_source_if_modified_since: Optional[datetime.datetime]=None
    copy_source_if_none_match: Optional[StrictStr]=None
    copy_source_if_unmodified_since: Optional[datetime.datetime]=None
    expires: Optional[datetime.datetime]=None
    grant_full_control: Optional[StrictStr]=None
    grant_read: Optional[StrictStr]=None
    grant_read_acp: Optional[StrictStr]=None
    grant_write_acp: Optional[StrictStr]=None
    metadata: Optional[Dict[StrictStr, StrictStr]]=None
    metadata_directive: Optional[
        Literal['COPY', 'REPLACE']
    ]=None
    tagging_directive: Optional[
        Literal['COPY', 'REPLACE']
    ]=None
    server_side_encryption: Optional[
        Literal[
            'AES256',
            'aws:kms',
            'aws:kms:dsse'
        ]
    ]=None
    storage_class: Optional[
        Literal[
            'STANDARD',
            'REDUCED_REDUNDANCY',
            'STANDARD_IA',
            'ONEZONE_IA',
            'INTELLIGENT_TIERING',
            'GLACIER',
            'DEEP_ARCHIVE',
            'OUTPOSTS',
            'GLACIER_IR',
            'SNOW',
            'EXPRESS_ONEZONE'
        ]
    ]=None
    website_redirect_location: Optional[StrictStr]=None
    sse_customer_algorithm: Optional[StrictStr]=None
    sse_customer_key: Optional[StrictStr]=None
    sse_kms_key_id: Optional[StrictStr]=None
    sse_kms_encryption_context: Optional[StrictStr]=None
    bucket_key_enabled: Optional[StrictBool]=None
    copy_source_sse_customer_algorithm: Optional[StrictStr]=None
    copy_source_sse_customer_key: Optional[StrictStr]=None
    request_payer: Optional[
        Literal['requester']
    ]=None
    tagging: Optional[StrictStr]=None
    object_lock_mode: Optional[
        Literal['GOVERNANCE', 'COMPLIANCE']
    ]=None
    object_lock_retain_until_date: Optional[datetime.datetime]=None
    object_lock_legal_hold_status: Optional[
        Literal['ON', 'OFF']
    ]=None
    expected_bucket_owner: Optional[StrictStr]=None
    expected_source_bucket_owner: Optional[StrictStr]=None

    def to_options(self):

        options = self._filtered_options_to_dict()

        uppercased_options = {
            convert_key_to_boto3_arg_upper_matching(
                key,
                [
                    'acl',
                    'acp',
                    'crc32',
                    'crc32c',
                    'kms',
                    'sha1',
                    'sha256',
                    'sse'
                ]
            ): value  for key, value in options.items() if key_contains_patterns(
                key,
                [
                    'acl',
                    'grant_read_acp',
                    'grant_write_acp',
                    'sse_customer_algorithm',
                    'sse_customer_key',
                    'sse_kms_key_id',
                    'sse_kms_encryption_context',
                    'copy_source_sse_customer_algorithm',
                    'copy_source_sse_customer_key'
                ]
            )
        }


        parsed_options = {
            convert_key_to_boto3_arg(
                key
            ): value for key, value in options.items()
        }

        parsed_options.update(uppercased_options)

        return parsed_options