import datetime
from pydantic import StrictStr
from typing import Optional
from werkflow_aws.models.base import AWSBoto3Base
from werkflow_aws.models.parsing import (
    convert_key_to_boto3_arg, 
    convert_key_to_boto3_arg_upper_matching,
    key_contains_patterns
)
from typing import Optional, Literal, Dict


class AWSs3UploadPartCopyOptions(AWSBoto3Base):
    copy_source:  str | Dict[
        Literal['bucket','key','version_id'],
        str
    ]=None,
    copy_source_if_match: Optional[StrictStr]=None
    copy_source_if_modified_since: Optional[datetime.datetime]=None
    copy_source_if_none_match: Optional[StrictStr]=None
    copy_source_if_unmodified_since: Optional[datetime.datetime]=None
    copy_source_range: Optional[StrictStr]=None
    sse_customer_algorithm: Optional[StrictStr]=None
    sse_customer_key: Optional[StrictStr]=None
    copy_source_sse_customer_algorithm: Optional[StrictStr]=None
    copy_source_sse_customer_key: Optional[StrictStr]=None
    request_payer: Optional[
        Literal['requester']
    ]=None
    expected_bucket_owner: Optional[StrictStr]=None
    expected_source_bucket_owner: Optional[StrictStr]=None

    def to_options(self):
        options = self._filtered_options_to_dict()

        copy_source = options.get('copy_source')
        if isinstance(copy_source, dict):
            copy_source = {
                convert_key_to_boto3_arg(
                    key
                ): value for key, value in copy_source.items()
            }

            options['copy_source'] = copy_source

        uppercased_options = {
            convert_key_to_boto3_arg_upper_matching(
                key,
                [
                    'sse'
                ]
            ): value  for key, value in options.items() if key_contains_patterns(
                key,
                [
                    'content_md5',
                    'checksum_crc32',
                    'checksum_crc32c',
                    'checksum_sha1',
                    'checksum_sha256',
                    'sse_customer_algorithm',
                    'sse_customer_key',
                    'sse_kms_encryption_context',
                    'copy_source_sse_customer_algorithm',
                    'copy_source_sse_customer_key'
                ]
            )
        }

        parsed_options = {
            convert_key_to_boto3_arg(
                key
            ): value for key, value in options.items() if key not in uppercased_options
        }

        parsed_options.update(uppercased_options)

        return parsed_options


