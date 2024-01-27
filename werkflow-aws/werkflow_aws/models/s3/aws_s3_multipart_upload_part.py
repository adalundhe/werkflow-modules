from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt
)
from werkflow_aws.models.base import AWSBoto3Base
from werkflow_aws.models.parsing import (
    convert_key_to_boto3_arg, 
    convert_key_to_boto3_arg_upper_matching,
    key_contains_patterns
)
from typing import Optional


class AWSs3MultipartUploadPart(AWSBoto3Base):
    checksum_crc32: Optional[StrictStr]=None
    checksum_crc32c: Optional[StrictStr]=None
    checksum_sha1: Optional[StrictStr]=None
    checksum_sha256: Optional[StrictStr]=None
    e_tag: StrictStr
    part_number: StopIteration

    def to_options(self):
        options = self._filtered_options_to_dict()

        uppercased_options = {
            convert_key_to_boto3_arg_upper_matching(
                key,
                [
                    'crc32',
                    'crc32c',
                    'sha1',
                    'sha256',
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
                    'grant_read_acp',
                    'grant_write_acp',
                    'sse_customer_algorithm',
                    'sse_customer_key',
                    'sse_kms_encryption_context'
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

