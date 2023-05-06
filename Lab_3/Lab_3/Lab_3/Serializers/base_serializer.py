from abc import ABC, abstractmethod


class BaseSerializer(ABC):
    @abstractmethod
    def dumps(self, obj) -> str:
        pass

    @abstractmethod
    def loads(self, string: str):
        pass

    def dump(self, obj, source_file):
        source_file.write(self.dumps(obj))

    def load(self, source_file):
        return self.loads(source_file.read())


