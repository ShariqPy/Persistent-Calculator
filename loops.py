import time 
print("-------THE COUNTDOWN-------")  


while True: 
    try:
        text = input("Write your text:  ") 
        the_time = int(input("The duration(in seconds):  ")) 

        for i in range(the_time,0, -1):
            seconds = i % 60 
            minutes = int(i//60)%60
            hours = int(i//3600)%24 
            days = int(i//86400) 
            print(f"{days}:{hours:02}:{minutes:02}:{seconds:02}")
            time.sleep(1) 

        print(f"{text}") 
    except ValueError:
        print("check your inputs carefully.")
           
  