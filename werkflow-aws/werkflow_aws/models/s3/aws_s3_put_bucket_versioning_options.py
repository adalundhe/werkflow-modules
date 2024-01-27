from pydantic import (
    StrictStr
)
from typing import Literal, Optional, Dict
from werkflow_aws.models.base import AWSBoto3Base
from werkflow_aws.models.parsing import (
    convert_key_to_boto3_arg, 
    convert_key_to_boto3_arg_upper_matching,
    key_contains_patterns
)
from .aws_s3_versioning_configuration import AWSs3VersioningConfiguration


class AWSs3PutBucketVersioningOptions(AWSBoto3Base):
    checksum_algorithm: Optional[
        Literal[
            'CRC32',
            'CRC32C',
            'SHA1',
            'SHA256'
        ]
    ]=None
    mfa: Optional[StrictStr]=None
    versioning_configuration: Optional[
        AWSs3VersioningConfiguration
    ]=None
    expected_bucket_owner: Optional[StrictStr]=None

    def to_options(self):

        options = self._filtered_options_to_dict()
        
        if versioning_configuration := self.versioning_configuration:
            options['versioning_configuration'] = versioning_configuration.to_data()

        uppercased_options = {
            convert_key_to_boto3_arg_upper_matching(
                key,
                [
                    'mfa'
                ]
            ): value  for key, value in options.items() if key_contains_patterns(
                key,
                [
                    'mfa_delete'
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