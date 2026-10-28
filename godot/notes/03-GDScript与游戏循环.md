# 03：GDScript 与游戏循环

## 学习目标

读完后，你应能给节点附加脚本，理解常见生命周期回调，并用 `delta` 编写与帧率无关的运动。

## 1. GDScript 的基本特征

GDScript 是面向 Godot 的高级、面向对象、渐进类型语言，使用缩进组织代码块。外观与 Python 有相似之处，但它不是 Python，也不基于 Python。

一个脚本文件隐式地代表一个类。`extends` 指明它继承的引擎类型：

```gdscript
extends Sprite2D
```

这表示脚本获得 `Sprite2D` 及其父类型的属性和方法，例如 `texture`、`position`、`rotation` 和 `_process()`。

## 2. 变量、常量和函数

```gdscript
extends Node2D

const MAX_HEALTH := 100
var health: int = MAX_HEALTH
var speed := 400.0

func heal(amount: int) -> void:
	health = mini(health + amount, MAX_HEALTH)
```

- `const` 定义常量，名称使用 `ALL_CAPS`。
- 脚本顶部的 `var` 是成员变量，每个脚本实例各有一份。
- 函数内部的 `var` 是局部变量，只在该作用域内存在。
- `:=` 让编译器根据初始值推断类型。
- `health: int` 显式声明类型。
- `func` 定义函数，缩进表示函数体。

命名约定：节点/类使用 PascalCase，变量和函数使用 snake_case，常量使用 ALL_CAPS。

## 3. 三个常见回调

### `_init()`

对象在内存中创建时调用，类似构造入口。此时不适合假设子节点已经准备好。

```gdscript
func _init() -> void:
	print("Created")
```

### `_ready()`

节点及其子节点已经进入场景树并完成实例化后调用，适合获取子节点、连接信号。

```gdscript
func _ready() -> void:
	var timer = get_node("Timer")
	timer.timeout.connect(_on_timer_timeout)
```

### `_process(delta)`

节点每帧收到一次更新回调。`delta` 是距上一帧经过的秒数。

```gdscript
func _process(delta: float) -> void:
	rotation += PI * delta
```

物理相关运动通常还要学习 `_physics_process(delta)`；基础显示与输入轮询示例可以先使用 `_process(delta)`。

## 4. 为什么运动要乘 `delta`

如果每帧直接执行：

```gdscript
position.x += 10
```

移动速度会随帧率改变。帧率越高，每秒移动次数越多。

改成：

```gdscript
position.x += speed * delta
```

其中 `speed` 表示“像素/秒”，`speed * delta` 表示这一帧应移动的距离。无论帧间隔长短如何变化，运动都以时间为基准。

旋转同理：Godot 默认使用弧度，`PI` 表示半圈弧度，`TAU` 表示整圈弧度。

## 5. Vector2：方向与速度

`Vector2` 同时包含 x、y 两个分量，可表示位置、方向或速度。

```gdscript
extends Sprite2D

var speed := 400.0
var angular_speed := PI

func _process(delta: float) -> void:
	rotation += angular_speed * delta
	var velocity := Vector2.UP.rotated(rotation) * speed
	position += velocity * delta
```

逐层理解：

1. `Vector2.UP` 是向上的单位方向。
2. `.rotated(rotation)` 按当前节点朝向旋转方向。
3. 乘以 `speed` 得到速度向量。
4. 乘以 `delta` 得到本帧位移。

这种直接修改 `position` 的方式不会自动处理墙体或地面碰撞；需要碰撞时应使用适当的物理节点和方法。

## 6. 初学者常见的语法与数值陷阱

### 整数除法

两个整数相除会执行整数除法：

```gdscript
print(5 / 2)
print(5 / 2.0)
```

第一个结果是 `2`，第二个结果是 `2.5`。需要小数时，至少让一个操作数是浮点数或进行类型转换。

### 缩进错误

函数体、条件体和循环体必须正确缩进。出现 `Indented block expected` 时，先检查冒号与下一行缩进。

### 把成员变量当全局变量

成员变量属于当前脚本实例。另一个同类实例会有自己的副本，不会自动共享。

### 忘记继承带来的能力

Inspector 中看到的很多属性来自父类型。查 API 时不仅要看当前类，也要看它继承的类。

## 小结

脚本通过继承扩展节点；`_ready()` 适合初始化场景关系，`_process(delta)` 适合每帧更新；速度和角速度乘以 `delta`，运动才以秒而不是帧为单位。

## 官方来源与下一步

- [Creating your first script](https://docs.godotengine.org/en/stable/getting_started/step_by_step/scripting_first_script.html)
- [GDScript reference](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html)
- 上一篇：[场景实例化](02-场景实例化.md)
- 下一篇：[输入与信号](04-输入与信号.md)
- 对应练习：[脚本、输入与信号](../exercises/02-脚本输入与信号.md)
