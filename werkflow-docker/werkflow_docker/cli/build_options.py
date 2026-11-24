from typing import List, Optional

from pydantic import BaseModel, StrictBool, StrictStr

from .build_argument import BuildArgument
from .build_cache_image import BuildCacheImage
from .build_envar import BuildEnvar
from .build_host import BuildHost
from .build_label import BuildLabel
from .build_secret import BuildSecret


class BuildOptions(BaseModel):
    add_host: Optional[BuildHost] = None
    build_arguments: Optional[List[BuildArgument]] = None
    build_envars: Optional[List[BuildEnvar]] = None
    build_labels: Optional[List[BuildLabel]] = None
    build_secrets: Optional[List[BuildSecret]] = None
    cache_from: Optional[List[BuildCacheImage]] = None
    compress: StrictBool = False
    force_rm: StrictBool = False
    no_cache: StrictBool = False
    platform: Optional[StrictStr] = None
    pull: StrictBool = False
    quiet: StrictBool = False
    rm: StrictBool = False
    squash: StrictBool = False

    def to_string(self) -> str:
        options: List[str] = []

        if self.add_host:
            options.append(f'--add-host {self.add_host.to_string()}')

        if self.build_arguments:
            for argument in self.build_arguments:
                options.append(f'--build-arg {argument.to_string()}')

        if self.build_envars:
            for envar in self.build_envars:
                options.append(f'--build-arg {envar.to_string()}')

        if self.build_labels:
            for label in self.build_labels:
                options.append(f'--label {label.to_string()}')

        if self.build_secrets:
            for secret in self.build_secrets:
                options.append(f'--secret {secret.to_string()}')

        if self.cache_from:
            for cache_image in self.cache_from:
                options.append(f'--cache-from {cache_image.to_string()}')

        if self.compress:
            options.append('--compress')

        if self.force_rm:
            options.append('--force-rm')

        if self.no_cache:
            options.append('--no-cache')

        if self.platform:
            options.append(f'--platform {self.platform}')

        if self.pull:
            options.append('--pull')

        if self.quiet:
            options.append('--quiet')

        if self.rm:
            options.append('--rm')

        if self.squash:
            options.append('--squash')

        return ' '.join(options)
