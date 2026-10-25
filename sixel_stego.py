# -*- coding: utf-8 -*-
# @Author: sawd6

from argparse import ArgumentParser, RawDescriptionHelpFormatter

def init() -> None:
    parser = ArgumentParser(
        description='一个适用于img2sixel生成文件的孪生颜色寄存器隐写工具/提取工具（颜色索引隐写范畴）',
        # usage='',
        add_help = False,
        formatter_class=RawDescriptionHelpFormatter, # 用于保留描述中的换行
        epilog='详见csdn...'
    )

    parser.add_argument('-h', '--help', action='store_true')
    parser.add_argument('-v', '--version', action='version', version='0.0.1')

    hide = parser.add_subparsers(
        title='两个子工具：隐写工具/提取工具',
        # description='可用的',
        dest='commands',
        required=True,
        metavar='hide'
    )

    args = parser.parse_args()
    # if

def main() -> None:
    init()

if __name__ == '__main__':
    main()
