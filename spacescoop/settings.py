import sys
import os
import json
import copy
import operator


SHORT_NAME = 'spacescoop'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARENT_DIR = os.path.dirname(BASE_DIR)

sys.path.append(os.path.join(PARENT_DIR, 'django-apps'))

SECRETS_FILE = os.path.join(BASE_DIR, 'secrets.json')
if os.path.isfile(SECRETS_FILE):
    fdata = open(SECRETS_FILE)
    secrets = json.load(fdata)
    fdata.close()
else:
    raise 'No secrets found!'

DEBUG = False
DJANGO_SETTINGS_CONFIG = os.environ.get('DJANGO_SETTINGS_CONFIG', None)
if DJANGO_SETTINGS_CONFIG == 'DEV':
    DEBUG = True
    # DEBUG_TOOLBAR_PATCH_SETTINGS = False

# cannonical base URL for the website
SITE_URL = 'http://www.spacescoop.org'

ADMINS = (
    ('Vaclav Ehrlich', secrets['ADMIN_EMAIL']),
)

# MANAGERS = ADMINS

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets['SECRET_KEY']

ALLOWED_HOSTS = [
    'www.spacescoop.org',
    'spacescoop.org',
    '188.166.22.9',
    'spacescoop',
    'spacescoop.local',
    'localhost',  # for when I set DEBUG = False in development
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'pipeline',

    'parler',
    'ckeditor',
    'taggit',
    'taggit_autosuggest',

    'sorl.thumbnail',
    # 'filer',
    # 'easy_thumbnails',

    'institutions',
    'smartpages',
    'spacescoop',
    'spacescoops',
    'spacescoop.newsletter',
    'spacescoop.search',
    'glossary',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'CacheMiddleware'
    'django.middleware.locale.LocaleMiddleware',  # see https://docs.djangoproject.com/en/1.8/topics/i18n/translation/#how-django-discovers-language-preference
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'spacescoop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            # https://docs.djangoproject.com/en/1.8/ref/templates/api/#built-in-template-context-processors
            'context_processors': [
                # debug, sql_queries
                'django.template.context_processors.debug',
                # request
                'django.template.context_processors.request',
                # user, perms
                'django.contrib.auth.context_processors.auth',
                # messages, DEFAULT_MESSAGE_LEVELS
                'django.contrib.messages.context_processors.messages',
                # LANGUAGES, LANGUAGE_CODE
                'django.template.context_processors.i18n',
                # THUMBNAIL_ALIASES
                'django_ext.context_processors.thumbnail_aliases',
                # SITE_URL
                'django_ext.context_processors.site_url',
            ],
            'debug': False,
        },
    },
]

WSGI_APPLICATION = 'spacescoop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'spacescoop',
        'USER': secrets['DATABASE_USER_PROD'],
        'PASSWORD': secrets['DATABASE_PASSWORD_PROD'],
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

import django.conf.locale
django.conf.locale.LANG_INFO['gu'] = {
    'bidi': False,
    'code': 'gu',
    'name': 'Gurajati',
    'name_local': 'ગુજરાતી',
}
django.conf.locale.LANG_INFO['hi'] = {
    'bidi': False,
    'code': 'hi',
    'name': 'Hindi',
    'name_local': 'हिंदी',
}
django.conf.locale.LANG_INFO['mt'] = {
    'bidi': False,
    'code': 'mt',
    'name': 'Maltese',
    'name_local': 'Malti',
}
django.conf.locale.LANG_INFO['si'] = {
    'bidi': False,
    'code': 'si',
    'name': 'Sinhalese',
    'name_local': 'සිංහල',
}
django.conf.locale.LANG_INFO['tet'] = {
    'bidi': False,
    'code': 'tet',
    'name': 'Tetum',
    'name_local': 'tetun',
}
django.conf.locale.LANG_INFO['zh'] = {
    'fallback': ['zh-hans'],
}
django.conf.locale.LANG_INFO['quc'] = {
    'bidi': False,
    'code': 'quc',
    'name': 'K’iche’',
    'name_local': 'K’iche’',
}
django.conf.locale.LANG_INFO['tzj'] = {
    'bidi': False,
    'code': 'tzj',
    'name': 'Tz’utujil',
    'name_local': 'Tz’utujil',
}
django.conf.locale.LANG_INFO['ar'] = {
    'bidi': False,
    'code': 'ar',
    'name': 'Arabic',
    'name_local': 'العربيّة',
}
django.conf.locale.LANG_INFO['he'] = {
    'bidi': False,
    'code': 'he',
    'name': 'Hebrew',
    'name_local': 'עברית',
}


