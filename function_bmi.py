# 计算 BMI 指数并输出体重状况
def fun_bmi(person, height, weight):
    bmi = weight/(height*height)
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

fun_bmi("zhangSan",1.73,70)
fun_bmi("Lucy",1.62,50)
