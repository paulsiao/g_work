# 写在前面的话
- 推荐图书：python编程从入门到实践
- 邮箱
    - 教大家用python发邮件
    - 对邮箱进行设置，只要设置好了，通过邮箱地址和授权码就能发送邮件
- 

# 0. OOP- python面向对象
- Python的面向对象
- 面向对象编程
    - 基础
    - 公有私有
    - 继承
    - 组合，Minxi
- 魔法函数
    - 魔法函数概述
    - 构造类魔法函数
    - 运算类魔法函数
 
# 1. 面向对象概述（ObjectOriented，OO）
- OOP思想
    - 接触到任意一个任务，首先想到的是任务这个世界的构成，是由模型构成的
- 几个名词
    - OO：面向对象
    - OOA：面向对象的分析
    - OOD：面向对象的设计
    - OOI：面向对象的实现
    - OOP：面向对象的编程
    - OOA -> OOD -> OOI： 面向对象的实现过程
- 类和对象的概念
    - 类：抽象名词，代表一个集合，共性的事物
    - 对象： 具象的事物，单个个体
    - 类跟对象的关系
        - 一个具象，代表一类事物的某一个个体
        - 一个是抽象，代表的是一大类事物
- 类中的内容， 应该具有两个内容
    - 表明事物的特征，叫做属性（变量）
    - 表明事物功能或动作，称为成员方法（函数）
    
# 2. 类的基本实现
- 类的命名
    - 遵守变量命名的规范
    - 大驼峰（由多个单词构成，每个单词首字母大写，单词跟单词直接相连）
    - 尽量避开跟系统命名相似的命名
- 如何声明一个类
    - 必须用class关键字
    - 类由属性和方法构成，其他不允许出现
    - 成员属性定义可以直接使用变量赋值，如果没有纸，使用None
    - 案例 01.py
- 实例化类

            变量 = 类名（） # 实例化一个对象
- 访问对象成员
    - 使用点操作符
    
                ojb.成员属性名称
                obj.成员方法
- 可以通过默认那只变量检查类和对象的所有成员
    - 对象所有成员检查
            
            # dict前后各有两个下划线
            obj.__dict__
    - 类所有的成员
            # dict前后各有两个下划线
            class_name.__dict__
            


# 3. anaconda基本使用
- anaconda主要是一个虚拟环境管理器
- 还是一个安装包管理器
- conda list：显示anaconda安装的包
- conda env list：显示anaconda的虚拟环境列表
- conda create -n xxx python=3.6: 创建python版本为3.6的虚拟环境，名称为xxx

# 4. 类和对象的成员分析
- 类和对象都可以存储成员，成员可以归类所有，也可以归对象所有
- 类存储成员时使用的是与类关联的一个对象
- 独享存储成员是存储在当前对象中
- 对象访问一个成员时，如果对象中没有该成员，尝试访问类中的同名成员，如果对象中有此成员，一定使用对象中的成员
- 创建对象的时候，类中的成员不会放入对象当中，而是得到一个空的对象，没有成员
- 通过对象类中成员重新赋值或者通过对象添加成员时，对应成员会保持在对象中，而不会修改类

# 5. 关于self
- self在对象的方法中表示当前对象本身，如果通过对象调用一个方法，那么该对象会自动传入当前方法中的第一个参数中
- self并不是关键字，只是一个用于接收对象的普通参数，理论上可以用任何一个普通变量名代替
- 方法中有self形参的方法成为非绑定类的方法，可以通过对象访问，没有self的是绑定类的方法只能通过类访问
- 使用类访问绑定类的方法时，如果类方法中需要访问当前类的成员，可以同过__class__成员名来访问

# 6. 面向对象的三大特性
- 封装
- 继承
- 多态

## 6.1 封装
- 封装就是对对象的成员进行访问的限制
- 封装的三个级别：
    - 公开，public
    - 受保护的，protected
    - 私有的，private
    - public，private，protected不是关键字
- 判别对象的位置
    - 对象内部
    - 对象外部
    - 子类中

- 私有
    - 私有成员是最高级别的封装，只能在当前类或对象中访问
    - 在成员前面添加两个下划线即可
            
            class person（）：
                # name是共有的成员
                name = “liuying”
                #__age就是私有成员 
                __age = 18
    - Python的私有不是真私有，是一种成为name mangling的改名策略，可以使用对象，_classname_attributename访问
- 受保护的封装 protected
    - 受保护的封装是将对象成员进行一定级别的封装，然后， 在类中或者字类中都可以进行访问，但是在外部不可以
    - 封装方法：在成员名称前添加一个下划线即可
- 公开的，公共的 public
    - 公共的封装实际对成员没有任何操作，任何地方都可以访问
    
## 3.2 继承
- 继承就是一个类可以获得另外一个类中的成员属性和成员方法
- 作用： 减少代码，增加代码的复用功能，同时可以设置类与类直接的关系
- 继承与被继承的概念：
    - 被继承的类叫父类，也叫基类，也叫超类
    - 用于继承的类，叫子类，也叫派生类
    - 继承与被继承一定存在一个 is - a 关系