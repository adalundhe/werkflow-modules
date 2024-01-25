from pydantic import BaseModel
from ..parsing import convert_key_to_boto3_arg



class AWSBoto3Options(BaseModel):

    def _filtered_options_to_dict(self):

        options = self.dict()

        return {
            key: value for key, value in options.items() if value is not None
        }

    def to_options(self):
        return {
            convert_key_to_boto3_arg(
                key
            ): value for key, value in self._filtered_options_to_dict()
        }

