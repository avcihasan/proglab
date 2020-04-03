import random
def get_n_random_numbers(n=10,min_=-5,max_=5):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min_,max_))
    return numbers
s=get_n_random_numbers(5,0,2)
print(s)

def my_frequency_with_dict(list):
    frequency_dict={}  #dict()={}
    for item in list:
        if(item in frequency_dict):
            frequency_dict[item]=frequency_dict[item]+1
        else:
            frequency_dict[item]=1
    return frequency_dict
print (my_frequency_with_dict(list))

def my_frequency_with_list_of_tuples(list_1):
    frequency_list=[]
    for i in range(len(list_1)):
        s=False
        for j in range(len(frequency_list)):
            if(list_1[i]==frequency_list[j][0]):
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):
            frequency_list.append([list_1[i],1])
    return frequency_list

print(my_frequency_with_list_of_tuples(s))


def my_mode_with_dict(my_hist_d):
    frequency_max=-1
    mode=-1
    for key in my_hist_d.keys():
        if my_hist_d[key]>frequency_max:
            frequency_max=my_hist_d[key]
            mode=key
    return mode,frequency_max


print(my_mode_with_dict(my_frequency_with_dict(s)))



def my_mode_with_list(my_hist_list):
    frequency_max=-1
    mode=-1
    for item,frequency in my_hist_list:
        if(frequency>frequency_max):
           frequency_max=frequency
           mode=item
    return mode,frequency_max

print(my_mode_with_list(my_frequency_with_list_of_tuples(s)))