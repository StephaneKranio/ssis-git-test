import re
import sys

# lire le contenu du fichier
if len(sys.argv) > 1:
    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    # remplacer GUID
    clean = re.sub(r'\{[0-9A-Fa-f\-]{36}\}', '{IGNORED-GUID}', data)
    with open(path, "w", encoding="utf-8") as f:
        f.write(clean)
else:
    # mode stdin/stdout (pour Git filter)
    data = sys.stdin.read()
    clean = re.sub(r'\{[0-9A-Fa-f\-]{36}\}', '{IGNORED-GUID}', data)
    sys.stdout.write(clean)