# the default translation – the final attempt if no better matching translation is found
LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', 'English'),
    ('nl', 'Dutch'),
    ('it', 'Italian'),
    ('de', 'German'),
    ('es', 'Spanish'),
    ('pl', 'Polish'),
    ('sq', 'Albanian'),
    ('ar', 'Arabic'),
    ('bn', 'Bengali'),
    ('bg', 'Bulgarian'),
    ('zh', 'Chinese'),
    ('cs', 'Czech'),
    ('da', 'Danish'),
    ('fa', 'Farsi'),
    ('fr', 'French'),
    ('el', 'Greek'),
    ('gu', 'Gujarati'),
    ('he', 'Hebrew'),
    ('hi', 'Hindi'),
    ('hu', 'Hungarian'),
    ('is', 'Icelandic'),
    ('id', 'Indonesian'),
    ('ja', 'Japanese'),
    ('quc', 'K’iche’'),
    ('ko', 'Korean'),
    ('mt', 'Maltese'),
    #('mam', 'Mam'),
    ('no', 'Norwegian'),
    ('pt', 'Portuguese'),
    ('ro', 'Romanian'),
    ('ru', 'Russian'),
    ('si', 'Sinhalese'),
    ('sl', 'Slovenian'),
    ('sw', 'Swahili'),
    ('ta', 'Tamil'),
    ('tet', 'Tetum'),
    ('tr', 'Turkish'),
    ('tzj', 'Tz’utujil'),
    ('uk', 'Ukrainian'),
    ('vi', 'Vietnamese'),
    ('cy', 'Welsh'),
)
LANGUAGES = sorted(LANGUAGES, key=operator.itemgetter(0))

# # Languages using BiDi (right-to-left) layout
# LANGUAGES_BIDI = global_settings.LANGUAGES_BIDI + ("ug",)

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

USE_L10N = True
FORMAT_MODULE_PATH = (
    'formats',
)
DATETIME_FORMAT = 'Y-m-d H:i:s'

USE_TZ = True


# Media

MEDIA_ROOT = os.path.join(PARENT_DIR, 'spacescoop_uploads')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PARENT_DIR, 'spacescoop_static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'static/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'pipeline.finders.PipelineFinder',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# parler
# http://django-parler.readthedocs.org/en/latest/
# https://github.com/edoburu/django-parler
PARLER_LANGUAGES = {
    None: (
        # {'code': 'en',},
        # {'code': 'de',},
        # {'code': 'pt',},
        # {'code': 'ar',},
        # {'code': 'vi',},
    ),
    'default': {
        'fallbacks': ['en'],
        'hide_untranslated': True,   # False is the default; let .active_translations() return fallbacks too.
    }
}

# Email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = secrets['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = secrets['EMAIL_HOST_PASSWORD']
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_SUBJECT_PREFIX = '[spacescoop] '


# Caching
USE_ETAGS = True  # Note: disable debug toolbar while testing!


# Pipeline
PIPELINE = {
    # 'CSS_COMPRESSOR': None,
    'JS_COMPRESSOR': None,
    'STYLESHEETS': {
        'styles': {
            'source_filenames': (
                # 'css/fonts.css',
                # 'css/reset.css',
                'slick/slick.css',
                'slick/slick-theme.css',
                'css/main.css',
                # 'css/media_1280.css',
                # 'css/media_1080.css',
                # 'css/media_992.css',
                # 'css/media_768.css',
                # 'css/media_600.css',
                # 'css/media_480.css',
            ),
            'output_filename': 'css/spacescoop.min.css',
            'extra_context': {
                'media': 'screen',
            },
        },
    },
    'JAVASCRIPT': {
        'scripts': {
            'source_filenames': [
                'js/jquery-1.11.3.min.js',
                'js/bootstrap.min.js',
                'slick/slick.min.js',
                'js/jquery.sharrre.min.js',
                'js/menus.js',
                # 'js/scripts.js',
            ],
            'output_filename': 'js/spacescoop.min.js',
        }
    }
}

