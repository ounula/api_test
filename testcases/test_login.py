import os
from common.readexcel import ReadExcel
from common.contants import DATA_DIR
from library.ddt import ddt, data
from common.myconfig import conf
from common.handle_request import HandleRequest
from common.mylogger import my_log
import pytest

data_file_path = os.path.join(DATA_DIR, "apicases.xlsx")


class TestLogin:
    http = HandleRequest()
    excel = ReadExcel(data_file_path, "login")
    excel_data = excel.read_data()

    @pytest.mark.parametrize("test_data", excel_data)
    def test_login(self, test_data):
        # ------第一步：准备用例数据------------
        # 拼接完整的接口地址
        url = conf.get_str("env", "url") + test_data["url"]
        # 请求的方法
        method = test_data["method"]
        # 请求参数
        data = eval(test_data["data"])
        # 请求头
        headers = eval(conf.get_str("env", "headers"))
        # 预期结果
        expected = eval(test_data["expected"])
        # 该用例在表单的中所在行
        row = test_data["case_id"] + 1
        # ------第二步：发送请求到接口，获取实际结果--------
        response = self.http.send(url=url, method=method, json=data, headers=headers)
        result = response.json()

        # -------第三步：比对预期结果和实际结果-----
        try:
            # 业务码断言
            assert expected["code"] == result["code"]
            # msg断言
            assert expected["msg"] == result["msg"]
        except AssertionError as e:
            # excel中回写结果
            self.excel.write_data(row=row, column=8, value="未通过")
            # 记录apicases.xlsx日志
            my_log.info("用例：{}--->执行未通过".format(test_data["title"]))
            my_log.error(e)
            # 报告中打印预期和实际结果
            print("预取结果：{}".format(expected))
            print("实际结果：{}".format(result))
            raise e
        else:
            # excel中回写结果
            self.excel.write_data(row=row, column=8, value="通过")
            # 记录日志
            my_log.info("用例：{}--->执行通过".format(test_data["title"]))
