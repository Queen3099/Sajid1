# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))