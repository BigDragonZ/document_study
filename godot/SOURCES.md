# 官方文档来源

版本基线：Godot Engine **4.7 stable** 英文文档。以下页面用于核对概念、操作流程和示例语法；正文是中文归纳，不是官方中文翻译。

## 学习入口

- [Godot Docs – 4.7 branch](https://docs.godotengine.org/en/stable/)：文档首页、版本和离线文档入口。
- [Step by step](https://docs.godotengine.org/en/stable/getting_started/step_by_step/index.html)：官方基础学习顺序，涵盖节点、场景、实例化、脚本、输入和信号。
- [Your first 2D game](https://docs.godotengine.org/en/stable/getting_started/first_2d_game/index.html)：Dodge the Creeps 完整 2D 游戏教程及素材入口。
- [Your first 3D game](https://docs.godotengine.org/en/stable/getting_started/first_3d_game/index.html)：Squash the Creeps 进阶 3D 教程及素材入口。

## 基础概念

- [Nodes and Scenes](https://docs.godotengine.org/en/stable/getting_started/step_by_step/nodes_and_scenes.html)：节点特征、场景树、主场景、运行场景和 `res://`。
- [Creating instances](https://docs.godotengine.org/en/stable/getting_started/step_by_step/instancing.html)：PackedScene、实例化、属性覆盖、Resource 共享与 Make Unique。
- [Creating your first script](https://docs.godotengine.org/en/stable/getting_started/step_by_step/scripting_first_script.html)：`extends`、成员变量、`_init()`、`_process(delta)`、Vector2 和帧率无关运动。
- [Listening to player input](https://docs.godotengine.org/en/stable/getting_started/step_by_step/scripting_player_input.html)：Input 单例、输入动作、持续输入和方向控制。
- [Using signals](https://docs.godotengine.org/en/stable/getting_started/step_by_step/signals.html)：编辑器/代码连接信号、Timer、自定义信号、参数与 `emit()`。

## 完整 2D 项目

- [Coding the player](https://docs.godotengine.org/en/stable/getting_started/first_2d_game/03.coding_the_player.html)：玩家输入、归一化、动画、边界限制、受击信号和延迟禁用碰撞。
- [Creating the enemy](https://docs.godotengine.org/en/stable/getting_started/first_2d_game/04.creating_the_enemy.html)：Mob 场景、RigidBody2D、随机动画和离屏清理。
- [The main game scene](https://docs.godotengine.org/en/stable/getting_started/first_2d_game/05.the_main_game_scene.html)：Main、Timer、Path2D/PathFollow2D、PackedScene 和生成流程。
- [Heads up display](https://docs.godotengine.org/en/stable/getting_started/first_2d_game/06.heads_up_display.html)：CanvasLayer、HUD、开始/结束流程和用组清理旧敌人。

## 语言参考

- [GDScript reference](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html)：语言特性、关键字、类型、运算符、控制流、类、导出属性和信号。

## 进阶主题

- [Physics introduction](https://docs.godotengine.org/en/stable/tutorials/physics/physics_introduction.html)：碰撞对象、碰撞形状、物理回调、层和掩码。
- [Animation](https://docs.godotengine.org/en/stable/tutorials/animation/index.html)：动画手册入口。
- [User interface (UI)](https://docs.godotengine.org/en/stable/tutorials/ui/index.html)：Control、布局、主题和界面手册入口。
- [Audio](https://docs.godotengine.org/en/stable/tutorials/audio/index.html)：音频流、总线和播放相关主题入口。
- [Saving games](https://docs.godotengine.org/en/stable/tutorials/io/saving_games.html)：持久对象、序列化、FileAccess、JSON 和 `user://` 存档。
- [Export](https://docs.godotengine.org/en/stable/tutorials/export/index.html)：项目导出与各平台指南入口。
- [Pausing games and process mode](https://docs.godotengine.org/en/stable/tutorials/scripting/pausing_games.html)：SceneTree 暂停与节点 Process Mode。

## 使用建议

先通过教程理解概念，再用类参考查询精确 API。阅读类参考时确认页面仍位于 `en/stable`，避免把其他 Godot 版本的示例直接混入本项目。
