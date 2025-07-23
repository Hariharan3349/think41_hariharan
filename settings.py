INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
    'core',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
