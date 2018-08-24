import xml.etree.ElementTree as et
import xml.dom.minidom
from urllib.parse import unquote
class Xml():

    @classmethod
    def resove_xml(cls,body=None):
        root = et.fromstring(body)
        properties = root.findall('properties')[0]
        systems = properties.findall('system')[0]

        params = {}
        for s in systems:
            key = unquote(s.get('key'))
            value = unquote(s.get('value'))
            params[key] = value

        sessions = properties.findall('session')[0]
        for s in sessions:
            key = unquote(s.get('key'))
            value = unquote(s.get('value'))
            params[key] = value
        return params

    @classmethod
    def generate_xml(cls,params):
        doc = xml.dom.minidom.Document()
        root = doc.createElement('response')
        doc.appendChild(root)
        result = doc.createElement('result')
        codeNode = doc.createElement('code')
        codeNode.appendChild(doc.createTextNode(str(params['code'])))
        reasonNode = doc.createElement('reason')
        reasonNode.appendChild(doc.createTextNode(str(params['reason'])))
        result.appendChild(codeNode)
        result.appendChild(reasonNode)

        properties = doc.createElement('properties')
        sessionNode = doc.createElement('session')
        propertyNode = doc.createElement('property')

        propertyNode.setAttribute('key', params['key'])
        propertyNode.setAttribute('value', params['value'])
        sessionNode.appendChild(propertyNode)
        properties.appendChild(sessionNode)

        root.appendChild(result)
        root.appendChild(properties)

        return doc.toxml(encoding='gbk')



