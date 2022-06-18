import yaml


def load():
    with open("config.yaml", "r") as f:
        config = yaml.full_load(f)

    return config
