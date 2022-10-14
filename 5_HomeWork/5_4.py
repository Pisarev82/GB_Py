# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open("input.txt", "w") as file:
    file.write("""eeeeellk wrrrriiiffgj wrrrgggrsssrrrrrsssf 
rioiiiiiii iiprrrmkkkk jkjjjjjjjrrrrrrr
ааалллллыххх аваоцукепо вчеорыкоо""") 

with open("input.txt", "r") as file:
    input_str = file.read()

encoded_str = ''
def encoded_to_str (input_str):
    encoded_str_1 = ''
    i = 0
    count = 1
    while i < len(input_str)-1:
        if input_str[i] == input_str[i+1]:
            count += 1
        if input_str[i] != input_str[i+1]:
            encoded_str_1 = encoded_str_1 + str(count) + input_str[i]
            count = 1
        i += 1  
    else:
        encoded_str_1 = encoded_str_1 + str(count) + input_str[i]
    return encoded_str_1
with open("encoded.txt", "w") as file:
    file.write(encoded_to_str (input_str))

with open("encoded.txt", "r") as file:
    encoded_str = file.read()
def decoded_to_str (encoded_str):
    result = ''
    i = 0
    while i < len(encoded_str)-1:
        j = 1
        decoder_chr = ''
        if encoded_str[i].isdigit(): 
            j = int(encoded_str[i])
            decoder_chr = encoded_str[i+1]
        for x in range(j): 
            result += decoder_chr
        i += 1
    return result
with open("decoded.txt", "w") as file:
    file.write(decoded_to_str (encoded_str))







# print("___________________")
# text_list = list(filter(lambda x : x.isdigit(), encoded_str))
# text_list2 = list(filter(lambda x : not x.isdigit(), encoded_str))
# decoded_str = ''
# for i in range(len(text_list)):
#     decoded_str += int(text_list[i])*text_list2[i]
# print(decoded_str)


# text_list3 = [first(i, j) for i in text_list for j in  text_list2]



# print(text_list3)
#     result_str = ''
#     for i in input_str:
#         result_str = list([j for j in itertools.groupby(i)])
        


    