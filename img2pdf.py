#!/usr/bin/env python
# coding: utf-8

# In[1]:


# get_ipython().system('pip install reportlab')


# In[13]:


import sys, os, re
import datetime
import json
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from PIL import Image


# In[14]:


# 対象ディレクトリの画像ファイルリストを取得
def get_print_img_list(dir_path):
    print_img_list = []
    for file_name in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, file_name)):
            print_img_list.append(os.path.join(dir_path, file_name))

    return print_img_list


# In[15]:


# 対象ディレクトリの画像を使ってPDF作成
def create_pdf(dir_path, pdfdir_path):
    # 対象ディレクトリの画像ファイルリストを取得
    print_img_list = get_print_img_list(dir_path)

    print(f'「{os.path.basename(dir_path)}」出力中...')
    # A4 サイズの PDF ファイルを定義する
    file_name = os.path.join(pdfdir_path, os.path.basename(dir_path) + '.pdf')
    pdf = canvas.Canvas(file_name, pagesize=A4)
    pdf.setPageSize((a4_width, a4_height))

    for print_img in print_img_list:
        img = Image.open(print_img)
        (img_w, img_h) = img.size
        pdf.setPageSize((img_w, img_h))
        pdf.drawInlineImage(img, 0, 0, width = img_w, height = img_h)
        pdf.showPage()
        print(f'{os.path.basename(print_img)}保存')
    # ファイルを保存
    pdf.save()
    print('完了')


# In[17]:


if __name__ == '__main__':
    # 実行ファイルのディレクトリパスを取得
    # directory_path = os.path.dirname(os.path.abspath(sys.argv[0])) + os.sep
    directory_path = os.getcwd()

    # 引数があれば印刷カードリストを受け取る
    if len(sys.argv) > 1:
        print_card_list_file = sys.argv[1]

    # 画像ファイルパス
    imgdir_path = os.path.join(directory_path, 'img')

    # 保存用ディレクトリ作成
    pdfdir_path = os.path.join(directory_path, 'pdf')
    if not os.path.isdir(pdfdir_path):
        os.makedirs(pdfdir_path)

    a4_width = 21.0 * cm
    a4_height = 29.7 * cm

    for dirname in os.listdir(imgdir_path):
        dir_path = os.path.join(imgdir_path, dirname)
        if os.path.isdir(dir_path):
            create_pdf(dir_path, pdfdir_path)


# In[ ]:




