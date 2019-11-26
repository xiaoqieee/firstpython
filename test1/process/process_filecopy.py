import multiprocessing
import os


def copy_file(file_name, old_folder_name, new_folder_name):
    print("-----模拟拷贝文件[%s]----" % (old_folder_name + "\\" + file_name))
    old_f = open(old_folder_name + "/" + file_name, "rb")
    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(old_f.read(1024))
    old_f.close()
    new_f.close()


def main():
    old_folder_name = input("请输入要拷贝的文件夹:")
    new_folder_name = old_folder_name + "[附件]"
    try:
        os.mkdir(new_folder_name)
    except FileExistsError:
        pass
    file_names = os.listdir(old_folder_name)

    pool = multiprocessing.Pool(5)
    for file_name in file_names:
        pool.apply_async(copy_file, (file_name, old_folder_name, new_folder_name))
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
