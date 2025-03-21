# 各模块功能

"""
    依赖包控制区:
    import
    from        import
"""
###########################################################
"""
    实现功能介绍
"""
###########################################################
"""
    重要信息变量定义区:
"""
###########################################################
"""
    各类的定义区:
        类属性
        类的初始化方法
        类的功能方法
"""



# 命名规则:
"""
    1、程序项目名: 
        BambooSiceDetectionSystem
            
            # 要进行判空操作,若程序发现找不到该文件夹,自动创建
            /CameraGetPicture       -------相机实时获取到的图片(每次检测完成后清空; 可能不需要)
                .jpg
            
            # 要进行判空操作,若程序发现找不到该文件夹,自动创建
            /DetectionResults       ------检测结果图片(绘制有检测框、类名、置信度)
                /开始检测时间2025-03-19-11-07
                    .jpg
                    
            # 要进行判空操作,若程序发现找不到该文件夹,自动创建        
            /TrainDatasets      ------用户上传的训练集照片(程序需要判断文件结构是否正确、完整)
                /datasets
                    /images
                        train
                            .jpg
                        val
                            .jpg
                    /labels
                        train
                            .txt
                        val
                            .txt
                    data.yaml
                /datasets1
                ......          ------为减小程序的占用空间大小, 完成训练后仅保存模型文件(相对路径)
            
            /TrainModels        ------训练模型
                /OriginalModels      ------YOLOv8的原始模型
                    yolov8n.pt
                    yolov8s.pt
                /UserUploadModels       ------用户上传的模型
                    .pt
                
            /UserOperationSystem        ------用户操作系统
                /config     ------配置文件
                    Users.json      -------存放用户信息数据
                    CurrentLoginUser.json       -------存放当前登录用户的信息
                    CurrentSystemSetting.json       ------存放当前系统参数设置
                    HelpInformation.txt         ------存放帮助界面的文字信息
                    README.txt
                    
                /Library            ------存放程序需要的包
                    /UltralyticsResourceCode    ------YOLO算法的源码
                    ......
                /UI         ------存放程序的交互界面文件
                    .ui
                /src            ------存放功能模块和主程序文件        

    2、各功能模块文件: 
        main.py             主程序
        assistant_information.py            帮助信息界面和其他
        login.py                登录界面功能            
        users_manager.py                用户管理界面功能
        detect_setting.py               检测设置页面功能       
        model_setting.py                算法模型页面功能
        camera_communicate.py           相机通信页面功能---基于奥比中光工业相机实现
        
    3、类名: 大驼峰
        class User:     用户类
            ...
        
        class OrbbecCamera:     相机类
            ...
        
        class YOLOv8Detector:       检测器类
            ...
        
        class Model:        算法模型类
            ...
        
    4、方法名: 
        # 登录窗口LoginWindow: 点击登录按钮,校验密码、账号--->跳转到MainWindow, 关闭当前窗口
            def check_login(self):
                def jump_to_MainWindow(self):
        
        # 主界面MainWindow: 
            # 相机通信：
            
            # 算法模型：
                # 用户上传模型：
                    # 上传模型
                    def user_upload_model(self):
                    
                    # 保存上传的模型
                    def save_upload_model(self):
                    
                # 更改模型的保存路径：
                    # 更改按钮
                    def change_model_save_path(self):
                        ...
                    
                # 在线训练模型：
                    # 上传数据集
                    def user_upload_datasets(self):
                    
                    # 选择模型(推荐使用原始)
                    def user_choice_model(self):
                    
                    # 开始训练
                    def start_train_model(self):
            
            # 检测设置
                # 更改当前检测模型
                def change_detect_model(self):
                
                # 更改日志保存路径
                def change_log_save_path(self):
                
                # 开始检测
                def check_start_detect(self):
                    # 加载日志
                
                # 停止检测
                def check_stop_detect(self):
                
                # 图片检测
                def bamboo_detecct(self):

            # 帮助信息模块：
            def load_help_file(self):
            
            # 用户模块：
                # 显示当前登录账户的用户名
                current_login_username
                
                # 显示当前登录账户的账号
                current_login_account
                
                # 用户管理按钮：跳转到用户管理窗口
                def check_user_manager(self,current_login_premission):
                    判断权限
                    if not current_login_premission == "超级管理员":
                        发送信息弹窗：权限不足,无法使用该功能
                        return
                    def jump_to_UserManagerWindow(self):
                    
                
                # 退出登录: 进入登录窗口
                def logout(self):
                    self.    = ()     # 实例化窗口
                    self.    .show()
                    
                    
        # 用户管理窗口UserManagerWindow: 
            # 新增按钮
            def add_user(self):
            
            # 删除按钮
            def delete_user(self):
            
            # 权限修改
            def edit_user_permission(self):
            
            # 保存
            def save_user_data(self):
    ******  # 退出窗口        
            
    5、变量名: 
        current_login_username   
        current_login_account   ---当前登录的账号(作为索引、持久化保存)
        current_login_password
        current_login_premission
        
        存放到文件夹内: _path       存放到文件夹: _folder_path
        current_model_save_path   模型文件默认/当前保存路径
"""
"""
    JSON文件加载中路径的获取方法:
        1、指定json文件的路径
        2、使用脚本获取:
            # 获取当前脚本所在的目录
            current_dir = os.path.dirname(__file__)

            # 构造 CurrentSystemSetting.json 文件的相对路径
            config_dir = os.path.join(current_dir, "..", "config")
            json_file_path = os.path.join(config_dir, "CurrentSystemSetting.json")
"""