from microbit import *
import utime 
  
# 定义引脚枚举  
class JoystickBitPin:  
    P12 = 12  
    P13 = 13  
    P14 = 14  
    P15 = 15  
  
# 定义摇杆类型枚举  
class RockerType:  
    X = 1  
    Y = 2  
  
# 假设ButtonType的High和Low对应于引脚上的高电平和低电平  
ButtonType = {  
    'down': 0,  # 低电平表示按下  
    'up': 1     # 高电平表示释放  
}  

class JOYSTICKBIT(object):
      """基本描述

      joystick游戏手柄

      """ 
      def init_joystick_bit(self):  
            """初始化摇杆位 
            P0设置为低电平(假设这是用于其他目的,如初始化LED或其他功能)
            """ 
            pin0.write_digital(0)
            
            # 设置P12, P13, P14, P15为输入并启用上拉电阻  
            pin12.set_pull(pin12.PULL_UP) 
            pin13.set_pull(pin13.PULL_UP) 
            pin14.set_pull(pin14.PULL_UP)   
            pin15.set_pull(pin15.PULL_UP)  
            
            # P16设置为高电平（可能是振动马达的控制引脚）  
            pin16.write_digital(1) 
      
      def get_button(self,button):  
            # 获取按钮状态
          pin = 1
          if button == JoystickBitPin.P12:
              pin12.set_pull(pin12.PULL_UP)
              pin = pin12.read_digital()
          elif button == JoystickBitPin.P13:
              pin13.set_pull(pin13.PULL_UP)
              pin = pin13.read_digital()
          elif button == JoystickBitPin.P14:
              pin14.set_pull(pin14.PULL_UP)
              pin = pin14.read_digital()
          elif button == JoystickBitPin.P15:
              pin15.set_pull(pin15.PULL_UP)
              pin = pin15.read_digital()
          return not pin  # 返回True如果按钮被按下（低电平），否则返回False  
                
      def on_button_event(self,button, event_type, handler):  
            # 在MicroPython中，没有直接的onPulsed事件。你可能需要轮询或使用中断。  
            # 这里仅提供一个轮询的示例。
            # 注意：这个函数不会直接注册一个事件处理程序，而是立即检查按钮状态并调用处理程序（如果需要）。  
            # 你需要在一个循环中调用此函数来轮询按钮。 
            if JOYSTICKBIT.get_button(self,button) == (event_type == ButtonType['down']):  
                  handler()  
         
      def get_rocker_value(self,rocker):  
            # 获取摇杆值（在MicroPython中，使用ADC读取模拟值）
            # adc = display.scroll(pin0.read_analog()) # 假设ADC通道0连接到了摇杆X（P1）和Y（P2）  
            if rocker == RockerType.X:   # P1是摇杆X的模拟输入   # 设置ADC分辨率  
                  return pin1.read_analog()   # 读取模拟值  
            elif rocker == RockerType.Y:   # P2是摇杆Y的模拟输入  # 设置ADC分辨率  
                  return pin2.read_analog()  # 读取模拟值  
            else:  
                  return 0  
       
      def vibration_motor(self,time_ms): 
            # 振动马达控制函数  
            pin16.write_digital(0) # 启动振动马达  
            utime.sleep_ms(time_ms)  # 等待指定的毫秒数  
            pin16.write_digital(1)  # 停止振动马达  
            
            # 示例用法：  
            # init_joystick_bit()  
            # print(get_button(JoystickBitPin.P12))  
            # on_button_event(JoystickBitPin.P13, ButtonType['down'], lambda: print("Button P13 pressed!"))  
            # print(get_rocker_value(RockerType.X))  
            # vibration_motor(500)  # 振动500毫秒

joystickbit = JOYSTICKBIT()


if __name__ == '__main__':
     
      joystickbit.init_joystick_bit()
      # JOYSTICKBIT.get_button(JoystickBitPin.P12)
      # JOYSTICKBIT.on_button_event(JoystickBitPin.P12,ButtonType['down'],lambda: print("Button P12 pressed!"))
      # JOYSTICKBIT.get_rocker_value(RockerType.X)
      # JOYSTICKBIT.vibration_motor(100)
