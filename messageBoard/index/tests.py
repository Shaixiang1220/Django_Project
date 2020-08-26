from django.test import TestCase
from django.test import Client
from .models import Message

# Create your tests here.
class MessageTest(TestCase):
    # 添加数据
    def setUp(self):
        Message.objects.create(name='Lucy', content='Django入门')
        Message.objects.create(name='May', content='入门到放弃')

    # 编写测试用例
    def test_Message(self):
        # 编写用例
        info = Message.objects.get(name='Lucy')
        # 判断测试用例的执行结果
        self.assertIsNotNone(info.timestamp)

    # 编写测试用例
    def test_post(self):
        # 编写用例
        c = Client()
        data = {
            'name': 'Tim',
            'content': '删库到跑路'
        }
        response = c.post('/', data=data)
        status_code = response.status_code
        info = Message.objects.get(name='Tim')
        # 判断测试用例的执行结果
        self.assertEqual(status_code, 302)
        self.assertEqual(info.content, '删库到跑路')
