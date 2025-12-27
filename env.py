import os
# os.environ["STANZA_RESOURCES_DIR"] = "./models/translate/stanza_models"
os.environ["ARGOS_PACKAGES_DIR"] = "./models/translate/argos_translate/packages"
from argostranslate import translate, package, utils

print(package.get_installed_packages())

