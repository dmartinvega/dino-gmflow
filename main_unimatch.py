from main_flow import main as main_flow
from argparse import Namespace
from src.utils.plot_flow import save_flow_image_from_csv_uv_batch

import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path="configs/unimatch_flow/", config_name="02-print-flow-from-classic-cv-sidex-results")
def my_app(cfg : DictConfig) -> None:
    args_namespace = Namespace(**cfg)
    save_flow_image_from_csv_uv_batch(args_namespace.input_directory, args_namespace.output_path)
    # main_flow(config_namespace)

if __name__ == "__main__":
    my_app()