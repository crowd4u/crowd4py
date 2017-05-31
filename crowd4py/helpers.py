def get_post_url(etroot):
    """
    get post url from etree object
    :param etroot: lxml.etree object
    :return: url
    """
    post_url = "http:" + etroot.find('post_url').text
    return post_url


def get_value_from_xml(etroot):
    """
    get keys and values as array object from lxml.etree object
    :param etroot:lxml.etree object
    :return name, value: both are array object.
    """
    keys = []
    value = []
    for child in etroot.iter('parameter'):
        keys.append(child.find('name').text)
        value.append(child.find('value').text)
    return keys, value
