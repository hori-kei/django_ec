from .base import *

# 本番環境用設定

DEBUG = False

ALLOWED_HOSTS = ["*"]


STORAGES["staticfiles"]["BACKEND"] = "whitenoise.storage.CompressedManifestStaticFilesStorage"
