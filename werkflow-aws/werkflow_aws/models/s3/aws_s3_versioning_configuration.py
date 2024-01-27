from typing import Literal, Optional
from werkflow_aws.models.base import AWSBoto3Base
from werkflow_aws.models.parsing import (
    convert_key_to_boto3_arg, 
    convert_key_to_boto3_arg_upper_matching,
    key_contains_patterns
)


class AWSs3VersioningConfiguration(AWSBoto3Base):
    mfa_delete: Optional[
        Literal['Enabled', 'Disabled']
    ]=None
    status: Optional[
        Literal['Enabled', 'Suspended']
    ]=None

    def to_options(self):

        options = self._filtered_options_to_dict()

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
