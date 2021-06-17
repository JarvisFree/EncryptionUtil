#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    ：2020/11/4 19:02
@Author  ：维斯
@File    ：jar_encryption_util.py
@Version ：1.0
@Function：
"""

import random


class JarRandomUtil:
    NUMBER = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    LOWER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    UPPER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
    LOWER_UPPER = LOWER + UPPER
    NUMBER_LOWER_UPPER = NUMBER + LOWER_UPPER
    NUMBER_LOWER = NUMBER + LOWER
    NUMBER_UPPER = NUMBER + UPPER

    def random_int_str(self, count: int, first_zero: bool = False):
        """
        生成指定长度的随机数据字符串
        :param count: 长度
        :param first_zero: 生成的数字字符串 首位是否可以为零
        :return: 字符串数字
        """
        if first_zero:
            return self.__random_base(count, self.NUMBER)
        else:
            while True:
                value = self.__random_base(count, self.NUMBER)
                if str(value[0]) != '0':
                    return value

    def random_lower_str(self, count: int):
        """
        生成指定长度的随机小写字母字符串
        :param count: 长度
        :return:
        """
        return self.__random_base(count, self.LOWER)

    def random_upper_str(self, count: int):
        """
        生成指定长度的随机大写字母字符串
        :param count: 长度
        :return:
        """
        return self.__random_base(count, self.UPPER)

    def random_low_upp_str(self, count: int):
        """
        生成指定长度的随机字母（大、小写）字符串
        :param count: 长度
        :return:
        """
        return self.__random_base(count, self.LOWER_UPPER)

    def random_low_upp_number_str(self, count: int):
        """
        生成指定长度的随机字符（大小写字母+数字）
        :param count: 长度
        :return:
        """
        return self.__random_base(count, self.NUMBER_LOWER_UPPER)

    def random_low_number_str(self, count: int):
        """
        生成指定长度的随机字符（小写字母+数字）
        :param count: 长度
        :return:
        """
        return self.__random_base(count, self.NUMBER_LOWER)

    def random_upp_number_str(self, count: int):
        """
        生成指定长度的随机字符（大写字母+数字）
        :param count: 长度
        :return:
        """
        return self.__random_base(count, self.NUMBER_UPPER)

    @staticmethod
    def random_ip():
        """
        随机IP地址
        :return:
        """
        ip = '{}.{}.{}.{}'.format(
            random.randint(1, 223),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        return ip

    @staticmethod
    def __random_base(count: int, type):
        value = ''
        for c in range(count):
            value += str(type[random.randint(0, len(type) - 1)])
        return value


class JarEncryptionUtil:
    ENCODING = 'utf-8'  # ISO-8859-1

    @staticmethod
    def str_encryption_ascii(str_1: str, salt=0):
        """
        字符串转ASCII码
        :param str_1: 字符串
        :param salt: 盐
        :return: ASCII码列表
        """
        ascii_list = []
        for i in range(len(str_1)):
            # 字符串 —> ASCII
            ascii_list.append(ord(str_1[i]) + int(salt))
        return ascii_list

    @staticmethod
    def ascii_encryption_str(ascii_1: list, salt=0):
        """
        ASCII码转字符串
        :param ascii_1: ASCII列表
        :param salt: 盐
        :return: 字符串
        """
        result = ''
        for i in range(len(ascii_1)):
            # ASCII —> 字符串
            result += chr(ascii_1[i] - int(salt))
        return result

    @staticmethod
    def read_file(file: str):
        """
        读取文件数据
        :param file: 文件路径
        :return: 文件内容
        """
        with open(file, 'r', encoding=JarEncryptionUtil.ENCODING) as f:
            content = f.read()
        return content

    @staticmethod
    def write_file(file: str, str_data: str):
        """
        写入文件数据
        :param file: 文件路径
        :param str_data: 写入数据
        """
        str_data.encode(encoding=JarEncryptionUtil.ENCODING).decode(encoding=JarEncryptionUtil.ENCODING)
        with open(file, 'w', encoding=JarEncryptionUtil.ENCODING) as f:
            f.write(str_data)

    @staticmethod
    def encode_util(encode_str, salt: int):
        out_error = ''
        # 1 输入
        string = encode_str
        salt = salt  # 0-999999
        print('明文：{}'.format(string))

        # 2 程序控制
        salt += 1000000
        result = JarEncryptionUtil.str_encryption_ascii(string, salt)
        salt_len = 7  # 单个字符加密后的密文长度
        index = 0
        for a in result:
            if len(str(a)) != salt_len:
                return '', '加密出错 请联系开发者（错误代码：{}_{}）'.format(string[index], a)
            index += 1
        # 2.1 打乱密文（每个字符密文前面加7位随机数）
        new_result = []
        for a in result:
            # new_result.append(int(JarRandomUtil().random_int_str(7)))
            if 1000000 <= salt < 1100000:
                new_result.append(salt + 1307827)
            if 1100000 <= salt < 1200000:
                new_result.append(salt + 1648841)
            if 1200000 <= salt < 1300000:
                new_result.append(salt + 1114911)
            if 1300000 <= salt < 1400000:
                new_result.append(salt + 1121454)
            if 1400000 <= salt < 1500000:
                new_result.append(salt + 1331019)
            if 1500000 <= salt < 1600000:
                new_result.append(salt + 1219992)
            if 1600000 <= salt < 1700000:
                new_result.append(salt + 1754956)
            if 1700000 <= salt < 1800000:
                new_result.append(salt + 1236456)
            if 1800000 <= salt < 1900000:
                new_result.append(salt + 1551500)
            if 1900000 <= salt:
                new_result.append(salt + 1156813)
            new_result.append(a)
        # 2.2 拼接打乱后的密文
        result_str = ''
        for a in new_result:
            result_str += str(a)
        print('密文：{}'.format(result_str))
        return result_str, out_error

    @staticmethod
    def decode_util(mi, salt: int):
        out_error = ''
        # 1 输入
        m_str = mi
        m_salt = salt  # 0-999999

        # 2 程序控制
        if not m_str.isdigit():
            return '', '此密文不是本软件加密的'
        if len(m_str) % 7 != 0:
            return '', '此密文不是本软件加密的'
        m_salt += 1000000
        # 2.1 删除无用字符
        old_str = []
        for count in range(int(len(m_str) / 7)):
            count += 1
            m_str = m_str[7:]  # 删除前7个字符
            if count % 2 != 0:
                old_str.append(int(m_str[:7]))  # 取前7个字符
        # print('正确密文\n{}'.format(old_str))
        result = JarEncryptionUtil.ascii_encryption_str(old_str, m_salt)
        print('解密后：' + result)
        if result.find('񋏜') != -1:
            return '', '解密出错 请正确输入盐值与密文'
        return result, out_error


if __name__ == '__main__':
    pass
