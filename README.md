# My-Python-Learning-Journey

一个用于总结 Python 课程所学内容的代码仓库：把课堂上讲过的知识点和课后练习整理成可运行的脚本，用 Git 记录每次修改，在 GitHub 上公开，方便回顾与展示。

## 项目简介

本仓库用来总结 Python 课程上学过的代码。课程的知识点分散在讲义、课堂演示和课后作业里，时间一长容易忘；把它们统一写成能直接运行的脚本、按功能命名归档，既方便随时回看当时是怎么实现的，也能把学习成果展示给别人。

目前仓库已整理两个基础练习：用函数计算 BMI 指数并判断体重状况，以及用 `os` 模块创建多层目录结构。

## 文件说明

| 文件名 | 用途 |
| --- | --- |
| `function_bmi.py` | BMI 指数计算。定义 `fun_bmi()` 函数，传入姓名、身高、体重，输出 BMI 数值和对应的体重状况；文件末尾附两组调用示例。 |
| `directory_ops.py` | 目录操作练习。使用 `os.mkdir()` 与 `os.makedirs()` 创建 `PsyStudy` 及其子目录，练习单层目录与多层目录的创建方式。 |
| `README.md` | 项目说明文档，即本文件。 |
| `.gitignore` | Git 忽略规则，排除 Python 缓存、虚拟环境、密钥文件和作业文档等不应进入仓库的内容。 |
| `LICENSE` | 开源许可证（MIT License）。 |

## 代码说明

### 1. `function_bmi.py` —— BMI 指数计算

核心是一个带三个参数的函数：先用公式算出 BMI，再用 `if / elif / else` 按区间给出结论。

```python
def fun_bmi(person, height, weight):
    bmi = weight / (height * height)
    print(person + "的身高：" + str(height) + "米 \t 体重：" + str(weight) + "千克")
    print(person + "的BMI指数为：" + str(bmi))
    if bmi < 18.5:
        print("体重过轻")
    elif bmi < 24.9:
        print("正常范围，注意保持")
    elif bmi < 29.9:
        print("体重过重")
    else:
        print("肥胖")
```

几点说明：

- **计算公式**：BMI = 体重(kg) ÷ 身高(m)²。身高以「米」为单位传入，所以调用时写 `1.73` 而不是 `173`；
- **函数封装**：把计算和判断都放进函数里，算几个人就调用几次，不用复制一遍代码；
- **条件分支**：四个区间从上到下依次判断，`elif` 保证只会命中其中一个分支。区间边界取「小于」，所以 18.5 会落在「正常范围」里；
- **类型转换**：`str()` 把数值转成字符串，才能用 `+` 与前面的文字拼接后输出。

调用示例：

```python
fun_bmi("zhangSan", 1.73, 70)   # BMI 约 23.39，正常范围，注意保持
fun_bmi("Lucy", 1.62, 50)       # BMI 约 19.05，正常范围，注意保持
```

### 2. `directory_ops.py` —— 创建目录结构

```python
import os
os.mkdir("PsyStudy")
os.mkdir(r"PsyStudy\data")
os.makedirs(r"PsyStudy\results\figures")
```

- `os.mkdir()` 一次只能建**一层**目录，所以要先建 `PsyStudy`，再在它下面建 `data`。如果父目录不存在就直接建子目录，会抛出 `FileNotFoundError`；
- `os.makedirs()` 可以**递归创建**多层目录，一次就把 `results\figures` 两层全部建出来；
- 字符串前的 `r` 表示原始字符串，反斜杠不会被当作转义字符，写 Windows 路径时更省事；
- 脚本重复执行时，因为目录已存在会抛 `FileExistsError`，实际使用时通常会先用 `os.path.exists()` 判断一下。

## 运行方式

```bash
python function_bmi.py
python directory_ops.py
```

环境要求：Python 3.x，无需安装任何第三方库，仅使用内置的 `os` 模块。

## 学习心得与规划

实际上在 GitHub 上浏览并了解其他相对复杂的 Python 项目对于我这个英语不怎么好的人来说，有点难度，一定要找README.md 文件仔细阅读，幸亏有很多专门设置中文文档，后面我又去下载了沉浸式翻译插件，才极大方便了我的阅读。

整个任务开始时，我先是借助 DeepSeek harness帮我完成基本的创建本地仓库，然后上传的操作，结果发现我不知道他做了什么，复刻不了他的操作，只能自己重来，一步步让他告诉我怎么做。

整体下来，最大感受就是能借助有用的工具，并进行合理使用，能极大地方便对于个人项目的操作，后面我利用 desktop 能对仓库进行管理，对于我的 Python 学习来讲，就像一份可更新的学习文档，能清晰地反映我的学习改进历程，能通过不同的 branch方便进行展示代码优化和改进思路。

因此后面不只是对于 Python，还有我后面的 ComfyUI 学习，GitHub 都能为我提供广阔的资源，以及记录我的成长路径。

每一次完成练习、找到优秀的代码或资源，我都能放到仓库里去进行说明与分享，我在 B 站观看的很多 GitHub 教程视频中也提到要乐于分享自己的收获，在这个以开源精神闻名的社区里
