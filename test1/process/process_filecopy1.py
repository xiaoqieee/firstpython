import multiprocessing
import os


def copy_file(queue, file_name, old_folder_name, new_folder_name):
    # print("-----模拟拷贝文件[%s]----" % (old_folder_name + "\\" + file_name))
    old_f = open(old_folder_name + "/" + file_name, "rb")
    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(old_f.read())
    old_f.close()
    new_f.close()
    # 如果拷贝完，则向队列中写入一个消息，表示已经完成
    queue.put(file_name)


def main():
    old_folder_name = input("请输入要拷贝的文件夹:")
    new_folder_name = old_folder_name + "[附件]"
    try:
        os.mkdir(new_folder_name)
    except FileExistsError:
        pass
    file_names = os.listdir(old_folder_name)

    pool = multiprocessing.Pool(5)
    q = multiprocessing.Manager().Queue()
    for file_name in file_names:
        pool.apply_async(copy_file, (q, file_name, old_folder_name, new_folder_name))
    pool.close()
    file_count = len(file_names)
    cnt = 0
    while True:
        file_name = q.get()
        cnt += 1
        print("已经完成拷贝[%0.2f%%]:%s" % (cnt / file_count * 100, file_name))
        if cnt == file_count:
            break


if __name__ == '__main__':
    main()
