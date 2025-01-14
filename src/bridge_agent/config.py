from bridge_agent.models.config import Config

config: Config

with open("config.json", "r") as f:
    config = Config.model_validate_json(f.read())

assert config is not None, "Failed to load config.json"
