import json
from pathlib import Path
from .schemas.garden_config import GardenConfig, GardenConfigUpdate


class GardenConfigService:
    def __init__(self, filename: Path):
        self.filename = filename

    def write_config(self, new_config: GardenConfig):
        with open(self.filename, 'r') as file:
            json.dump(new_config, file)

    def get(self) -> GardenConfig:
        with open(self.filename, 'r') as file:
            config = GardenConfig(**json.load(file))
        return config

    def update(self, new_config: GardenConfigUpdate):
        config = self.get()
        new_config_dict = new_config.dict()
        for key, value in new_config_dict.items():
            if hasattr(config, key) and value is not None:
                setattr(config, key, value)
        self.write_config(config)
        return config

    @classmethod
    def get_new_instance(cls, filename: Path = Path('garden_config.json')):
        yield GardenConfigService(filename)
