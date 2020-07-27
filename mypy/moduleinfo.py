"""Collection of names of notable Python library modules.

Both standard library and third party modules are included. The
selection criteria for third party modules is somewhat arbitrary.

For packages we usually just include the top-level package name, but
sometimes some or all submodules are enumerated. In the latter case if
the top-level name is included we include all possible submodules
(this is an implementation limitation).

These are used to give more useful error messages when there is
no stub for a module.
"""

from typing import Set

MYPY = False
if MYPY:
    from typing_extensions import Final


third_party_modules = {
    # From Python 3 Wall of Superpowers (https://python3wos.appspot.com/)
    'simplejson',
    'requests',
    'six',
    'pip',
    'virtualenv',
    'boto',
    'setuptools',
    'dateutil',
    'pytz',
    'pyasn1',
    'nose',
    'yaml',
    'lxml',
    'jinja2',
    'docutils',
    'markupsafe',
    'paramiko',
    'Crypto',
    'rsa',
    'django',
    'coverage',
    'pika',
    'colorama',
    'ecdsa',
    'psycopg2',
    'httplib2',
    'mock',
    'pycparser',
    'pep8',
    'redis',
    'pymongo',
    'sqlalchemy',
    'pygments',
    'werkzeug',
    'selenium',
    'supervisor',
    'zc.buildout',
    'meld3',
    'PIL',
    'paste',
    'flask',
    '_mysql',
    'MySQLdb',
    'greenlet',
    'carbon',
    'psutil',
    'paste.deploy',
    'kombu',
    'babel',
    'anyjson',
    'py',
    'OpenSSL',
    'numpy',
    'sphinx',
    'tornado',
    'zope.interface',
    'itsdangerous',
    'fabric',
    'amqp',
    'mako',
    'pyflakes',
    'concurrent.futures',
    'pyparsing',
    'celery',
    'unittest2',
    'setuptools_git',
    'decorator',
    'ordereddict',
    'urllib3',
    'iso8601',
    'gunicorn',
    'prettytable',
    'webob',
    'flake8',
    'pytest',
    'billiard',
    'backports.ssl_match_hostname',
    'south',
    'gevent',
    'netaddr',
    'pylint',
    'logilab.common',
    'twisted',
    'msgpack',
    'blessings',
    'oauth2client',
    'ujson',
    'mozrunner',
    'googleapiclient',
    'markdown',
    'pyasn1',
    'html5lib',
    'isodate',
    'tox',
    'mozdevice',
    'cython',
    'raven',
    'mozprocess',
    'mozprofile',
    'mozinfo',
    'mozlog',
    'pandas',
    'lockfile',
    'pycurl',
    'novaclient',
    'ply',
    'eventlet',
    'suds',
    'zmq',
    'memcache',
    'netifaces',
    'repoze.lru',
    'testtools',
    'cups',
    'oauth2',
    'scipy',
    'thrift',
    'statsd',
    'BeautifulSoup',
    'bs4',
    'sklearn',
    'cmd2',
    'alembic',
    'gflags',
    'gflags_validators',
    'sqlparse',
    'debug_toolbar',
    'cov_core',
    'unidecode',
    'websocket',
    'webtest',
    'django_extensions',
    'networkx',
    'newrelic',
    'pymysql',
    'pytest_cov',
    'matplotlib',
    'djcelery',
    'google.protobuf',
    'compressor',
    'aspen',
    'subunit',
    'libcloud',
    'versiontools',
    'chardet',
    'blinker',
    'pystache',
    'passlib',
    'xlrd',
    'pygeoip',
    'configobj',
    'cjson',
    'testrepository',
    'zc.recipe.egg',
    'jsonpointer',
    'amqplib',
    'rdflib',
    'SPARQLWrapper',
    'jsonpatch',
    'mrjob',
    'pexpect',
    'google.apputils',
    'ansible',
    'django_nose',
    'd2to1',
    'routes',
    'tempita',
    'testscenarios',
    'demjson',
    'openid',
    'uwsgidecorators',
    'wtforms',
    'dns',
    'alabaster',
    'M2Crypto',
    'reportlab',
    'feedparser',
    'ldap',
    'hgtools',
    'whoosh',
    'path',
    'nosexcover',
    'iptools',
    'xlwt',
    'keyring',
    'termcolor',
    'flask_sqlalchemy',
    'httpretty',
    'magic',
    'leaderboard',
    'sqlobject',
    'nltk',

    # Skipped (name considered too generic):
    # - fixtures
    # - migrate (from sqlalchemy-migrate)
    # - git (GitPython)

    # Other
    'formencode',
    'pkg_resources',
    'wx',
    'gi.repository',
    'pygtk',
    'gtk',
    'PyQt4',
    'PyQt5',
    'pylons',

    # for use in tests
    '__dummy_third_party1',
}  # type: Final

