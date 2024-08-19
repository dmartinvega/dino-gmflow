from main_flow import main as main_flow

from argparse import Namespace

import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path="configs/unimatch_flow/", config_name="dino-enhanced-brightness")
def my_app(cfg : DictConfig) -> None:
    config_namespace = Namespace(**cfg)
    main_flow(config_namespace)

if __name__ == "__main__":
    my_app()