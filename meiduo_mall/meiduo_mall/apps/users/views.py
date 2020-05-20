from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
# Create your views here.
from django.views import View
# 导入,可以使此次请求忽略csrf校验
from django.views.decorators.csrf import csrf_exempt


class RegisterView(View):
    """用户注册"""

    @csrf_exempt
    def post(self, request):
        """
        提供注册界面
        :param request: 请求对象
        :return: 注册界面
        """
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        mobile = request.POST.get('mobile')
        allow = request.POST.get('allow')

        # 判断参数是否齐全
        # if not all([username, password, password2, mobile, allow]):
        #     return HttpResponseForbidden('缺少必传参数')
        # # 判断用户名是否是5-20个字符
        # if not re.match(r'^[a-zA-Z0-9_-]{5,20}$', username):
        #     return HttpResponseForbidden('请输入5-20个字符的用户名')
        # # 判断密码是否是8-20个数字
        # if not re.match(r'^[0-9A-Za-z]{8,20}$', password):
        #     return HttpResponseForbidden('请输入8-20位的密码')
        # # 判断两次密码是否一致
        # if password != password2:
        #     return HttpResponseForbidden('两次输入的密码不一致')
        # # 判断手机号是否合法
        # if not re.match(r'^1[3-9]\d{9}$', mobile):
        #     return HttpResponseForbidden('请输入正确的手机号码')
        # # 判断是否勾选用户协议
        # if allow != 'on':
        #     return HttpResponseForbidden('请勾选用户协议')
        # 使用django认证加密密码
        password = make_password(password)
        login(request, )
        return HttpResponse(password)
