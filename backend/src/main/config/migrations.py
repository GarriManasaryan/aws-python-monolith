from pathlib import Path
from alembic.config import Config
from alembic import command
import os

from config.mylogger import logger

main_folder = Path(__file__).resolve().parent.parent
script_location_path = os.path.join(main_folder, 'alembic')
alembic_ini_path = os.path.join(main_folder, 'alembic.ini')


def run_migrations():
    alembic_cfg = Config(alembic_ini_path)
    alembic_cfg.set_main_option("script_location", os.path.join(script_location_path))
    command.upgrade(alembic_cfg, "head")