from slugify import Slugify
AUTOSLUG_SLUGIFY_FUNCTION = Slugify(translate=None, max_length=200, to_lower=True)

# Thumbnails
# http://sorl-thumbnail.readthedocs.org/en/latest/reference/settings.html
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
THUMBNAIL_DBM_FILE = os.path.join(PARENT_DIR, 'usr/redis/thumbnails_spacescoop')
# THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.convert_engine.Engine'  #TODO: revisit this choice
THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.pil_engine.Engine'  #TODO: revisit this choice
THUMBNAIL_KEY_PREFIX = 'sorl-thumbnail-spacescoop'
THUMBNAIL_PRESERVE_FORMAT = 'True'
# THUMBNAIL_ALTERNATIVE_RESOLUTIONS = [1.5, 2]
THUMBNAIL_ALIASES = {
    'original_news_source': 'x60',
    'article_feature': '880x410',
    'article_cover': '680x400',
    'article_thumb': '320',
    'article_thumb_inline': '198x200',
}

# Taggit
TAGGIT_CASE_INSENSITIVE = True
FORCE_LOWERCASE = True

# CK editor
CKEDITOR_UPLOAD_PATH = 'upload/'
CKEDITOR_CONFIGS = {
    ## see http://docs.cksource.com/CKEditor_3.x/Developers_Guide/Toolbar

    # 'default': {
    #     'fillEmptyBlocks': False,
    #     'toolbar': 'Custom',
    #     'toolbar_Custom': [
    #         ['Source', ],
    #         ['Bold', 'Italic', '-', 'Subscript', 'Superscript', '-', 'Undo', 'Redo', 'RemoveFormat', ],
    #         ['Glossary', ],
    #         ['Link', 'Unlink', ],
    #         # ['Image', ],
    #         ['BidiLtr', 'BidiRtl', ],
    #     ],
    #     # 'extraPlugins': 'codesnippet',
    #     'extraPlugins': 'glossary',
    #     'contentsCss': ['%sckeditor/ckeditor/contents.css' % STATIC_URL, '%scss/ckeditor-content.css' % STATIC_URL],
    # },
    # 'small': {
    #     'fillEmptyBlocks': False,
    #     'toolbar': 'Custom',
    #     'toolbar_Custom': [
    #         ['Source', ],
    #         ['Bold', 'Italic', '-', 'Subscript', 'Superscript', '-', 'Undo', 'Redo', 'RemoveFormat', ],
    #         ['Link', 'Unlink', ],
    #         # ['Image', ],
    #         ['BidiLtr', 'BidiRtl', ],
    #     ],
    #     'height': 100,
    # },
    'smartpages': {
        'fillEmptyBlocks': False,
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Source', ],
            ['Format', ],
            ['Bold', 'Italic', '-', 'Underline', 'Subscript', 'Superscript', '-', 'Undo', 'Redo', 'RemoveFormat', ],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', ],
            ['Link', 'Unlink', ],
            ['Image', 'Table', 'SpecialChar', ],
            ['Maximize', 'ShowBlocks', ],
            ['BidiLtr', 'BidiRtl', ],
        ],
        'width': 845,
    },
    'default': {
        'fillEmptyBlocks': False,
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Source', ],
            ['Bold', 'Italic', '-', 'Subscript', 'Superscript', '-', 'Undo', 'Redo', 'RemoveFormat', ],
            ['Link', 'Unlink', ],
            # ['Image', ],
            ['BidiLtr', 'BidiRtl', ],
        ],
    },
}
CKEDITOR_CONFIGS['small'] = copy.deepcopy(CKEDITOR_CONFIGS['default'])
CKEDITOR_CONFIGS['small']['height'] = 100

