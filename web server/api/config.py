from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    """Base application settings.
    Provides environmental constants throughout the application

    Args:
        BaseSettings (pydantic.BaseSettings): BaseSettings super
        class by pydantic
    """

    HOST: str
    PORT: int
    THREADS: int
    BYTES_SIZE: int

    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls,
                              v: Union[str,
                                       List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        """Configuration file which imports environment variables"""

        case_sensitive = True
        env_file = ".env"


settings = Settings()