# Modules and packages common to Python 2.7 and 3.x.
common_std_lib_modules = {
    'abc',
    'aifc',
    'antigravity',
    'argparse',
    'array',
    'ast',
    'asynchat',
    'asyncore',
    'audioop',
    'base64',
    'bdb',
    'binascii',
    'binhex',
    'bisect',
    'bz2',
    'cProfile',
    'calendar',
    'cgi',
    'cgitb',
    'chunk',
    'cmath',
    'cmd',
    'code',
    'codecs',
    'codeop',
    'collections',
    'colorsys',
    'compileall',
    'contextlib',
    'copy',
    'crypt',
    'csv',
    'ctypes',
    'curses',
    'datetime',
    'decimal',
    'difflib',
    'dis',
    'distutils',
    'doctest',
    'dummy_threading',
    'email',
    'encodings',
    'fcntl',
    'filecmp',
    'fileinput',
    'fnmatch',
    'formatter',
    'fractions',
    'ftplib',
    'functools',
    'genericpath',
    'getopt',
    'getpass',
    'gettext',
    'glob',
    'grp',
    'gzip',
    'hashlib',
    'heapq',
    'hmac',
    'imaplib',
    'imghdr',
    'importlib',
    'inspect',
    'io',
    'json',
    'keyword',
    'lib2to3',
    'linecache',
    'locale',
    'logging',
    'macpath',
    'macurl2path',
    'mailbox',
    'mailcap',
    'math',
    'mimetypes',
    'mmap',
    'modulefinder',
    'msilib',
    'multiprocessing',
    'netrc',
    'nis',
    'nntplib',
    'ntpath',
    'nturl2path',
    'numbers',
    'opcode',
    'operator',
    'optparse',
    'os',
    'ossaudiodev',
    'parser',
    'pdb',
    'pickle',
    'pickletools',
    'pipes',
    'pkgutil',
    'platform',
    'plistlib',
    'poplib',
    'posixpath',
    'pprint',
    'profile',
    'pstats',
    'pty',
    'py_compile',
    'pyclbr',
    'pydoc',
    'pydoc_data',
    'pyexpat',
    'quopri',
    'random',
    're',
    'resource',
    'rlcompleter',
    'runpy',
    'sched',
    'select',
    'shelve',
    'shlex',
    'shutil',
    'site',
    'smtpd',
    'smtplib',
    'sndhdr',
    'socket',
    'spwd',
    'sqlite3',
    'sqlite3.dbapi2',
    'sqlite3.dump',
    'sre_compile',
    'sre_constants',
    'sre_parse',
    'ssl',
    'stat',
    'string',
    'stringprep',
    'struct',
    'subprocess',
    'sunau',
    'symbol',
    'symtable',
    'sysconfig',
    'syslog',
    'tabnanny',
    'tarfile',
    'telnetlib',
    'tempfile',
    'termios',
    'textwrap',
    'this',
    'threading',
    'timeit',
    'token',
    'tokenize',
    'trace',
    'traceback',
    'tty',
    'types',
    'unicodedata',
    'unittest',
    'urllib',
    'uu',
    'uuid',
    'warnings',
    'wave',
    'weakref',
    'webbrowser',
    'wsgiref',
    'xdrlib',
    'xml.dom',
    'xml.dom.NodeFilter',
    'xml.dom.domreg',
    'xml.dom.expatbuilder',
    'xml.dom.minicompat',
    'xml.dom.minidom',
    'xml.dom.pulldom',
    'xml.dom.xmlbuilder',
    'xml.etree',
    'xml.etree.ElementInclude',
    'xml.etree.ElementPath',
    'xml.etree.ElementTree',
    'xml.etree.cElementTree',
    'xml.parsers',
    'xml.parsers.expat',
    'xml.sax',
    'xml.sax._exceptions',
    'xml.sax.expatreader',
    'xml.sax.handler',
    'xml.sax.saxutils',
    'xml.sax.xmlreader',
    'zipfile',
    'zlib',
    # fake names to use in tests
    '__dummy_stdlib1',
    '__dummy_stdlib2',
}  # type: Final

