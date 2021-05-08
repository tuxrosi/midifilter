from lxml import etree


def parse(input):
    et = etree.fromstring(input.encode("utf-8"))
    type_elements = et.findall(".//type")
    types = []
    for type_element in type_elements:
        types.append(type_element.text)
    return types
