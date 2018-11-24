import allure
class Test_01():
    @allure.step("测试步骤001")
    def test_er(self):
        print("报告失败")

    @allure.step("测试步骤002")
    def test_we(self):
        print("报告成功")
