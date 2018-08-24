import re

import requests
from flask import make_response
from flask_restful import Resource, request

from robot.tools.xml import Xml
from robot import app


class XmHandler(Resource):

    # @jwt_required()
    def post(self):
        data = request.get_data()
        if data is None:
            app.logger.error('post data is none')
            return None, 200
        if len(data) == 0:
            app.logger.error('post data is blank')
            return None, 404
        try:
            data = re.sub('gbk', 'utf-8', data.decode('utf-8')).encode('utf-8')
        except BaseException as e:
            app.logger.error('请求内容编码格式错误,%s' % str(e))
            return '请求内容编码格式错误', '500'
        params = Xml.resove_xml(data)

        _info = params.get('inputchoosecontent')
        print(params.get('imUserNumber'), ': ', _info)

        app.logger.info('%s: %s', params.get('imUserNumber'), _info)
        data = {
            'key': '5765096de11a4f5381e4c63cb84392ea',
            'info': _info,
            'userid': 'robot',
        }
        api_url = 'http://www.tuling123.com/openapi/api'
        response = requests.post(api_url, data).json()
        print('机器人: ', response.get('text'))
        app.logger.info('机器人: %s',response.get('text'))
        results = {}
        results['key'] = 'inputchooseresult'
        results['value'] = response.get('text')
        results['code'] = 0
        results['reason'] = '响应成功'
        try:
            data = Xml.generate_xml(results)
            result = data
        except BaseException as e:
            app.logger.error('编码转换异常,%s' % str(e))
            return "编码转换异常", 500
        resp = make_response(result)
        resp.headers["Content-type"] = "application/xml;charset=gbk"
        return resp
