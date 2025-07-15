from pydantic_settings import BaseSettings, SettingsConfigDict


__all__ = ["env_config"]


class EnvConfig(BaseSettings):
    project_name: str

    model_config = SettingsConfigDict(env_prefix="ENV_")


env_config = EnvConfig()
