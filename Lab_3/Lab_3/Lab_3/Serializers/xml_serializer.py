import re

import regex
from Serializers import BaseSerializer
from Serializers import DictSerializer

from Serializers import nonetype


class XmlSerializer(BaseSerializer):
    NONE_LITERAL = "null"

    KEY_GROUP_NAME = "key"
    VALUE_GROUP_NAME = "value"

    XML_SCHEME_SOURCE = "xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" " + \
                        "xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\""

    XML_SCHEME_PATTERN = "xmlns:xsi=\"http://www\.w3\.org/2001/XMLSchema-instance\" " + \
                         "xmlns:xsd=\"http://www\.w3\.org/2001/XMLSchema\""

    ELEMENTARY_NAMES_PATTERN = "int|float|bool|str|NoneType|list|dict"

    XML_ELEMENT_PATTERN = fr"(\<(?P<{KEY_GROUP_NAME}>{ELEMENTARY_NAMES_PATTERN})\>" + \
                          fr"(?P<{VALUE_GROUP_NAME}>([^<>]*)|(?R)+)\</(?:{ELEMENTARY_NAMES_PATTERN})\>)"

    FIRST_XML_ELEMENT_PATTERN = fr"(\<(?P<{KEY_GROUP_NAME}>{ELEMENTARY_NAMES_PATTERN})\s*({XML_SCHEME_PATTERN})?\>" + \
                                fr"(?P<{VALUE_GROUP_NAME}>([^<>]*)|(?R)+)\</(?:{ELEMENTARY_NAMES_PATTERN})\>)"

    def dumps(self, obj) -> str:
        obj = DictSerializer.to_dict(obj)
        return self.__dumps_from_dict(obj, is_first=True)

    def __dumps_from_dict(self, obj, is_first=False) -> str:
        if type(obj) in (int, float, bool, nonetype):
            return self.__create_xml_element(type(obj).__name__, str(obj), is_first)

        if type(obj) is str:
            data = self.__mask_symbols(obj)
            return self.__create_xml_element(str.__name__, data, is_first)

        if type(obj) is list:
            data = ''.join([self.__dumps_from_dict(o) for o in obj])
            return self.__create_xml_element(list.__name__, data, is_first)

        if type(obj) is dict:
            data = ''.join(
                [f"{self.__dumps_from_dict(item[0])}{self.__dumps_from_dict(item[1])}" for item in obj.items()])
            return self.__create_xml_element(dict.__name__, data, is_first)

        else:
            raise ValueError

    def loads(self, string: str):
        obj = self.__loads_to_dict(string, is_first=True)
        return DictSerializer.from_dict(obj)

    def __loads_to_dict(self, string: str, is_first=False):
        string = string.strip()
        xml_element_pattern = self.FIRST_XML_ELEMENT_PATTERN if is_first else self.XML_ELEMENT_PATTERN

        match = regex.fullmatch(xml_element_pattern, string)

        if not match:
            raise ValueError

        key = match.group(self.KEY_GROUP_NAME)
        value = match.group(self.VALUE_GROUP_NAME)

        if key == int.__name__:
            return int(value)

        if key == float.__name__:
            return float(value)

        if key == bool.__name__:
            return value == str(True)

        if key == str.__name__:
            return self.__unmask_symbols(value)

        if key == nonetype.__name__:
            return None

        if key == list.__name__:
            matches = regex.findall(self.XML_ELEMENT_PATTERN, value)
            return [self.__loads_to_dict(match[0]) for match in matches]

        if key == dict.__name__:
            matches = regex.findall(self.XML_ELEMENT_PATTERN, value)
            return {self.__loads_to_dict(matches[i][0]):
                        self.__loads_to_dict(matches[i + 1][0]) for i in range(0, len(matches), 2)}
        else:
            raise ValueError

    def __create_xml_element(self, name: str, data: str, is_first=False):
        if is_first:
            return f"<{name} {self.XML_SCHEME_SOURCE}>{data}</{name}>"
        else:
            return f"<{name}>{data}</{name}>"

    @staticmethod
    def __mask_symbols(string: str) -> str:
        return string.replace('&', "&amp;").replace('<', "&lt;").replace('>', "&gt;"). \
                      replace('"', "&quot;").replace("'", "&apos;")

    @staticmethod
    def __unmask_symbols(string: str) -> str:
        return string.replace("&amp;", '&').replace("&lt;", '<').replace("&gt;", '>'). \
                      replace("&quot;", '"').replace("&apos;", "'")
