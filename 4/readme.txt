1、首先用
easy_install virtualenv
easy_install pip
2、在根目录中
virtualenv --no-site-packages ENV
3、之后会在根目录中生成一个ENV目录，进入这个目录中的Scripts目录
4、执行activate.bat
5、进入到虚拟状态
pip install Flask Flask-Cache Flask-SQLAlchemy
pip freeze > requirements.txt
6、下载打包工具
https://raw.github.com/SAEPython/saepythondevguide/master/dev_server/bundle_local.py
python bundle_local.py -r requirements.txt
将virutalenv.bundle目录到应用的目录下。
修改index.wsgi文件，在导入其它模块之前，将virtualenv.bundle目录或者 virtualenv.bundle.zip添加到module的搜索路径中，示例代码如下：

import os
import sys

app_root = os.path.dirname(__file__)

# 两者取其一
sys.path.insert(0, os.path.join(app_root, 'virtualenv.bundle'))

到此，所有的依赖包已经导出并加入到应用的目录里了。