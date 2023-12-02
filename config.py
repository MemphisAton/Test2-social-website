from dataclasses import dataclass
from typing import Optional

from environs import Env


@dataclass
class DatabaseConfig:
    SECRET_KEY: str


@dataclass
class Config:
    db: DatabaseConfig


def load_config(path: Optional[str]) -> Config:
    env: Env = Env()
    env.read_env(path)
    return Config(db=DatabaseConfig(SECRET_KEY=env('SECRET_KEY')))
