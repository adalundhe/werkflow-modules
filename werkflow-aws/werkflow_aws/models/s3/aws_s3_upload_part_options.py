from pydantic import StrictStr, StrictInt
from typing import Optional
from werkflow_aws.models.base import AWSBoto3Base
from werkflow_aws.models.parsing import (
    convert_key_to_boto3_arg, 
    convert_key_to_boto3_arg_upper_matching,
    key_contains_patterns
)
from typing import Optional, Literal


class AWSs3UploadPartOptions(AWSBoto3Base):
    content_length: Optional[StrictInt]=None
    content_md5: Optional[StrictStr]=None
    checksum_algorithm: Optional[
        Literal[
            'CRC32',
            'CRC32C',
            'SHA1',
            'SHA256'
        ]
    ]=None
    checksum_crc32: Optional[StrictStr]=None
    checksum_crc32c: Optional[StrictStr]=None
    checksum_sha1: Optional[StrictStr]=None
    checksum_sha256: Optional[StrictStr]=None
    sse_customer_algorithm: Optional[StrictStr]=None
    sse_customer_key: Optional[StrictStr]=None
    request_payer: Optional[
        Literal['requester']
    ]=None
    expected_bucket_owner: Optional[StrictStr]=None

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
                    'sse_customer_algorithm',
                    'sse_customer_key'
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


