from pydantic import (
    BaseModel,
    StrictBool
)
from typing import (
    List,
    Optional
)
from .build_argument import BuildArgument
from .build_cache_image import BuildCacheImage
from .build_envar import BuildEnvar
from .build_host import BuildHost
from .build_label import BuildLabel
from .build_secret import BuildSecret


class BuildOptions(BaseModel):
    add_host: Optional[BuildHost]
    build_arguments: Optional[List[BuildArgument]]
    build_envars: Optional[List[BuildEnvar]]
    build_labels: Optional[List[BuildLabel]]
    build_secrets: Optional[List[BuildSecret]]
    cache_from: Optional[List[BuildCacheImage]]
    compress: StrictBool=False
    force_rm: StrictBool=False
    no_cache: StrictBool=False
    platform: Optional[StrictBool]
    pull: StrictBool=False
    quiet: StrictBool=False
    rm: StrictBool=False
    squash: StrictBool=False

    def to_string(self) -> str:

        options = ''

        if self.add_host:

            host = self.add_host.to_string()

            options = f'--add-host {host}'

        if self.build_arguments and len(self.build_arguments) > 0:
            
            arguments: List[str] = []

            for argument in self.build_arguments:
                argument_kv = argument.to_string()
                arguments.append(
                    f'--build-arg {argument_kv}'
                )

            arguments = ' '.join(arguments)      
            options = f'{options} {arguments}'

        if self.build_envars and len(self.build_envars) > 0:

            arguments: List[str] = []

            for argument in self.build_envars:
                argument_kv = argument.to_string()
                arguments.append(
                    f'--env {argument_kv}'
                )

            arguments = ' '.join(arguments)
            options = f'{options} {arguments}'

        if self.build_labels and len(self.build_labels) > 0:

            labels: List[str] = []

            for label in self.build_labels:
                label_kv = label.to_string()
                labels.append(
                    f'--label {label_kv}'
                )

            labels = ' '.join(labels)
            options = f'{options} {labels}'

        if self.build_secrets and len(self.build_secrets) > 0:

            secrets: List[str] = []

            for secret in self.build_secrets:
                secret_data = secret.to_string()
                secrets.append(
                    f'--secret {secret_data}'
                )

            secrets = ' '.join(secrets)
            options = f'{options} {secrets}'

        if self.cache_from and len(self.cache_from) > 0:

            cache_images: List[str] = []

            for cache_image in self.cache_from:
                cache_option = cache_image.to_string()
                cache_images.append(
                    f'--cache-from {cache_option}'
                )

            cache_images = ' '.join(cache_images)
            options = f'{options} {cache_images}'

        if self.compress:
            options = f'{options} --compress'

        if self.force_rm:
            options = f'{options} --force-rm'
        
        if self.no_cache:
            options = f'{options} --no-cache'

        if self.platform:
            options = f'{options} --platform {self.platform}'
        
        if self.pull:
            options = f'{options} --pull'

        if self.quiet:
            options = f'{options} --quiet'

        if self.rm:
            options = f'{options} --rm'

        if self.squash:
            options = f'{options} --squash'

        return options
        


            