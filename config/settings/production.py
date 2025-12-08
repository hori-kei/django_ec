import dj_database_url

from .base import *

# 本番環境用設定

DEBUG = False

ALLOWED_HOSTS = ["*"]

# Heroku Postgres を使う
DATABASES["default"] = dj_database_url.config(
    conn_max_age=600,
    ssl_require=True,
)

STORAGES["default"]["BACKEND"] = "cloudinary_storage.storage.MediaCloudinaryStorage"

STORAGES["staticfiles"]["BACKEND"] = "whitenoise.storage.CompressedManifestStaticFilesStorage"
