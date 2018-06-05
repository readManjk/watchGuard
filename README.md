# watchGuard
根据用户要求选择特定产品的性能描述

一：解决方案
1. 在网址首页，通过Python发送request get请求即可获得首页html
2. 通过BeautifulSoup模块解析html，可获得各产品型号
3. 观察web请求，可以发现产品的对比数据访问网址是由下拉列表的value组合。
   比如：https://www.watchguard.com/wgrd-products/appliances-compare/1320/3025/4206
   访问该网址即可获得1320、3025、4206相对应型号的参数。
4. 这里我们简化模型，将value设置成相同如：https://www.watchguard.com/wgrd-products/appliances-compare/1320/1320/1320
   这样就可以获得单独的一个型号产品参数，然后通过request get请求获取该产品的html
5. 创建一个Product产品类，每一个不同的型号产品实例化该类，该类拥有产品name属性和get_performance等等方法，
   第4步获取到的单独产品html后，实例化Product类，这样每个产品就是一个对象
6. 要获取performance数据，就调用产品对象的相应方法，获得数据后再写入CSV文件即可

二：项目结构及模块设计
1. 该项目采用MVC结构设计，M层为逻辑层，V层为视图层，C层为控制层。

2. M层中含 connection.py、watchguard.py product.py

   connection.py: 接受url 发送request get 请求，返回html
   
   watchguard.py：获取用户指定的产品型号，然后根据产品value_id值，调用connection的方法获取到每一个产品的html
   然后实例化Product类，存储产品对象.
   
   product.py: 产品类，每个型号产品实例化该类，拥有属性name、get_product_performance方法和暂未实现的(get_product_hardware,
   get_product_security,get_product_vpn_tunnels,get_product_networking_feature等方法)
   
3. V层中含 visual.py

   visual.py: 接受逻辑层(M)传来的数据，根据用户指定方式存储数据
   
4. C层中含 control.py

   control.py: 协调 M和V层进行工作，接受用户数据调用逻辑层(M)进行处理，然后将得到的数据拿给视图层(V)去按照用户特指方式去实现
   
5. common文件夹含一些公共调用模块

6. config文件夹含一些配置模块

三：脚本使用方法
1. Python3环境直接运行run文件夹中的run.py,运行结果在data文件下以performance.csv存储
   

