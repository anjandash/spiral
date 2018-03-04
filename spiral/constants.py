'''
constants: constants used in Spiral splitters.
'''

common_suffix_numbers = {'16', '32', '64', '128', '256', '512', '1024'}
'''
List of numbers that are commonly put after some other strings, to form
symbols such as "int32", "float64", etc.
'''

# General principles for the following:
# 1. Only put in terms that at least one digit in them.
# 2. Avoid 2-character sequences, because they match too many things and
#    cause too many bad splits.
# 3. Stick to computing terms that many people use or have used, not stuff
#    that a particular program happens to use.
# 4. Generally, avoid packages for particular languages, like "urllib3".
#
# Sources for the following:
# - https://en.wikipedia.org/wiki/List_of_computing_and_IT_abbreviations
# - https://en.wikipedia.org/wiki/List_of_codecs
# - https://en.wikipedia.org/wiki/Comparison_of_video_codecs
# - the book 'The Definitivei Guide to iReport' by Toffoli, 2007
# - various lists and dictionaries of computing terms found by Googling
# - personal experience
 
common_terms_with_numbers = {
    '1st',
    '1to1',
    '2of7',
    '2nd',
    '3d',
    '3of9',
    '3ivx',
    '3rd',
    '88k',
    'a52',
    'ac2',
    'ac3',
    'ada83',
    'ada95',
    'amd64',
    'asn1',
    'avs1',
    'avs2',
    'b2b',
    'b2c',
    'b2e',
    'b8zs',
    'base64',
    'bit7',
    'bzip2',
    'bz2',
    'c2a',
    'c3p0',
    'c4s',
    'cast5',
    'ciks1',
    'coconut98',
    'code128',
    'code128a',
    'code128b',
    'code128c',
    'code39',
    'color16',
    'color32',
    'com1',
    'com2',
    'com3',
    'com4',
    'crc32',
    'cvv2',
    'ddr2',
    'ddr3',
    'ddr4',
    'd2d',
    'd2d2t',
    'd3d',
    'db2',
    'db9',
    'des3',
    'ds0',
    'ds1',
    'ean128',
    'ean13',
    'e2e',
    'e3cp',
    'ec2',
    'f2f',
    'f95',
    'fat32',
    'float128',
    'float32',
    'float64',
    'float96',
    'fma99',
    'fs1015',
    'fs1016',
    'fs1023',
    'g711',
    'g718',
    'g719',
    'g721',
    'g722',
    'g723',
    'g726',
    'g728',
    'g729',
    'g729a',
    'g729d',
    'gtk3',
    'h261',
    'h262',
    'h263',
    'h264',
    'h265',
    'h323',
    'hdf5',
    'hi10p',
    'hi422p',
    'hi444pp',
    'hl7',
    'html3',
    'html4',
    'html5',
    'i10n',
    'i18n',
    'i2c',
    'i386',
    'ia32',
    'ia64',
    'id10t',
    'ie10',
    'ie11',
    'ie12',
    'ie13',
    'ie6',
    'ie7',
    'ie8',
    'ie9',
    'imap4',
    'int128',
    'int16',
    'int2of5',
    'int32',
    'int64',
    'int8',
    'jpa2',
    'ipv4',
    'ipv6',
    'ipv6cp',
    'iso[0-9]{2,}',
    'ix86',
    'j2ee',
    'j2me',
    'j2se',
    'java10',
    'java6',
    'java7',
    'java8',
    'java9',
    'jdk10',
    'jdk11',
    'jdk12',
    'jdk13',
    'jdk14',
    'jdk15',
    'jdk16',
    'jpeg2000',
    'koi8r',
    'l10n',
    'l2f',
    'l2s',
    'l2tp',
    'l2tp',
    'l3f',
    'l3s',
    'l3tp',
    'log10',
    'log2',
    'log4j',
    'lpt1',
    'lpt2',
    'lpt4',
    'lpt4',
    'md5',
    'mp3',
    'mp4',
    'mpeg1',
    'mpeg2',
    'mpeg25',
    'mpeg3',
    'mpeg4',
    'multi2',
    'ns3',
    'nw7',
    'o2o',
    'oauth1',
    'oauth2',
    'os10',
    'os11',
    'os12',
    'os13',
    'os7',
    'os8',
    'os9',
    'p2p',
    'p2sc',
    'p3p',
    'p4m',
    'pep8',
    'perl5',
    'pop3',
    'px64',
    'python2',
    'python3',
    'qt4',
    'r2d2',
    'rc5',
    'rc6',
    'rfc[0-9]{3,}',
    'rj11',
    'rj45',
    'rot13',
    'scc14shippingcode',
    'sha1',
    'sha1024',
    'sha256',
    'sha384',
    'sha512',
    'sint16',
    'sint32',
    'sint64',
    'sint8',
    'sm4',
    'smb2',
    'socks4',
    'ss7',
    'sscc18',
    'std2of5',
    'sys32',
    'uint16',
    'uint32',
    'uint64',
    'uint8',
    'usd3',
    'usd4',
    'utf16',
    'utf32',
    'utf8',
    'v2p',
    'vc1',
    'vc3',
    'vcard3',
    'vcard4',
    'vp3',
    'vp4',
    'vp5',
    'vp6',
    'vp6e',
    'vp6s',
    'vp7',
    'vp8',
    'vp9',
    'w3af',
    'w3c',
    'win32',
    'win64',
    'windows7',
    'windows10',
    'windows11',
    'x11',
    'x11r4',
    'x11r5',
    'x11r6',
    'x208',
    'x209',
    'x21',
    'x214',
    'x215',
    'x216',
    'x217',
    'x219',
    'x224',
    'x225',
    'x226',
    'x227',
    'x229',
    'x25',
    'x264',
    'x265',
    'x28',
    'x29',
    'x3d',
    'x3j16',
    'x3t10',
    'x400',
    'x409',
    'x500',
    'x509',
    'x64',
    'x680',
    'x75',
    'x86',
    'xfree86',
    'xga2',
    'xml10',
    'xml11',
    'y2k',
}
'''
Set of common abbreviations and symbols that contain numbers. Entries can be
regular expressions.
'''

