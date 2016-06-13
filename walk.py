import os

def walk(dirname):
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print os.path.join(root, filename)

print walk('.')
