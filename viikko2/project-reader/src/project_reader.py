from urllib import request
from project import Project

import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        deserialized = toml.loads(content)

        name = deserialized['tool']['poetry']['name']
        description = deserialized['tool']['poetry']['description']
        dependencies = list(deserialized['tool']['poetry']['dependencies'].keys())
        dev_dependencies = list(deserialized['tool']['poetry']['dev-dependencies'].keys())

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)
