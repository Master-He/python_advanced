# ==========  动态导入模块方式 1 ============ #
# 注意：模块名不包括.py后缀
imp_module = 'test_import_class'
imp_class = 'ClassA'

# 方式1：使用__import__()导入模块
# 导入指定模块，导入时会执行全局方法。
ip_module = __import__(imp_module)
# dir()查看模块属性
print(dir(ip_module))

# 使用getattr()获取imp_module的类
test_class = getattr(ip_module, imp_class)
# 动态加载类test_class生成类对象
cls_obj = test_class()
# 查看对象属性
print(dir(cls_obj))
for attr in dir(cls_obj):
    # 加载非__前缀的属性
    if attr[0] != '_':
        # 获取导入obj方法。
        class_attr_obj = getattr(cls_obj, attr)

        # 判断类属性是否为函数
        if hasattr(class_attr_obj, '__call__'):
            # 执行函数
            class_attr_obj()
        else:
            # 输出类属性值
            print(attr, ' type:', type(class_attr_obj), ' value:', class_attr_obj)



# ==========  动态导入模块方式 2 ============ #
# 方式2：使用importlib
# importlib相比__import__()，操作更简单、灵活，支持reload()
import importlib
ip_module = importlib.import_module('.', imp_module)
ip_module_cls = getattr(ip_module, imp_class)
cls_obj = ip_module_cls()
if 'int_value' in dir(cls_obj):
    print(cls_obj.int_value)
    cls_obj.int_value = 10
    print(cls_obj.int_value)

# reload()重新加载，一般用于原模块有变化等特殊情况。
# reload()之前该模块必须已经使用import导入模块。
# 重新加载模块，但原来已经使用的实例还是会使用旧的模块，而新生产的实例会使用新的模块，reload后还是用原来的内存地址。
ip_module = importlib.reload(ip_module)
print(getattr(ip_module, imp_class).int_value)

# 循环多次加载相同文件，手动修改文件数据，发现重新加载后输出内容变更。
from time import sleep
for i in range(30):
    ip_module = importlib.reload(ip_module)
    print(getattr(ip_module, imp_class).int_value)
    sleep(3)









