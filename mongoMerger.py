# -*- coding: utf-8 -*-
import csv
def inportFile(file_arg,model_file_arg,identify_col):#file_arg:加入檔名變數 model_file_arg:主要檔名變數 identify_col:加入檔案uid所在column
    tmp_hash ={}
    f = open(file_arg,'r')
    origin_f = open(model_file_arg,'r')
    reader = csv.reader(f)
    first_line = next(reader)#first line of file
    first_line_col = len(first_line)#first line contains how many column
    for line in csv.reader(f):
        tmp_hash[line[identify_col]]=line
    for line in csv.reader(origin_f):
        if tmp_hash.get(line[4])!= None:
            hash[line[4]].extend(tmp_hash[line[4]])
        else:
            try:
                hash[line[4]].extend(['']*first_line_col)
            except KeyError as e:
                print e
                pass
    title.extend(first_line)#存入標題list
    f.close()
    origin_f.close()


test_file_dir='./exam_exam_overall_616_20151117.csv'
sc_video_dir='./analytic_video_content_616_20151117.csv'
mongo_video_dir='./video.csv'
mongo_allExec_dir='./allexercise.csv'
mongo_correctExrc_dir='./corexcecise.csv'
mongo_post_dir='./post.csv'
mongo_reply_dir='./reply.csv'
mongo_like_dir='./like.csv'
write_file_dir = './mergecsv.csv'
f_test = open(test_file_dir,'r')

f_write = open(write_file_dir,'w')
w = csv.writer(f_write)
hash = {}

# 寫入標題list==============
title = []
reader = csv.reader(f_test)
title.extend(next(reader))#f_test標題
#end of 寫入標題list=======================

for line in csv.reader(f_test):
    hash[line[4]] = line
inportFile(sc_video_dir,test_file_dir,4)
inportFile(mongo_video_dir,test_file_dir,0)
inportFile(mongo_allExec_dir,test_file_dir,0)
inportFile(mongo_correctExrc_dir,test_file_dir,0)
inportFile(mongo_post_dir,test_file_dir,0)
inportFile(mongo_reply_dir,test_file_dir,0)
inportFile(mongo_like_dir,test_file_dir,0)

out = []
out.append(title)#標題list
for row in hash:
    out.append(hash[row])
w.writerows(out)

f_test.close()
f_write.close()
