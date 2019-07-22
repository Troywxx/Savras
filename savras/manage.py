from flask_script import Manager, Server
from main import app
#使用Flask Script可以创建命令，并在Flask的应用上下文(Application Context)中执行，因为这样才能对Flask对象进行修改
manager = Manager(app) #把app传给Manager对象，以初始化Flask Script

@manager.shell
def make_shell_context():
    return dict(app=app)
#make_shell_context函数会创建一个Python命令行，并在应用上下文中执行，返回的字典会告诉Flask Script在打开命令行时进行一些默认的导入工作
#一些Flask扩展只有在Flask应用对象被创建之后才会被初始化

if __name__ == '__main__':
    manager.run()
#Python标准方式，用来限制仅在用户直接运行文件的时候，才执行代码
