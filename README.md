# aobi_auto_grow
奥比岛自动种菜项目
效果详见：https://www.bilibili.com/video/BV1oX4y1i7Fj/

# 环境说明：
- cmd执行adb命令，如果报不支持的命令，请把bin/adb加入到环境变量中
- 需要安装依赖包pip install -r requirements.txt
- 当前只支持种第一页的种子
- 当前只做了亚麻的自动化种植，如果需要加入其他类型作物请在resources\images目录下创建作物全拼的目录，然后参考yama文件夹下的截图截对应作物的截图以同样的文件名放到目录下
- 执行环境：雷霆模拟器，开启root、开启system.vmdk共享；作物最好以视频示例摆放，不要有其他的遮盖物