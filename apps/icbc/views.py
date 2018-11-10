#encoding: utf-8
from flask import Blueprint, request, render_template, session, g
from flask import views
from .forms import RegistForm, LoginForm, TransferForm
from apps.icbc.models import User
from config import session as db_session
from apps.icbc.decorators import loginRequired

bp = Blueprint('icbc', __name__)


@bp.route('/')
def index():
    return render_template('icbc/index.html')


class RegistView(views.MethodView):
    def get(self):
        return render_template("icbc/regist.html")

    def post(self):
        form = RegistForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            deposit = form.deposit.data
            user = User(
                email = email,
                username = username,
                password = password,
                deposit = deposit
            )
            db_session.add(user)
            db_session.commit()
            return '注册成功！'
        else:
            print(form.errors)
            return '注册失败'


class LoginView(views.MethodView):
    def get(self):
        return render_template('icbc/login.html')

    def post(self):
        form = LoginForm(request.form)
        if form.validate:
            email = form.email.data
            password = form.password.data
            user = db_session.query(User).filter(User.email==email, User.password==password).first()
            if user:  # 如果存在此用户
                session['user_id'] = user.id
                return '登陆成功'
            else:
                return '用户或密码错误'
        else:
            print(form.errors)
            return self.get()


class TransferView(views.MethodView):
    def get(self):
        return render_template('icbc/transfer.html')

    decorators = [loginRequired]
    def post(self):
        csrf_token = request.form.get('csrf_token')
        form = TransferForm(request.form)
        if form.validate():
            email = form.email.data
            money = form.money.data
            id = session['user_id']
            # 转账发起人
            user_s = db_session.query(User).filter(User.id==id).first()
            # 转账接收者
            user_t = db_session.query(User).filter(User.email==email).first()
            # 判断转账发起人的余额是否大于要转账的金额
            if user_s.deposit >= money:
                user_s.deposit -= money
                user_t.deposit += money
                db_session.commit()
                return '转账成功'
            else:
                return '余额不足'
        else:
            print(form.errors)
            return self.get()

bp.add_url_rule('/regist/', view_func=RegistView.as_view('regist'))
bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
bp.add_url_rule('/transfer/', view_func=TransferView.as_view('transfer'))