# Python 2 standard library modules.
python2_std_lib_modules = common_std_lib_modules | {
    'BaseHTTPServer',
    'Bastion',
    'CGIHTTPServer',
    'ConfigParser',
    'Cookie',
    'DocXMLRPCServer',
    'HTMLParser',
    'MimeWriter',
    'Queue',
    'SimpleHTTPServer',
    'SimpleXMLRPCServer',
    'SocketServer',
    'StringIO',
    'UserDict',
    'UserList',
    'UserString',
    'anydbm',
    'atexit',
    'audiodev',
    'bsddb',
    'cPickle',
    'cStringIO',
    'commands',
    'cookielib',
    'copy_reg',
    'curses.wrapper',
    'dbhash',
    'dircache',
    'dumbdbm',
    'dummy_thread',
    'fpformat',
    'future_builtins',
    'hotshot',
    'htmlentitydefs',
    'htmllib',
    'httplib',
    'ihooks',
    'imputil',
    'itertools',
    'linuxaudiodev',
    'markupbase',
    'md5',
    'mhlib',
    'mimetools',
    'mimify',
    'multifile',
    'multiprocessing.forking',
    'mutex',
    'new',
    'os2emxpath',
    'popen2',
    'posixfile',
    'repr',
    'rexec',
    'rfc822',
    'robotparser',
    'sets',
    'sgmllib',
    'sha',
    'sre',
    'statvfs',
    'stringold',
    'strop',
    'sunaudio',
    'time',
    'toaiff',
    'urllib2',
    'urlparse',
    'user',
    'whichdb',
    'xmllib',
    'xmlrpclib',
}  # type: Final

# Python 3 standard library modules (based on Python 3.5.0).
python3_std_lib_modules = common_std_lib_modules | {
    'asyncio',
    'collections.abc',
    'concurrent',
    'concurrent.futures',
    'configparser',
    'copyreg',
    'dbm',
    'ensurepip',
    'enum',
    'html',
    'http',
    'imp',
    'ipaddress',
    'lzma',
    'pathlib',
    'queue',
    'readline',
    'reprlib',
    'selectors',
    'signal',
    'socketserver',
    'statistics',
    'tkinter',
    'tracemalloc',
    'turtle',
    'turtledemo',
    'typing',
    'unittest.mock',
    'urllib.error',
    'urllib.parse',
    'urllib.request',
    'urllib.response',
    'urllib.robotparser',
    'venv',
    'xmlrpc',
    'xxlimited',
    'zipapp',
}  # type: Final


def is_third_party_module(id: str) -> bool:
    return is_in_module_collection(third_party_modules, id)


def is_py2_std_lib_module(id: str) -> bool:
    return is_in_module_collection(python2_std_lib_modules, id)


def is_py3_std_lib_module(id: str) -> bool:
    return is_in_module_collection(python3_std_lib_modules, id)


def is_in_module_collection(collection: Set[str], id: str) -> bool:
    components = id.split('.')
    return any(
        '.'.join(components[:prefix_length]) in collection
        for prefix_length in range(1, len(components) + 1)
    )
