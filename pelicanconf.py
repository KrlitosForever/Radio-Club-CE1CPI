AUTHOR = 'Carlos Carrasco Varas'
SITENAME = 'Radio Club Copiapó CE1CPI'
SITEURL = ""

PATH = "content"
THEME = 'themes/ce1cpi'

STATIC_PATHS = ['images', 'extra']
THEME_STATIC_PATHS = ['static']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# Crear alias para archivos estáticos del tema
THEME_STATIC_DIR = 'static'

TIMEZONE = 'America/Santiago'

DEFAULT_LANG = 'Es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DATE_FORMATS = {"es": "%d-%m-%Y"}

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

OUTPUT_PATH = 'docs/'
