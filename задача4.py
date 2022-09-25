# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
nums = [str(i) for i in range(0,10)]
path = "input_4_task.txt"
with open(path) as file:
    first_string = file.readline()
print (first_string)
def rle_coding (string_to_code):
    result = ""
    count = 1
    i = 0
    while i < len(string_to_code):
        count = 1
        j = i + 1
        while j < len(string_to_code):
            if string_to_code[i] == string_to_code[j]:
                count += 1
            j += 1    
        result += str(count) + string_to_code[i]
        i += count
    return(result)
coded_str = rle_coding(first_string)
def get_num_len (position, string):
    temp = 0
    i = position
    while (i < len(string)) & (string[i] in nums):
            i += 1
    temp = i - position
    return(temp)

def rle_encoding (code_to_string):
    result = ""
    i = 0
    
    while i<len(code_to_string):
        temp_char = ""
        temp_num = ""
        if (get_num_len(i, code_to_string) > 0):
            for j in range (i, i + get_num_len(i,code_to_string)):
                temp_num += code_to_string[i]
            num = int(temp_num)
            temp_char = code_to_string[i+get_num_len(i,code_to_string)]
            for k in range (0, num):
                result += temp_char
            i = i + 1 + get_num_len(i,code_to_string)
    return (result)

coded_str= rle_coding(first_string)
print (coded_str)
encoded_str = rle_encoding (coded_str)
print (encoded_str)
with open ("result_4_task_coded.txt","w") as data:
    data.write(coded_str)
with open ("result_4_task_encoded.txt","w") as data:
    data.write(encoded_str)