CKEDITOR_CONFIGS['spacescoop'] = copy.deepcopy(CKEDITOR_CONFIGS['default'])
CKEDITOR_CONFIGS['spacescoop']['extraPlugins'] = 'glossary'
CKEDITOR_CONFIGS['spacescoop']['contentsCss'] = ['%sckeditor/ckeditor/contents.css' % STATIC_URL, '%scss/ckeditor-content.css' % STATIC_URL]
CKEDITOR_CONFIGS['spacescoop']['toolbar_Custom'].insert(2, ['Glossary', ])
# CKEDITOR_CONFIGS['spacescoop']['toolbar_Custom'].append(['Glossary', ])

WHOOSH_INDEX_PATH = os.path.join(PARENT_DIR, '/home/web/usr/whoosh_index/spacescoop')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        # send an email to the site admins on every HTTP 500 error when DEBUG=False.
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'error_log': {
            # 'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(PARENT_DIR, 'usr/log/spacescoop-error.log'),
        },
        'default': {
            'class': 'logging.StreamHandler',
        },
        # 'request_error': {
        #     'level': 'ERROR',
        #     # 'filters': ['require_debug_false'],
        #     'class': 'logging.FileHandler',
        #     'filename': 'request_error.log',
        # }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'error_log'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['default', ],
            'level': 'INFO',
        }
    }
}

if DJANGO_SETTINGS_CONFIG == 'DEV':
    # TIME_ZONE = 'Europe/Lisbon'
    STATIC_ROOT = '/tmp'
    TEMPLATES[0]['OPTIONS']['debug'] = True  # TEMPLATE_DEBUG
    # debug toolbar
    INTERNAL_IPS = ('127.0.0.1',)
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'JQUERY_URL':'',
    }
    EMAIL_SUBJECT_PREFIX = '[spacescoop dev] '
    # CELERY_ALWAYS_EAGER = True  # Tasks are run synchronously
    THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.dbm_kvstore.KVStore'  # in-memory sorl KV store
    THUMBNAIL_DUMMY = True
    # THUMBNAIL_DUMMY_SOURCE = 'http://placekitten.com/%(width)s/%(height)s'
    # THUMBNAIL_DUMMY_RATIO = 1.5

    WHOOSH_INDEX_PATH = os.path.join(PARENT_DIR, 'usr/whoosh_index/spacescoop')

elif DJANGO_SETTINGS_CONFIG == 'PROD':
    DEBUG = False
    # PIPELINE_JS['scripts']['source_filenames'].append('js/download-analytics.js')

else:
    if DJANGO_SETTINGS_CONFIG:
        raise EnvironmentError(1, 'DJANGO_SETTINGS_CONFIG environment variable set to invalid value: %s' % DJANGO_SETTINGS_CONFIG)
    else:
        raise EnvironmentError(1, 'DJANGO_SETTINGS_CONFIG environment variable not set')


# # SILENCED_SYSTEM_CHECKS = ['deprecation.RemovedInDjango19Warning', ]
# import logging, copy
# from django.utils.log import DEFAULT_LOGGING

# # LOGGING = copy.deepcopy(DEFAULT_LOGGING)
# LOGGING['filters']['suppress_deprecated'] = {
#     '()': 'spacescoop.settings.SuppressDeprecated'  
# }
# LOGGING['handlers']['console']['filters'].append('suppress_deprecated')

# class SuppressDeprecated(logging.Filter):
#     def filter(self, record):
#         WARNINGS_TO_SUPPRESS = [
#             'RemovedInDjango19Warning: The django.contrib.admin.util module has been renamed',
#             'RemovedInDjango19Warning: The utilities in django.db.models.loading are deprecated in favor of the new application loading system',
#             'RemovedInDjango19Warning: django.utils.importlib will be removed',
#         ]
#         # Return false to suppress message.
#         return not any([warn in record.getMessage() for warn in WARNINGS_TO_SUPPRESS])


from django.contrib import admin
admin.site.site_header = 'Space Scoop: Administration'
