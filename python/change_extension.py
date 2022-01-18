import os
import glob

cur_path = os.getcwd()
cur_file_list = os.listdir()

before_ext = input("바꾸기 전 파일 확장자명을 적어주세요.[예시 \".xls\"]: ")
after_ext = input("바꾼 이후 파일 확장자명을 적어주세요.[예시 \".xlsx\"]: ")

targetPathPattern = cur_path+r"/*"+before_ext
target_filelist = glob.glob(targetPathPattern)

print("======바꾸기 전======")
for i in target_filelist:
    print(i)
print("======바꾼 후======")
for target in target_filelist:
    target_path = target[:len(target)-len(before_ext)]
    os.rename(target, target_path+after_ext)
    print(target_path+after_ext)