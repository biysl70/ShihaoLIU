"""
A simple robot simulator on a 2D grid.
"""

from enum import Enum
from typing import Tuple


class Facing(Enum):  # Facing 我们定义为一个枚举类，用于定义方向。如有疑问可以自行 Google / Ask AI
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3


class Grid():
    def __init__(self, width: int, height: int, enemy_pos: tuple):  # DO NOT EDIT THIS METHOD
        self.width: int = width
        self.height: int = height
        self._current_pos: tuple = (0, 0)
        self.current_direction = Facing.UP
        self.enemy_pos: tuple = enemy_pos
        self.position_history: dict = {}  # 用于存储位置历史，键为步数，值为坐标

    @property
    def current_pos(self) -> Tuple[int, int]:
        """
        current_pos 属性的 getter，返回私有属性 _current_pos
        """
        return self._current_pos

    @current_pos.setter
    def current_pos(self, value: Tuple[int, int]) -> None:
        """
        current_pos 属性的 setter（作为第 1 题留空）

        要求：
          - 接受一个长度为 2 的 tuple (x, y)
          - 若传入非 tuple 或长度不为 2，应抛出 TypeError
          - 将 x, y 强制转换为 int ，检查是否超出了宽高范围，如果任何一个超出则将其限制在最大宽高范围即可
          - 处理后存入 self._current_pos
        """
        pass  # TODO: Question 1

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(
                "current_pos must be a tuple of length 2, e.g., (x, y).")

        try:
            x, y = int(value[0]), int(value[1])
        except Exception as e:
            raise TypeError(
                "current_pos elements must be convertible to int.") from e

        if x < 0:
            x = 0
        elif x > self.width:
            x = self.width

        if y < 0:
            y = 0
        elif y > self.height:
            y = self.height

        self._current_pos = (x, y)

    @property
    def enemy_pos(self) -> Tuple[int, int]:
        return self._enemy_pos

    @enemy_pos.setter
    def enemy_pos(self, value: Tuple[int, int]) -> None:
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(
                "enemy_pos must be a tuple of length 2, e.g., (x, y).")
        try:
            ex, ey = int(value[0]), int(value[1])
        except Exception as e:
            raise TypeError(
                "enemy_pos elements must be convertible to int.") from e

        if ex < 0:
            ex = 0
        elif ex > self.width:
            ex = self.width

        if ey < 0:
            ey = 0
        elif ey > self.height:
            ey = self.height

        self._enemy_pos = (ex, ey)

    def move_forward(self) -> Tuple[int, int]:  # type: ignore
        '''
        让机器人向当前方向走一格
        返回新的坐标 (x,y) 同时更新成员变量
        利用好上面的 setter
        以右为X轴正方向，上为Y轴正方向
        '''
        pass  # TODO: Question 2
        x, y = self.current_pos
        if self.current_direction == Facing.RIGHT:
            x += 1
        elif self.current_direction == Facing.UP:
            y += 1
        elif self.current_direction == Facing.LEFT:
            x -= 1
        elif self.current_direction == Facing.DOWN:
            y -= 1

        self.current_pos = (x, y)
        return self.current_pos

    def turn_left(self) -> Facing:  # type: ignore
        '''
        让机器人逆时针转向
        返回一个新方向 (Facing.UP/DOWN/LEFT/RIGHT)
        '''
        pass  # TODO: Question 3a

        new_val = (self.current_direction.value + 1) % 4
        self.current_direction = Facing(new_val)
        return self.current_direction

    def turn_right(self) -> Facing:  # type: ignore
        '''
        让机器人顺时针转向
        '''
        pass  # TODO: Question 3b

        new_val = (self.current_direction.value - 1) % 4
        self.current_direction = Facing(new_val)
        return self.current_direction

    def find_enemy(self) -> bool:  # type: ignore
        '''
        如果找到敌人（机器人和敌人坐标一致），就返回true
        '''
        pass  # TODO: Question 4
        return self.current_pos == self.enemy_pos

    def record_position(self, step: int) -> None:
        '''
        将当前位置记录到 position_history 字典中
        键(key)为步数 step，值(value)为当前坐标 self.current_pos
        例如：step=1 时，记录 {1: (0, 0)}
        '''
        pass  # TODO: Question 5a
        self.position_history[int(step)] = self.current_pos

    def get_position_at_step(self, step: int) -> tuple:  # type: ignore
        '''
        从 position_history 字典中获取指定步数的坐标
        如果该步数不存在，返回 None
        '''
        pass  # TODO: Question 5b
        return self.position_history.get(int(step), None)


"""
在这里你需要实现 AdvancedGrid 类，继承自 Grid 类，并添加以下功能：
1. 追踪移动步数
2. 计算到敌人的曼哈顿距离

类名：AdvancedGrid
继承自：Grid
包含以下新属性：
- steps: int - 追踪移动步数，初始值为 0

包含以下方法：
1. move_forward(self) -> Tuple[int, int]
    调用父类的 move_forward 方法完成移动
    新增实现：移动步数 self.steps 加 1
    返回：移动后新坐标

2. distance_to_enemy(self) -> int
    计算当前位置到敌人位置的曼哈顿距离
    曼哈顿距离 = |x1 - x2| + |y1 - y2|
    返回：曼哈顿距离值

"""
# TODO: Question 6


class AdvancedGrid(Grid):
    def __init__(self, width: int, height: int, enemy_pos: tuple):
        super().__init__(width, height, enemy_pos)
        self.steps: int = 0

    def move_forward(self) -> Tuple[int, int]:  # type: ignore

        new_pos = super().move_forward()

        self.steps += 1
        return new_pos

    def distance_to_enemy(self) -> int:
        x, y = self.current_pos
        ex, ey = self.enemy_pos
        return abs(x - ex) + abs(y - ey)
