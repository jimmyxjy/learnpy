#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse



parser = argparse.ArgumentParser(description='')
parser.add_argument('string', type=str, help='')
args = parser.parse_args()

# 实现一个函数trim()，去除字符串的首位空格
def trim(s):
	if s[:1] == ' ':
		s = trim(s[1:])
	if s[:-1] == ' ':
		s = trim(s[:-1])
	return s

if __name__ == '__main__':
	print(trim(args.string))