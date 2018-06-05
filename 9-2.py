
answer = input("誕生日は？")

with open("answer.txt","w+") as f:
    f.write(answer)
    
