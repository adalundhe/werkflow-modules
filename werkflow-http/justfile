requirements_path := "requirements.txt"
profile := "prod"
region := "us-east-1"
base_path := invocation_directory()


blueprint *ARGS:
    blueprint create {{ARGS}} --path {{base_path}}


setup-venv venv_path requirements_path=requirements_path:
    #! /usr/bin/env bash
    python -m venv {{venv_path}}

    if [[ -e {{requirements_path}} ]]; then
        source {{venv_path}}/bin/activate && \
        pip install {{requirements_path}}
    fi

create-werkflow name *ARGS:
    #! /usr/bin/env bash
    just setup-venv ".{{name}}" && \
    source .{{name}}/bin/activate && \
    pip install --quiet poetry && \
    poetry init -q --name={{name}} \

    blueprint create {{ARGS}} --path {{base_path}} --name {{name}} --template werkflow

update:
    rm -rf "$HOME/.cache/nix" && \
    rm -rf "$HOME/justfile" && \
    nix develop "github:scorbettum/local-dev"
    echo "Please reopen your terminal."

remove:
    sed -i 's/nix develop \"github:scorbettum\/local-dev\"//g' "$HOME/.zshrc"
    sed -i 's/source \"$HOME\/.devenv\/bin\/activate\"//g' "$HOME/.zshrc"
    sed -i 's/source \"$HOME\/.devenv\/bin\/activate\"//g' "$HOME/.zshrc"
    sed -i 's/eval \"$(direnv hook zsh)\"//g' "$HOME/.zshrc"
    rm -rf "$HOME/.cache/nix"
    rm -rf "$HOME/justfile"
    echo "Please reopen your terminal."

aws-login profile=profile region=region:
    aws-login {{profile}} {{region}}


container *ARGS:
    dcon {{ARGS}}
