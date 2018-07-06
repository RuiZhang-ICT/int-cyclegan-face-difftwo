list_path = '/home/sherryzhang/img_align_celeba/list_attr_celeba.txt'

fin = open(list_path)
fin.readline()
attr_list = fin.readline().split()
img_list = fin.readlines()
fin.close()

#select_attr_list = ['Black_Hair', 'Mustache']
#select_attr_list = ['Blond_Hair', 'No_Beard']
select_attr_list = ['Eyeglasses', 'Mouth_Slightly_Open']
select_attr_value = ['-1', '1']
img_length = 150000
out_path = 'img_list_noglass_mouthopen.txt'

select_img_list = []
for attr, attr_val in zip(select_attr_list, select_attr_value):
    attr_id = attr_list.index(attr) +1
    select_list_tmp = []
    count = 0
    for img_info in img_list:
        img_info_list = img_info.split()
        if img_info_list[attr_id] == attr_val:
            select_list_tmp.append(img_info_list[0])
        count += 1
        if count > img_length:
            break
    print(attr, len(select_list_tmp))
    print select_list_tmp[0:10]
    select_img_list.append(select_list_tmp)

set_res = set(select_img_list[0])
for img_list_tmp in select_img_list:
    set_res = set_res & set(img_list_tmp)
print(select_attr_list, len(set_res))

fout = open(out_path, 'w')
for img_id in list(set_res):
    fout.write(img_id + '\n')
fout.close()


