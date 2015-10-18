import os

IS_DEBUG = bool(int(os.environ.get('GD_DEBUG', '0')))
NO_THREADS = bool(int(os.environ.get('GD_NOTHREADS', '1')))
DO_LOG_FUSE_MESSAGES = bool(int(os.environ.get('GD_DO_LOG_FUSE_MESSAGES', '0')))
