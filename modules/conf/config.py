import yaml


def load():
    """Loads the configuration"""
    with open("config.yaml", "r") as f:
        config = yaml.full_load(f)

    return config
