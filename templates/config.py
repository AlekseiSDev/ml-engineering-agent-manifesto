from __future__ import annotations

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Project settings using Pydantic Settings.

    Environment variables take precedence over values in .env file.
    Example: PROJECT_NAME="My Awesome Project" python src/main.py
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Project Metadata
    PROJECT_NAME: str = "ml-project"
    EXPERIMENT_NAME: str = "baseline"

    # Paths
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
    DATA_DIR: Path = BASE_DIR / "data"
    MODEL_DIR: Path = BASE_DIR / "models"

    # Training Hyperparameters (examples)
    BATCH_SIZE: int = 32
    LEARNING_RATE: float = 1e-4
    EPOCHS: int = 10

    # Infrastructure
    DEVICE: str = "cuda"  # or "cpu"


# Global settings instance
settings = Settings()