special_computing_terms = {
    'adware',
    'ascii',
    'autoexec',
    'autosave',
    'autocommit',
    'backend',
    'backlink',
    'backprop',
    'backreference',
    'barcode',
    'bboard',
    'bitblt',
    'bitcoin',
    'blocklist',
    'bnf',
    'btree',
    'builtin',
    'bytecode',
    'bzip',
    'callback',
    'camelcase',
    'charset',
    'cgi',
    'checkbox',
    'classpath',
    'copyleft',
    'dataflow',
    'datastore',
    'deadlock',
    'defragment',
    'deprecated',
    'devop',
    'devops',
    'distro',
    'dns',
    'ebnf',
    'ecmascript',
    'eeprom',
    'embeddable',
    'esata',
    'exec',
    'ext',
    'facebook',
    'gmail',
    'groupware',
    'gzip',
    'hardwire',
    'hardwired',
    'hashmap',
    'hashset',
    'hostname',
    'hyperscale',
    'inode',
    'io',
    'iscsi',
    'itunes',
    'javabean',
    'javadoc',
    'javascript',
    'jdbc',
    'json',
    'jvm',
    'linker',
    'listserv',
    'llvm',
    'logon',
    'macos',
    'malware',
    'memoization',
    'metamodel',
    'microkernel',
    'middleware',
    'millis',
    'mmx',
    'multipass',
    'multitasking',
    'msata',
    'nan',
    'newline',
    'nvme',
    'online',
    'opcode',
    'overclock',
    'overclocked',
    'parallelizable',
    'petaflop',
    'petaflops',
    'phish',
    'phishing',
    'pickling',
    'prefill',
    'popup',
    'pseudocode',
    'quicktime',
    'refactoring',
    'regex',
    'rmi',
    'scrollbar',
    'segfault',
    'shebang',
    'signedness',
    'socks',
    'sunos',
    'symlink',
    'sysop',
    'tarball',
    'thread',
    'throwable',
    'todo',
    'txt',
    'underclock',
    'warez',
    'worklist',
    'xml',
    'xterm',
    'xwindows',
}
'''
Terms that are not usually found in dictionaries, and should be considered
single words rather than split.  These tend to be specialized computing
terms, including terms that contain one or more dictionary words inside
them; for example, "checkbox" would in normal English be considered two
words, but has come to be accepted as a common neologism in computing.
'''
